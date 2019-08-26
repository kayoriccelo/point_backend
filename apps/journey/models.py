from django.db import models
from django.utils.translation import ugettext_lazy as _


class Journey(models.Model):
    code = models.CharField(_('code'), max_length=10)
    description = models.CharField(_('description'), max_length=300)
    entry = models.TimeField(_('entry'), null=True, blank=True)
    interval_output = models.TimeField(_('interval output'), null=True, blank=True)
    return_interval = models.TimeField(_('return interval'), null=True, blank=True)
    leave = models.TimeField(_('leave'), null=True, blank=True)
    has_remunerated_rest = models.BooleanField(default=True)
    company = models.ForeignKey('company.Company', verbose_name=_('company'), related_name='journey',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('journey')
        verbose_name_plural = _('journeys')
        db_table = 'journey'
        ordering = ['code', 'description', ]
