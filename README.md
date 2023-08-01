*** Clonar el repositorio ***
En una carpeta de su preferencia(pueden hacer una llamada "Proyecto Final"), mediante cmd u otra consola, clonar el repositorio con el siguiente comando:
```
git clone #httpdelrepositorio
```
*** Para instalar el proyecto ***
Crean un entorno virtual con el siguiente comando:
```
py -m venv venv   o   python -m venv venv
venv\Scripts\activate
```
*** instalar las dependencias ***
```
pip install -r requirements.txt
```
*** Para crear la base de datos ***
```
Hacer un archivo en la carpeta Settings llamado local.py y agregar lo que dice en el archivo base.py respecto de la base de datos
-linea 76 a 92
```
*** Para crear las migraciones ***
```
python manage.py makemigrations
python manage.py migrate
```
*** Para ejecutar el proyecto ***
```
python manage.py runserver
```
***Recomendaciones***
```
-Instalar en VSC la extension de GitHub Pull Requests and Issues (se maneja mejor el control de versiones)
-SIEMPRE controlar que esten en SU rama, para evitar conflictos de las ramas. rama indicada: STAGE-(su nombre)
-En caso de USAR OTRO NOMBRE PARA EL ENTORNO: AGREGARLO en el .GITIGNORE, mediante: nombredelentorno/
-EVITAR subir archivos de db, pw, caché, etc. (agregarlos al .gitignore antes de hacer el commit)
-EVITAR HACER PUSH A LA RAMA MAIN O DEVELOPMENT, SOLO HACERLO A LA RAMA STAGE.
-GRACIAS los quiero mucho ✨
-Si no, hay tabla 😠
```
