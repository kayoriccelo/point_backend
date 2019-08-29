from rest_framework import serializers

from apps.employee.models import Employee
from .models import Journey


class JourneySerializer(serializers.ModelSerializer):

    class Meta:
        model = Journey
        fields = '__all__'

    def to_internal_value(self, data):
        return data

    def validate(self, attrs):
        data = self.context['request'].data

        if not 'code' in data or not data['code']:
            raise serializers.ValidationError('Code not informed.')

        if not 'description' in data or not data['description']:
            raise serializers.ValidationError('Description not informed.')

        try:
            data['company'] = Employee.objects.get(cpf=self.context['request'].user.cpf).company
        except Employee.DoesNotExist:
            raise serializers.ValidationError('Company not found.')

        return super(JourneySerializer, self).validate(attrs)
