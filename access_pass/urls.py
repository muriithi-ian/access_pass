from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('access_form/', views.access_form, name='access_form'),
]