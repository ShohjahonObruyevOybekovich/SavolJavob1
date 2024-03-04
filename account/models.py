from django.db import models
from django.contrib.auth.models import AbstractUser

from account.managers import UserManager


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13, unique=True, blank=True, null=True)
    username = None
    USERNAME_FIELD = 'phone'
    objects = UserManager()

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Avataringizni_aratish'
        verbose_name_plural = 'Avataringizni_aratish'
