"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.views.static import serve

from myApp.UserInfo import views as UserView
from myApp.BookList import views as BookView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    
    #加载静态资源,在前端显示封面图片
    re_path(r'^media/bookCover(?P<path>.*)$', serve, {'document_root': BookView.AVATAR_ROOT}),
    re_path(r'^media/bookContent(?P<path>.*)$', serve, {'document_root': BookView.CONTENT_ROOT}),
    
    #userInfo相关
    path('userInfo/login/', UserView.login),
    path('userInfo/regester/', UserView.regester),
    
    #Home相关
    path('bookList/getallbook/', BookView.getAllBook),
    path('bookList/recordinfo/', BookView.recordInfo),
    
    #BookList相关
    path('bookList/getbooktype/', BookView.getBookType),
    path('bookList/avatarupload/', BookView.avatarUpload),
    path('bookList/contentupload/', BookView.contentupload),
    path('bookList/getbooklist/', BookView.submitBookList),
    path('bookList/getbookcategory/', BookView.getBookCategory),
    
    #BookDetail相关
    path('bookList/getbookinfo/', BookView.getBookInfo),
    
    #ChapterDetail相关
    path('bookList/getchapter/', BookView.getChapter),
    
    #DataStatistics相关
    path('bookList/getallrecorddata/', BookView.getallrecorddata),
]
