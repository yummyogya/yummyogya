from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_food/', views.add_food, name='add_food'),
    path('edit_food/<int:pk>/', views.edit_food, name='edit_food'),
    path('delete_food/<int:pk>/', views.delete_food, name='delete_food'),
]