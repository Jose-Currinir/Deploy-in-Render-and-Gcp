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
  a.	Traspazar info (pip freeze > requirements.txt)  
  b.	Instalar módulos (pip install -r .\requirements.txt)  