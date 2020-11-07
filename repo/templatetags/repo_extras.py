from django import template
from ..services import get_user_dep, is_sub_admin, is_authorized
register = template.Library()


@register.filter
def getValue(value, arg):
    return getattr(value, arg)


@register.filter
def isSubAdmin(value):
    return is_sub_admin(value)


@register.filter
def isAuthorized(value):
    return is_authorized(value)


@register.filter
def getUserDep(value):
    return get_user_dep(value)
