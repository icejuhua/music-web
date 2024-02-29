# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/2/29 10:50
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : del_favorite_music_list.py
# @Software: PyCharm
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from music_web.models.favorite_music_list.favorite_music import Favorite_Music

class Del_Favorite_Music_List(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self,request):
        data = json.loads(request.body.decode("utf-8"))
        user_id = data.get("user_id","")
        music_id = data.get("music_id","")

        if not user_id:
            return Response({
                "error_msg":"用户id为空"
            })

        if not music_id:
            return Response({
                "error_msg":"音乐id为空"
            })
        Favorite_Music.objects.get(user_id=user_id,music_id=music_id).delete()
        return Response({
            "error_msg":"success"
        })

