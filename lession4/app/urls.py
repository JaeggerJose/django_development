from django.urls import path
from .views import Index, Test
urlpatterns = [
    path('', Index.as_view()),
    path('test.php', Test.as_view()),
]
