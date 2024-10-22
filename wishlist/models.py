from django.contrib.auth.models import User
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50)
    restaurant = models.CharField(max_length=100)
    rating = models.FloatField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food, related_name='wishlists')

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
