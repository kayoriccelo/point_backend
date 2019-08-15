from django.db import models
from django.utils.translation import ugettext_lazy as _


class Jornada(models.Model):
    codigo = models.CharField(_('codigo'), max_length=10)
    descricao = models.CharField(_('descricao'), max_length=300)
    entrada = models.TimeField(_('entrada'), null=True, blank=True)
    saida_intervalo = models.TimeField(_('entrada intervalo'), null=True, blank=True)
    retorno_intervalo = models.TimeField(_('saida intervalo'), null=True, blank=True)
    saida = models.TimeField(_('saida'), null=True, blank=True)
    possui_dsr = models.BooleanField(default=True)
    empresa = models.ForeignKey('empresa.Empresa', verbose_name=_('empresa'), related_name='jornada',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('jornada')
        verbose_name_plural = _('jornadas')
        db_table = 'jornada'
        ordering = ['descricao']