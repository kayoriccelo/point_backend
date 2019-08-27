from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_simplejwt import views as jwt_views

from apps.core.views import CustomTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('apps.core.urls')),
    url(r'^api/token/$', CustomTokenView.as_view(), name='token_obtain_pair'),
    url(r'^api/token-refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
