# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-30 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdepartment',
            name='department_id',
            field=models.CharField(default=1, max_length=10, verbose_name='\u90e8\u95e8ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userposition',
            name='position_id',
            field=models.CharField(default=2, max_length=10, verbose_name='\u804c\u4f4dID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userloginrecord',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u767b\u9646\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8'),
        ),
    ]