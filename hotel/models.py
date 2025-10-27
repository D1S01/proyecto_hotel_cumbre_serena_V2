from django.db import models
from django.contrib.auth.models import User
import uuid 


class Habitacion(models.Model):
    tipo_habitacion = [ 
                        ('Individual', 'Individual'), 
                        ('Doble', 'Doble'), 
                        ('Matrimonial', 'Matrimonial'), 
                        ('Triple', 'Triple'), 
                        ('Suite', 'Suite'), 
                        ('Familiar', 'Familiar'),
    ]
    
    tipo_camas = [ 
                  ('Individual', 'Individual'), 
                  ('Doble', 'Doble'), 
                  ('Queen', 'Queen'), 
                  ('King', 'King'), 
                  ('Extra Grande', 'Extra Grande') 
    ]
    
    num_habitacion = models.IntegerField(unique=True)
    cantidad_camas = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()
    tipo = models.CharField(max_length=30, choices=tipo_habitacion)
    camas = models.CharField(max_length=30, choices=tipo_camas)
    vistas = models.CharField(max_length=300)
    imagen = models.ImageField(blank=True, null=True, upload_to='media')
    
class Rol(models.Model):
    administrador = 'Administrador'
    recepcionista = 'Recepcionista'
    huesped = 'Huesped'
    
    opciones = [
        (administrador, 'Administrador'),
        (recepcionista, 'Recepcionista'),
        (huesped, 'Huesped')
    ]
    
    nombre = models.CharField(max_length=100, choices=opciones, unique=True)
    def __str__(self): 
        return self.nombre
    
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nacionalidad = models.CharField(max_length=100)
    rut = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField()
    nombre_completo = models.CharField(max_length=200)
    numero_telefonico = models.CharField(max_length=9, unique=True)
    correo = models.EmailField(unique=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo

class Consulta(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    respuesta = models.TextField(blank=True, null=True)
    
class Reclamo(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    respuesta = models.TextField(blank=True, null=True)

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_llegada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    huespedes_menores = models.BooleanField(null=True, blank=True)
    preferencias = models.TextField(null=True, blank=True)
    numero_reserva = models.CharField(max_length=20, unique=True, blank=True)
    precio_total = models.IntegerField()
    
    def __str__(self):
        return f"Reserva {self.numero_reserva} - {self.usuario}" 
    
    def save(self, *args, **kwargs): 
        if not self.numero_reserva: 
            self.numero_reserva = self.generar_numero_reserva() 
        super().save(*args, **kwargs) 
    
    def generar_numero_reserva(self): 
        return str(uuid.uuid4()).split('-')[0]
    
    class Meta:
        constraints = [ 
                       models.UniqueConstraint(fields=['habitacion', 'fecha_llegada', 'fecha_salida'], name='reserva general unica') 
        ]
        
class Servicio(models.Model):
    opciones_servicios = [
        ('room_service', 'Room Service'),
        ('extra', 'Servicio Extra'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=opciones_servicios)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"

class RoomService(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_total = models.IntegerField()

    def __str__(self):
        return f"{self.servicio.nombre} - Reserva {self.reserva.numero_reserva}"
        
class Anuncio(models.Model):
    tipo_anuncio = [ 
                        ('publicitario', 'publicitario'), 
                        ('alerta', 'alerta'), 
                        ('informativo', 'informativo'), 
    ]
    imagen = models.ImageField(blank=True, null=True, upload_to='imagenes_anuncios')
    descripcion = models.TextField()
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=tipo_anuncio)