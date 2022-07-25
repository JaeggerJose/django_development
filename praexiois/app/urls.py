from django import views
from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('/create/', views.create, name='create'),
    path('/create_active/', views.create_active, name='create_active'),
]
