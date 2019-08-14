from django.db import models
from django.utils.translation import ugettext_lazy as _


class Empresa(models.Model):
    cnpj = models.CharField(_('CNPJ'), max_length=100)
    razao_social = models.CharField(_(u'razão social'), max_length=300)
    email = models.EmailField(_('email'), null=True, blank=True)
    telefone = models.CharField(_('telefone'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _('empresa')
        verbose_name_plural = _('empresas')
        db_table = 'empresa'
