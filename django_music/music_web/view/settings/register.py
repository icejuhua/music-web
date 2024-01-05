# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/5 16:58
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : register.py
# @Software: PyCharm
from rest_framework.views import APIView
from rest_framework.response import Response


class Register_Api(APIView):
    # def get(self, request):
    #     return Response(...)

    def post(self, request):
        data = request.POST
        username = data.get("username","").strip()
        name = data.get("name","").strip()
        password = data.get("password","").strip()

        print(username,name,password)
        msg = {
            "error_msg":"success",
            "code":200
        }

        return Response(msg)

    # def put(self, request, pk):
    #     ...
    #     return Response(...)
    #
    # def delete(self, request, pk):
    #     ...
    #     return Response(...)