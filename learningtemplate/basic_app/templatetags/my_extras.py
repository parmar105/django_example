from django import template

# to register this custom template filter
register = template.Library()


def cut(value, arg):
    """
        this will remove the arg from the string!
    """
    return value.replace(arg, '')


register.filter('cut', cut)