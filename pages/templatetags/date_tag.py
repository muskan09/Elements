from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='todate')
def convert_str_date(value):
    return value.date()

