from django.urls import path
from django.conf import settings
from .views import (HabiacionCreateView, HabiacionListView, HabiacionUpdateView, HabitacionDeleteView, CrearConsultaView, ResponderConsultaView, DetalleConsultaView,
                    ListaConsultasView, ModificarConsultaView, EliminarConsultaView, CrearReclamoView, ListaReclamoView, ResponderReclamoView, DetalleReclamoView,
                    ModificarReclamoView, EliminarReclamoView, ReservaCreateView, ModificarReservaView, HabitacionDetailView, ReservaListarView, ReservaDeleteView, generar_pdf_detalle_reserva, ver_grafico_reservas,
                    CrearAnuncioView, ModificarAnuncioView, EliminarAnuncioView, ListarAnuncioView, ServicioCreateView, ServicioListView, ServicioUpdateView, ServicioDeleteView,
                    RegistrarRoomServiceView, RoomServiceDeleteView, RoomServiceListView, RoomServiceUpdateView)

urlpatterns = [
    path('listaHabitaciones/', HabiacionListView.as_view(), name='listaHabitaciones'),
    path('crearHabitacion/', HabiacionCreateView.as_view(), name='crearHabitacion'),
    path('actualizarHabitacion/<int:pk>/', HabiacionUpdateView.as_view(), name='actualizarHabitacion'),
    path('eliminarHabitacion/<int:pk>/', HabitacionDeleteView.as_view(), name='eliminarHabitacion'),
    path('detailHabitacion/<int:pk>/', HabitacionDetailView.as_view(), name='detailRoom'),

    path('crearConsulta/', CrearConsultaView.as_view(), name='crearConsulta'),
    path('responderConsulta/<int:pk>/', ResponderConsultaView.as_view(), name='responderConsulta'),
    path('listaConsultas/', ListaConsultasView.as_view(), name='listaConsultas'),
    path('modificarConsultas/<int:pk>/', ModificarConsultaView.as_view(), name='modificarConsultas'),
    path('eliminarConsultas/<int:pk>/', EliminarConsultaView.as_view(), name='eliminarConsultas'),
    path('detalleConsulta/<int:pk>/', DetalleConsultaView.as_view(), name='detalleConsulta'),

    path('crearReclamo/', CrearReclamoView.as_view(), name='crearReclamo'),
    path('responderReclamo/<int:pk>/', ResponderReclamoView.as_view(), name='responderReclamo'),
    path('listaReclamos/', ListaReclamoView.as_view(), name='listaReclamos'),
    path('modificarReclamo/<int:pk>/', ModificarReclamoView.as_view(), name='modificarReclamo'),
    path('eliminarReclamo/<int:pk>/', EliminarReclamoView.as_view(), name='eliminarReclamo'),
    path('reclamo/<int:pk>/', DetalleReclamoView.as_view(), name='detalleReclamo'),
    
    path('crearReserva/<int:pk>/', ReservaCreateView.as_view(), name='createReserva'),
    path('listReserva/', ReservaListarView.as_view(), name='listaReservas'),
    path('eliminarReserva/<int:pk>/', ReservaDeleteView.as_view(), name='eliminar_reserva'),
    path('generar_pdf/<int:reserva_id>/', generar_pdf_detalle_reserva, name='generar_pdf'),
    path('ver-grafico-reservas/', ver_grafico_reservas, name='ver_grafico_reservas'),
    path('modificarReserva/<int:pk>/', ModificarReservaView.as_view(), name='modificarReserva'),    
    path('crearAnuncio/', CrearAnuncioView.as_view(), name='crear_anuncio'), 
    path('listaAnuncios/', ListarAnuncioView.as_view(), name='lista_anuncios'), 
    path('editar/<int:pk>/', ModificarAnuncioView.as_view(), name='modificar_anuncio'), 
    path('eliminar/<int:pk>/', EliminarAnuncioView.as_view(), name='eliminar_anuncio'),
    
    path('crearServicio/', ServicioCreateView.as_view(), name='crear_servicio'),
    path('listaServicios/', ServicioListView.as_view(), name='listaServicios'),
    path('modificarServicio/<int:pk>/', ServicioUpdateView.as_view(), name='modificar_servicio'),
    path('eliminarServicio/<int:pk>/', ServicioDeleteView.as_view(), name='eliminar_servicio'),
    
    path('registrarSolicitud/', RegistrarRoomServiceView.as_view(), name='registrar_Solicitud'),
    path('eliminarSolicitud/<int:pk>/', RoomServiceDeleteView.as_view(), name='eliminar_Solicitud'),
    path('modificarSolicitud/<int:pk>/', RoomServiceUpdateView.as_view(), name='modificar_Solicitud'),
    path('listaSolicitudes/', RoomServiceListView.as_view(), name='listaSolicitudes'),
    ]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
