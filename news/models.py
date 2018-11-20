# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Column(models.Model):
	name = models.CharField('类别名字',max_length=256)
	slug = models.CharField('类别网址',max_length=256,db_index=True)
	intro  = models.TextField('类别简介',default='')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '类别'
		verbose_name_plural = '类别'
		ordering = ['name']   #排序方式--按照name属性排序

@python_2_unicode_compatible
class Article(models.Model):
	column  = models.ManyToManyField(Column,verbose_name='类别归属')
	title = models.CharField('标题',max_length=256)
	slug = models.CharField('网址',max_length=256,db_index=True)
	author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='皮皮友')
	content = models.TextField('说明',default='',blank=True)
	published = models.BooleanField('正式发布',default=True)
	pub_date = models.DateTimeField('发布时间',auto_now_add=True,editable=True)
	update_time = models.DateTimeField('更新时间',auto_now=True,null=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '嘻嘻'
		verbose_name_plural = '嘻嘻'

