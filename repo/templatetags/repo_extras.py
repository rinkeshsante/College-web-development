from django import template
from ..services import get_user_dep
register = template.Library()


@register.filter
def getValue(value, arg):
    return getattr(value, arg)


@register.filter
def getUserDep(value):
    return get_user_dep(value)
