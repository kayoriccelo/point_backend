from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.point_marking.viewsets import PointMarkingViewSet
from apps.company.viewsets import CompanyViewSet
from apps.employee.viewsets import EmployeeViewSet
from apps.journey.viewsets import JourneyViewSet
from apps.consult_point.viewsets import ConsultPointViewSet


router = DefaultRouter()
router.register(r'company', CompanyViewSet, base_name='company')
router.register(r'employee', EmployeeViewSet, base_name='employee')
router.register(r'journey', JourneyViewSet, base_name='journey')
router.register(r'pointmarking', PointMarkingViewSet, base_name='pointmarking')

urlpatterns = router.urls

urlpatterns += [
    url(r'^consultpoint/', ConsultPointViewSet.as_view()),
]
