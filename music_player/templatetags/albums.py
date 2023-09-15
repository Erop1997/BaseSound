from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('albums.html')
def albums():
    albums_list = Album.objects.filter(is_uploaded = True)
    return {'albums_list':albums_list}
