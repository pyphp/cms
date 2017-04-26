#coding:utf-8

import xadmin
from xadmin import views
from .models import Show

class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True
class GlobalSetting(object):
	site_title = 'longge'
	site_footer = 'powerd by longge'
	menu_style = "accordion"					

class ShowAdmin(object):
	list_display = ('ip','address','keywords','access_page','access_time','source','is_sem','user_type')
xadmin.site.register(Show,ShowAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)