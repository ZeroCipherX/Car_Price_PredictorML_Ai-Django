from django.urls import path
from .views import main_view, predict, result # Import the predict view function
urlpatterns = [
    path('', main_view, name='main'),   
    path('predict/', predict, name='predict'),
    path('predict/result/', result, name='result'),
]
