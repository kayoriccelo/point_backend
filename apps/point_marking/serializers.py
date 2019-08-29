from datetime import datetime

from rest_framework import serializers

from apps.employee.models import Employee
from apps.user_custom.models import UserCustom
from .models import PointMarking


class PointMarkingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PointMarking
        fields = '__all__'

    def to_internal_value(self, data):
        return data

    def validate(self, attrs):

        if not 'type' in attrs:
            raise serializers.ValidationError('Type not informed.')

        if not 'cpf' in attrs:
            raise serializers.ValidationError('Cpf not informed.')

        if not 'hour' in attrs:
            raise serializers.ValidationError('Hour not informed.')

        if not 'password' in attrs:
            raise serializers.ValidationError('Password not informed.')

        try:
            attrs['employee'] = Employee.objects.get(cpf=attrs['cpf'])
        except Employee.DoesNotExist:
            raise serializers.ValidationError('Cpf not registered.')

        try:
            user_custom = UserCustom.objects.get(cpf=attrs['cpf'])
        except Employee.DoesNotExist:
            raise serializers.ValidationError('User not found.')

        if not user_custom.check_password(attrs['password']):
            raise serializers.ValidationError('Password invalid.')

        points = PointMarking.objects.filter(employee__cpf=attrs['cpf'], date=datetime.now().date(), type=attrs['type'])

        if points.count() > 0:
            raise serializers.ValidationError('This type of marking has already been made.')

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
            raise serializers.ValidationError({'non_field_errors': 'Could not mark point.'})

        return point_marking


