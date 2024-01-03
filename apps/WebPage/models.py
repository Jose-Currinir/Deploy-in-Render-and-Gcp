from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator, EmailValidator
from django.forms import ValidationError
import re

"""
1. Aquí creamos las tablas que contendrá nuestra base de datos
2. Una vez tengamos los modelos creados debemos generar las migraciones y subirlas, eso se realiza con los siguientes comandos
    2.1 python manage.py makemigrations  
    2.2 python manage.py migrate
3. Una vez tengamos subidas las migraciones, nos debemos dirigir al archivo admin.py
"""
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
    nombre = models.CharField(max_length=30, validators=[MinLengthValidator(2),prevenir_inyeccion_sql])
    porcentaje = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(100), validar_porcentaje])

class Proyecto(models.Model):
    foto = models.ImageField(upload_to='fotos_proyectos/')
    nombre = models.CharField(max_length=30)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    cliente = models.CharField(max_length=20, validators=[validar_longitud(4,20)])
    fecha = models.DateField(auto_now_add=True)
    url_acceso = models.URLField()
    reflexion_personal = models.TextField(validators=[MinLengthValidator(4), MaxLengthValidator(200), prevenir_inyeccion_sql])

class Testimonio(models.Model):
    foto = models.ImageField(upload_to='fotos_testimonios/', validators=[...])
    nombre = models.CharField(max_length=20, validators=[MinLengthValidator(4), prevenir_inyeccion_sql])
    cargo = models.CharField(max_length=50, validators=[MinLengthValidator(4), MaxLengthValidator(30), prevenir_inyeccion_sql])
    proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)
    testimonio = models.TextField(validators=[MinLengthValidator(4), MaxLengthValidator(200), prevenir_inyeccion_sql])

"""
class Articulo(models.Model):
    foto = models.ImageField(upload_to='fotos_articulos/')
    titulo = models.CharField(max_length=20, validators=[MinLengthValidator(4)])
    descripcion = models.TextField(validators=[MinLengthValidator(4), MaxLengthValidator(100)])
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(auto_now_add=True)
"""

class Mensaje(models.Model):
    nombre = models.CharField(max_length=20, validators=[MinLengthValidator(4)])
    correo = models.EmailField(validators=[EmailValidator()])
    asunto = models.CharField(max_length=20, validators=[MinLengthValidator(4)])
    mensaje = models.TextField(validators=[MinLengthValidator(4), MaxLengthValidator(100)])
