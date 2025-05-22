from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank':True,'null':True}

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True,verbose_name='Email')
    phone = models.CharField(unique = True,max_length=35,verbose_name='Телефон',**NULLABLE)
    telegram = models.CharField(max_length=150,unique=True,verbose_name='Телеграмм',**NULLABLE)
    is_active = models.BooleanField(default = True, verbose_name = 'Активность')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
