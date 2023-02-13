"""File containing views."""
import stripe
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from djstripe.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY

from .models import Item

stripe.api_key = STRIPE_SECRET_KEY


def buy_view(request, id: int) -> JsonResponse:
    """Get a Stripe Session Id to pay for the selected Item."""
    item = get_object_or_404(Item, pk=id)
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


def item_view(request, id: int) -> HttpResponse:
    """Get information about the selected Item."""
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item.html', {'item': item, 'stripe_public_key': STRIPE_PUBLIC_KEY})