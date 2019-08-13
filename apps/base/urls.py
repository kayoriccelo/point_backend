from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.usuarios.viewsets import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, base_name='usuario')

urlpatterns = router.urls
