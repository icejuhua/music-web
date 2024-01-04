from django.contrib import admin

# Register your models here.
from .models import Test_DEle,Test_User,Test_Player



admin.site.register(Test_User)
admin.site.register(Test_DEle)
admin.site.register(Test_Player)