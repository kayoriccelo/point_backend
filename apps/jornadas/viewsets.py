from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.base.mixins import MixinFilterEmpresa
from .models import Jornada
from .serializers import JornadaSerializer


class JornadaViewSet(viewsets.ModelViewSet, MixinFilterEmpresa):
    queryset = Jornada.objects.all()
    serializer_class = JornadaSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('id',)
    search_fields = ('descricao', 'codigo',)
