# Deploy-in-Render-and-Gcp

Este es el procedimiento para poder desplegar servicios web con el framework Django y servir las imágenes con Google Cloud Plataform.

Prerrequisitos para poder crear un proyecto de Django.
  1.	Debemos tener instalado Python y agregado al PATH
  2.	Procedemos a instalar Django. Pip install django

1.	Debemos crear el proyecto en nuestra máquina.  
  a.	django-admin startproject nombre_de_tu_proyecto .
  b.	El proyecto se debe crear con esta estructura, que facilitara la implementación de nuevas aplicaciones
  
2.	Una vez creado el proyecto, podemos proceder a crear las aplicaciones.
  a.	python manage.py startapp nombre_de_tu_app
  b.  Una vez hayamos creado la app, debemos moverla dentro de la carpeta apps.
  c.  Dentro de la carpeta apps debemos crear un archivo __init__.py Este nos permitirá inicializar la carpeta de aplicaciones, así se podrán reconocer dentro del proyecto general.
  d.  Como cambiamos la ruta de las apps creadas, dentro de cada app debemos acceder al archivo apps.py y anteponer apps. Dentro de la variable name
  
3.	El resto de la estructura hay que copiar la que se encuentra en este repositorio.
   
4.	Crear el entorno virtual que contendrá los paquetes instalados para nuestro proyecto.  
  a.	python -m venv env  
  b.	Procedemos a activarlo con el siguiente comando. (.\env\Scripts\activate)  
  c.	Para desactivarlo debemos tipear deactivate
  
6.	Una vez instalamos todos los modulos debemos traspasar esa información a nuestro archivo requirements.txt  
  a. Modulos necesarios para poder trabajar
    django-jazzmin          (Tema personalizado)
    google-cloud-storage    (Bibliotecas para trabajar con google cloud storage)
    google-cloud            (Biblioteca para autenticar con google)
    gunicorn                (Servidor http necesario para render)
    django-storages         (Colección de almacenamiento para django)
    django                  (Django para desarrollo web)
    dj-database-url         (Biblioteca para trabajar bases de datos en django)
    python-dotenv           (Permite el uso de variables de entorno)
    django-environ          (Permite el uso de variables de entorno)
    django-dump-load-utf8   (no se que hace)
    z

  b.	Traspazar info (pip freeze > requirements.txt)  
  c.	Instalar módulos (pip install -r .\requirements.txt)  

1. Comenzamos con el desarrollo y modelado de la base de datos (models.py).

2. Creamos y aplicamos las migraciones de la base de datos

3. Ahora preparamos la administración de la base de datos, la cual se ve en el archivo (admin.py) 

4.  Después que tenemos el acceso a los datos debemos trabajar en el archivo (views.py). En las vistas contiene la lógica de negocio y determina como se presentan los datos al usuario.

5.  Una vez tengamos listas las views, procedemos a trabajar en el archivo (urls.py), este archivo es el que estructura las solicitudes a las vistas correspondientes

