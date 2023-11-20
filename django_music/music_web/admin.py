from django.contrib import admin

# Register your models here.
from .models import Test_DEle,Test_User



admin.site.register(Test_User)
admin.site.register(Test_DEle)