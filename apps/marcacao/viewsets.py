from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet

from .models import Marcacao
from .serializers import MarcacaoSerializer


class MarcacaoViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Marcacao.objects.all()
    serializer_class = MarcacaoSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('date', )
