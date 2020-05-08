from django import template

register = template.Library()


@register.filter(name='get_dict_prop')
def get_dict_prop(value, arg):
    return value.get(arg)


@register.filter(name='is_in_array')
def is_in_array(value, arg):
    is_true = arg in value
    return is_true


@register.filter(name='get_dict_value')
def get_dict_value(value, arg):
    return value.get(arg)
