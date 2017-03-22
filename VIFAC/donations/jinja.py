# -*- coding: utf-8 -*-
from jinja2 import Environment
from widget_tweaks.templatetags.widget_tweaks import *

def environment(**options):
    from django.contrib.staticfiles.storage import staticfiles_storage
    from django.urls import reverse
    
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'attr': set_attr,
        'add_error_attr': add_error_attr,
        'append_attr': append_attr,
        'add_class': add_class,
        'add_error_class': add_error_class,
        'set_data': set_data,
        'field_type': field_type,
        'widget_type': widget_type
    })
    
    
    return env
