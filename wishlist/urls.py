from django.urls import path
from .views import add_to_wishlist, view_wishlist, remove_from_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('add_to_wishlist/<int:food_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', view_wishlist, name='view_wishlist'),
    path('remove_from_wishlist/<int:food_id>/', remove_from_wishlist, name='remove_from_wishlist'),
]
