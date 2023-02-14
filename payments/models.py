"""File containing models."""
from django.db import models


class Item(models.Model):
    """Model `Item`."""

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Discount(models.Model):
    """Model `Discount`."""

    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=2)


class Tax(models.Model):
    """Model `Tax`."""

    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=2)


class Order(models.Model):
    """Model `Order`."""

    paid = models.BooleanField(default=False)
    stripe_session_id = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    items = models.ManyToManyField(Item)
    discounts = models.ManyToManyField(Discount, blank=True)
    taxes = models.ManyToManyField(Tax, blank=True)

    def get_total_cost(self) -> int:
        """Get total cost."""
        total = sum(item.price for item in self.items.all())
        total -= sum(discount.amount for discount in self.discounts.all())
        total *= (1 + sum(tax.amount for tax in self.taxes.all()))
        return total

    def create_stripe_session(self, success_url, cancel_url):
        """Create stripe sesion."""
        import stripe
        from django.conf import settings
        stripe.api_key = settings.STRIPE_SECRET_KEY
        line_items = [{
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(self.get_total_cost() * 100),
                'product_data': {
                    'name': f'Order #{self.id}',
                },
            },
            'quantity': 1,
        }]
        for discount in self.discounts.all():
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(-discount.amount * 100),
                    'product_data': {
                        'name': f'Discount: {discount.name}',
                    },
                },
                'quantity': 1,
            })
        for tax in self.taxes.all():
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(self.get_total_cost() * tax.amount * 100),
                    'product_data': {
                        'name': f'Tax: {tax.name}',
                    },
                },
                'quantity': 1,
            })

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
        )
        self.stripe_session_id = session.id
        self.save()
        return session.id
