from django.contrib import admin

# Register your models here.
#from .models import Test_DEle,Test_User,Test_Player
from music_web.models.user.music_user import Music_User


admin.site.register(Music_User)

# admin.site.register(Test_User)
# admin.site.register(Test_DEle)
# admin.site.register(Test_Player)