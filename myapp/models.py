from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from myapp.manager import CustomManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    GUILD_MEMBER_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    SERVER_CHOICES = [
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('N.America', 'N.America'),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    total_fame = models.CharField(max_length=50)  
    kill_fame = models.CharField(max_length=50)
    playerkill = models.IntegerField(default=0)
    guild_member = models.CharField(max_length=5, choices=GUILD_MEMBER_CHOICES, default='no')
    server_name = models.CharField(max_length=12, choices=SERVER_CHOICES, default='Asia')
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    phone = models.CharField(max_length=19)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def _str_(self):
        return self.email







         
