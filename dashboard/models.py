

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()  # Mengubah tipe data price menjadi IntegerField
    description = models.TextField()
    category = models.CharField(max_length=100)
    restaurant = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)  # rating (misal dari 0-5)
    image_url = models.URLField()  # link URL untuk gambar
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.name