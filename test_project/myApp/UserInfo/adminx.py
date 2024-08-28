import xadmin
from xadmin.views import CommAdminView
from .models import *

#网页头部导航标题 底部信息
#定制xadmin
class GlobalSetting(object):
    site_title='书籍管理系统后台'
    site_footer='create By Deen_Li'
    menu_style='accordion'

class UserBookCollectionAdmin(object):
    list_display = ('id', 'user', 'book', 'notes', 'collected_at')
    list_display_links = ('id', 'user', 'book')
    list_filter = ('id', 'user', 'book')
    list_per_page = 20
    search_fields = ('id', 'user', 'book')
class UserAdmin(object):
    model_icon = 'fa fa-wrench'
    list_display = ('id', 'name', 'password', 'gender', 'email', 'created_at','isSuperUser')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 20
    
class UserBookClickAdmin(object):
    model_icon = 'fa fa-wrench'
    list_display = ('book', 'user', 'clicked_at')
    list_display_links = ('book', 'user', 'clicked_at')
    list_filter = ('book',)
    search_fields = ('book',)
    list_per_page = 20
    

xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(UserBookCollection, UserBookCollectionAdmin)
xadmin.site.register(User, UserAdmin)
xadmin.site.register(UserBookClick, UserBookClickAdmin)
