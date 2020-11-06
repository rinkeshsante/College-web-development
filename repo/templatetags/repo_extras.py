from django import template

register = template.Library()


@register.filter
def getValue(value, arg):
    return getattr(value, arg)
