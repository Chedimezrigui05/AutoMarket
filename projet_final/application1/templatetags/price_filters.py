from decimal import Decimal, InvalidOperation

from django import template

register = template.Library()


@register.filter
def prix_million(value):
    try:
        amount = Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        return ''

    million = amount / Decimal('1000000')
    return f"{million.quantize(Decimal('0.01'))} M DT"
