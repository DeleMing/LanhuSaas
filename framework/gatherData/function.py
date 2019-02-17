# -*- coding: utf-8 -*-

from models import *
from django.forms.models import model_to_dict
from DataBaseManage.models import *
from DataBaseManage.function import *
import MySQLdb
import datetime
import json
from gatherData.models import *
from gatherDataHistory.models import *
from alertRule.function import *
from account.models import *
from blueking.component.shortcuts import *


# 采集测试参数初始化方法
def gather_test_init():
    info = dict()
    # ------------临时测试时用的数据，实际应从info对象中获取参数,由celery提供info对象--------
    # sql测试用监控项ID：'1'
    # 文件测试用监控项ID：'1'
    # 接口测试用监控项ID：'2'
    info['id'] = '2'
    # sql测试用类型：'sql'
    # 文件测试用类型：'file'
    # 接口测试用类型：'interface'
    info['gather_params'] = 'interface'
    # sql测试用参数：'46'
    # 文件测试用参数：'192.168.1.10,/fk/test.txt'
    # 接口测试用参数：'http://localhost:8989,user=root$password=123'
    info['params'] = 'http://localhost:8989,user=root$password=123'
    # sql测试用采集规则：'SELECT @cp=china_point@,@jp=japan_point@ FROM test_gather_data WHERE id=2'
    # 文件测试用采集规则：'echo "1234"'
    # 接口测试用采集规则：'SELECT @cty=city@,@cap=email.capacity@ FROM test_gather_data'
    info['gather_rule'] = 'SELECT @cty=city@,@cap=email.capacity@ FROM test_gather_data'
    # ------------------------------------------------------------------------------------
    return info


# 采集参数解析
def gather_param_parse(info):
    # 采集参数对象
    gather_params = dict()
    # 字段索引
    field_start = 7
    field_end = info['gather_rule'].find('FROM') - 1
    # 采集目标具体字段
    gather_params['target_field'] = list()
    # 采集表存储的键名
    gather_params['gather_field'] = list()
    # 采集所需的一些额外参数
    gather_params['extra_param'] = dict()
    # 获取采集规则的字段有哪些
    gather_params['rule_fields_str'] = info['gather_rule'][field_start:field_end]
    rule_fields = gather_params['rule_fields_str'].split(',')
    for rule_field in rule_fields:
        field = rule_field.strip('@').split('=')
        gather_params['gather_field'].append(field[0])
        gather_params['target_field'].append(field[1])
    if 'sql' == info['gather_params']:
        # 根据参数获取数据库连接配置
        conn_info = Conn.objects.filter(id=info['params']).get()
        # 解密存储在数据库中的数据库密码
        conn_info.password = decrypt_str(conn_info.password)
        gather_params['extra_param']['connection_param'] = conn_info
    elif 'interface' == info['gather_params']:
        interface_params = info['params'].split(',')
        # 获取接口url参数
        gather_params['extra_param']['interface_url'] = interface_params[0]
        request_params = interface_params[1].split('$')
        request_param_dict = dict()
        # 获取调用接口所需的参数
        for request_param in request_params:
            temp_param = request_param.split('=')
            request_param_dict[temp_param[0]] = temp_param[1]
        gather_params['extra_param']['request_param_dict'] = request_param_dict
    elif 'file' == info['gather_params']:
        pass
    return gather_params


# 重复的采集字段数据迁移到历史记录
def gather_data_migrate(item_id):
    # 获取当前采集表中的数据是否为空，否则可能需要将某监控项的采集数据迁移到历史采集表中
    length = TDGatherData.objects.count()
    # 数据采集表存在数据的情况
    if 0 != length:
        # 如果采集表中存在监控项id与当前采集的监控项id对应相同的数据，则将采集表中的此部分数据移至历史记录
        length2 = TDGatherData.objects.filter(item_id=item_id).count()
        if 0 != length2:
            # 开始迁移表数据
            migrate_data = TDGatherData.objects.filter(item_id=item_id).all()
            for data in migrate_data:
                TDGatherHistory(**model_to_dict(data)).save()
            TDGatherData.objects.filter(item_id=item_id).all().delete()


# 采集的key-value定义
def gather_key_define(gather_field):
    data_set = list()
    for field in gather_field:
        temp = dict()
        temp['key'] = field.strip()
        temp['value'] = list()
        temp['value_str'] = ''
        data_set.append(temp)
    return data_set


# 遍历JSON字典中的所有key：json_dict需要递归的JSON字典，target_field目标采集字段，data_set采集结果，json_path当前遍历的JSON路径
def recursion_json_dict(json_dict, target_field, data_set, json_path):
    if isinstance(json_dict, dict):
        # 遍历，筛选，并将结果集整理为key-value形式的采集数据
        for key, value in json_dict.items():
            if isinstance(value, dict):
                recursion_json_dict(value, target_field, data_set, '%s.%s' % (json_path, key))
            elif isinstance(value, list):
                for v in value:
                    recursion_json_dict(v, target_field, data_set, '%s.%s' % (json_path, key))
            else:
                json_path = '%s.%s' % (json_path, key)
                # print "PATH: %s" % json_path
                count = 0
                for field in target_field:
                    index = field.rfind('.')
                    if -1 != index:
                        single_key = field[index + 1:]
                    else:
                        single_key = field
                    # print 'FIELD: %s, SINGLE_KEY: %s, KEY: %s, JSON_PATH: %s' % (field, single_key, key, json_path)
                    if single_key == key:
                        if str(json_path).endswith(field):
                            t = data_set[count]
                            t['value'].append(str(value))
                            t['value_str'] = ','.join(t['value'])
                    count += 1
                # print 'PATH: %s' % json_path
                index1 = json_path.rfind('.')
                json_path = json_path[0:index1]


# 采集方法，返回参数gather_status为ok采集正常，返回empty采集结果为空，返回error采集规则错误
def gather_data(info):
    # 采集测试参数初始化
    info = gather_test_init()
    # 采集状态，默认为ok
    gather_status = 'ok'
    # 获取数据采集的类型
    gather_type = info['gather_params']
    # 采集数据库中的数据
    if "sql" == gather_type:
        # 获取采集参数
        gather_params = gather_param_parse(info)
        # 生成数据库采集使用的sql
        gather_sql = info['gather_rule'].replace(gather_params['rule_fields_str'], ','.join(gather_params['target_field']))
        # 获取数据库连接参数
        conn_params = gather_params['extra_param']['connection_param']
        # 连接指定数据库
        conn = MySQLdb.connect(host=conn_params.ip, user=conn_params.username, passwd=conn_params.password, db=conn_params.databasename, port=int(conn_params.port))
        cursor = conn.cursor()
        #采集规则是否异常判断
        # noinspection PyBroadException
        try:
            cursor.execute(gather_sql)
            result = cursor.fetchall()
        except Exception:
            print 'EXCEPTION'
            gather_status = 'error'
            return gather_status
        # 获取当前采集时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 历史采集数据迁移
        gather_data_migrate(info['id'])
        if 0 != len(result):
            # 定义key-value
            data_set = gather_key_define(gather_params['gather_field'])
            # 将结果集整理为key-value形式的采集数据
            for unit in result:
                count = 0
                for data in unit:
                    t = data_set[count]
                    t['value'].append(str(data))
                    t['value_str'] = ','.join(t['value'])
                    count += 1
            # 将采集的数据保存到td_gather_data中
            for item in data_set:
                TDGatherData(item_id=info['id'], gather_time=now, data_key=item['key'], data_value=item['value_str']).save()
        else:
            gather_status = 'empty'
    elif "interface" == gather_type:
        # 接口方式采集数据
        # 获取采集参数
        gather_params = gather_param_parse(info)
        # 定义key-value
        data_set = gather_key_define(gather_params['gather_field'])
        # 发送请求，判断接口返回的信息，接口采集是否出错,如果出错，方法立即返回error结束
        pass
        # 发送请求，从接口获取JSON数据，此处为模拟数据
        json_data = '{"username":"mary","age":"20","info":[{"tel":"1234566","mobile_phone":"15566757776","email":{"home":"home@qq.com","company":"company@qq.com","capacity":"2000"}}],"money":{"capacity":"50000","type":"RMB"},"address":[{"city":"beijing","code":"1000022"},{"city":"shanghai","code":"2210444"}]}'
        # 将JSON字符串解析为python字典对象，便于筛选并采集数据
        json_dict = json.loads(json_data)
        # 判断接口是否返回了空数据
        if 0 != len(json_dict):
            # 获取当前采集时间
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 历史采集数据迁移
            gather_data_migrate(info['id'])
            # 遍历，筛选，并将结果集整理为key-value形式的采集数据
            recursion_json_dict(json_dict, gather_params['target_field'], data_set, '$')
            # print data_set
            # 将采集的数据保存到td_gather_data中
            for item in data_set:
                TDGatherData(item_id=info['id'], gather_time=now, data_key=item['key'], data_value=item['value_str']).save()
        else:
            gather_status = 'empty'
    else:
        # 文件方式采集数据
        user_account = BkUser.objects.filter(id=1).get()
        # 根据id为1的用户获取客户端操作快速执行脚本
        client = get_client_by_user(user_account)
        client.set_bk_api_ver('v2')
        # 脚本内容，使用Base64编码
        script_content = base64.b64encode(info['gather_rule'])
        temp_param = info['params'].split(',')
        # 目标文件的IP地址
        ip_location = temp_param[0]
        # 目标文件所在服务器的路径
        file_path = temp_param[1]
        # 蓝鲸业务ID，暂固定为2
        biz_id = '2'
        # 蓝鲸云区域ID，暂固定为0
        cloud_id = '0'
        # 蓝鲸Agent所在IP地址，暂固定为192.168.1.52
        agent_id = '192.168.1.52'
        # 向蓝鲸平台请求执行快速执行脚本
        bk_params = {
            'bk_biz_id': biz_id,
            'script_content': script_content,
            'is_param_sensitive': 0,
            'account': 'root',
            'script_type': 1,
            'ip_list': [
                {
                    'bk_cloud_id': cloud_id,
                    'ip': agent_id
                }
            ]
        }
        res = client.job.fast_execute_script(bk_params)
        print res
    # 数据采集完毕后使用告警规则检查数据合法性
    rule_check(info['id'])
    return gather_status
