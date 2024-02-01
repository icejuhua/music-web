# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/15 11:07
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : test.py
# @Software: PyCharm
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AutuTest(APIView):
    permission_classes = ([IsAuthenticated])  # 用于验证
    def post(self,request):
        print(request.data)
        return Response({
            "error_msg":"success"
        })

    def get(self,request):
        print(123)
        return Response({
            "error_msg":"success"
        })
