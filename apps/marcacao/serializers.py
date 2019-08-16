from datetime import datetime

from rest_framework import serializers

from apps.funcionarios.models import Funcionario
from .models import Marcacao


class MarcacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marcacao
        fields = '__all__'

    def to_internal_value(self, data):
        return data

    def validate(self, attrs):

        if not 'cpf' in attrs:
            raise serializers.ValidationError({'error': 'Cpf não informado.'})

        if not 'hora' in attrs:
            raise serializers.ValidationError({'error': 'Hora não informado.'})

        if not 'password' in attrs:
            raise serializers.ValidationError({'error': 'Senha não informado.'})

        if not 'tipo' in attrs:
            raise serializers.ValidationError({'error': 'Tipo não informado.'})

        try:
            attrs['funcionario'] = Funcionario.objects.get(cpf=attrs['cpf'])
        except Funcionario.DoesNotExist:
            raise serializers.ValidationError({'error': 'Cpf não cadastrado.'})

        marcacoes = Marcacao.objects.filter(
            funcionario__cpf=attrs['cpf'],
            data=datetime.now().date(),
            tipo=attrs['tipo'])

        if marcacoes.count() > 0:
            raise serializers.ValidationError({'error': 'Este tipo de marcação já foi efetuada.'})

        return attrs

    def create(self, validated_data):

        try:
            marcacao = Marcacao()
            marcacao.data = datetime.now().date()
            marcacao.dia_semana = datetime.now().isoweekday()
            marcacao.hora = validated_data['hora'][0:5]
            marcacao.tipo = validated_data['tipo']
            marcacao.funcionario = validated_data['funcionario']
            marcacao.save()
        except Exception as e:
            raise serializers.ValidationError({'error': 'Não foi possivel efetuar marcação.'})

        return marcacao


