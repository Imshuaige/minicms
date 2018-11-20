# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Column(models.Model):
	name = models.CharField('Column_name',max_length=256)
	slug = models.CharField('Column_url',max_length=256,db_index=True)
	intro  = models.TextField('Section_profile',default='')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Column'
		verbose_name_plural = 'Column'
		ordering = ['name']

@python_2_unicode_compatible
class Article(models.Model):
	column  = models.ManyToManyField(Column,verbose_name='Attribution_columns')
	title = models.CharField('Title',max_length=256)
	slug = models.CharField('URL',max_length=256,db_index=True)
	author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='Writer')
	content = models.TextField('Content',default='',blank=True)
	published = models.BooleanField('Released',default=True)
	pub_date = models.DateTimeField('Publish_date',auto_now_add=True,editable=True)
	update_time = models.DateTimeField('Update_date',auto_now=True,null=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Course'
		verbose_name_plural = 'Course'

