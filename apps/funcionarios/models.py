from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.usuarios.models import Usuario


class Funcionario(models.Model):
    cpf = models.CharField(_(u'cpf'), max_length=11, null=True)
    nome = models.CharField(_(u'nome'), max_length=140, null=True)
    user = models.OneToOneField(Usuario, verbose_name=_("usuario"), null=True, related_name='funcionarios',
                                on_delete=models.CASCADE)
    jornada = models.ForeignKey('jornadas.Jornada', verbose_name=_('jornada'), null=True, related_name='funcionarios',
                                on_delete=models.DO_NOTHING)
    empresa = models.ForeignKey('empresa.Empresa', verbose_name=_('empresa'), null=True, related_name='funcionarios',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('funcionario')
        verbose_name_plural = _('funcionarios')
        db_table = 'funcionario'
