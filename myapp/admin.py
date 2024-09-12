from django.contrib import admin
from myapp.models import *
# # Register your models here.

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('-date_joined',)

admin.site.register(CustomUser)
