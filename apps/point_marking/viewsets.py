from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet

from apps.core.mixins import MixinFilterEmployeeCompany
from .models import PointMarking
from .serializers import PointMarkingSerializer


class PointMarkingViewSet(mixins.CreateModelMixin, GenericViewSet, MixinFilterEmployeeCompany):
    queryset = PointMarking.objects.all()
    serializer_class = PointMarkingSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('date', )
