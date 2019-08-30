from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import UserCustom
from .serializers import UserCustomSerializer, UserProfileSerializer


class UserAllowAnyViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = (AllowAny,)


class UserCustomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer

    def get_queryset(self):
        user = UserCustom.objects.filter(cpf=self.request.user.cpf)

        return user


class UserProfileViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        user = UserCustom.objects.filter(cpf=self.request.user.cpf)

        return user

