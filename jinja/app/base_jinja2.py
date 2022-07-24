from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from .myfilter import test

def environment(**optins):
    env = Environment(**optins)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse
    })
    env.filters['test'] = test
    return env