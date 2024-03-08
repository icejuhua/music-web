# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/3/7 16:34
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : add_comment.py
# @Software: PyCharm
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from music_web.models.music.music import Music
from music_web.models.user.music_user import Music_User
from music_web.models.music.comments import Comments
class Add_Comment(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self,request):
        data = json.loads(request.body.decode("utf-8"))
        user_id = data.get("user_id","")
        music_id = data.get('music_id',"")
        comments_text = data.get("comments_text","")

        if not user_id:
            return Response({
                "code":500,
                "error_msg":"用户id不能为空"
            })
        if not music_id:
            return Response({
                "code":500,
                "error_msg":"音乐id不能为空",
            })
        user = Music_User.objects.get(id=user_id)
        music = Music.objects.get(id=music_id)
        Comments.objects.create(user=user,
                                          music=music,
                                          comments_text=comments_text)
        return Response({
            "code":200,
            "error_msg":"success"
        })


