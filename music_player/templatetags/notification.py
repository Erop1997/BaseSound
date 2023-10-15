from django import template
from django.shortcuts import redirect
from ..models import Notificaton,Notification_object
import ast

register = template.Library()

@register.inclusion_tag('notification.html', takes_context=True)
def notification(context):
    request = context['request']
    notify_objects = Notification_object.objects.get_or_create(notify = Notificaton.objects.get(notify_user = request.user))
    deleted_objects = [i for i in notify_objects[0].deleted_things.split(';') if i]
    added_songs = list(reversed(notify_objects[0].notify_song.filter(is_new=True)))
    added_albums = list(reversed(notify_objects[0].notify_album.filter(is_new=True)))
    path = [i for i in str(request.get_full_path()).split('?') if i]
    path = [i for i in path[0].split('/') if i]
    path = '.'.join(path)
    deleted_tracks = [ast.literal_eval(i) for i in deleted_objects if 'track' in i]
    deleted_albums = [ast.literal_eval(i) for i in deleted_objects if 'album' in i]
    length = len(added_songs) + len(added_albums) + len(deleted_tracks) + len(deleted_albums)

    return {'notify_objects': notify_objects, 'path': path, 'deleted_objects':deleted_objects, 'added_songs':added_songs, 'added_albums':added_albums, 'deleted_tracks':deleted_tracks, 'deleted_albums':deleted_albums, 'length':length}