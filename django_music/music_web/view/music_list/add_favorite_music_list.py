# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/2/28 15:24
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : add_favorite_music_list.py
# @Software: PyCharm
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from music_web.models.favorite_music_list.favorite_music import Favorite_Music

class Add_Favorite_Music(APIView):
    permission_classes = ([IsAuthenticated])  # 用于验证

    def post(self,request):
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get("user_id","")
        music_id = data.get("music_id","")
        if Favorite_Music.objects.filter(user_id=user_id,music_id=music_id):
            return Response({
                "error_msg":"is_add"
            })


        if not user_id:
            return Response({
                "error_msg":"用户id为空"
            })
        if not music_id:
            return Response({
                "error_msg":"音乐id为空"
            })
        #创建数据库对象，插入数据
        Favorite_Music.objects.create(user_id=user_id,music_id=music_id)
        return Response({
            "error_msg":"success"
        })




