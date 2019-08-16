from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.base.mixins import MixinFilterEmpresa
from .models import Funcionario
from .serializers import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet, MixinFilterEmpresa):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('id',)
    search_fields = ('nome', 'cpf',)
