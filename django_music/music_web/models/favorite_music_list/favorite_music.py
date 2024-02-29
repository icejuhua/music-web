# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/5 10:25
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : music_user.py
# @Software: PyCharm
from django.db import models

class Favorite_Music(models.Model):
    user_id = models.IntegerField()
    music_id = models.IntegerField()


