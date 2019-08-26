from rest_framework import serializers

from apps.user_custom.models import UserCustom
from .models import Journey


class JourneySerializer(serializers.ModelSerializer):

    class Meta:
        model = Journey
        fields = '__all__'

    def to_internal_value(self, data):
        return data

    def validate(self, attrs):
        data = self.context['request'].data

        try:
            data['company'] = UserCustom.objects.get(cpf=self.context['request'].user.cpf).company
        except UserCustom.DoesNotExist:
            raise serializers.ValidationError({'error': 'Company not found.'})

        return super(JourneySerializer, self).validate(attrs)
