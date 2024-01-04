# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/4 16:38
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : index.py
# @Software: PyCharm
from music_web.views import *
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #path('', name="index"),
    # 获取token和刷新token 可以替代登录api
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

