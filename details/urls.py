# details/urls.py
from django.urls import path
from . import views

app_name = 'details'

urlpatterns = [
    path('details/<int:item_id>/', views.food_detail, name='food_detail'),
    path('add_review/', views.add_review, name='add_review'),
    # URL lainnya
]

