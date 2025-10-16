
from django.contrib import admin
from django.urls import path, include
from hotel.views import HabiacionListView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HabiacionListView.as_view(), name='listaHabitaciones'),
    path('atenciones/', include('hotel.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
