from django.urls import path
from .views import my_view  # Import specific view functions

urlpatterns = [
    path('', my_view, name='home'),  # Define the URL pattern and its corresponding view
]