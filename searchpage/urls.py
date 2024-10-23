from django.urls import path
from .views import search_makanan_view

app_name = 'searchpage'
urlpatterns = [
    path('', search_makanan_view, name='search_makanan'),  # URL untuk pencarian makanan
]