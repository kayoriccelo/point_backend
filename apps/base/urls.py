from rest_framework.routers import DefaultRouter

from apps.usuarios.viewsets import UsuarioViewSet
from apps.empresa.viewsets import EmpresaViewSet


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, base_name='usuario')
router.register(r'empresa', EmpresaViewSet, base_name='empresa')


urlpatterns = router.urls
