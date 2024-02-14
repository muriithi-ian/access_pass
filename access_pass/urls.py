from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('access_form/', views.AccessFormView.as_view(views.FORMS), name='form'),
    path('success/', views.success, name='success'),
    path('applicants/', views.tables, name='applicants'),
    path('visit_request/<int:visit_id>', views.visit_request, name='visit_request'),
    path('accept/', views.tables, name='accept'),
    path('decline/', views.tables, name='decline'),
]