
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from hotel.views import HabiacionListView, HomeTemplateView
=======
from hotel.views import HabiacionListView
>>>>>>> 7716b6c7481c705a0dcd04b897689f2e2377fad9
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', HomeTemplateView.as_view(), name='home'),
    path('habitaciones/', HabiacionListView.as_view(), name='listaHabitaciones'),
=======
    path('', HabiacionListView.as_view(), name='listaHabitaciones'),
>>>>>>> 7716b6c7481c705a0dcd04b897689f2e2377fad9
    path('atenciones/', include('hotel.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
