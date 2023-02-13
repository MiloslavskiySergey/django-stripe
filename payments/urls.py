"""File containing urls."""
from django.urls import path

from .views import buy_view, item_view

urlpatterns = [
    path('buy/<int:id>/', buy_view, name='buy'),
    path('item/<int:id>/', item_view, name='item'),
]
