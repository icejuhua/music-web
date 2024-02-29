# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/2/29 15:32
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : download_music.py
# @Software: PyCharm
from django.http import HttpResponse
from pydub import AudioSegment
import requests
import tempfile
import os

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import shutil
class DownLoad_Music(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self,request):
        # 远程服务器上的音频文件 URL
        remote_audio_url = "https://zd.vatebur.cn/0002.flac"  # 替换为实际的音频文件 URL

        # 从远程服务器下载音频文件
        response = requests.get(remote_audio_url)
        print("下载完成")
        # 创建临时文件保存下载的音频数据
        with tempfile.NamedTemporaryFile(delete=False) as temp_download_file:
            temp_download_file.write(response.content)
        print("保存临时文件1")
        # 使用Pydub加载临时文件中的音频数据
        audio = AudioSegment.from_file(temp_download_file.name, format="flac")
        print("加载音频完成")
        # 将音频文件转换为MP3格式并保存到另一个临时文件
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_mp3_file:
            mp3_audio = audio.export(temp_mp3_file.name, format="mp3")
        print("保存为另一个临时文件")
        # 读取临时MP3文件内容并返回给用户
        with open(mp3_audio.name, 'rb') as file:
            response = HttpResponse(file.read(), content_type='audio/mpeg')
            response['Content-Disposition'] = 'inline; filename="output.mp3"'

        target_folder = "path/to/your/target/folder"  # 替换为你想要保存文件的目标文件夹路径
        mp3_file_path = os.path.join(target_folder, "output.mp3")

        shutil.move(temp_mp3_file.name, mp3_file_path)
        print("MP3 文件保存成功:", mp3_file_path)


        # 删除临时文件
        os.unlink(temp_download_file.name)
        os.unlink(temp_mp3_file.name)

        return response