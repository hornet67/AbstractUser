from django import forms
from myapp.models import CustomUser


class CustomUserForm(forms.ModelForm):
        class Meta:
                model = CustomUser
                fields = ['email', 'password']
