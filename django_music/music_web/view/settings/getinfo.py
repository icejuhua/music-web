# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/4 14:08
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : getinfo.py
# @Software: PyCharm
import json
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from music_web.models.user.music_user import Music_User

class GetInfo_Api(APIView):
    permission_classes = ([IsAuthenticated])#用于验证
    def get(self,request):
        user = request.user
        #根据登录的用户返回数据给前端
        music_user = Music_User.objects.get(user=user)
        return Response({
            "user_id":music_user.id,
            "username":music_user.user.username,
            "name":music_user.name,
            "photo_path":music_user.photo_path,
            "role":music_user.role,
            "info":music_user.info,
            "error_msg": "success",
        })

