from django import template

register = template.Library()

def cut(value, arg):
    """
    this cuts/removes args
    """
    return value.replace(arg, '')

register.filter('cut', cut)