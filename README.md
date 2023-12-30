# Deploy-in-Render-and-Gcp

Este es el procedimiento para poder desplegar servicios web con el framework Django y servir las imágenes con Google Cloud Plataform  
1.	Debemos crear el proyecto en nuestra máquina.  
  a.	django-admin startproject nombre_de_tu_proyecto  
  b.	El proyecto se debe crear con esta estructura, que facilitara la implementación de nuevas aplicaciones
  
2.	Ahora podemos crear las aplicaciones que contendrá nuestro proyecto.  
  a.	python manage.py startapp nombre_de_tu_app .  
  b.	Al crear las aplicaciones con ese punto no se generará una carpeta que las contenga, para ello debemos mover la aplicación creada dentro de la carpeta apps  
  c.	Dentro de la carpeta apps debemos crear un archivo __init__.py Este nos permitirá inicializar la carpeta de aplicaciones, así se podrán reconocer dentro del proyecto general.  
  d.	Como cambiamos la ruta de las apps creadas, dentro de cada app debemos acceder a apps.py y anteponer apps. Dentro de name
  
3.	El resto de la estructura hay que copiar la que se encuentra en este repositorio.
   
4.	Crear el entorno virtual que contendrá los paquetes instalados para nuestro proyecto.  
  a.	python -m venv env  
  b.	Procedemos a activarlo con el siguiente comando. (.\env\Scripts\activate)  
  c.	Para desactivarlo debemos tipear deactivate
  
6.	Una vez instalamos todos los modulos debemos traspasar esa información a nuestro archivo requirements.txt  
  a.	Traspazar info (pip freeze > requirements.txt)  
  b.	Instalar módulos (pip install -r .\requirements.txt)  
 
