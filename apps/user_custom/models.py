from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserCustom(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    first_access = models.BooleanField(default=True)
    company = models.ForeignKey('company.Company', verbose_name=_('company'), null=True, related_name='users',
                                on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['email', 'cpf']
