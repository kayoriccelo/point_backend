from datetime import datetime, timedelta
from collections import OrderedDict

from rest_framework import serializers

from apps.employee.models import Employee
from apps.point_marking.models import PointMarking


class ConsultPointSerializer(serializers.Serializer):
    def validate(self, attrs):

        try:
            company = Employee.objects.get(cpf=self.context['user'].cpf).company
        except:
            raise serializers.ValidationError({'error': 'Employee not registered at company.'})

        cpf = self.context['request']['cpf'] if 'cpf' in self.context['request'] else self.context['user'].cpf

        try:
            attrs['employee'] = Employee.objects.get(cpf=cpf, company=company)
        except:
            raise serializers.ValidationError({'error': 'Cpf not registered.'})

        if 'start' in self.context['request']:
            attrs['start'] = self.context['request']['start']
        else:
            raise serializers.ValidationError({'error': 'Start not informed.'})

        if 'end' in self.context['request']:
            attrs['end'] = self.context['request']['end']
        else:
            raise serializers.ValidationError({'error': 'End not informed.'})

        return attrs

    @staticmethod
    def daterange(d1, d2):
        return (d1 + timedelta(days=i) for i in range((d2 - d1).days + 1))

    @staticmethod
    def get_point_marking(points, type_marking):
        points_filter = points.filter(type=type_marking)

        if points_filter.count() > 0:
            return str(points_filter.first().hour)[0:5]

        return '-'

    def to_representation(self, instance):
        data = self.validated_data

        journey = data['employee'].journey
        ret = OrderedDict()
        ret['cpf'] = data['employee'].cpf
        ret['name'] = data['employee'].name
        ret['journey'] = f'{journey.code} - {journey.description}: `{journey.entry} / ' \
            f'{journey.interval_output} / {journey.return_interval} / {journey.leave}`'
        ret['points'] = []

        for item_date in self.daterange(datetime.strptime(data['start'], '%Y-%m-%d').date(),
                                        datetime.strptime(data['end'], '%Y-%m-%d').date()):
            points = PointMarking.objects.filter(employee=data['employee'], date=item_date)

            point_dict = OrderedDict()
            point_dict['date'] = item_date.strftime('%d/%m/%Y')
            point_dict['entry'] = self.get_point_marking(points, 'E')
            point_dict['interval_output'] = self.get_point_marking(points, 'SI')
            point_dict['return_interval'] = self.get_point_marking(points, 'R')
            point_dict['leave'] = self.get_point_marking(points, 'S')

            ret['points'].append(point_dict)

        return ret
