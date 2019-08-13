from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.Serializer):

    def validate(self, attrs):
        data = self.context['request'].data

        try:
            Usuario.objects.get(cpf=data['cpf'])
            raise serializers.ValidationError(u'Já possui um conta.')
        except Usuario.DoesNotExist:
            pass

        try:
            Usuario.objects.get(username=data['login'])
            raise serializers.ValidationError(u'login já existente.')
        except Usuario.DoesNotExist:
            pass

        return attrs

    def save(self, **kwargs):
        data = self.context['request'].data

        try:
            usuario = Usuario(cpf=data['cpf'], last_name=data['nome'],
                              email=data['email'], username=data['login'])
            usuario.set_password(data['senha'])
            usuario.save()
        except:
            raise serializers.ValidationError(u'Erro ao cadastrar nova conta.')

        return usuario
