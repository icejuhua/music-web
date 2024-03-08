# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/3/7 9:46
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : get_commnets_info.py
# @Software: PyCharm


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from music_web.models.music.comments import Comments
from music_web.models.music.music import Music
from music_web.models.user.music_user import Music_User

class Get_Comments_Info(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self,request):
        music_id = request.GET.get("music_id")
        user_id = request.GET.get("user_id")

        if not user_id:
            return Response({
                "code": 500,
                "error_msg": "用户id不能为空"
            })

        if not music_id:
            return Response({
                "code":500,
                "error_msg":"音乐id不能为空"
            })
        # 用户可能为空
        user = Music_User.objects.filter(id=user_id)[0]
        music = Music.objects.get(id=music_id)
        comment_list = Comments.objects.filter(music=music)
        res_list = []
        for comment in comment_list:
            #处理时间
            comment_date = comment.comments_time
            comment_date = comment_date.strftime("%Y-%m-%d %H:%M:%S")
            #判断一下当前评论是不是当前用户发出的
            if comment.user == user:
                is_own = True
            else:
                is_own = False

            data = {
                "user_name":comment.user.name,
                "music_name":comment.music.music_name,
                "comments_text":comment.comments_text,
                "create_time":comment_date,
                "is_own":is_own,
                "comment_id":comment.id
            }
            res_list.append(data)

        return Response({
            "code":200,
            "comments":res_list,
            "error_msg":"success"
        })



