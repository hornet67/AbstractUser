from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Custom_User_form(UserCreationForm):
          class Meta:
                  model = User
                  fields = ['email','password','password1']