# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/2/20 17:15
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : index.py
# @Software: PyCharm
from django.urls import path
from music_web.view.mainview.get_music_info import GetMusicInfo
urlpatterns = [
    path("get-music-info/",GetMusicInfo.as_view(),name='getmusicinfo')

]