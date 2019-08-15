from rest_framework import serializers

from apps.funcionarios.models import Funcionario
from .models import Jornada


class JornadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jornada
        fields = '__all__'

    def to_internal_value(self, data):
        return data

    def validate(self, attrs):
        data = self.context['request'].data

        try:
            data['empresa'] = Funcionario.objects.get(cpf=self.context['request'].user.cpf).empresa
        except Funcionario.DoesNotExist:
            raise serializers.ValidationError({'error': 'Empresa não encontrada.'})

        return super(JornadaSerializer, self).validate(attrs)
