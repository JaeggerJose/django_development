from atexit import register
from django import template

register = template.Library()

@register.filter
def test_filter(value, args):
    return value * args