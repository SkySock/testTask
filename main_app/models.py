from django.db import models
from django.db.models import Sum


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=512)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['price', 'name']

    def __str__(self):
        return f"Item(id={self.pk}, name={self.name})"


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def price(self):
        return self.items.aggregate(sum_price=Sum('price'))['sum_price']
