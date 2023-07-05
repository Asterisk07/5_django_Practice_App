from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='index'),
    path('success/', views.success, name='success'),
    path('pdf/<str:file1>/', views.serve_pdf, name='serve-pdf'),
    path('check_username_exists/', views.check_username_exists, name='check_username_exist'),
    # Add more URL patterns for your app here
]