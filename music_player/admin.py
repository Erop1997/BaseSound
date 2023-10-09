from django.contrib import admin
from .models import *


admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Singer)
admin.site.register(Playlist)
admin.site.register(Notificaton)
admin.site.register(Notification_object)