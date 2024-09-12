from django.urls import path
from myapp.views import *


urlpatterns = [
   path('signup/', signup, name='signup'),
   path('login/', signin, name='login'),
]