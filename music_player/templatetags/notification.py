from django import template
from ..models import Notificaton,Notification_object

register = template.Library()

@register.inclusion_tag('notification.html', takes_context=True)
def notification(context):
    request = context['request']
    notify_objects = Notification_object.objects.get(notify = Notificaton.objects.get(notify_user = request.user))
    return {'notify_objects': notify_objects}