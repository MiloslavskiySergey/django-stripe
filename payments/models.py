"""File containing models."""
from django.db import models


class Item(models.Model):
    """Model `Item`."""

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    """Model `Order`."""

    items = models.ManyToManyField(Item)
    paid = models.BooleanField(default=False)
    stripe_session_id = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_total_cost(self) -> int:
        return sum(item.price for item in self.items.all())

    def create_stripe_session(self, success_url, cancel_url):
        import stripe
        from django.conf import settings
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(self.get_total_cost() * 100),
                    'product_data': {
                        'name': f'Order #{self.id}',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
        )
        self.stripe_session_id = session.id
        self.save()
        return session.id
