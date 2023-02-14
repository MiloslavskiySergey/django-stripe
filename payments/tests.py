"""File containing test."""
from django.test import Client, TestCase
from django.urls import reverse

from .models import Item


class ItemTests(TestCase):
    """Test Item."""

    def setUp(self) -> None:
        """Create test data."""
        self.item = Item.objects.create(
            name='Test Item',
            description='This is a test item',
            price=1000
        )
        self.client = Client()

    def test_buy_view(self) -> None:
        """Test GET method `buy`."""
        response = self.client.get(reverse('buy', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'session_id')

    def test_item_view(self) -> None:
        """Test GET method `item`."""
        response = self.client.get(reverse('item', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')
        self.assertContains(response, 'This is a test item')
        self.assertContains(response, 'Price: 1000')
