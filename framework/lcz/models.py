# -*- coding: utf-8 -*-
from django.db import models

class Conn(models.Model):
    connname = models.CharField(u'连接名称',max_length=30)
    type = models.CharField(u'连接类型',max_length=30)
    ip = models.CharField(u'ip地址',max_length=30)
    port = models.CharField(u'端口',max_length=50)
    username = models.CharField(u'用户名',max_length=155)
    databasename = models.CharField(u'数据库名称',max_length=125)
    password = models.CharField(u'密码',max_length=155)

class TDataBase(models.Model):
    name = models.CharField(u'数据库名称',max_length=30)
