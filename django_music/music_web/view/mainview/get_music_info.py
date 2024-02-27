# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/2/20 17:15
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : get_music_info.py
# @Software: PyCharm
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from music_web.models.music.music import Music
from rest_framework.response import Response

class GetMusicInfo(APIView):
    permission_classes = ([IsAuthenticated])  # 用于验证
    def get(self,request):
        #获取数据库中所有的数据
        music_list = Music.objects.all()
        res_list = []
        for music in music_list:
            formatted_music = {
                "name": music.music_name,
                "artist": music.music_creater,
                "url": music.music_path,
                "cover": music.music_image,
                "lrc": music.music_lrc_path,
                "total_time":music.music_total_time
            }

            res_list.append(formatted_music)



        return Response({
            "music_list":res_list
        })