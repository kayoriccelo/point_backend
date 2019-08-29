from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import DashboardSerializer


class DashboardViewSet(APIView):
    serializer_class = DashboardSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data={}, context={'request': self.request.GET, 'user': self.request.user})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)