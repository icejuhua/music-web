# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/5 16:58
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : register.py
# @Software: PyCharm
import json

from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from django_music import settings
from music_web.models.user.music_user import Music_User


class Register_Api(APIView):
    # def get(self, request):
    #     return Response(...)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))  # 使用axios时候必须用这样来获取JSON数据，再进行处理

        username = data.get("username","").strip()
        name = data.get("name","").strip()
        password = data.get("password","").strip()
        password_confim = data.get("password_confirm","").strip()
        info = data.get("info","").strip()

        if not username or not password:
            return Response({
                "error_msg" : "用户名和密码不能为空"
            })
        if not name:
            return Response({
                "error_msg": "昵称不能为空"
            })
        if password != password_confim:
            return Response({
                "error_msg":"密码不一致"
            })
        if User.objects.filter(username=username).exists():
            return Response({
                "error_msg": "用户已经存在"
            })
        user = User(username=username)
        user.set_password(password)
        user.save()
        if not info:
            info = "该用户很懒，什么都没写"
        image_path = settings.VATE_URL+'image/'+username+'.png'
        print(image_path)
        Music_User.objects.create(user=user,info=info,name=name,photo_path=image_path)



        return Response({
            "error_msg": "success"
        })



    # def put(self, request, pk):
    #     ...
    #     return Response(...)
    #
    # def delete(self, request, pk):
    #     ...
    #     return Response(...)