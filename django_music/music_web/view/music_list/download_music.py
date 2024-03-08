# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/2/29 15:32
# @Author : lanlan
# @Email : lanlan_bupt@126.com
# @File : download_music.py
# @Software: PyCharm
import json

from django.http import HttpResponse
from pydub import AudioSegment
import requests
import tempfile
import os
from django.http import StreamingHttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import shutil
class DownLoad_Music(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self,request):
        #取出数据
        data = json.loads(request.body.decode("utf-8"))
        url = data.get("url","").strip()
        music_type = data.get("music_type","").strip()
        music_name = data.get("music_name","").strip()
        encode_type = data.get("encode_type","").strip()
        music_type = music_type.split('.')[-1]

        print(url,music_type,music_name,encode_type)

        # 远程服务器上的音频文件 URL
        remote_audio_url = url  # 替换为实际的音频文件 URL

        # 从远程服务器下载音频文件
        response = requests.get(remote_audio_url)
        print("下载完成")
        # 创建临时文件保存下载的音频数据
        with tempfile.NamedTemporaryFile(delete=False) as temp_download_file:
            temp_download_file.write(response.content)
        print("保存临时文件1")
        # 使用Pydub加载临时文件中的音频数据
        audio = AudioSegment.from_file(temp_download_file.name, format=music_type)
        print("加载音频完成")
        # 将音频文件转换为MP3格式并保存到另一个临时文件
        with tempfile.NamedTemporaryFile(suffix='.'+encode_type, delete=False) as temp_mp3_file:
            mp3_audio = audio.export(temp_mp3_file.name, format=encode_type)
        print("保存为另一个临时文件")

        print(mp3_audio.name)
        # 读取临时MP3文件内容并返回给用户
        with open(mp3_audio.name, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename={0}'.format(music_name+'.'+encode_type)
        # target_folder = "./"  # 替换为你想要保存文件的目标文件夹路径
        # mp3_file_path = os.path.join(target_folder, "output.mp3")
        #
        # # 获取绝对路径
        # absolute_mp3_file_path = os.path.abspath(mp3_file_path)
        # print("MP3 文件保存的绝对路径:", absolute_mp3_file_path)
        #
        #
        #
        # shutil.move(mp3_audio.name, mp3_file_path)
        # print("MP3 文件保存成功:", mp3_file_path)


        # 删除临时文件
        os.unlink(temp_download_file.name)
        os.unlink(mp3_audio.name)

        return response