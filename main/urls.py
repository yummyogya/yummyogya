from django.urls import path
from main.views import show_main, show_xml, show_json, show_json_by_id, show_xml_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:pk>/', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:pk>/', show_xml_by_id, name='show_xml_by_id'),
]