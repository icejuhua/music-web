import json

from django.contrib.auth import authenticate
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from .models import Test_User
# Create your views here.


def index_test(request):
    return HttpResponse("这是主界面")
@csrf_exempt
def vue_test(request):
    print(request.POST)
    return HttpResponse("successful")
@csrf_exempt
def login_test(request):
    data = json.loads(request.body.decode('utf-8')) #获取JSON数据，再进行处理
    msg = {"error_msg":"success"}

    Useraccount = data.get("username")
    Password = data.get("password")
    User = Test_User.objects.filter(User_Account=Useraccount)
    print(Useraccount,Password)
    if User.exists() :
        if User[0].User_Pwd == Password:
            msg["error_msg"] = "success"
        else:
            msg["error_msg"] = "密码错误"
    else:
        msg["error_msg"] = "用户不存在"
    #Username = User.User_Account
    #Password = User.User_Pwd

    return JsonResponse(msg,safe=False)

class LoginView(APIView):
    def post(self,request):
        data = json.loads(request.body.decode('utf-8'))  # 获取JSON数据，再进行处理
        Useraccount = data.get("username")
        Password = data.get("password")


        print("user",Useraccount,Password)
        user = authenticate(User_Account="13363123")
        print(f"查找到的用户是{user}")
        if user is not None:
            token,created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token':token.key,'error_msg':"success"})
        else:
            return JsonResponse({'error_msg': "falled"})
