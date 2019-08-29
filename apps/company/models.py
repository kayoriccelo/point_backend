from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    cnpj = models.CharField(_('cnpj'), max_length=14)
    business_name = models.CharField(_(u'business name'), max_length=140)
    email = models.EmailField(_('email'), null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = _('company')
        db_table = 'company'
