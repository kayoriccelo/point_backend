from rest_framework import serializers

from apps.jornadas.models import Jornada
from apps.usuarios.models import Usuario
from .models import Funcionario


class FuncionarioSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email')
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Funcionario
        fields = '__all__'

    def to_internal_value(self, data):
        return data

    def validate(self, attrs):
        data = self.context['request'].data

        if not 'cpf' in data or not data['cpf']:
            raise serializers.ValidationError({'error': 'CPF não informado.'})

        if self.context['request'].method == 'POST':
            try:
                usuario = Usuario.objects.get(cpf=data['cpf'])
            except:
                usuario = None
            if usuario:
                raise serializers.ValidationError({'error': 'Cpf ja cadastrado.'})

        if not 'nome' in data or not data['nome']:
            raise serializers.ValidationError({'error': 'Nome não informado.'})

        if not 'jornada' in data or not data['jornada']:
            raise serializers.ValidationError({'error': 'Jornada não informado.'})

        if not 'email' in data or not data['email']:
            raise serializers.ValidationError({'error': 'Email não informado.'})

        if not 'username' in data or not data['username']:
            raise serializers.ValidationError({'error': 'Usuário não informado.'})

        if self.context['request'].method == 'POST':
            if not 'new_password' in data or not data['new_password']:
                raise serializers.ValidationError({'error': 'Senha não informado.'})

        try:
            data['empresa'] = Funcionario.objects.get(cpf=self.context['request'].user.cpf).empresa
        except Funcionario.DoesNotExist:
            raise serializers.ValidationError({'error': 'Empresa não encontrada.'})

        try:
            data['jornada'] = Jornada.objects.get(id=data['jornada'])
        except Jornada.DoesNotExist:
            raise serializers.ValidationError({'error': 'Jornada não encontrada.'})

        return data

    def create(self, validated_data):
        try:
            usuario = Usuario()
            usuario.cpf = validated_data['cpf']
            usuario.email = validated_data['email']
            usuario.first_name = validated_data['nome']
            usuario.username = validated_data['username']
            usuario.set_password(validated_data['new_password'])
            usuario.save()
        except:
            raise serializers.ValidationError({'error': 'Error ao salvar usuario. ' + e})

        try:
            funcionario = Funcionario()
            funcionario.cpf = validated_data['cpf']
            funcionario.nome = validated_data['nome']
            funcionario.jornada = validated_data['jornada']
            funcionario.empresa = validated_data['empresa']
            funcionario.user = usuario
            funcionario.save()
        except:
            raise serializers.ValidationError({'error': 'Error ao salvar funcionário.'})

        return funcionario

    def update(self, instance, validated_data):
        try:
            instance.cpf = validated_data['cpf']
            instance.nome = validated_data['nome']
            instance.jornada = validated_data['jornada']
            instance.user.cpf = validated_data['cpf']
            instance.user.email = validated_data['email']
            instance.user.username = validated_data['username']
            if 'new_password' in validated_data:
                instance.user.set_password(validated_data['new_password'])
            instance.user.save()
            instance.save()
        except:
            raise serializers.ValidationError({'error': 'Error ao salvar funcionário.'})

        return instance