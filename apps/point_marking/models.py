from django.db import models
from django.utils.translation import ugettext_lazy as _


TIPO_MARCACAO = (
    ('E', 'Entry'),
    ('IO', 'Interval Output'),
    ('RI', 'Return Interval'),
    ('L', 'Leave'),
)


class PointMarking(models.Model):
    date = models.DateField()
    day_week = models.CharField(max_length=20)
    hour = models.TimeField()
    type = models.CharField(_('type of marking'), max_length=2, choices=TIPO_MARCACAO, default='E')
    employee = models.ForeignKey('employee.Employee', verbose_name=_('employee'), related_name='point_marking',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('point_marking')
        db_table = 'point_marking'
        ordering = ['date', 'hour', 'employee']
