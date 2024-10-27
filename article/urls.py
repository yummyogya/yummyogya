from django.urls import path
from article.views import article_detail, article_list

app_name = 'article'

urlpatterns = [
    path('',article_list, name='article_list'),
    path('<int:id>/',article_detail, name='article_detail'),
    path('load_more/', article_list, name='load_more_articles'),
]