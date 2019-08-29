from rest_framework import serializers

from apps.journey.models import Journey
from apps.user_custom.models import UserCustom
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    journey_display = serializers.CharField(source='journey.description')

    class Meta:
        model = Employee
        fields = '__all__'

    def to_internal_value(self, data):
        return data

    def validate(self, attrs):
        data = self.context['request'].data

        if not 'cpf' in data or not data['cpf']:
            raise serializers.ValidationError('Cpf not informed.')

        try:
            data['user'] = UserCustom.objects.get(cpf=data['cpf'])
        except:
            data['user'] = None

        if not 'name' in data or not data['name']:
            raise serializers.ValidationError('Name not informed.')

        if not 'journey' in data or not data['journey']:
            raise serializers.ValidationError('Journey not informed.')

        try:
            data['company'] = Employee.objects.get(cpf=self.context['request'].user.cpf).company
        except UserCustom.DoesNotExist:
            raise serializers.ValidationError('Company not found.')

        try:
            data['journey'] = Journey.objects.get(id=data['journey'])
        except Journey.DoesNotExist:
            raise serializers.ValidationError('Journey not found.')

        return data

    def create(self, validated_data):
        try:
            employee = Employee()
            employee.cpf = validated_data['cpf']
            employee.name = validated_data['name']
            employee.journey = validated_data['journey']
            employee.company = validated_data['company']
            employee.user = validated_data['user']
            employee.save()
        except:
            raise serializers.ValidationError({'non_field_errors': 'Unable to save employee.'})

        return employee

    def update(self, instance, validated_data):
        try:
            instance.cpf = validated_data['cpf']
            instance.name = validated_data['name']
            instance.journey = validated_data['journey']
            instance.user = validated_data['user']
            instance.save()
        except:
            raise serializers.ValidationError({'non_field_errors': 'Unable to save employee.'})

        return instance
