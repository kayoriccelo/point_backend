from django.contrib.auth.models import AbstractUser
from django.db import models


class UserCustom(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    first_access = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['email', 'cpf']
