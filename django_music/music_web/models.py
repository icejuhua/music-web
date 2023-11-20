from django.db import models

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

