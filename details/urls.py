# details/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:item_id>/', views.food_detail, name='food_detail'),
]
