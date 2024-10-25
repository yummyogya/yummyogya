from django.urls import path
from . import views

app_name = 'profilepage'

urlpatterns = [
    path('profile/', views.show_profile, name='show_profile'),
]
