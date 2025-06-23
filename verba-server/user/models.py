from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager

# Create your models here.

class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    user_name = models.CharField(unique=True,max_length=40)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name",]
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    
    def __str__(self):
        return f"{self.user}'s profile"