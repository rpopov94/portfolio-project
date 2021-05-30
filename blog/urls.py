from django.urls import path

from .views import *

urlpatterns = [
    path('', all_articles, name='all_articles'),
    path('<int:blog_id>/', detail, name='detail'),
]
