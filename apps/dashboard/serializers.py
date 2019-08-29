from rest_framework import serializers
from collections import OrderedDict
from django.db.models import Count

from apps.employee.models import Employee
from apps.point_marking.models import PointMarking


class DashboardSerializer(serializers.Serializer):

    def incrementa_item(self, field, values, label):
        colors = [
            'fill-color: rgb(124, 181, 236); fill-opacity: 0.6;',
            'fill-color: rgb(0, 134, 64); fill-opacity: 0.6;',
            'fill-color: rgb(247, 163, 92); fill-opacity: 0.6;',
            'fill-color: rgb(144, 237, 125); fill-opacity: 0.6;',
            'fill-color: rgb(128, 133, 233); fill-opacity: 0.6;',
            'fill-color: rgb(241, 92, 128); fill-opacity: 0.6;',
            'fill-color: rgb(228, 211, 84); fill-opacity: 0.6;',
            'fill-color: rgb(43, 144, 143); fill-opacity: 0.6;',
            'fill-color: rgb(244, 91, 91); fill-opacity: 0.6;',
            'fill-color: rgb(145, 232, 225); fill-opacity: 0.6;'
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
