from django.shortcuts import redirect, render
<<<<<<< HEAD
from django.views.generic import TemplateView
=======
>>>>>>> 7716b6c7481c705a0dcd04b897689f2e2377fad9
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Habitacion, Consulta, Reclamo, Reserva, Usuario, Anuncio, Servicio, RoomService
from .forms import HabitacionForm, ConsultaForm, ReclamoForm, ReservaForm, RespuestaReclamoForm, RespuestaConsultaForm, AnuncioForm, ServicioForm, RoomServiceForm
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.views.decorators.cache import cache_control
from datetime import datetime
import pytz
from django.http import HttpResponse
from django.db.models import Count
from django.conf import settings
import os
import matplotlib.pyplot as plt
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# def es_administrador(user): 
#     return Trabajador.objects.filter(user=user, rol__nombre='Administrador').exists()

class HabiacionListView(ListView):
    model = Habitacion
    template_name = 'hotel/list_habitacion.html'
    context_object_name = 'habitacion'

<<<<<<< HEAD
class HomeTemplateView(TemplateView):
    template_name = 'hotel/base.html'

=======
>>>>>>> 7716b6c7481c705a0dcd04b897689f2e2377fad9
@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
# @method_decorator(user_passes_test(es_administrador), name='dispatch')
class HabiacionCreateView(CreateView):
    model = Habitacion
    template_name = 'hotel/habitacion_form.html'
    success_url = reverse_lazy('listaHabitaciones')
    form_class = HabitacionForm

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch') 
# @method_decorator(user_passes_test(es_administrador), name='dispatch')
class HabiacionUpdateView(UpdateView):
    model = Habitacion
    template_name = 'hotel/actualizar_habitacion.html'
    success_url = reverse_lazy('listaHabitaciones')
    form_class = HabitacionForm

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch') 
# @method_decorator(user_passes_test(es_administrador), name='dispatch')   
class HabitacionDeleteView(DeleteView):
    model = Habitacion
    template_name = 'hotel/confirmar_eliminacion.html'
    context_object_name = 'habitacion'
    success_url = reverse_lazy('listaHabitaciones')
    
class HabitacionDetailView(DetailView):
    model = Habitacion
    template_name = 'hotel/detalle_habitacion.html'
    context_object_name = 'habitacion'

@method_decorator(login_required, name='dispatch')     
class ResponderConsultaView(UpdateView): 
    model = Consulta 
    form_class = RespuestaConsultaForm 
    template_name = 'hotel/responder_consulta.html' 
    success_url = reverse_lazy('listaConsultas')
    
    def form_valid(self, form): 
        return super().form_valid(form)

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class CrearConsultaView(CreateView):
    model = Consulta
    template_name = 'hotel/consulta.html'
    form_class = ConsultaForm
    success_url = reverse_lazy('listaConsultas')

    def form_valid(self, form):
        usuario = Usuario.objects.filter(user=self.request.user).first()

        if usuario:
            form.instance.usuario = usuario
            return super().form_valid(form)
        else:
            form.add_error(None, 'El usuario logueado no tiene un perfil de Usuario asociado.')
            return self.form_invalid(form)

@method_decorator(login_required, name='dispatch')
class ListaConsultasView(ListView):
    model = Consulta
    template_name = 'hotel/listaConsultas.html'
    context_object_name = 'consulta'

    def get_queryset(self):
        user = self.request.user
        usuario = Usuario.objects.filter(user=user).first()

        if usuario and usuario.rol and usuario.rol.nombre in ['Administrador', 'Recepcionista']:
            return Consulta.objects.all()
        elif usuario and usuario.rol and usuario.rol.nombre == 'Huesped':
            return Consulta.objects.filter(usuario=usuario)
        else:
            return Consulta.objects.none()

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class ModificarConsultaView(UpdateView):
    model = Consulta
    template_name = 'hotel/modificarConsulta.html'
    success_url = reverse_lazy('listaConsultas')
    form_class = ConsultaForm

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class EliminarConsultaView(DeleteView):
    model = Consulta
    template_name = 'hotel/eliminarConsulta.html'
    context_object_name = 'consulta'
    success_url = reverse_lazy('listaConsultas')

@method_decorator(login_required, name='dispatch')     
class DetalleConsultaView(DeleteView):
    model = Consulta 
    template_name = 'hotel/detalle_consulta.html' 
    context_object_name = 'consulta'

@method_decorator(login_required, name='dispatch')    
class ResponderReclamoView(UpdateView): 
    model = Reclamo 
    form_class = RespuestaReclamoForm 
    template_name = 'hotel/responder_reclamo.html' 
    success_url = reverse_lazy('listaReclamos')
    
    def form_valid(self, form): 
        return super().form_valid(form)

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class CrearReclamoView(CreateView):
    model = Reclamo
    template_name = 'hotel/crearReclamo.html'
    form_class = ReclamoForm
    success_url = reverse_lazy('listaReclamos')

    def form_valid(self, form):
        usuario = Usuario.objects.filter(user=self.request.user).first()

        if usuario:
            form.instance.usuario = usuario
            return super().form_valid(form)
        else:
            form.add_error(None, 'El usuario logueado no tiene un perfil de Usuario asociado.')
            return self.form_invalid(form)
        
@method_decorator(login_required, name='dispatch')
class ListaReclamoView(ListView):
    model = Reclamo
    template_name = 'hotel/listaReclamos.html'
    context_object_name = 'reclamo'

    def get_queryset(self):
        user = self.request.user
        usuario = Usuario.objects.filter(user=user).first()

        if usuario and usuario.rol and usuario.rol.nombre in ['Administrador', 'Recepcionista']:
            return Reclamo.objects.all()
        elif usuario and usuario.rol and usuario.rol.nombre == 'Huesped':
            return Reclamo.objects.filter(usuario=usuario)
        else:
            return Reclamo.objects.none()

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class ModificarReclamoView(UpdateView):
    model = Reclamo
    template_name = 'hotel/modificarReclamo.html'
    success_url = reverse_lazy('listaReclamos')
    form_class = ReclamoForm

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class EliminarReclamoView(DeleteView):
    model = Reclamo
    template_name = 'hotel/eliminarReclamo.html'
    context_object_name = 'reclamo'
    success_url = reverse_lazy('listaReclamos')

@method_decorator(login_required, name='dispatch')     
class DetalleReclamoView(DetailView): 
    model = Reclamo 
    template_name = 'hotel/detalle_reclamo.html' 
    context_object_name = 'reclamo'
    
#reserva

def generar_pdf_detalle_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    perfil = reserva.usuario 

    timezone = pytz.timezone('America/Santiago')
    fecha_llegada_local = reserva.fecha_llegada.astimezone(timezone)
    fecha_salida_local = reserva.fecha_salida.astimezone(timezone)

    fecha_llegada_formateada = fecha_llegada_local.strftime('%d/%m/%Y %I:%M %p')
    fecha_salida_formateada = fecha_salida_local.strftime('%d/%m/%Y %I:%M %p')

    huespedes_menores = "Sí" if reserva.huespedes_menores else "No"

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reserva_{reserva.numero_reserva}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    p.drawString(100, height - 100, f"Detalles de la Reserva #{reserva.numero_reserva}")
    p.drawString(100, height - 140, f"Habitación: {reserva.habitacion.num_habitacion}")
    p.drawString(100, height - 160, f"Fecha de Llegada: {fecha_llegada_formateada}")
    p.drawString(100, height - 180, f"Fecha de Salida: {fecha_salida_formateada}")
    p.drawString(100, height - 200, f"Huéspedes Menores: {huespedes_menores}")
    p.drawString(100, height - 220, f"Preferencias: {reserva.preferencias}")
    p.drawString(100, height - 240, f"Precio por noche: {reserva.habitacion.precio}")
    p.drawString(100, height - 260, f"Precio total: {reserva.precio_total}")

    p.drawString(100, height - 280, "Datos del Usuario:")
    p.drawString(100, height - 300, f"Nombre Completo: {perfil.nombre_completo}")
    p.drawString(100, height - 320, f"Correo Electrónico: {perfil.correo}")
    p.drawString(100, height - 340, f"Teléfono: {perfil.numero_telefonico}")
    p.drawString(100, height - 360, f"RUT: {perfil.rut}")

    p.setFont("Helvetica-Bold", 36)
    p.setFillColorRGB(1, 0, 0)
    p.drawString(width - 200, height - 20, "-------------")
    p.drawString(width - 200, height - 50, "PAGADO")
    p.drawString(width - 200, height - 70, "-------------")

    p.showPage()
    p.save()

    return response

def generar_grafico_reservas(fecha_inicio, fecha_fin):
    todas_las_habitaciones = Habitacion.objects.all()
    
    reservas = Reserva.objects.filter(fecha_llegada__gte=fecha_inicio, fecha_salida__lte=fecha_fin)
        
    reservas_por_habitacion = reservas.values('habitacion__num_habitacion').annotate(total=Count('id')).order_by('-total')
     
    reservas_dict = {reserva['habitacion__num_habitacion']: reserva['total'] for reserva in reservas_por_habitacion}
    
    habitaciones = [habitacion.num_habitacion for habitacion in todas_las_habitaciones] 
    totales = [reservas_dict.get(habitacion.num_habitacion, 0) for habitacion in todas_las_habitaciones]

    plt.figure(figsize=(10, 6))
    plt.bar(habitaciones, totales, color='blue')
    plt.xlabel('Numero de Habitacion')
    plt.ylabel('Numero de Reservas')
    plt.title('Reservas por Habitacion')
    plt.xticks(habitaciones)
    plt.yticks(range(0, max(totales) + 1, 1))
    
    
    grafico = 'reservas_por_habitacion.png'
    ruta_grafico = os.path.join(settings.MEDIA_ROOT, grafico)
    plt.savefig(ruta_grafico)
    plt.close()
    
    return os.path.join(settings.MEDIA_URL, grafico)

def ver_grafico_reservas(request):
    year_actual = datetime.now().year
    
    fecha_inicio = datetime.strptime(f'{year_actual}-01-01', '%Y-%m-%d')
    fecha_fin = datetime.strptime(f'{year_actual + 1}-12-31', '%Y-%m-%d')  
        
    ruta_grafico = generar_grafico_reservas(fecha_inicio, fecha_fin)
        
    return render(request, 'hotel/grafico_reservas.html', {'ruta_grafico': ruta_grafico})


@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'hotel/reserva_form.html'

    def get_success_url(self): 
        return reverse_lazy('listaReservas')

    def form_valid(self, form):
        habitacion_id = self.kwargs['pk']
        habitacion = get_object_or_404(Habitacion, id=habitacion_id)
        fecha_llegada = form.cleaned_data['fecha_llegada']
        fecha_salida = form.cleaned_data['fecha_salida']

        reservas_existentes = Reserva.objects.filter(habitacion=habitacion)
        for reserva in reservas_existentes:
            if fecha_llegada <= reserva.fecha_salida and fecha_salida >= reserva.fecha_llegada:
                form.add_error(None, ValidationError('La habitación se encuentra reservada para las fechas seleccionadas, reintente.'))
                return self.form_invalid(form)

        duracion_estancia = (fecha_salida - fecha_llegada).days
        precio_total = habitacion.precio * duracion_estancia

        form.instance.habitacion = habitacion
        form.instance.precio_total = precio_total

        usuario = None
        if self.request.user.is_authenticated:
            usuario = Usuario.objects.filter(user=self.request.user).first()

        if usuario:
            form.instance.usuario = usuario
            self.object = form.save()
            return super().form_valid(form)
        else:
            self.request.session['reserva_temp'] = {
                'habitacion_id': habitacion.id,
                'fecha_llegada': str(fecha_llegada),
                'fecha_salida': str(fecha_salida),
                'precio_total': precio_total
            }
            return redirect('signup')

    def form_invalid(self, form):
        habitacion_id = self.kwargs['pk']
        habitacion = get_object_or_404(Habitacion, id=habitacion_id)
        reservas_existentes = Reserva.objects.filter(habitacion=habitacion).order_by('fecha_llegada')
        fechas_disponibles = []

        fecha_actual = None
        for reserva in reservas_existentes:
            if fecha_actual is None:
                fecha_actual = reserva.fecha_salida
            elif fecha_actual < reserva.fecha_llegada:
                fechas_disponibles.append((fecha_actual, reserva.fecha_llegada))
                fecha_actual = reserva.fecha_salida
            else:
                fecha_actual = max(fecha_actual, reserva.fecha_salida)

        if fecha_actual is not None:
            fechas_disponibles.append((fecha_actual, None))

        context = self.get_context_data(form=form, fechas_disponibles=fechas_disponibles)
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
class ReservaListarView(ListView):
    model = Reserva
    template_name = 'hotel/mis_reservas.html'
    context_object_name = 'reserva'

    def get_queryset(self):
        user = self.request.user
        usuario = Usuario.objects.filter(user=user).first()

        if usuario and usuario.rol and usuario.rol.nombre in ['Administrador', 'Recepcionista']:
            return Reserva.objects.all()
        elif usuario and usuario.rol and usuario.rol.nombre == 'Huesped':
            return Reserva.objects.filter(usuario=usuario)
        else:
            return Reserva.objects.none()
        
@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')  
class ReservaDeleteView(DeleteView): 
    model = Reserva 
    template_name = 'hotel/eliminar_reserva.html' 
    success_url = reverse_lazy('listaReservas')
    context_object_name = 'reserva'

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class ModificarReservaView(UpdateView):
    model = Reserva
    template_name = 'hotel/modificar_reserva.html'
    form_class = ReservaForm
    success_url = reverse_lazy('listaReservas')

    def form_valid(self, form):
        habitacion = form.instance.habitacion
        fecha_llegada = form.cleaned_data['fecha_llegada']
        fecha_salida = form.cleaned_data['fecha_salida']

        reservas_existentes = Reserva.objects.filter(habitacion=habitacion).exclude(id=self.object.id)
        for reserva in reservas_existentes:
            if fecha_llegada <= reserva.fecha_salida and fecha_salida >= reserva.fecha_llegada:
                form.add_error(None, ValidationError('La habitación se encuentra reservada para las fechas seleccionadas, reintente.'))
                return self.form_invalid(form)

        usuario = Usuario.objects.filter(user=self.request.user).first()
        if usuario:
            form.instance.usuario = usuario

        self.object = form.save()
        return super().form_valid(form)

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
# @method_decorator(user_passes_test(es_administrador), name='dispatch')
class CrearAnuncioView(CreateView):
    model = Anuncio 
    form_class = AnuncioForm 
    template_name = 'hotel/crear_anuncio.html' 
    success_url = reverse_lazy('lista_anuncios')

@method_decorator(login_required, name='dispatch')    
class ListarAnuncioView(ListView):
    model = Anuncio
    template_name = 'hotel/lista_anuncios.html'
    context_object_name = 'anuncios'

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
# @method_decorator(user_passes_test(es_administrador), name='dispatch')
class ModificarAnuncioView(UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'hotel/modificar_anuncio.html'
    success_url = reverse_lazy('lista_anuncios')

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
# @method_decorator(user_passes_test(es_administrador), name='dispatch')
class EliminarAnuncioView(DeleteView):
    model = Anuncio
    template_name = 'hotel/eliminar_anuncio.html'
    success_url = reverse_lazy('lista_anuncios')
    
    
class ServicioCreateView(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'hotel/crear_servicio.html'
    success_url = reverse_lazy('listaServicios')  
    
class ServicioListView(ListView):
    model = Servicio
    template_name = 'hotel/lista_servicios.html'
    context_object_name = 'servicio'

class ServicioUpdateView(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'hotel/editar_servicio.html'
    success_url = reverse_lazy('listaServicios')

class ServicioDeleteView(DeleteView):
    model = Servicio
    template_name = 'hotel/eliminar_servicio.html'
    success_url = reverse_lazy('listaServicios')

class RegistrarRoomServiceView(View):
    template_name = 'hotel/registrarSolicitud.html'

    def get(self, request):
        form = RoomServiceForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RoomServiceForm(request.POST)
        if form.is_valid():
            habitacion = form.cleaned_data['habitacion']
            servicio = form.cleaned_data['servicio']

            reserva = Reserva.objects.filter(habitacion=habitacion).first()
            if not reserva:
                form.add_error('habitacion', 'No hay una reserva activa para esta habitación.')
                return render(request, self.template_name, {'form': form})

            RoomService.objects.create(
                reserva=reserva,
                servicio=servicio,
                precio_total=servicio.precio
            )
            return redirect('listaSolicitudes')  
        return render(request, self.template_name, {'form': form})

class RoomServiceUpdateView(UpdateView):
    model = RoomService
    form_class = RoomServiceForm
    template_name = 'hotel/actualizarSolicitud.html'
    success_url = reverse_lazy('listaSolicitudes')

class RoomServiceDeleteView(DeleteView):
    model = RoomService
    template_name = 'hotel/eliminarSolicitud.html'
    context_object_name = 'solicitud'
    success_url = reverse_lazy('listaSolicitudes')

class RoomServiceListView(ListView):
    model = RoomService
    template_name = 'hotel/lista_solicitudes.html'
    context_object_name = 'solicitud'
