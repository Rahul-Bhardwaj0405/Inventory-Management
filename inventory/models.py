from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def update_info(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price is not None:
            self.price = price
        self.save()
