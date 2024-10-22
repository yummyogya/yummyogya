from django.db import models
from django.contrib.auth.models import User
from django.apps import apps  

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        'wishlist.Makanan', on_delete=models.CASCADE  
    )

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
