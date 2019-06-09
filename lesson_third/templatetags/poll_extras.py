from django import template

register = template.Library()


@register.filter(name="my_lower_filter")
def my_lower_filter(value):
    return value.lower()


@register.filter(name='compare_number')
def compare_number(value):
    if value == 0:
        return "ZERO!"
    elif 0 < value < 10:
        return "Число от 0 до 10"
    elif 10 < value < 50:
        return "Число от 10 до 50"
    else:
        return "Число больше 50!"


@register.filter(name='get_date_color')
def get_due_date_color(value):
    if value == 0:
        return "red"
    elif 0 < value < 10:
        return "green"
    elif 10 < value < 50:
        return "blue"
    else:
        return "black"


register.simple_tag(lambda x: x - 1, name='minusone')


@register.simple_tag(name='minustwo')
def some_function(value):
    return value - 2
