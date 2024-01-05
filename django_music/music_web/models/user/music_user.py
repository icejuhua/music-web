# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/5 9:29
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : music_user.py
# @Software: PyCharm
from django.db import models
from django.contrib.auth.models import User

class Music_User(models.Model):
    #让Django中自带的User表中和这个表一一对应起来，并且当User表执行删除操作的时候，这个表也同步执行删除
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,default="user")#用户昵称
    role = models.IntegerField(default=1)#用户角色
    photo_path = models.CharField(max_length=556,default="/test/")#头像 为空给个默认头像
    info = models.TextField(max_length=5,default="该用户很懒，什么都没输入")


    #这个函数作用是在后台中，在这个表的界面中显示内容，这里显示的是user的名字
    def __str__(self):
        return str(self.user)

# class Test3(models.Model):
#     Test_id = models.IntegerField(max_length=200)
#     Test_char = models.CharField(max_length=100)
