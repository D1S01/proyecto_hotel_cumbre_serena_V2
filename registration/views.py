from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from hotel.models import Usuario, Reserva
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from hotel.forms import FormularioUsuarios, FormularioRegistroHuesped, FormularioEditarPerfil, FormularioEditarPerfilAdmin

@login_required
def deshabilitar_usuario(request, user_id):
    perfil = Usuario.objects.filter(id=user_id).first()

    if perfil:
        perfil.is_active = False
        perfil.user.is_active = False
        perfil.user.save()
        perfil.save()
    return redirect('Lista_usuarios')

@login_required
def habilitar_usuario(request, user_id):
    perfil = Usuario.objects.filter(id=user_id).first()

    if perfil:
        perfil.is_active = True
        perfil.user.is_active = True
        perfil.user.save()
        perfil.save()
    return redirect('Lista_usuarios')

@method_decorator(login_required, name='dispatch')
class EditarPerfilUsuarioView(UpdateView):
    model = Usuario
    form_class = FormularioEditarPerfil
    template_name = 'registration/editar_perfil.html'
    success_url = reverse_lazy('listaHabitaciones')

    def get_object(self):
        user = self.request.user
        return Usuario.objects.filter(user=user).first()

    def get_initial(self):
        initial = super().get_initial()
        perfil = self.get_object()
        if perfil:
            initial['username'] = perfil.user.username
        return initial

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')  
class EditarUsuarioParaAdminView(UpdateView):
    model = Usuario
    form_class = FormularioEditarPerfilAdmin
    template_name = 'registration/editar_usuario_paraAdmin.html'
    success_url = reverse_lazy('Lista_usuarios')
    
    def get_object(self):
        return Usuario.objects.get(pk=self.kwargs['pk'])
    
    def get_initial(self): 
        initial = super().get_initial() 
        initial['username'] = self.get_object().user.username 
        return initial

@method_decorator(login_required, name='dispatch')
class PerfilUsuarioView(DetailView):
    model = Usuario
    template_name = 'registration/profile.html'
    context_object_name = 'usuario'

    def get_object(self):
        user = self.request.user
        return Usuario.objects.filter(user=user).first()

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class CrearUsuarioView(CreateView):
    model = Usuario
    form_class = FormularioUsuarios 
    template_name = 'registration/crear_usuario.html' 
    success_url = reverse_lazy('Lista_usuarios')
    
class RegistroHuespedView(CreateView):
    model = Usuario
    form_class = FormularioRegistroHuesped 
    template_name = 'registration/registro_huesped.html' 
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)

        usuario = self.object  # Este es el Usuario recién creado
        reserva_temp = self.request.session.get('reserva_temp')

        if reserva_temp:
            Reserva.objects.create(
                usuario=usuario,
                habitacion_id=reserva_temp['habitacion_id'],
                fecha_llegada=reserva_temp['fecha_llegada'],
                fecha_salida=reserva_temp['fecha_salida'],
                precio_total=reserva_temp['precio_total'],
            )
            del self.request.session['reserva_temp']

        return response
    
@method_decorator(login_required, name='dispatch')
class ListaUsuariosView(ListView):
    template_name = 'registration/lista_usuarios.html'
    context_object_name = 'usuario'

    def get_queryset(self):
        return Usuario.objects.all()