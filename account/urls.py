from django import views
from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    #path('create/', views.create, name='create'),
    path('create/', views.ldap_write_user_and_group_file, name='ldap_write_user_and_group_file'),

]