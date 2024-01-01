from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator, EmailValidator
from django.forms import ValidationError
import re

#
def validar_longitud(min_len, max_len):
    def validator(value):
        if not (min_len <= len(value) <= max_len):
            raise ValidationError(f'El texto debe tener entre {min_len} y {max_len} caracteres.')
    return validator
#
def validar_telefono(value):
    if not value.isdigit() or len(value) != 8:
        raise ValidationError('El número de teléfono debe ser un número de 8 dígitos.')
#
def validar_porcentaje(value):
    if not isinstance(value, int):
        raise ValidationError('El porcentaje debe ser un número entero.')
#
def prevenir_inyeccion_sql(value):
    if re.search(r'[^a-zA-Z0-9\s]', value):
        raise ValidationError('Caracteres inválidos detectados.')


class InformacionPersonal(models.Model):
    foto = models.ImageField(upload_to='foto_personal/')
    nombre = models.CharField(max_length=20, validators=[validar_longitud(4, 20)])
    ocupacion = models.CharField(max_length=20, validators=[validar_longitud(4, 20)])
    email = models.EmailField(validators=[EmailValidator()])
    telefono = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$')])
    presentacion = models.TextField(validators=[MinLengthValidator(4), MaxLengthValidator(500), prevenir_inyeccion_sql])
    habilidades = models.ManyToManyField('Habilidad')


class Habilidad(models.Model):
    nombre = models.CharField(max_length=30, validators=[MinLengthValidator(2), ...])  # Validación contra inyección SQL
    porcentaje = models.IntegerField(validators=[...])  # Validación de número entero

class Proyecto(models.Model):
    foto = models.ImageField(upload_to='fotos_proyectos/', validators=[...])
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    cliente = models.CharField(max_length=20, validators=[MinLengthValidator(4)])
    fecha = models.DateField(auto_now_add=True)
    url_acceso = models.URLField()
    reflexion_personal = models.TextField(validators=[MinLengthValidator(4), MaxLengthValidator(200), ...])

class Testimonio(models.Model):
    foto = models.ImageField(upload_to='fotos_testimonios/', validators=[...])
    nombre = models.CharField(max_length=20, validators=[MinLengthValidator(4)])
    cargo = models.CharField(max_length=50)
    proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)
    testimonio = models.TextField(validators=[MinLengthValidator(4), MaxLengthValidator(100), ...])

class Articulo(models.Model):
    foto = models.ImageField(upload_to='fotos_articulos/', validators=[...])
    titulo = models.CharField(max_length=20, validators=[MinLengthValidator(4)])
    descripcion = models.TextField(validators=[MinLengthValidator(4), MaxLengthValidator(100)])
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(auto_now_add=True)

class Mensaje(models.Model):
    nombre = models.CharField(max_length=20, validators=[MinLengthValidator(4), ...])
    correo = models.EmailField(validators=[EmailValidator()])
    asunto = models.CharField(max_length=20, validators=[MinLengthValidator(4), ...])
    mensaje = models.TextField(validators=[MinLengthValidator(4), MaxLengthValidator(100), ...])
