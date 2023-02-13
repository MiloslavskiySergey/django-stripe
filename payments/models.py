"""File containing models."""
from django.db import models


class Item(models.Model):
    """Model `Item`."""

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name
