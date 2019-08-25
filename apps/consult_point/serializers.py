from datetime import datetime, timedelta
from collections import OrderedDict

from rest_framework import serializers

from apps.employee.models import Employee
from apps.point_marking.models import PointMarking


class ConsultPointSerializer(serializers.Serializer):
    def validate(self, attrs):

        try:
            attrs['employee'] = Employee.objects.get(cpf=self.context['request']['cpf'],
                                                     company__employees__user__cpf=self.context['user'].cpf)
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
            return points_filter.first().hour

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

        for item_data in self.daterange(datetime.strptime(data['start'], '%Y-%m-%d').date(),
                                        datetime.strptime(data['end'], '%Y-%m-%d').date()):
            points = PointMarking.objects.filter(employee=data['employee'], data=item_data)

            point_dict = OrderedDict()
            point_dict['data'] = item_data.strftime('%d/%m/%Y')
            point_dict['entry'] = self.get_point_marking(points, 'E')
            point_dict['interval_output'] = self.get_point_marking(points, 'SI')
            point_dict['return_interval'] = self.get_point_marking(points, 'R')
            point_dict['leave'] = self.get_point_marking(points, 'S')

            ret['points'].append(point_dict)

        return ret
