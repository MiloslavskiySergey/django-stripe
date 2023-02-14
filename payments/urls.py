"""File containing urls."""
from django.urls import path

from .views import buy_order_view, buy_view, cancel_view, checkout_view, item_view, success_view

urlpatterns = [
    path('buy/<int:item_id>/', buy_view, name='buy'),
    path('item/<int:item_id>/', item_view, name='item'),
    path('buy_order/<int:item_id>/', buy_order_view, name='buy_order'),
    path('checkout/', checkout_view, name='checkout_view'),
    path('success/<int:order_id>/', success_view, name='success_view'),
    path('cancel/', cancel_view, name='cancel_view')
]
