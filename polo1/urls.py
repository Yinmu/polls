#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Administrator
@file: urls.py
@time: 2019/09/19
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]