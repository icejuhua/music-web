# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/30 14:47
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : uploadHeadImage.py
# @Software: PyCharm
import json
import qiniu
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from qiniu import Auth
from qiniu import CdnManager
from django.conf import settings


#获取上传的token，上传图片的实际逻辑还是在前端操作
class uploadImg(APIView):

    permission_classes = ([IsAuthenticated])  # 用于验证
    def post(self,request):
        q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
        data = json.loads(request.body.decode('utf-8'))  # 使用axios时候必须用这样来获取JSON数据，再进行处理
        # 要上传的空间
        bucket_name = 'icejuhua'
        # 上传后保存的文件名
        key = data.get("key_name", "").strip()
        key = "image/"+key + '.png'
        print(key)
        # 生成上传 Token，可以指定过期时间等
        upload_token = q.upload_token(bucket_name, key, 3600)

        return Response({
            "upload_token":upload_token,
            "image_name":key
        })

class reFreshCDN(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self,request):
        print("refresh")
        # 账户ak，sk
        access_key = settings.QINIU_ACCESS_KEY
        secret_key = settings.QINIU_SECRET_KEY
        auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
        cdn_manager = CdnManager(auth)
        #取出请求的名字，拼接成url
        data = json.loads(request.body.decode('utf-8'))
        user_name = data.get("user_name", "").strip()
        if user_name is None:
            return Response({
                "error_msg":"请先登录"
            })
        url = settings.VATE_URL+'image/'+user_name+'.png'
        print(url)
        # 需要刷新的文件链接
        urls = [
            url
        ]
        # 刷新链接
        refresh_url_result = cdn_manager.refresh_urls(urls)

        return Response({
            "error_msg" : "success"
        })
