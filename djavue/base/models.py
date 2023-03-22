from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image': self.image,
        }

# class Buy(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products

#     def __str__(self):
#         return f"{self.user.username}'s shopping cart with {self.product.name}"

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s shopping cart with {self.product.name}"

# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name

class Coupon(models.Model):
    PERCENTAGE = 'PC'
    ABSOLUTE = 'AB'
    DISCOUNT_TYPES = [
        (PERCENTAGE, 'Percentage'),
        (ABSOLUTE, 'Absolute'),
    ]
    name = models.CharField(max_length=100)
    kind_of_discount = models.CharField(max_length=2, choices=DISCOUNT_TYPES, default=ABSOLUTE)
    discount_value = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def to_dict_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'kind_of_discount': self.kind_of_discount,
            'discount_value': self.discount_value,
        }