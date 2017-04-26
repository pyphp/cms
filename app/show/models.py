# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Show(models.Model):
	ip = models.CharField(default='',max_length=32,verbose_name=u'ip地址')
	address =models.CharField(default='',max_length=32,verbose_name=u'地址')
	access_time = models.CharField(default='',max_length=32,verbose_name=u'访问时间')
	source = models.CharField(default='',max_length=500,verbose_name=u'来源')	
	keywords = models.CharField(default='',max_length=100,verbose_name=u'搜索词')
	is_sem = models.CharField(default='no',choices=(('yes',u'是'),('no',u'否')),max_length=5,verbose_name=u'是否推广')
	entrance = models.CharField(default='',max_length=1000,verbose_name=u'入口页面')
	page_total = models.IntegerField(default=1,max_length=10,verbose_name=u'页面数')
	last_page = models.CharField(default='',max_length=1000,verbose_name=u'最后停留')
	last_time = models.CharField(default='',max_length=100,verbose_name=u'上一次访问')
	user_type = models.CharField(default='new',choices=(('new',u'新用户'),('old',u'老用户')),max_length=3,verbose_name=u'用户类型')
	access_os = models.CharField(default='',max_length=50,verbose_name='操作系统')
	access_isp = models.CharField(default='',max_length=50,verbose_name='运营商')
	access_screen = models.CharField(default='',max_length=100,verbose_name='屏幕分辨率')
	access_page = models.CharField(default='',max_length=300,verbose_name='访问页面')

	class Meta:
		verbose_name = '统计表'
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.ip
			