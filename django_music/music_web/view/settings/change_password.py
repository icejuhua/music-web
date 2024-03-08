# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/3/8 16:48
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : change_password.py
# @Software: PyCharm
import json

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class Change_PassWord(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self,request):
        data = json.loads(request.body.decode("utf-8"))
        old_password = data.get("old_password","").strip()
        new_password = data.get("new_password","").strip()
        confirm_password = data.get("confirm_password","").strip()
        if not old_password and not new_password and not confirm_password:
            return Response({
                "code":500,
                "error_msg":"旧密码，新密码，确认密码为空"
            })

        print(request.user)
        print(old_password)

        return Response({
            "code":200,
            "error_msg":"success"
        })




