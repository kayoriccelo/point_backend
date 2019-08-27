from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import UserCustom
from .serializers import UserCustomSerializer


class UserCustomViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = (AllowAny,)
