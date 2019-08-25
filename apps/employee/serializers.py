from rest_framework import serializers

from apps.journey.models import Journey
from apps.user_custom.models import UserCustom
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email')
    username = serializers.CharField(source='user.username')
    journey_display = serializers.CharField(source='journey.description')

    class Meta:
        model = Employee
        fields = '__all__'

    def to_internal_value(self, data):
        return data

    def validate(self, attrs):
        data = self.context['request'].data

        if not 'cpf' in data or not data['cpf']:
            raise serializers.ValidationError({'error': 'Cpf not informed.'})

        if self.context['request'].method == 'POST':
            try:
                user_custom = UserCustom.objects.get(cpf=data['cpf'])
            except:
                user_custom = None
            if user_custom:
                raise serializers.ValidationError({'error': 'Cpf already registered.'})

        if not 'name' in data or not data['name']:
            raise serializers.ValidationError({'error': 'Name not informed.'})

        if not 'journey' in data or not data['journey']:
            raise serializers.ValidationError({'error': 'Journey not informed.'})

        if not 'email' in data or not data['email']:
            raise serializers.ValidationError({'error': 'Email not informed.'})

        if not 'username' in data or not data['username']:
            raise serializers.ValidationError({'error': 'Username not informed.'})

        if self.context['request'].method == 'POST':
            if not 'new_password' in data or not data['new_password']:
                raise serializers.ValidationError({'error': 'Password not informed.'})

        try:
            data['company'] = Employee.objects.get(cpf=self.context['request'].user.cpf).company
        except Employee.DoesNotExist:
            raise serializers.ValidationError({'error': 'Company not found.'})

        try:
            data['journey'] = Journey.objects.get(id=data['journey'])
        except Journey.DoesNotExist:
            raise serializers.ValidationError({'error': 'Journey not found.'})

        return data

    def create(self, validated_data):
        try:
            user_custom = UserCustom()
            user_custom.cpf = validated_data['cpf']
            user_custom.email = validated_data['email']
            user_custom.first_name = validated_data['nome']
            user_custom.username = validated_data['username']
            user_custom.set_password(validated_data['new_password'])
            user_custom.save()
        except:
            raise serializers.ValidationError({'error': 'Unable to save user.'})

        try:
            employee = Employee()
            employee.cpf = validated_data['cpf']
            employee.name = validated_data['name']
            employee.journey = validated_data['journey']
            employee.company = validated_data['company']
            employee.user = user_custom
            employee.save()
        except:
            raise serializers.ValidationError({'error': 'Unable to save employee.'})

        return employee

    def update(self, instance, validated_data):
        try:
            instance.cpf = validated_data['cpf']
            instance.name = validated_data['name']
            instance.journey = validated_data['journey']
            instance.user.cpf = validated_data['cpf']
            instance.user.email = validated_data['email']
            instance.user.username = validated_data['username']
            if 'new_password' in validated_data:
                instance.user.set_password(validated_data['new_password'])
            instance.user.save()
            instance.save()
        except:
            raise serializers.ValidationError({'error': 'Unable to save employee.'})

        return instance
