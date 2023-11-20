# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/10/31 14:35
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : urls.py
# @Software: PyCharm
from music_web.views import *
from django.urls import path,include


urlpatterns = [
    path("",index_test,name = "index"),
    path("vue_test/",vue_test,name="vue_test"),
    path("login_test/",login_test,name="login_test")


]