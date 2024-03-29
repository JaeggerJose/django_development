from django import views
from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.IndexView, name='index'),
    #path('create/', views.create, name='create'),
    path('create/active/', views.create_active, name='create_active'),

    #jason file
    path('users/', views.UsersView.as_view(), name='users_json'),
    path('jobs/', views.JobsView.as_view(), name='jobs_json'),
]

