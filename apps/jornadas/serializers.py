from rest_framework import serializers

from .models import Jornada


class JornadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jornada
        fields = '__all__'
