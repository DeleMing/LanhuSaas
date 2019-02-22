# -*- coding: utf-8 -*-

from django.db import models
from monitorScene.models import Scene


class Monitor(models.Model):
    """
    单元信息表
    """
    monitor_name = models.CharField(verbose_name=u'监控项名称', max_length=50, unique=True)
    monitor_type = models.CharField(verbose_name=u'监控项类型',max_length=10)
    jion_id = models.PositiveIntegerField(verbose_name=u'关联ID')
    gather_rule = models.CharField(verbose_name=u'采集规则', max_length=500)
    gather_params = models.CharField(verbose_name=u'采集参数', max_length=500)
    params = models.CharField(verbose_name=u'监控参数', max_length=500)
    width = models.PositiveIntegerField(verbose_name=u'宽')
    height = models.PositiveIntegerField(verbose_name=u'高')
    font_size = models.PositiveIntegerField(verbose_name=u'字体大小')
    period = models.PositiveIntegerField(verbose_name=u'采集周期')
    start_time = models.TimeField(verbose_name=u'开始时间')
    end_time = models.TimeField(verbose_name=u'结束时间')
    create_time = models.TimeField(verbose_name=u'创建时间', auto_now_add=True)
    creator = models.CharField(verbose_name=u'创建人', max_length=10)
    editor = models.CharField(verbose_name=u'编辑人', max_length=10)
    edit_time = models.DateTimeField(verbose_name=u'修改时间', auto_now=True)
    status = models.PositiveIntegerField(verbose_name=u'监控状态')
    contents = models.CharField(verbose_name=u'显示内容',max_length=500)

    def __str__(self):
        return self.id


    class Meta:
        verbose_name = u'监控项信息表'
        verbose_name_plural = u'监控项信息'
        db_table = 'tb_monitor_item'


class Job(models.Model):
    job_id = models.PositiveIntegerField(verbose_name=u'关联ID')
    instance_id = models.PositiveIntegerField(verbose_name=u'作业实列ID')
    status = models.PositiveIntegerField(verbose_name=u'作业状态')
    test_flag = models.PositiveIntegerField(verbose_name=u'测试标识')
    start_time = models.TimeField(verbose_name=u'开始时间',auto_now_add=True)
    job_log = models.CharField(verbose_name=u'作业日志', max_length=5000)

    class Meta:
        verbose_name = u'作业实列表'
        verbose_name_plural = u'作业实列信息'
        db_table = 'td_job_instance'

#status：1表示FAILED  2表示RUNNING   3表示SUSPENDED   4表示REVOKED   5表示FINISHED
#test_flag 1表示测试  2表示非测试
class Flow(models.Model):
    flow_id = models.PositiveIntegerField(verbose_name=u'关联ID')
    instance_id = models.PositiveIntegerField(verbose_name=u'流程实列ID')
    status = models.PositiveIntegerField(verbose_name=u'节点状态')
    test_flag = models.PositiveIntegerField(verbose_name=u'测试标识')
    start_time = models.TimeField(verbose_name=u'开始时间',auto_now_add=True)

    class Meta:
        verbose_name = u'流程实列表'
        verbose_name_plural = u'流程实列信息'
        db_table = 'td_flow_instance'


class Flow_Node(models.Model):
    flow_id = models.PositiveIntegerField(verbose_name=u'流程ID')
    node_name = models.CharField(verbose_name=u'节点名称',max_length=50)
    start_time = models.CharField(verbose_name=u'开始时间',max_length=50)
    end_time = models.CharField(verbose_name=u'结束时间',max_length=50)

    class Meta:
        verbose_name = u'流程节点表'
        verbose_name_plural = u'流程节点信息'
        db_table = 'tb_flow_node'


class scene_monitor(models.Model):
    x = models.PositiveIntegerField(verbose_name=u'x坐标')
    y= models.PositiveIntegerField(verbose_name=u'y坐标')
    scale = models.PositiveIntegerField(verbose_name=u'比例')
    score = models.PositiveIntegerField(verbose_name=u'打分')
    order = models.PositiveIntegerField(verbose_name=u'排序')
    item = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    pos = models.ForeignKey(Scene,on_delete=models.CASCADE)
    class Meta:
        verbose_name = u'场景监控项'
        verbose_name_plural = u'场景监控项'
        db_table = "tl_scene_monitor"