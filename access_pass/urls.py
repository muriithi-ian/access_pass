from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('access_form/', views.AccessFormView.as_view(views.FORMS), name='form'),
    # path('rules/', views.dc_rules, name='rules'),
    # path('applicants/', views.applicants, name='applicants'),
    # path('visit_request/', views.visit_request, name='visit_request'),
    # path('sign_nda/', views.sign_nda, name='sign NDA'),
    path('success/', views.success, name='success'),
    path('applicants/', views.tables, name='applicants'),
    path('accept/', views.tables, name='accept'),
    path('decline/', views.tables, name='decline'),
]