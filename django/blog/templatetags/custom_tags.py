# Custom template tags or custom filters for blog are here
import re

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="nbsp2space", is_safe=True)
@stringfilter
def nbsp2space(value):
    """This filter replaces &nbsp to space"""
    return re.sub("&nbsp;", " ", value, flags=re.IGNORECASE)
