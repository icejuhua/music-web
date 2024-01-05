# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/4 16:41
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : music_user.py
# @Software: PyCharm

from django.urls import path,include
import music_web.urls.settings.index

urlpatterns = [
    #path('',name="index"),
    path('settings/',include(music_web.urls.settings.index))


]