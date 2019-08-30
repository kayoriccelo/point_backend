from rest_framework import serializers
from collections import OrderedDict
from django.db.models import Count

from apps.employee.models import Employee
from apps.point_marking.models import PointMarking


class DashboardSerializer(serializers.Serializer):

    def incrementa_item(self, field, values, label):
        colors = [
            'fill-color: #0a2910; fill-opacity: 0.7;',
            'fill-color: #155121; fill-opacity: 0.7;',
            'fill-color: #1a6529; fill-opacity: 0.7;',
            'fill-color: #258e3a; fill-opacity: 0.7;',
            'fill-color: #2fb64a; fill-opacity: 0.7;',
            'fill-color: #49d064; fill-opacity: 0.7;',
            'fill-color: #71da86; fill-opacity: 0.7;',
            'fill-color: #9ae5a9; fill-opacity: 0.7;',
            'fill-color: #c2efcb; fill-opacity: 0.7;',
            'fill-color: #ebfaee; fill-opacity: 0.7;',
        ]

        ret = [["Element", label, {"role": "style"}, {"role": "style"}]]

        for index, value in enumerate(values):
            item = [
                value[field],
                value['count'],
                colors[index],
                'opacity: 0.2'
            ]
            ret.append(item)

        return ret

    def to_representation(self, instance):
        request = self.context

        params = {'company': Employee.objects.get(cpf=request['user'].cpf).company}

        employees = Employee.objects.filter(**params).values('journey__description').annotate(
            count=Count('journey__description')).order_by('-name')[:10]

        points = PointMarking.objects.filter(employee__company=params['company']).values(
            'employee__journey__description').annotate(count=Count('employee__journey__description')).order_by(
            '-employee__journey__description')[:10]

        dashboard_dict = OrderedDict()
        dashboard_dict['employees'] = self.incrementa_item('journey__description', employees, 'Employees')
        dashboard_dict['points'] = self.incrementa_item('employee__journey__description', points, 'Point Marking')

        return dashboard_dict
