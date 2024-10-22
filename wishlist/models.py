from django.db import models
from django.contrib.auth.models import User
from wishlist.models import Product  # Sesuaikan dengan nama app yang memuat model Product

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
