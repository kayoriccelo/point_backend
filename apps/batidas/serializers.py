from datetime import datetime, timedelta
from collections import OrderedDict

from rest_framework import serializers

from apps.funcionarios.models import Funcionario
from apps.marcacao.models import Marcacao


class BatidaSerializer(serializers.Serializer):
    def validate(self, attrs):

        try:
            attrs['funcionario'] = Funcionario.objects.get(cpf=self.context['request']['cpf'],
                                                           empresa__funcionarios__user__cpf=self.context['user'].cpf)
        except:
            raise serializers.ValidationError({'error': 'Cpf não cadastrado.'})

        if 'inicio' in self.context['request']:
            attrs['inicio'] = self.context['request']['inicio']
        else:
            raise serializers.ValidationError({'error': 'Inicio não informado.'})

        if 'final' in self.context['request']:
            attrs['final'] = self.context['request']['final']
        else:
            raise serializers.ValidationError({'error': 'Final não informado.'})

        return attrs

    @staticmethod
    def daterange(d1, d2):
        return (d1 + timedelta(days=i) for i in range((d2 - d1).days + 1))

    @staticmethod
    def get_marcacao(lista, tipo):
        marcacao = lista.filter(tipo=tipo)

        if marcacao.count() > 0:
            return marcacao.first().hora

        return '-'

    def to_representation(self, instance):
        data = self.validated_data

        jornada = data['funcionario'].jornada
        ret = OrderedDict()
        ret['cpf'] = data['funcionario'].cpf
        ret['nome'] = data['funcionario'].nome
        ret['jornada'] = f'{jornada.codigo} - {jornada.descricao}: `{jornada.entrada} / ' \
            f'{jornada.saida_intervalo} / {jornada.retorno_intervalo} / {jornada.saida}`'
        ret['marcacoes'] = []

        for item_data in self.daterange(datetime.strptime(data['inicio'], '%Y-%m-%d').date(),
                                        datetime.strptime(data['final'], '%Y-%m-%d').date()):
            marcacoes = Marcacao.objects.filter(funcionario=data['funcionario'], data=item_data)

            marc_dict = OrderedDict()
            marc_dict['data'] = item_data.strftime('%d/%m/%Y')
            marc_dict['entrada'] = self.get_marcacao(marcacoes, 'E')
            marc_dict['saida_intervalo'] = self.get_marcacao(marcacoes, 'SI')
            marc_dict['retorno_intervalo'] = self.get_marcacao(marcacoes, 'R')
            marc_dict['saida'] = self.get_marcacao(marcacoes, 'S')

            ret['marcacoes'].append(marc_dict)

        return ret
