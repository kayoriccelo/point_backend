from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    fone = models.CharField(max_length=14, blank=True, null=True)
    primeiro_acesso = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['email', 'cpf']
