from django import template

register = template.Library()

@register.filter(name='getColor')
def get_color_from_topics(value):
    if 'web development' in str(value).lower():
        return '#0dcaf0'
    elif 'machine learning' in str(value).lower():
        return '#20c997' 
    elif 'deep learning' in str(value).lower():
        return '#dc3545'
    elif 'Miscellaneous' in str(value).lower():
        return '#ffc107'
    return '#0d6efd'

@register.filter(name='shorten')
def shorten_string(value):
    return str(value)[:50]+'...'