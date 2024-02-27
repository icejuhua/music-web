from django.contrib import admin


from music_web.models.user.music_user import Music_User
from music_web.models.music.music import Music


admin.site.register(Music_User)
admin.site.register(Music)

