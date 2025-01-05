# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：backend 
@File    ：view.py
@Author  ：樊昕
@Contact ：fanxin.hit(a)gmail.com
@Date    ：2025/01/05 21:05 
@explain : 文件说明
'''
from django.shortcuts import render

def index(request):
    return render(request, '../templates/index.html')