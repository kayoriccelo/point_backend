from django.utils.six import text_type
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.employee.models import Employee
from apps.user_custom.models import UserCustom


class CustomTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenObtainPairSerializer, self).validate(attrs)
        refresh = self.get_token(self.user)

        try:
            UserCustom.objects.get(cpf=self.user.cpf, is_superuser=False)
        except UserCustom.DoesNotExist:
            raise serializers.ValidationError(u'Not Authorized.')

        try:
            employee = Employee.objects.get(cpf=self.user.cpf)
        except Employee.DoesNotExist:
            employee = None

        try:
            user = UserCustom.objects.get(cpf=self.user.cpf, is_admin=True)
        except UserCustom.DoesNotExist:
            user = None

        if not user and not employee:
            raise serializers.ValidationError(u'Awaiting authorization.')

        data['refresh'] = text_type(refresh)
        data['access'] = text_type(refresh.access_token)

        return data
