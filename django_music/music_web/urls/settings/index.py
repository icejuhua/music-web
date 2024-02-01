# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/4 16:38
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : music_user.py
# @Software: PyCharm
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from music_web.view.settings.register import Register_Api
from music_web.view.settings.getinfo import GetInfo_Api
from music_web.view.settings.test import AutuTest
from music_web.view.settings.changeinfo import ChangeInfo
from music_web.view.settings.uploadHeadImage import uploadImg

urlpatterns = [
    #path('', name="index"),
    # 获取token和刷新token 可以替代登录api
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #注册
    path('register/',Register_Api.as_view(),name='register_api'),
    #获取用户信息
    path("getinfo/",GetInfo_Api.as_view(),name='getinfo_api'),
    #测试
    path("Aututest/",AutuTest.as_view(),name='test'),
    #修改个人信息
    path("changeinfo/",ChangeInfo.as_view(),name='changeinfo'),
    #获取上传七牛云的token
    path("upload-token/",uploadImg.as_view(),name='uploadImg')

]

