import imp
from django.urls import path
from .views import Message
urlpatterns = [
    path('message/<str:message_type>', Message.as_view()),
]
