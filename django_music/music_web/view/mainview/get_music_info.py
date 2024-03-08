# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/2/20 17:15
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : get_detail_music_info.py
# @Software: PyCharm
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from music_web.models.music.music import Music
from rest_framework.response import Response
from music_web.models.user.music_user import Music_User
from music_web.models.favorite_music_list.favorite_music import Favorite_Music
class GetMusicInfo(APIView):
    permission_classes = ([IsAuthenticated])  # 用于验证
    def get(self,request):
        #获取当前登录用户的id，以便获取歌曲是否添加到喜欢
        get_type = request.GET.get("get_type")



        user = request.user
        user_id = (Music_User.objects
                   .get(user=user).id)

        favorite_list = Favorite_Music.objects.filter(user_id=user_id)
        favorite_list = [item.music_id for item in favorite_list]
        #判断要获取的歌单是什么类型的
        music_list = None

        if get_type == "all":
            music_list = Music.objects.all()#获取数据库中所有的数据
        elif get_type == "favorite":
            music_list = Music.objects.filter(id__in=favorite_list)

        res_list = []
        for music in music_list:
            add_status = music.id in favorite_list
            formatted_music = {
                "name": music.music_name,
                "artist": music.music_creater,
                "url": music.music_path,
                "cover": music.music_image,
                "lrc": music.music_lrc_path,
                "total_time":music.music_total_time,
                "music_type":music.music_type,
                "music_id":music.id,
                "add_status":add_status,

            }


            res_list.append(formatted_music)



        return Response({
            "music_list":res_list,
            "error_msg":"success"
        })