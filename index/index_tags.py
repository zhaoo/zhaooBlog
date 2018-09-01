from django import template
from index.models import Setting

register = template.Library()

@register.simple_tag
def get_setting():
    return Setting.objects.last()
