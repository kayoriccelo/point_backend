from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.core.mixins import MixinFilterCompany
from .models import Journey
from .serializers import JourneySerializer


class JourneyViewSet(viewsets.ModelViewSet, MixinFilterCompany):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('id',)
    search_fields = ('description', 'code',)
