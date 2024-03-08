# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/2/7 14:21
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : music.py
# @Software: PyCharm
from django.db import models


class Music(models.Model):
    music_name = models.CharField(null=True,default="未知歌曲",max_length=500)
    music_path = models.URLField(null=True,default="/music/test/")
    music_image = models.URLField(null=True,default="/test/")
    music_lrc_path = models.URLField(null=True,blank=True)

    music_total_time = models.FloatField()
    music_creater = models.CharField(null=True,default="未知创作家",max_length=200)
    music_upload_user_id = models.IntegerField(null=True,blank=True)#允许为空为了直接添加数据比较方便
    music_upload_time = models.DateTimeField(auto_now=True)#每次保存的时候自动储存时间，前端就不需要操作了
    music_type = models.CharField(null=True,blank=True,max_length=50)#上传的音乐类型
    music_info = models.TextField(null=True,blank=True,default="该歌曲暂未添加介绍")
    music_level = models.IntegerField(default=1)


    def __str__(self):
        return str(self.music_name)
