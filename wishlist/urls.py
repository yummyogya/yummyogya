from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add-to-wishlist/<int:food_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove-from-wishlist/<int:food_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
