# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='monitor_type',
            field=models.CharField(max_length=10, verbose_name='\u76d1\u63a7\u9879\u7c7b\u578b'),
        ),
    ]
