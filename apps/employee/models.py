from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.user_custom.models import UserCustom


class Employee(models.Model):
    cpf = models.CharField(_(u'cpf'), max_length=11, null=True)
    name = models.CharField(_(u'name'), max_length=140, null=True)
    user = models.OneToOneField(UserCustom, verbose_name=_("user"), null=True, related_name='users',
                                on_delete=models.CASCADE)
    journey = models.ForeignKey('journey.Journey', verbose_name=_('journey'), null=True, related_name='employees',
                                on_delete=models.DO_NOTHING)
    company = models.ForeignKey('company.Company', verbose_name=_('company'), null=True, related_name='employees',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
        db_table = 'employee'
