from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Rol


@receiver(post_migrate)
def crear_roles_predeterminados(sender, **kwargs):
    roles_definidos = [opcion[0] for opcion in Rol.opciones]
    for nombre_rol in roles_definidos:
        Rol.objects.get_or_create(nombre=nombre_rol)
        

