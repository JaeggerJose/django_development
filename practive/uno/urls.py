from django.urls import path
from uno import views as user_view
urlpatterns = [
    path('uno/', user_view.UsersView.as_view()),
]
