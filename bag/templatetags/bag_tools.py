from django import template


register = template.Library()

@register.filter(name='calc_subtotal') # This decorator is used to register the function as a template tag
def calc_subtotal(price, quantity):
    return price * quantity