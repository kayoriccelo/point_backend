import django_filters

from .models import Empresa


class EmpresaFilter(django_filters.FilterSet):
    cpf = django_filters.CharFilter(field_name="funcionarios__user__cpf", lookup_expr='iexact')

    class Meta:
        model = Empresa
        fields = {'cpf': ['exact']}
