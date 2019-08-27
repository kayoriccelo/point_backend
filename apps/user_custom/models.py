from django.contrib.auth.models import AbstractUser
from django.db import models


class UserCustom(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    first_access = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'cpf']
