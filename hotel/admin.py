from django.contrib import admin
from hotel.models import Usuario, Rol, Reserva, Consulta, Reclamo, Anuncio
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Administracion de Usuarios
class AdministracionUsuarios(admin.ModelAdmin):
    list_display = ('user', 'nacionalidad', 'rut', 'fecha_nacimiento', 'nombre_completo', 'numero_telefonico', 'correo', 'rol') 
    search_fields = ('user__username', 'nacionalidad', 'rut', 'nombre_completo', 'numero_telefonico', 'correo', 'rol__nombre')
    list_filter = ('rol__nombre',)
admin.site.register(Usuario, AdministracionUsuarios)

admin.site.register(Rol)

class TablaUsuarios(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'usuarios'

class UserAdmin(BaseUserAdmin):
    inlines = (TablaUsuarios,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Anuncio)
admin.site.register(Reserva)
admin.site.register(Consulta)
admin.site.register(Reclamo)