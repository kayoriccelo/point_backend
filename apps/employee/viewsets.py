from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.core.mixins import MixinFilterCompany
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet, MixinFilterCompany):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('id',)
    search_fields = ('name', 'cpf',)
