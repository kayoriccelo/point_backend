import django_filters

from .models import Company


class CompanyFilter(django_filters.FilterSet):
    cpf = django_filters.CharFilter(field_name="employees__user__cpf", lookup_expr='iexact')

    class Meta:
        model = Company
        fields = {'cpf': ['exact']}
