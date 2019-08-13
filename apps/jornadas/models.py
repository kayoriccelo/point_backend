from django.db import models
from django.utils.translation import ugettext_lazy as _


DIAS_SEMANA = (
    (1, 'SEG'),
    (2, 'TER'),
    (3, 'QUA'),
    (4, 'QUI'),
    (5, 'SEX'),
    (6, 'SAB'),
    (7, 'DOM'),
)


class Jornada(models.Model):
    codigo = models.CharField(_('codigo'), max_length=10)
    descricao = models.CharField(_('descricao'), max_length=300)
    empresa = models.ForeignKey('empresa.Empresa', verbose_name=_('empresa'), related_name='jornada',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('jornada')
        verbose_name_plural = _('jornadas')
        db_table = 'jornada'
        ordering = ['descricao']


class DiaTrabalhado(models.Model):
    jornada = models.ForeignKey(Jornada, verbose_name=_('jornada'), null=True, related_name='dia_trabalhado',
                                on_delete=models.CASCADE)
    dia = models.IntegerField(_('dia'), choices=DIAS_SEMANA, default=1)
    entrada = models.TimeField(_('entrada'))
    entrada_intervalo = models.TimeField(_('entrada intervalo'), null=True, blank=True)
    saida_intervalo = models.TimeField(_('saida intervalo'), null=True, blank=True)
    saida = models.TimeField(_('saida'), null=True, blank=True)

    class Meta:
        verbose_name = _(u'dia trabalhado')
        verbose_name_plural = _(u'dias trabalhado')
        db_table = 'dia_trabalhado'
        ordering = ['id']
