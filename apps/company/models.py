from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    cnpj = models.CharField(_('cnpj'), max_length=100)
    business_name = models.CharField(_(u'business name'), max_length=300)
    email = models.EmailField(_('email'), null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _('company')
        db_table = 'company'
