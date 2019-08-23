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
router.register(r'company', EmpresaViewSet, base_name='company')
router.register(r'employee', FuncionarioViewSet, base_name='employee')
router.register(r'journey', JornadaViewSet, base_name='journey')
router.register(r'pointmarking', MarcacaoViewSet, base_name='pointmarking')

urlpatterns = router.urls

urlpatterns += [
    url(r'^consultpoint/', BatidaViewSet.as_view()),
]
