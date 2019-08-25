from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ConsultPointSerializer


class ConsultPointViewSet(APIView):
    serializer_class = ConsultPointSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data={}, context={'request': self.request.GET, 'user': self.request.user})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
