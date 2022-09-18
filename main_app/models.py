from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=512)
    price = models.DecimalField(max_digits=6, decimal_places=2)
