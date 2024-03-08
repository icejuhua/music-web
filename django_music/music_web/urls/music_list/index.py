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
from music_web.view.music_list.get_detail_music_info import Get_Detail_Music_Info
from music_web.view.comment.get_commnets_info import Get_Comments_Info
from music_web.view.comment.add_comment import Add_Comment
from music_web.view.comment.del_comment import Del_Comment
urlpatterns = [
    path("add-favorite-music/",Add_Favorite_Music.as_view(),name="addFavoriteMusic"),
    path("del-favorite-music/",Del_Favorite_Music_List.as_view(),name="delFavoriteMusic"),
    path("download-music/",DownLoad_Music.as_view(),name="downloadmusic"),
    path("get-detail-music-info/",Get_Detail_Music_Info.as_view(),name="getdetailinfo"),
    #获取评论列表
    path("get-comments-info/",Get_Comments_Info.as_view(),name="getcommentsinfo"),
    #添加评论
    path("add-comments-info/",Add_Comment.as_view(),name="addcomment"),
    #删除评论
    path("del-comments-info/",Del_Comment.as_view(),name="delcomment"),
]