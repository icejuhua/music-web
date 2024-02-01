# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/17 17:16
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : changeinfo.py
# @Software: PyCharm
import json

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from music_web.models.user.music_user import Music_User
from rest_framework.views import APIView


class ChangeInfo(APIView):
    permission_classes = ([IsAuthenticated])  # 用于验证

    def post(self,request):
        data = json.loads(request.body.decode('utf-8'))

        name = data.get('name','').strip()
        info = data.get('info','').strip()

        music_user = Music_User.objects.get(user = request.user)
        music_user.name = name
        music_user.info = info
        music_user.save()

        return Response({
            "error_msg":"success"
        })


