from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .filters import EmpresaFilter
from .models import Empresa
from .serializers import EmpresaSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_class = EmpresaFilter

    def get_queryset(self):
        empresa = Empresa.objects.filter(funcionarios__user__cpf=self.request._user.cpf)
        return empresa

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
