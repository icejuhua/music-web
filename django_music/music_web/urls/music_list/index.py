# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/2/28 15:35
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : index.py
# @Software: PyCharm
from django.urls import path
from music_web.view.music_list.add_favorite_music_list import Add_Favorite_Music
from music_web.view.music_list.del_favorite_music_list import Del_Favorite_Music_List
from music_web.view.music_list.download_music import DownLoad_Music
urlpatterns = [
    path("add-favorite-music/",Add_Favorite_Music.as_view(),name="addFavoriteMusic"),
    path("del-favorite-music/",Del_Favorite_Music_List.as_view(),name="delFavoriteMusic"),
    path("download-music/",DownLoad_Music.as_view(),name="downloadmusic"),
]