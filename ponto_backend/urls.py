from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from apps.base.views import CustomTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('apps.base.urls')),
    url(r'^api/token/$', CustomTokenView.as_view(), name='token_obtain_pair'),
]
