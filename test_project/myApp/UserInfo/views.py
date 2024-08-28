from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password,check_password

from UserInfo.models import User
import json

# Create your views here.
def regester(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirmPassword')
    email = request.POST.get('email')
    gender = request.POST.get('gender')
    try:
        # 尝试获取用户名，如果存在则抛出 ObjectDoesNotExist 异常
        user_obj = User.objects.get(name__exact=user)
    except ObjectDoesNotExist:
        # 如果不存在，且两次输入密码完全一致，则创建新用户
        if password == confirmPassword:
            try:
                user_obj = User(name=user, password=make_password(password), email=email, gender=gender)
                user_obj.save()
            except Exception as e:
                print('发生未知错误，原因为: ',e)
                return JsonResponse({'codestatus': 2, 'message': '注册失败，发生未知错误'}, safe=False)
            else:
                return JsonResponse({'codestatus': 1, 'message': '注册成功'}, safe=False)
        else:
            return JsonResponse({'codestatus': 3, 'message': '注册失败，两次输入密码不一致'}, safe=False)
    else:
        return JsonResponse({'codestatus': 2, 'message': '注册失败，该用户名已注册'}, safe=False)
    
def login(request):
    username = request.POST.get('user')
    password = request.POST.get('password')
    if username and password:
        try:
            user = User.objects.get(name__exact=username)
        except:
            return JsonResponse({'loginstatus':2,'message':'该账号未注册'},safe=False) #未注册返回2
        
        if check_password(password, user.password):
            is_superuser = user.isSuperUser
            return JsonResponse({'loginstatus':1,'isSuperUser': is_superuser,'message':'登陆成功','userID':user.id},safe=False) #登陆成功返回1
    return JsonResponse({'loginstatus':3,'message':'密码错误'},safe=False) #密码错误返回3
    
    