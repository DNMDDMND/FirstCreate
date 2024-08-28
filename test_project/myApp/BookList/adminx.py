import xadmin
from .models import *

# list_display 控制列表展示的字段
# search_fields 控制可以通过搜索框搜索的字段名称，xadmin使用的是模糊查询
# list_filter 可以进行过滤操作的列
# ordering 默认排序的字段
# readonly_fields 在编辑页面的只读字段
# exclude 在编辑页面隐藏的字段
# list_editable 在列表页可以快速直接编辑的字段
# show_detail_fileds 在列表页提供快速显示详情信息
# refresh_times 指定列表页的定时刷新
# list_export 控制列表页导出数据的可选格式
# show_bookmarks 控制是否显示书签功能
# data_charts 控制显示图标的样式
# model_icon 控制菜单的图标

class BookBasicAdmin(object):
    model_icon = 'fa fa-wrench'
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at','click_count')
    list_display_links = ('id', 'title','click_count')
    list_filter = ('id', 'title', 'author')
    search_fields = ('id', 'title', 'author')
    list_per_page = 20


class BookChapterAdmin(object):
    model_icon = 'fa fa-wrench'
    list_display = ('id', 'book', 'title', 'order', 'created_at')
    list_display_links = ('id', 'book', 'title')
    list_filter = ('id', 'book', 'title')
    search_fields = ('id', 'book', 'title')
    list_per_page = 20
    

xadmin.site.register(BookBasic, BookBasicAdmin)
xadmin.site.register(BookChapter, BookChapterAdmin)
