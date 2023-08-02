##### DATABASE #######

#CREAR un archivo llamado local.py en la carpeta settings y agregar el siguiente código:
# respetar el nombre de "local.py", ya que esta previamente configurado en el archivo settings.py y en el .gitignore :)

from .base import *

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'proyectounion', #nombre de SU base de datos creada en MySQL
            'USER': 'root', #nombre de SU usuario creado en MySQL
            'PASSWORD': 'titanoboa2023', #SU password de usuario para conectar a la DB
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }