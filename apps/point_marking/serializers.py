from datetime import datetime

from rest_framework import serializers

from apps.employee.models import Employee
from .models import PointMarking


class PointMarkingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PointMarking
        fields = '__all__'

    def to_internal_value(self, data):
        return data

    def validate(self, attrs):

        if not 'cpf' in attrs:
            raise serializers.ValidationError({'error': 'Cpf not informed.'})

        if not 'hour' in attrs:
            raise serializers.ValidationError({'error': 'Hour not informed.'})

        if not 'password' in attrs:
            raise serializers.ValidationError({'error': 'Password not informed.'})

        if not 'type' in attrs:
            raise serializers.ValidationError({'error': 'Type not informed.'})

        try:
            attrs['employee'] = Employee.objects.get(cpf=attrs['cpf'])
        except Employee.DoesNotExist:
            raise serializers.ValidationError({'error': 'Cpf not registered.'})

        points = PointMarking.objects.filter(employee__cpf=attrs['cpf'], date=datetime.now().date(), type=attrs['type'])

        if points.count() > 0:
            raise serializers.ValidationError({'error': 'This type of marking has already been made.'})

        return attrs

    def create(self, validated_data):

        try:
            point_marking = PointMarking()
            point_marking.date = datetime.now().date()
            point_marking.day_week = datetime.now().isoweekday()
            point_marking.hour = validated_data['hour'][0:5]
            point_marking.type = validated_data['type']
            point_marking.employee = validated_data['employee']
            point_marking.save()
        except Exception as e:
            raise serializers.ValidationError({'error': 'Could not mark point.'})

        return point_marking


