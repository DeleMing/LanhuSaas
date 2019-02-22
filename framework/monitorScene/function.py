# -*- coding: utf-8 -*-
from __future__ import division
from django.views.decorators.csrf import csrf_exempt
import json
import math
from models import Scene
from models import position_scene
from monitor.models import scene_monitor,Monitor
from position.models import JobInstance


def monitor_show(request):
    monitor = Scene.objects.all()
    res_list = []
    for i in monitor:
        dic = {
            'id': i.id,
            'scene_name': i.scene_name,
            'scene_startTime': str(i.scene_startTime),
            'scene_endTime': str(i.scene_endTime),
            'scene_creator': i.scene_creator,
            'scene_creator_time': str(i.scene_creator_time),
            'scene_editor': i.scene_editor,
            'scene_editor_time': str(i.scene_editor_time),
            'pos_name':''
        }
        position = position_scene.objects.filter(scene=i.id)
        for c in position:
            job = JobInstance.objects.filter(id=c.position_id)
            for j in job:
                jobs = {
                    "pos_name" : j.pos_name
                }
                dic['pos_name']=jobs["pos_name"]
        res_list.append(dic)
    return res_list


def addSence(request):
    try:
       res = request.body
       senceModel = json.loads(res)
       senceModel2 = {
           "scene_name":senceModel['data']['scene_name'],
           "scene_startTime":senceModel['data']["scene_startTime"],
           "scene_endTime":senceModel['data']["scene_endTime"],
           "scene_creator":"admin"
       }
       Scene.objects.create(**senceModel2)
       id = Scene.objects.last()
       senceModel3 = {
           "scene":id,
           "position_id":senceModel['data']["pos_name"]
       }
       position_scene.objects.create(**senceModel3)
       info = make_log_info(u'增加场景', u'业务日志', u'Scene', sys._getframe().f_code.co_name,
                            get_active_user(request)['data']['bk_username'], '成功', '无')
       add_log(info)
       info2 = make_log_info(u'增加场景', u'业务日志', u'position_scene', sys._getframe().f_code.co_name,
                            get_active_user(request)['data']['bk_username'], '成功', '无')
       add_log(info2)
    except Exception as e:
        info = make_log_info(u'增加场景', u'业务日志', u'Scene', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '失败', repr(e))
        add_log(info)
        info = make_log_info(u'增加场景', u'业务日志', u'position_scene', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '失败', repr(e))
        add_log(info)
    return None


def select_table(request):
    res = request.body
    res_list = []
    monitor =Scene.objects.filter(scene_name__contains=res)
    for i in monitor:
        dic = {
            'id': i.id,
            'scene_name': i.scene_name,
            'scene_startTime': str(i.scene_startTime),
            'scene_endTime': str(i.scene_endTime),
            'scene_creator': i.scene_creator,
            'scene_creator_time': str(i.scene_creator_time),
            'scene_editor': i.scene_editor,
            'scene_editor_time': str(i.scene_editor_time),
        }
        position = position_scene.objects.filter(scene=i.id)
        for c in position:
            job = JobInstance.objects.filter(id=c.position_id)
            for j in job:
                jobs = {
                    "pos_name": j.pos_name
                }
                dic['pos_name'] = jobs["pos_name"]
        res_list.append(dic)
        print res_list
    return res_list


def delect(request):
    try:
        Scene.objects.filter(id=request.body).delete()
        position_scene.objects.filter(scene=request.body).delete()
        info = make_log_info(u'删除场景', u'业务日志', u'position_scene', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '成功', '无')
    except Exception as e:
        info = make_log_info(u'增加场景', u'业务日志', u'position_scene', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '失败', repr(e))
    add_log(info)
    return ""


def editSence(request):
    try:
        model = json.loads(request.body)
        senceModel2 = {
            "scene_name": model['data']['scene_name'],
            "scene_startTime": model['data']["scene_startTime"],
            "scene_endTime": model['data']["scene_endTime"],
            "scene_editor":"admin"
        }
        Scene.objects.filter(id=model['data']['id']).update(**senceModel2)
        info = make_log_info(u'编辑场景', u'业务日志', u'Scene', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '成功', '无')
        add_log(info)
        scene = Scene.objects.get(id=model['data']['id'])
        scene.save()
        job =JobInstance.objects.filter(pos_name=model['data']["pos_name"])
        for j in job:
            senceModel3 = {
            "scene_id": model['data']['id'],
            "position_id": j.id
            }
            print senceModel3
        position_scene.objects.filter(scene=senceModel3['scene_id']).update(**senceModel3)
        info2 = make_log_info(u'编辑场景', u'业务日志', u'position_scene', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '成功', '无')
        add_log(info2)
    except Exception as e:
        info = make_log_info(u'编辑场景', u'业务日志', u'Scene', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '失败', repr(e))
        add_log(info)
        info2 = make_log_info(u'编辑场景', u'业务日志', u'position_scene', sys._getframe().f_code.co_name,
                             get_active_user(request)['data']['bk_username'], '失败', repr(e))
        add_log(info2)
    return None


def pos_name(request):
    job=JobInstance.objects.all()
    res_list = []
    for i in job:
        dic = {
            'id': i.id,
            'pos_name': i.pos_name
        }
        res_list.append(dic)
    return res_list


def paging(request):
    res = json.loads(request.body)
    page = res['page']
    limit = res['limit']
    start_page = limit*page-9
    monitor = Scene.objects.all()[start_page-1:start_page+9]
    monitor2 = Scene.objects.all().values('id')
    page_count = math.ceil(len(monitor2)/10)
    res_list = []
    for i in monitor:
        dic = {
            'id': i.id,
            'scene_name': i.scene_name,
            'scene_startTime': str(i.scene_startTime),
            'scene_endTime': str(i.scene_endTime),
            'scene_creator': i.scene_creator,
            'scene_creator_time': str(i.scene_creator_time),
            'scene_editor': i.scene_editor,
            'scene_editor_time': str(i.scene_editor_time),
            'pos_name': '',
            'page_count': page_count,
        }
        position = position_scene.objects.filter(scene=i.id)
        for c in position:
            job = JobInstance.objects.filter(id=c.position_id)
            for j in job:
                jobs = {
                    "pos_name": j.pos_name
                }
                dic['pos_name'] = jobs["pos_name"]
        res_list.append(dic)
    return res_list


def scene_show():

    resluts = Monitor.objects.get(monitor_type="基本单元类型")
    print(resluts)
    return None