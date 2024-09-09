from django.urls import path
from .views import my_view ,signup,login # Import specific view functions

urlpatterns = [
    path('', my_view, name='home'),
    path('signup/',signup, name='signup'),
    path('login/',login, name='login'),
    
     
]