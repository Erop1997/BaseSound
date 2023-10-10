from django import template
from ..models import Notificaton,Notification_object

register = template.Library()

@register.inclusion_tag('notification.html', takes_context=True)
def notification(context):
    request = context['request']
    notify_objects = Notification_object.objects.get_or_create(notify = Notificaton.objects.get(notify_user = request.user))
    deleted_objects = notify_objects[0].deleted_things.strip().split(',')
    print(deleted_objects)
    return {'notify_objects': notify_objects, 'deleted_objects':deleted_objects}