"""File containing views."""
import stripe
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from djstripe.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY

from .models import Item, Order

stripe.api_key = STRIPE_SECRET_KEY


def buy_view(request, item_id: int) -> JsonResponse:
    """Get a Stripe Session Id to pay for the selected Item."""
    item = get_object_or_404(Item, pk=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(item.price * 100),
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return JsonResponse({'session_id': session.id})


def item_view(request, item_id: int) -> HttpResponse:
    """Get information about the selected Item."""
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item.html', {'item': item, 'stripe_public_key': STRIPE_PUBLIC_KEY})


def buy_order_view(request, item_id: int) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    """Buy order."""
    item = get_object_or_404(Item, pk=item_id)
    order = Order.objects.create()
    order.items.add(item)

    success_url = request.build_absolute_uri(reverse('success_view', kwargs={'order_id': order.id}))
    cancel_url = request.build_absolute_uri(reverse('cancel_view'))
    session_id = order.create_stripe_session(success_url, cancel_url)
    return redirect('checkout_view', session_id=session_id)


def checkout_view(request) -> HttpResponse:
    """Checkout."""
    session_id = request.GET.get('session_id')
    return render(request, 'checkout.html', {'session_id': session_id, 'stripe_public_key': STRIPE_PUBLIC_KEY})


def success_view(request, order_id: int) -> HttpResponse:
    """Success."""
    order = Order.objects.get(id=order_id)
    order.paid = True
    order.save()
    return render(request, 'success.html', {'order': order})


def cancel_view(request) -> HttpResponse:
    """Cansel."""
    return render(request, 'cancel.html')
