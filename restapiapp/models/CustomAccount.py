from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .appusermanager import CustomUserManager
from rest_framework.authtoken.models import Token

class CustomAccount(AbstractBaseUser):
    username = models.CharField(max_length=70,unique=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    isActive = models.BooleanField(default=True)
    isAdmin= models.BooleanField(default=False)
    
    USERNAME_FIELD= 'username'
    
    objects = CustomUserManager()

    class Meta:
        db_table = 'UserAccount'

    def __str__(self):
        return self.username
    
    def tokens(self):
        token, created = Token.objects.get_or_create(user=self)
        return {"token": str(token.key) }
