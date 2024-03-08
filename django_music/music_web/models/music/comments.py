# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/3/6 16:24
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : comments.py
# @Software: PyCharm
from django.db import models
from music_web.models.user.music_user import Music_User
from music_web.models.music.music import Music

class Comments(models.Model):
    # user_id = models.IntegerField()
    # music_id = models.IntegerField()
    user = models.ForeignKey(Music_User,on_delete=models.CASCADE)
    music = models.ForeignKey(Music,on_delete=models.CASCADE)
    comments_text = models.TextField()
    comments_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name}在{self.music.music_name}的评论"