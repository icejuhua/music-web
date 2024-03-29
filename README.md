## 毕设锐意制作中

## 2024.3.8更新日志

好久没有写更新日志了，零零散散的加了很多东西，大部分都写完了。剩下就是改改细节

- 转码下载可以了，只不过下的很慢
- 添加了歌曲详细信息界面，可以看到作者，歌名，评论等信息
- 在详细界面添加了评论功能，能够添加或者删除自己的评论
- 修改了在新用户注册时头像没有url，导致后期更新头像无效的bug
- 修改了在提交修改信息的之后，信息获取不完全
- 编写了修改密码的api，还没测试



## 2024.2.29更新日志

- 修改了加入喜爱的图标，添加了从歌单中移除的功能
- 添加了转码下载的api，还在测试，转码传输后下载的数据不对
- 后面准备搞评论功能，就差不多了

## 2024.2.28更新日志

- 添加了喜爱音乐的数据库，和加入的功能。
- 添加喜爱音乐列表的数据库

## 2024.2.27更新日志

- 添加了主页面分页功能
- 添加了下载源文件的功能
- 添加了转码下载和加入喜爱的按钮，功能还未实现

## 2024.2.26更新日志

- 添加了歌曲到七牛云并同步到数据库中
- 添加了播放界面，使用Aplayer组件作为播放的主要工具
- 更新了歌曲列表。主界面中能显示每首歌的信息了

## 2024.2.7更新日志

- 更新了上传头像后刷新api的功能，不用手动去七牛云刷新了
- 添加了音乐模型，准备设计主界面了

## 2024.2.1更新日志

好久没有推代码了，最近比较忙写的不多

- 更新了系统可以修改个人信息，修改密码，修改头像的功能
- 头像和音频数据准备存在七牛云图传，减轻服务器负担
- 有些部分使用了element-plus ui，感觉更好用
- 添加了后端刷新七牛云CDN的API，但还没有测试。没有刷新CDN，头像提交更新后不会及时变化

## 2024.1.12更新日志

- 完善了注册功能，登录功能，能够实现登录后自动跳转并且把按钮改成用户名



## 2024.1.10更新日志

- 更新了注册功能，加入了注册提示弹框




## 2024.1.5更新日志

做了注册的界面绘制，注册的aniox。后端的注册视图还没写。修改了后端的文件结构。修改了用户模型。

## 2024.1.4更新日志

快下班的时间有空把jwt的token验证做完了。但是还没弄登录跳转，models的文件结构也需要重新整理。道阻且长阿

## 2024.1.3更新日志

懒狗了，学期结束从开始搞，更新了jwt，用户model的更新

## 配置Django

1. 租用云服务器
2. 在云服务器上配置`docker`和`tmux`
3. 把`django`的`docker`镜像导入到云服务器中`scp django_lesson_1_0.tar django:`
4. 把docker镜像导入到服务器docker中 `docker load -i django_lesson_1_0.tar`
5. ![image-20231008021115635](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008021115635.png)
6. 使用镜像生成容器`docker run -p 20000:22 -p 8000:8000 --name django_server -itd django_lesson:1.0` 端口20000映射到22 端口8000映射到8000 指定别名为`django_server`
7. 进入容器`docker attach django_server`
8. 想要离开容器的时候使用挂起容器`ctrl+p ctrl+q`  关闭容器`ctrl+d`  配置ssh登录之后就可以直接退出了
9. 因为开了新端口然后去服务器开启对应端口

## 创建Django项目

1. 使用命令`django-admin startproject acapp`创建一个项目    **目录结构图**![image-20231008030816524](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008030816524.png)
2. 使用git维护项目
3. 尽量在tmux中运行项目，防止错关
4. 运行项目![image-20231008163304854](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008163304854.png)



## 创建git仓库并且使用git维护

1. 在git仓库中创建项目
2. ![image-20231008161820617](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008161820617.png)
3. 按照仓库要求配置本地git仓库
4. ![image-20231008161939529](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008161939529.png)
5. 使用`git add .` `git commit -m "xxx"`推送到本地仓库 然后再执行`git remote add origin git@git.acwing.com:1336378093/django_game.git`
6. 执行`git push `推送到远程仓库，
7. 如果要输入密码需要配置一下远程仓库的免密登录 把id_rsa.pub中的公钥添加到远程仓库的ssh密钥中，再执行`git push`就不需要输入密码了
8. ![image-20231008162915709](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008162915709.png)
9. 在本地git根目录下可以创建一个`gitignore`文件来屏蔽一些不需要上传的文件,屏蔽格式为：`*/文件名`



## 运行django项目并且编写

1. 运行命令`python3 manange.py runserver 0.0.0.0:8000`
2. 通过ip和端口访问服务器的时候会报错，需要将当前ip添加到`ALLOWED HOST`中改文件在项目的`acapp`中的`setting`中可以使用`ag`命令进行全文搜索
3. ![image-20231008164523539](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008164523539.png)
4. ![image-20231008164533217](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008164533217.png)
5. 添加完并保存文件刷新网页就成功了运行django
6. 创建一个新的app以便我们自己编写`python3 manage.py startapp xxx`
7. app文件结构为![image-20231008165858677](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008165858677.png)
8. `admin`中存放管理员页面能够看到的数据库 `models`定义网站数据库表 `views`用来写页面
9. 管理员界面的url为`8000/admin/`但是第一次会报错，需要退出程序，执行`python3 manange.py migrate`来同步数据库修改
10. 创建管理员用户`python3 manage.py createsuperuser`按照提示创建
11. 可以将urls views model文件先删除，然后创建对应文件夹以便管理多个文件，然后需要在每一个文件夹中创建一个__ init __.py文件，不然引用时会报错。
12. 需要把项目更改为中国时区，在`serrings`文件中修改`TIME_ZONE`
13. ![image-20231009132408725](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231009132408725.png)
14. 需要把添加的app加入settings里，添加的是对应app里的apps.py文件中的类名。对应的app名在`/game/apps.py中`![image-20231012161620854](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231012161620854.png)
15. ![image-20231009132706528](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231009132706528.png)
16. 配置静态`url`翻到`settings`里最后几行，下图表示把静态文件都放到static这个文件夹中，也就对应项目目录的static
17. ![image-20231012161819067](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231012161819067.png)

### 创建页面

先创建urls.py(做路由) 和 template(存储html)文件

**配置路由：**

1. 首先在view.py中先定义好需要返回的函数
2. 在对应app下的urls中配置url和函数的绑定![image-20231008173719959](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008173719959.png)
3. 如果是访问该url则执行view中的index函数
4. 在acapp中的url配置总url![image-20231008173844682](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231008173844682.png)
5. 如果访问game/的话则跳转到game里的url去解析
6. 创建html界面，在`templates/multiedns`下创建一个名叫web.html的文件
7. 在前端文件中，如果需要引用本地路径，则可以在文件开始 添加`{% load static %}`,在需要引用本地路径的时候可以用`{% static 'css/game.css' %}`
8. 引用jquery来编写前端代码，并且新建一个js代码，把前端代码放到客户机上去渲染。
9. ![image-20231012172404868](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231012172404868.png)
10. 每个py文件夹都要创建一个`__init__.py方便管理`如urls，views
11. ![image-20231012172629733](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231012172629733.png)
12. 在views文件夹下创建一个index.py用来渲染web端
13. ![image-20231012172729911](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231012172729911.png)
14. shortcuts模块为django中渲染模块
15. 在urls文件夹下创建一个index.py.作用是把url底下分文件中的py文件引用到一起的作用。可以仿照总的urls.py的写法
16. 创建菜单背景页面



## 路由访问逻辑

首先根据url会先进acapp下的url去寻找对应的函数，比如`/admin`就能在总的url中去找到。我们在总的urls中写了

```
 path('',include('game.urls.index')),                                  │
  path('admin/', admin.site.urls),  
```

所有当路由不是`admin/`的情况下，回去game.urls.index里继续找对应的路由

而index.py里是这样的

```
path("",index,name='index'),
  6     path("menu/",include("game.urls.menu.index")),
  7     path("playground/",include("game.urls.playground.index")),
  8     path("settings/",include("game.urls.settings.index")),

```



## docker常用命令

将当前用户添加到docker用户组
为了避免每次使用docker命令都需要加上sudo权限，可以将当前用户加入安装中自动创建的docker用户组(可以参考官方文档)：

`sudo usermod -aG docker $USER`
执行完此操作后，需要退出服务器，再重新登录回来，才可以省去sudo权限。

镜像（images）
`docker pull ubuntu:20.04`:拉取一个镜像
`docker images：`列出本地所有镜像
`docker image rm ubuntu:20.04` 或` docker rmi ubuntu:20.04`：删除镜像ubuntu:20.04
`docker [container] commit CONTAINER IMAGE_NAME:TAG`:创建某个container的镜像
`docker save -o ubuntu_20_04.tar ubuntu:20.04`：将镜像ubuntu:20.04导出到本地文件ubuntu_20_04.tar中
`docker load -i ubuntu_20_04.tar`：将镜像ubuntu:20.04从本地文件ubuntu_20_04.tar中加载出来
容器(container)
`docker [container] create -it ubuntu:20.04`：利用镜像ubuntu:20.04创建一个容器。
`docker ps -a`：查看本地的所有容器
`docker [container] start CONTAINER`：启动容器
`docker [container] stop CONTAINER`：停止容器
`docker [container] restart CONTAINER`：重启容器
`docker [contaienr] run -itd ubuntu:20.04`：创建并启动一个容器
`docker [container] attach CONTAINER`：进入容器
先按Ctrl-p，再按Ctrl-q可以挂起容器
`docker [container] exec CONTAINER COMMAND`：在容器中执行命令
`docker [container] rm CONTAINER`：删除容器
docker container prune：删除所有已停止的容器
docker export -o xxx.tar CONTAINER：将容器CONTAINER导出到本地文件xxx.tar中
docker import xxx.tar image_name:tag：将本地文件xxx.tar导入成镜像，并将镜像命名为image_name:tag
docker export/import与docker save/load的区别：
export/import会丢弃历史记录和元数据信息，仅保存容器当时的快照状态
save/load会保存完整记录，体积更大
docker top CONTAINER：查看某个容器内的所有进程
docker stats：查看所有容器的统计信息，包括CPU、内存、存储、网络等信息
docker cp xxx CONTAINER:xxx 或 docker cp CONTAINER:xxx xxx：在本地和容器间复制文件
docker rename CONTAINER1 CONTAINER2：重命名容器
docker update CONTAINER --memory 500MB：修改容器限制



## django项目结构

项目文件结构
templates目录：管理html文件
urls目录：管理路由，即链接与函数的对应关系
views目录：管理http函数
models目录：管理数据库数据
static目录：管理静态文件，比如：
	css：对象的格式，比如位置、长宽、颜色、背景、字体大小等
	js：对象的逻辑，比如对象的创建与销毁、事件函数、移动、变色等
	image：图片
	audio：声音

consumers目录：管理websocket函数

## 注意点

- 在编写shell脚本的时候开头是`#!/bin/bash`
- 如果刷新后没效果可能是浏览器缓存了js和css设置，可以在f12中停用缓存
- 使用`ctrl+shift+r`刷新缓存并且刷新界面

在引入BootStrap样式的时候遇到

```
Cannot read properties of undefined (reading '__vccOpts')
TypeError: Cannot read properties of undefined (reading '__vccOpts')
    at exports.default (webpack-internal:///./node_modules/vue-loader/dist/exportHelper.js:9:22)
    at eval (webpack-internal:///./src/views/user/account/UserAccountLoginView.vue:10:123)
    at ./src/views/user/account/UserAccountLoginView.vue (http://localhost:8080/js/app.js:102:1)
    at __webpack_require__ (http://localhost:8080/js/app.js:371:33)
    at fn (http://localhost:8080/js/app.js:605:21)
    at eval (webpack-internal:///./src/router/index.js:3:98)
    at ./src/router/index.js (http://localhost:8080/js/app.js:72:1)
    at __webpack_require__ (http://localhost:8080/js/app.js:371:33)
    at fn (http://localhost:8080/js/app.js:605:21)
    at eval (webpack-internal:///./src/main.js:4:65)
```

在确认安装`JQurey`和`BootStrap`后在vue.config.js中添加

```
const webpack = require('webpack')
module.exports = {
	chainWebpack: (config) => {
		config.plugin('provide').use(webpack.ProvidePlugin, [{
			$: 'jquery',
			jquery: 'jquery',
			jQuery: 'jquery',
			'window.jQuery': 'jquery'
		}])
	},
	css: {
		sourceMap: true
	}
}
```

在注册新库的时候需要关闭应用，不然可能会报错，找不到行



- 在后端中的`settings.py`中，如果在开发环境下，`DEBUG`最好设置为True，不然访问页面不会报具体的错误
- 想要引用`settings.py`中的数据，变量必须是大写，否则报错



## DJango解决跨域问题：

使用pip安装djiango-core-headers `pip install django-cors-headers`

![image-20231031153253063](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231031153253063.png)

在项目中的`settings.py`文件修改配置

在INSTALLED_APPS中添加`coresheaders`APP，报黄不要管

![image-20231031153358609](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231031153358609.png)

在文件末尾添加配置

![image-20231031153419913](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231031153419913.png)

在CORS_ALLOWD_ORINGINS中最好不要填`*`填需要访问前端网址，填*会报错

配置完后，使用前端ajax或者form访问的时候会报错，需要CSRF令牌验证。

1.可以在前端中进行处理。

2.在访问的视图函数中添加注释`@csrf_exempt`免除CSRF令牌验证，但会降低安全性



## 在Django中使用数据库模型

在Django中，一个在model中的类就是一个数据库，使用python语句定义，然后会自动转换为sql语句

![image-20231116110032638](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231116110032638.png)

添加修改好之后，在控制台输入

` python3 manage.py makemigrations  # 让 Django 知道我们在我们的模型有一些变更
python3 manage.py migrate   # 创建表结构`

如果需要修改数据库结构也是输入以上命令就行，但是注意如果数据库中有数据的话，会让你添加默认数据，否则不能添加

在对应app中admin.py中注册模型，让后台管理能显示数据库

![image-20231116111731725](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231116111731725.png)



登录后台就能看到数据库了

![image-20231116111818430](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231116111818430.png)

如果要删除表，可以使用navicat工具连接本地数据库，删除表之后，再删除migrations下出了__init__.py的所有文件，再重构数据库

如果要使用DJango中的`jwt`验证，用户用它自带的表就好了，如果需要额外添加参数，可以在自定义表中添加需要的参数，并且把自带表中的User作为用户的基本信息就好了

在Django中自带的用户系统中

![image-20240103110820900](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20240103110820900.png)

- Avtive代表账号是否被封禁
- Staff status是否能够进入后台页面
- Superuser status 是否有超级管理员权限
- ![image-20240103110955236](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20240103110955236.png)
- 上面的是组的内容
- ![image-20240103111009798](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20240103111009798.png)
- 用户的具体权限
- ![image-20240103111029818](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20240103111029818.png)
- 登录的时间和注册时间等。

#### 修改自带用户系统的密码安全性验证

在settings.py中找到`AUTH_PASSWORD_VALIDATORS`列表，默认是有一些验证方式要求的。这里我为了方便调试全部注释掉

![image-20240105095458922](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20240105095458922.png)

具体的验证方式参考https://doc.s.djangoproject.com/zh-hans/4.2/topics/auth/passwords/#enabling-password-validation



#### 扩展自带的数据库

在model中编写需要扩展的类，`music_user`

```python
from django.db import models
from django.contrib.auth.models import User

class Music_User(models.Model):
    #让Django中自带的User表中和这个表一一对应起来，并且当User表执行删除操作的时候，这个表也同步执行删除
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo_path = models.URLField(max_length=256,blank=True)#头像
    #这个函数作用是在后台中，在这个表的界面中显示内容，这里显示的是user的名字
    def __str__(self):
        return str(self.user)
```

然后执行迁移数据库的两条命令就好了，这样就能在后台看到添加的自定义数据了





## Django中使用视图

前端采用的是`axios`异步通信的方式，使用`axios.post`传输数据的时候，vue会自动把数据封装成JSON格式，如果想在视图中取出数据，直接用`request.POST.get`的方式是取不出数据的

要用

```python
data = json.loads(request.body.decode('utf-8')) #获取JSON数据，再进行处理
msg = {"error_msg":"success"}
Useraccount = data.get("username")
Password = data.get("password")
```

的方式取出数据解析，在存放数据

在操作数据库时，引入对用模型文件中对应的函数就能直接使用了。

```python
from .models import Test_User

User = Test_User.objects.filter(User_Account=Useraccount)#使用filter而不用get是防止账号为空程序报错

```

如果要返回JSON格式，使用python中的字典数据类型，返回的时候用`JsonResponse`就好

```python
msg = {"error_msg":"success"}
return JsonResponse(msg,safe=False)
```







## Django中Rest Framework和JWT

JWT:Json web Token

当客户端第一次向服务器发送请求的时候，服务器会根据客户端发送的用户信息，生成一段jwt发送给客户端，然后客户端吧jwt暂存在浏览器中。以后每次向服务器访问的时候会带上jwt信息来进行验证。服务器在接受到消息时候会验证该请求是哪个用户发的。

### 安装使用步骤

安装 Rest Framework和JWT

`pip install djangorestframework`

`pip install pyjwt`

`pip install djangorestframework-simplejwt`

需要在`setting.py`中的`INSTALLED_APPS`添加`rest_framework`和`rest_framework_simplejwt`

在`setting.py`添加rest_framework中添加jwt验证

```
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}
```

添加jwt配置,默认access是五分钟过期，refresh14天过期

```python
from datetime import timedelta
...

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': "adwdwad1WWWWh",#自定义的随机字符串
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


```

django后续版本中推荐在`view`中使用类的方式，

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class SnippetDetail(APIView):
    def get(self, request):  # 查找
        ...
        return Response(...)

    def post(self, request):  # 创建
        ...
        return Response(...)

    def put(self, request, pk):  # 修改
        ...
        return Response(...)

    def delete(self, request, pk):  # 删除
        ...
        return Response(...)


```

添加获取jwt和刷新jwt的路由

直接在对应路由的地方添加

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
```

安装app后，需要输入命令`python3 manage.py collectstatic`

访问对应路由后会出现对应界面

![image-20231219171242833](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231219171242833.png)

登录api就是获取token



在需要使用jwt验证的类中

```python
from rest_framework.permissions import IsAuthenticated

class InfoView(APIView):
    
	permission_classes = ([IsAuthenticated])
    def get(self,request):
        return Response({
            
        })
```

在前端中，使用jqure或者anxio都需要加上验证

```
$.ajax({
	url:"xxxx",
	type:'post',
	data:{
	xxxx
	},
	headers:{
		'Authorization'+"Bearer "+access,//获取的access
	},
})
```

### 对视图进行保护

当遇到需要用户登录才能操作的视图时，比如获取信息等视图可以在方法前添加注释`@permission_classes`来保证当前视图需要验证。或者在类中申明`permission_classes = ([IsAuthenticated])#用于验证`表示当前这个类的所有方法都需要验证。

### Django中Post和Get区别

在前端使用axios传递数据的时候，默认是进行一个json封装的。并且如果后端的api需要验证post和get是有区别的

#### post

```js
//在post方法中验证头应该放在第三个参数
axios.post("http://101.43.45.110:8000/api/settings/upload-token/",{
            key_name:store.state.user.username
        },{
            headers:{
                Authorization: "Bearer " + store.state.user.access_token,
            },
        }
        )
```

#### get

```js
//在post方法中验证头应该放在第三个参数
axios.get("http://101.43.45.110:8000/api/settings/upload-token/",{
            headers:{
                Authorization: "Bearer " + store.state.user.access_token,
            },
        },{
            key_name:store.state.user.username
        }
        )
```

在后端需要取值的时候使用

```python
data = json.loads(request.body.decode('utf-8'))  # 使用axios时候必须用这样来获取JSON数据，再进行处理
```

Get方式的取值

```python
def get(self,request):
        #直接取值就好，Axios会把get请求的参数放到请求头里，所有axios的post和get带参数是有区别的
        get_type = request.GET.get("get_type")
```







## 使用七牛云图传数据库

如何上传图片到数据库

1. 新建空间，并且设置为公开权限，方便操作。私有的话访问不能通过链接直接访问比较麻烦![image-20240201113447102](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20240201113447102.png)

2. 根据七牛云文档，在后端编写生成token的代码,如下图

3. 前端发送请求的时候需要带上token，具体参考https://developer.qiniu.com/kodo/1272/form-upload

4. 上传完图片后，由于七牛云用了CDN加速，还需要发送刷新CDN请求的api

   ```python
   q = Auth(ak, sk)
   data = json.loads(request.body.decode('utf-8'))  # 使用axios时候必须用这样来获取JSON数据，再进行处理
   # 要上传的空间
   bucket_name = name
   # 上传后保存的文件名
   key = data.get("key_name", "").strip()
   key = key + '.png'
   print(key)
   # 生成上传 Token，可以指定过期时间等
   upload_token = q.upload_token(bucket_name, key, 3600)
   ```

### 上传文件

如果想要在储存空间中分文件并且把文件上传到对应的文件夹中。那么需要在文件名前+文件夹名

例如我要



## Django中配置全局配置变量

有时候我需要一些全局的自定义变量，比如密钥，以便在项目中可以统一修改

只需要在settings中定义就可以了

```python
#七牛云的ak和sk
qiniu_access_key = 'xxxx'
qiniu_secret_key = 'xxxx'

```

在需要引用的地方

```python
from django.conf import settings

ak = settings.qiniu_access_key
```



## tmux快捷键

## 2、tmux 快捷键

会话相关命令：

- 查看已有会话：tmux ls
- 新建会话：tmux new -s <session-name>
- 接入会话：tmux attach -t <session-name> 或 tmux a -t 0
- 重命名会话：tmux rename-session -t 0 <new-name>
- 切换会话：tmux switch -t <session-name> 或 tmux s -t 0
- 杀死会话：tmux kill-session -t <session-name> 或 tmux kill-session -t 0

tmux 有大量快捷键，**所有的快捷键都需要通过前缀键唤起，默认的前缀键是 Ctrl+b。**

- 列出所有快捷键的命令：tmux list-keys

### 2.1、会话的快捷键

- s：列出所有会话
- d：离开当前会话
- $：重命名当前会话

### 2.2、窗口的快捷键

- c：创建一个新窗口
- n：切换到下一个窗口
- w：从列表中选择窗口
- <0~9>：切换到指定编号的窗口，编号显示在状态栏
- ,：窗口重命名

### 2.3、窗格的快捷键

- %：分成左右两个窗格
- "：分成上下两个窗格
- z：当前窗格全屏显示，再按一次恢复
- q：显示窗格编号
- t：在当前窗格显示时间
- <arrow key>：光标切换到其他窗格
- o：光标切换到下一个窗格
- {：左移当前窗格
- }：右移当前窗格
- Ctrl+o：上移当前窗格
- Alt+o：下移当前窗格
- space：切换窗格布局





## vue+前端相关

### 双向绑定

使用`v-model`标签对输入的内容可以进行双向绑定,并且在setup中要使用值的话，需要把变量返回

![image-20231118155435092](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20231118155435092.png)

```
let username = ref('');
    let password = ref('')

return{
      login,
      username,
      password,
    }
```



在form表单标签中使用@submit.prevent='函数名'可以对setup中的函数进行绑定

```
<form @submit.prevent="login" class="login-form">
```

使用函数对前端操作进行处理

```
const login = () =>{}
```

### 使用axios和后端进行交互

使用axios替换jquery，更好用。请注意，axios使用的是异步的方式，所以要取到返回的值需要特殊处理

**以下是使用`async/await`的例子：**

```javascript
setup() {
  const sendData = async () => {
    console.log("sending");
    try {
      const resp = await axios.post("http://101.43.45.110:8000/vue_test/", {
        message: '通信测试',
        error_message: 'success',
      });
      console.log(resp.data); // 打印返回的数据
    } catch (error) {
      console.error(error);
    }
  };

  return {
    sendData,
  };
}
```

**或者使用 `.then()`：**

```javascript
setup() {
  const sendData = () => {
    console.log("sending");
    axios.post("http://101.43.45.110:8000/vue_test/", {
      message: '通信测试',
      error_message: 'success',
    })
    .then(resp => {
      console.log(resp.data); // 打印返回的数据
    })
    .catch(error => {
      console.error(error);
    });
  };

  return {
    sendData,
  };
}

```

#### Axios带参数发送Post和Get请求

假设都需要请求头，保证后端安全

Post请求

```javascript
axios.post(url,{
    name:data.name,
    info:data.info,
},{
    headers:{
        Authorization: "Bearer " + content.state.access_token,
    },
}
//这是带上验证的请求
```







### 设置全局样式注意点

想要设置全局的布局或者样式，在app.vue中的style中不能使用`scoped`标签。这个标签是表明该样式只在当前的组件中生效，所以要设置全局背景的操作就会失效。

```vue
body{
    background:url("./assets/img/background.jpg");
    background-size: cover;
}

```

### 在vue中使用store保存后端获取的用户信息

在store文件夹下新建一个user.js用于保存用户基本信息，再在index.js中引入user.js

一般格式为

```javascript
  state: {//保存所存字段
  },
  getters: {
  },
  mutations: {//一般放更新信息函数
  },
  actions: {//一般放外部调用函数
  },
  modules: {//一般放引入的模块
    user:ModuleUser,
  }
```

使用token保证前后端安全通信

**安装`djangorestframework`模块**

```
pip install djangorestframework
```

安装完成后需要添加到setting.py中

```
INSTALLED_APPS = [
    # 其他应用
    'rest_framework',
]
```

使用`authenticate`验证登录用户的时候，密码匹配的是哈希值密码，所以不能直接修改明文密码

### 组件注册顺序问题

使用`v-model`绑定`ref`响应式变量的时候想在`setup`中打印出来，发现并没有值。这是因为vue3在组件实例话之前就有可能被调用，导致访问不到响应式变量的值。

正确做法

```vue
import { ref, onMounted } from 'vue';

// ...

setup() {
  let username = ref("");
  let name = ref("");

  // ... 其他数据

  onMounted(() => {
    console.log(username.value);
    console.log(name.value);
  });

  // ... 返回数据和方法
}

```



### 在不同组件中传递数据

我想在`UserAccountRegister.vue`中把注册错误信息传递给弹窗组件`ModelCompontens.vue`可以这么做

在`Reginster`中

```vue
<ModelComponents :error_msg="error_message"/>使用:自定义名称传递error_message的值
```

在`ModelComponents`中在`stript`中使用props获取值

```vue
props:{
        error_msg:{
            type:String,
            required:true,
        },
},
```

error_msg就是父组件传递的自定义名称

### VUEX

在vuex中我的项目是在主模块index.js底下创建许多个分模块

![image-20240223152142832](C:\Users\13363\AppData\Roaming\Typora\typora-user-images\image-20240223152142832.png)

然而如果想在子模块中访问主模块或者分模块的`state`或者`getter`中的数据需要这样做

```javascript
//子模块访问主模块
//需要在使用的函数中传入rootState参数
function(rootState){
    rootState.state||getter.xxx
}
//子模块访问子模块
function(rootState){
    rootState.子模块名.state||getter.xxx
}
```

如果想在一个模块中访问另一个模块的`action`中的函数可以这么做

```javascript
//在函数名中引入dispatch属性
get_music_info({commit,rootState,dispatch},data)
//直接调用user模块的action函数
dispatch('user/updataAccessFromRefresh');
```







### 下载相关

在前端中如果下载资源和当前页面同源，使用a标签加上download属性即可下载,download属性可以指定下载文件名

```html
<a href="xxxx.jpg" download="test.txt"></a>
```

如果不是同源，添加了download的属性，如果文件时浏览器能解析的问题，比如图片，音频，视频，则会进行显示，并不会下载。如果文件是其他类型，则会下载。

所以我采用通过`js`的方式下载成`blob`的格式再返回浏览器。这种方式下载浏览器不会显示下载进度

```javascript
download_music(content,data){
            console.log("开始下载");
            console.log("data",data);
            console.log(data.url);
            
            axios.get(data.url, {
                responseType: 'blob'
            })
            .then(response => {
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', data.name+data.music_type);
                document.body.appendChild(link);
                link.click();
            })
            .catch(error => {
                console.error('下载失败', error);
            });
        }
```

### ref和reactive的区别

两者都是响应式变量，即有变量改变的时候，会重新让组件加载数据

ref用户储存单个的响应式变量,并且改变值需要用value进行访问

```vue
const flag = ref(true)
```

reactive用于创建多个响应式变量，比如一个变量中有多个属性需要变成响应式变量

访问的时候只需要**变量.属性**就行 music.const

```
const music = reactive({
	const : 1
	flag : true
	}
)
```

### 子组件调用父组件的方法

子组件无法直接给父组件传递值，只能通过调用方法的方式给父组件的变量赋值





## 存在的BUG

- [ ] 对于其他界面，如果用户的token过期，后端无法访问。前端应该能够自动到登录界面
- [x] 在新建用户时，默认没有头像，新建头像的话头像路径没有填进数据库，更新名字后也需要更新信息
- [ ] 在转码下载的功能中，第二页的两首歌解码报错，目前不知道是歌曲问题还是翻页问题
- [ ] 用户等级系统暂时还没用上
- [ ] 头像太小
