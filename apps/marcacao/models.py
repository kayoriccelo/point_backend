from django.db import models
from django.utils.translation import ugettext_lazy as _


TIPO_MARCACAO = (
    ('E', 'Entrada'),
    ('SI', 'Saída Intervalo'),
    ('R', 'Retorno Intervalo'),
    ('S', 'Saída'),
    ('D', 'Desconsiderar'),
)


class Marcacao(models.Model):
    data = models.DateField()
    dia_semana = models.CharField(max_length=20)
    hora = models.TimeField()
    tipo = models.CharField(_('tipo de marcacao'), max_length=2, choices=TIPO_MARCACAO, default='E')
    funcionario = models.ForeignKey('funcionarios.Funcionario', verbose_name=_('funcionario'), related_name='marcacao',
                                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('marcacao')
        verbose_name_plural = _('marcacoes')
        db_table = 'marcacao'
        ordering = ['data', 'hora', 'funcionario']
