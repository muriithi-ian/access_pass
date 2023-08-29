from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('base/', views.base, name='base'),
    path('access_form/', views.access_form, name='access_form'),
    path('success/', views.success, name='success')
]