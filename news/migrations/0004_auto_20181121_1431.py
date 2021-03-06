# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-21 06:31
from __future__ import unicode_literals

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20181120_0656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '这个是么子', 'verbose_name_plural': '么子鸭'},
        ),
        migrations.AlterModelOptions(
            name='column',
            options={'ordering': ['name'], 'verbose_name': '类别', 'verbose_name_plural': '类别'},
        ),
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='首页显示'),
        ),
        migrations.AddField(
            model_name='column',
            name='nav_dispaly',
            field=models.BooleanField(default=False, verbose_name='导航显示'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='皮皮友'),
        ),
        migrations.AlterField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(to='news.Column', verbose_name='类别归属'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=True, verbose_name='正式发布'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=256, unique=True, verbose_name='网址'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='column',
            name='intro',
            field=models.TextField(default='', verbose_name='类别简介'),
        ),
        migrations.AlterField(
            model_name='column',
            name='name',
            field=models.CharField(max_length=256, verbose_name='类别名字'),
        ),
        migrations.AlterField(
            model_name='column',
            name='slug',
            field=models.CharField(db_index=True, max_length=256, verbose_name='类别网址'),
        ),
    ]
