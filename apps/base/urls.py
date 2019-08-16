from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.marcacao.viewsets import MarcacaoViewSet
from apps.usuarios.viewsets import UsuarioViewSet
from apps.empresa.viewsets import EmpresaViewSet
from apps.funcionarios.viewsets import FuncionarioViewSet
from apps.jornadas.viewsets import JornadaViewSet
from apps.batidas.viewsets import BatidaViewSet


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, base_name='usuario')
router.register(r'empresa', EmpresaViewSet, base_name='empresa')
router.register(r'funcionarios', FuncionarioViewSet, base_name='funcionario')
router.register(r'jornadas', JornadaViewSet, base_name='jornada')
router.register(r'marcacoes', MarcacaoViewSet, base_name='marcacao')

urlpatterns = router.urls

urlpatterns += [
    url(r'^batidas/', BatidaViewSet.as_view()),
]
