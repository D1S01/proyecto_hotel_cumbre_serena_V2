from django import forms
from hotel.models import Habitacion, Usuario, Consulta, Reclamo, Rol, Reserva, Anuncio, RoomService, Servicio
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import redirect
from django import forms
from django.contrib.auth.models import User
from .models import Usuario, Rol

class FormularioUsuarios(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Nombre de usuario', required=True, help_text='Obligatorio. Ingrese su nombre de usuario (nombre apellido)')    
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña', help_text='Obligatorio. Ingrese su contraseña.')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirme contraseña', help_text='Obligatorio. Confirme su contraseña.')
    nacionalidad = forms.CharField(max_length=100, required=True, help_text='Obligatorio. Ingrese su nacionalidad.')
    rut = forms.CharField(max_length=10, required=True, help_text='Obligatorio. Ingrese su RUT (11111111-1).')
    fecha_nacimiento = forms.DateField(required=True, help_text='Obligatorio. Formato: AA-MM-DD.')
    nombre_completo = forms.CharField(max_length=200, required=True, help_text='Obligatorio. Ingrese su nombre completo.')
    numero_telefonico = forms.CharField(max_length=9, required=True, help_text='Obligatorio. Ingrese su número telefónico.')
    correo = forms.EmailField(required=True, help_text='Obligatorio. Ingrese su correo electrónico.')
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), required=True, help_text='Obligatorio. Seleccione su rol.')

    class Meta:
        model = Usuario
        fields = [
            'username', 'password1', 'password2',
            'nacionalidad', 'rut', 'fecha_nacimiento',
            'nombre_completo', 'numero_telefonico',
            'correo', 'rol'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            email=self.cleaned_data['correo']
        )

        usuario = Usuario(
            user=user,
            nacionalidad=self.cleaned_data['nacionalidad'],
            rut=self.cleaned_data['rut'],
            fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
            nombre_completo=self.cleaned_data['nombre_completo'],
            numero_telefonico=self.cleaned_data['numero_telefonico'],
            correo=self.cleaned_data['correo'],
            rol=self.cleaned_data['rol']
        )

        if commit:
            user.save()
            usuario.save()

        return usuario

class FormularioRegistroHuesped(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Nombre de usuario', required=True, help_text='Obligatorio. Ingrese su nombre de usuario (nombre apellido)')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña', help_text='Obligatorio. Ingrese su contraseña.')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirme contraseña', help_text='Obligatorio. Confirme su contraseña.')
    nacionalidad = forms.CharField(max_length=100, required=True, help_text='Obligatorio. Ingrese su nacionalidad.')
    rut = forms.CharField(max_length=10, required=True, help_text='Obligatorio. Ingrese su RUT (11111111-1).')
    fecha_nacimiento = forms.DateField(required=True, help_text='Obligatorio. Formato: AA-MM-DD.')
    nombre_completo = forms.CharField(max_length=200, required=True, help_text='Obligatorio. Ingrese su nombre completo.')
    numero_telefonico = forms.CharField(max_length=9, required=True, help_text='Obligatorio. Ingrese su número telefónico.')
    correo = forms.EmailField(required=True, help_text='Obligatorio. Ingrese su correo electrónico.')

    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'nacionalidad', 'rut', 'fecha_nacimiento', 'nombre_completo', 'numero_telefonico', 'correo']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            email=self.cleaned_data['correo']
        )
        huesped = Usuario(
            user=user,
            nacionalidad=self.cleaned_data['nacionalidad'],
            rut=self.cleaned_data['rut'],
            fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
            nombre_completo=self.cleaned_data['nombre_completo'],
            numero_telefonico=self.cleaned_data['numero_telefonico'],
            correo=self.cleaned_data['correo'],
            rol=Rol.objects.get(nombre='Huesped')  
        )
        if commit:
            user.save() 
            huesped.save()  
        return huesped


class FormularioEditarPerfil(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Contraseña Actual', required=False) 
    password1 = forms.CharField(widget=forms.PasswordInput, label='Nueva Contraseña', required=False) 
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar Nueva Contraseña', required=False)
    username = forms.CharField(max_length=150, label='Nombre de usuario', required=True, help_text='Obligatorio. Ingrese su nombre de usuario (nombre apellido)')
    nacionalidad = forms.CharField(max_length=100, required=True, help_text='Obligatorio. Ingrese su nacionalidad.')
    rut = forms.CharField(max_length=10, required=True, help_text='Obligatorio. Ingrese su RUT (11111111-1).')
    fecha_nacimiento = forms.DateField(required=True, help_text='Obligatorio. Formato: AA-MM-DD.')
    nombre_completo = forms.CharField(max_length=200, required=True, help_text='Obligatorio. Ingrese su nombre completo.')
    numero_telefonico = forms.CharField(max_length=9, required=True, help_text='Obligatorio. Ingrese su número telefónico.')
    correo = forms.EmailField(required=True, help_text='Obligatorio. Ingrese su correo electrónico.')

    class Meta:
        model = Usuario
        fields = ['old_password', 'password1', 'password2', 'username', 'nacionalidad', 'rut', 'fecha_nacimiento', 'nombre_completo', 'numero_telefonico', 'correo']

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if old_password or password1 or password2:

            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Las contraseñas no coinciden.")

            if not self.instance.user.check_password(old_password):
                raise forms.ValidationError("La contraseña actual no es correcta.")

        return cleaned_data

    def save(self, commit=True):
        user = self.instance.user 
        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])
            if commit: 
                user.save() 
                return redirect('login')
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
            self.instance.save() 
        return self.instance

class FormularioEditarPerfilAdmin(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Contraseña Actual', required=False) 
    password1 = forms.CharField(widget=forms.PasswordInput, label='Nueva Contraseña', required=False) 
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar Nueva Contraseña', required=False)
    username = forms.CharField(max_length=150, label='Nombre de usuario', required=True, help_text='Obligatorio. Ingrese su nombre de usuario (nombre apellido)')
    nacionalidad = forms.CharField(max_length=100, required=True, help_text='Obligatorio. Ingrese su nacionalidad.')
    rut = forms.CharField(max_length=10, required=True, help_text='Obligatorio. Ingrese su RUT (11111111-1).')
    fecha_nacimiento = forms.DateField(required=True, help_text='Obligatorio. Formato: AA-MM-DD.')
    nombre_completo = forms.CharField(max_length=200, required=True, help_text='Obligatorio. Ingrese su nombre completo.')
    numero_telefonico = forms.CharField(max_length=9, required=True, help_text='Obligatorio. Ingrese su número telefónico.')
    correo = forms.EmailField(required=True, help_text='Obligatorio. Ingrese su correo electrónico.')
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), required=True, help_text='Obligatorio. Seleccione su rol.')

    class Meta:
        model = Usuario
        fields = ['old_password', 'password1', 'password2', 'username', 'nacionalidad', 'rut', 'fecha_nacimiento', 'nombre_completo', 'numero_telefonico', 'correo', 'rol']

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if old_password or password1 or password2:

            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Las contraseñas no coinciden.")

            if not self.instance.user.check_password(old_password):
                raise forms.ValidationError("La contraseña actual no es correcta.")

        return cleaned_data

    def save(self, commit=True):
        user = self.instance.user 
        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])
            if commit: 
                user.save() 
                return redirect('login')
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
            self.instance.save() 
        return self.instance

        
class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['num_habitacion', 'cantidad_camas', 'ubicacion', 'precio', 'tipo', 'camas', 'vistas', 'imagen']
        widgets = {
            'num_habitacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_camas':forms.NumberInput(attrs={'class':'form-control'}),
            'ubicacion':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.NumberInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'camas': forms.Select(attrs={'class': 'form-control'}),
            'vistas':forms.TextInput(attrs={'class':'form-control'}),
            'imagen':forms.ClearableFileInput(attrs={'class':'form-control'})
        }    
        
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ReclamoForm(forms.ModelForm):
    class Meta:
        model = Reclamo
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class RespuestaConsultaForm(forms.ModelForm):
    respuesta = forms.CharField(widget=forms.Textarea, label='Respuesta', required=True)

    class Meta:
        model = Consulta
        fields = ['respuesta']

class RespuestaReclamoForm(forms.ModelForm):
    respuesta = forms.CharField(widget=forms.Textarea, label='Respuesta', required=True)

    class Meta:
        model = Reclamo
        fields = ['respuesta']
          
class ReservaForm(forms.ModelForm):
    huespedes_menores = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Reserva
        fields = ['fecha_llegada', 'fecha_salida', 'huespedes_menores', 'preferencias']
        widgets = {
            'fecha_llegada': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'fecha_salida': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'preferencias': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        fecha_llegada = cleaned_data.get('fecha_llegada')
        fecha_salida = cleaned_data.get('fecha_salida')
        fecha_actual = timezone.now()

        if fecha_llegada and fecha_llegada < fecha_actual:
            self.add_error('fecha_llegada', 'La fecha de llegada no puede ser en el pasado.')

        if fecha_salida and fecha_salida < fecha_actual:
            self.add_error('fecha_salida', 'La fecha de salida no puede ser en el pasado.')

        if fecha_llegada and fecha_salida and fecha_llegada > fecha_salida:
            self.add_error('fecha_salida', 'La fecha de salida debe ser posterior a la fecha de llegada.')

        return cleaned_data
    
class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo', 'descripcion', 'tipo','imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
 
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'tipo', 'descripcion', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
class RoomServiceForm(forms.Form):
    habitacion = forms.ModelChoiceField(
        queryset=Habitacion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Habitación"
    )
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Servicio solicitado"
    )