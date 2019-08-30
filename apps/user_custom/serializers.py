from collections import OrderedDict

from rest_framework import serializers

from .models import UserCustom


class UserCustomSerializer(serializers.Serializer):

    def validate(self, attrs):
        data = self.context['request'].data

        try:
            UserCustom.objects.get(cpf=data['cpf'])
            raise serializers.ValidationError(u'You already have an account.')
        except UserCustom.DoesNotExist:
            pass

        try:
            UserCustom.objects.get(username=data['username'])
            raise serializers.ValidationError(u'Existing username.')
        except UserCustom.DoesNotExist:
            pass

        try:
            UserCustom.objects.get(email=data['email'])
            raise serializers.ValidationError(u'Existing email.')
        except UserCustom.DoesNotExist:
            pass

        return attrs

    def save(self, **kwargs):
        data = self.context['request'].data

        try:
            usuario = UserCustom(
                cpf=data['cpf'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                username=data['username'],
                is_active=True,
                is_staff=False
            )
            usuario.set_password(data['password'])
            usuario.save()
        except Exception as e:
            raise serializers.ValidationError({'non_field_errors': [u'Unable to register a new account. ']})

        return usuario

    def to_representation(self, instance):
        ret = OrderedDict()
        if instance:
            ret['cpf'] = instance.cpf
            ret['name'] = instance.first_name + ' ' + instance.last_name
            ret['role'] = 'admin' if instance.is_admin else 'guest'
            ret['isAuthenticated'] = True
        return ret


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCustom
        fields = ('id', 'first_name', 'last_name')

    def validate(self, attrs):

        if not 'new_password' in self.context['request'].data:
            raise serializers.ValidationError(u'New Password not informed.')

        if not 'password' in self.context['request'].data:
            raise serializers.ValidationError(u'Password not informed.')

        if not self.context['request'].user.check_password(self.context['request'].data['password']):
            raise serializers.ValidationError(u'Password invalid.')

        if not 'new_password' in self.context['request'].data:
            raise serializers.ValidationError(u'New Password not informed.')

        attrs['new_password'] = self.context['request'].data['new_password']

        return attrs

    def update(self, instance, validated_data):
        try:
            instance.first_name = validated_data['first_name']
            instance.last_name = validated_data['last_name']
            instance.set_password(validated_data['new_password'])
            instance.save()
        except Exception as e:
            raise serializers.ValidationError({'non_field_errors': [u'Unable to save profile. ']})

        return instance
