from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from core import settings
from core.yasg import urlpatterns as urlpatterns_yasg

urlpatterns = [
    path('', include('apps.shop.urls', namespace='shop')),
    path('user/', include('apps.user.urls', namespace='user')),
    path('basket/', include('apps.basket.urls', namespace='basket')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ----- API -----
urlpatterns += [
    path('api/v1/api-auth/', include('rest_framework.urls')),
    path('api/v1/token-auth/', include('djoser.urls')),
    re_path(r'^token-auth/', include('djoser.urls.authtoken')),
]

urlpatterns += urlpatterns_yasg
