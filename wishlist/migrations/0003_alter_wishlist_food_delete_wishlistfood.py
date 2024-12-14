# Generated by Django 5.1.2 on 2024-12-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_artikel'),
        ('wishlist', '0002_wishlistfood_alter_wishlist_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='food',
            field=models.ManyToManyField(related_name='wishlists', to='main.makanan'),
        ),
        migrations.DeleteModel(
            name='WishlistFood',
        ),
    ]
