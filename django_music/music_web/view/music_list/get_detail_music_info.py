# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/3/5 10:53
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : get_detail_music_info.py
# @Software: PyCharm


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from music_web.models.music.music import Music

class Get_Detail_Music_Info(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self,request):
        music_id = request.GET.get("music_id")
        if not music_id:
            return Response({
                "code":500,
                "error_msg":"id不能为空"
            })
        music = Music.objects.get(id = music_id)


        music_data = {
            "music_name" : music.music_name,
            "music_image_path" : music.music_image,
            "music_total_time" : music.music_total_time,
            "music_info" : music.music_info,
            "music_level" : music.music_level,
            "music_artist":music.music_creater,
        }
        return Response({
            "code":200,
            "error_msg":"success",
            "music_data":music_data
        })