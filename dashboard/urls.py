from django.urls import path
from .views import dashboard, add_food, edit_food, delete_food

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('add_food/', add_food, name='add_food'),
    path('edit_food/<int:pk>/', edit_food, name='edit_food'),
    path('delete_food/<int:pk>/', delete_food, name='delete_food'),
]
