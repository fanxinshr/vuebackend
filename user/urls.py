# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：backend 
@File    ：urls.py
@Author  ：樊昕
@Contact ：fanxin.hit(a)gmail.com
@Date    ：2025/01/03 21:54 
@explain : 文件说明
'''

from django.urls import  path
from user.views import TestView, JwtTestView,LoginView,MyTest

urlpatterns = [
    # 测试用
    path('test',TestView.as_view(),name='test'),
    # JWT测试
    path('jwttest',JwtTestView.as_view(),name='jwttest'),
    # 登录
    path('login',LoginView.as_view(),name='login'),
    # 测试用
    path('mytest',MyTest.as_view(),name='mytest'),

]
