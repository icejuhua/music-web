# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/3/8 15:01
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : del_comment.py
# @Software: PyCharm
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from music_web.models.music.comments import Comments
from music_web.models.user.music_user import Music_User
class Del_Comment(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self,request):
        data = json.loads(request.body.decode("utf-8"))
        comment_id = data.get("comment_id","")
        user_id = data.get("user_id","")
        if not comment_id:
            return Response({
                "code":500,
                "error_msg":"评论id不能为空"
            })
        if not user_id:
            return Response({
                "code":500,
                "error_msg":"用户id不能为空"
            })
        user = Music_User.objects.get(id = user_id)
        comment = Comments.objects.filter(id = comment_id,user=user)[0]

        if not comment:
            return Response({
                "code":500,
                "error_msg":"评论不存在"
            })
        #删除评论
        comment.delete()
        return Response({
            "code":200,
            "error_msg":"success"
        })


