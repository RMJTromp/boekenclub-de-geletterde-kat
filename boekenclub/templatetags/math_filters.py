from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplies the arg and the value"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):

        try:
            return int(value) * int(arg)
        except (ValueError, TypeError):
            return ''
