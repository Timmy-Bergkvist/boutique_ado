from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(requset):
    bag = requset.session.get('bag', {})
    if not bag:
        messages.error(requset, "There's nothin in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': '<put your public key here>',
        'client_secret': 'test client secret',
    }

    return render(requset, template, context)