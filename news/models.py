# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
#add new Field
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Column(models.Model):
	name = models.CharField('类别名字',max_length=256)
	slug = models.CharField('类别网址',max_length=256,unique=True)
	intro = models.TextField('类别简介',default='')
	nav_display = models.BooleanField('导航显示',default=False)
	home_display = models.BooleanField('首页显示',default=False)

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('column',args=(self.slug,))

	class Meta:
		verbose_name = '类别'
		verbose_name_plural = '类别'
		ordering = ['name']   #排序方式--按照name属性排序

@python_2_unicode_compatible
class Article(models.Model):
	column  = models.ManyToManyField(Column,verbose_name='类别归属')
	title = models.CharField('标题',max_length=256)
	slug = models.CharField('网址',max_length=256,unique=True)
	author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='皮皮友')
	content = UEditorField('内容', height=300, width=1000,
		default=u'', blank=True, imagePath="uploads/images/",
		toolbars='besttome', filePath='uploads/files/')
	published = models.BooleanField('正式发布',default=True)
	pub_date = models.DateTimeField('发布时间',auto_now_add=True,editable=True)
	update_time = models.DateTimeField('更新时间',auto_now=True,null=True)

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('article', args=(self.pk, self.slug))
	class Meta:
		verbose_name = '哈麻皮的属性'
		verbose_name_plural = '么子鸭'

