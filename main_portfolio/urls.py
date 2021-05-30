from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing, name='home'),
#    path('', views.homePageView, name='home'),
]
