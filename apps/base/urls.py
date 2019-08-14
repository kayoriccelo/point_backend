from rest_framework.routers import DefaultRouter

from apps.usuarios.viewsets import UsuarioViewSet
from apps.empresa.viewsets import EmpresaViewSet
from apps.funcionarios.viewsets import FuncionarioViewSet
from apps.jornadas.viewsets import JornadaViewSet


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, base_name='usuario')
router.register(r'empresa', EmpresaViewSet, base_name='empresa')
router.register(r'funcionarios', FuncionarioViewSet, base_name='funcionario')
router.register(r'jornadas', JornadaViewSet, base_name='jornada')


urlpatterns = router.urls
