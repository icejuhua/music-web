from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Test(models.Model):
    Test_id = models.IntegerField(max_length=200)
    Test_char = models.CharField(max_length=100)

class Test_User(models.Model):
    User_id = models.AutoField(primary_key = True)
    User_Account = models.CharField(max_length=20)
    User_Pwd = models.CharField(max_length=200,help_text="请输入密码")
    User_Level = models.IntegerField(default=1,null=True)
    User_Cre_DateTime = models.DateField()


class Test_DEle(models.Model):
    String = models.TextField(max_length=500)

class Test_Player(models.Model):
    #让Django中自带的User表中和这个表一一对应起来，并且当User表执行删除操作的时候，这个表也同步执行删除
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo_path = models.URLField(max_length=256,blank=True)
    #这个函数作用是在后台中，在这个表的界面中显示内容，这里显示的是user的名字
    def __str__(self):
        return str(self.user)



