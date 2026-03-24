# **Paso a Paso de creación del proyecto**

## Creamos carpeta contenedora del proyecto
VitalCare

## Abrimos PowerShell y ubicamos la ruta de la carpeta
.../VitalCare

## Abrimos VSCode desde la carpeta desde PowerShell

```sh
code .
```

## Creamos en entorno virtual

```sh
python -m venv venv
```
 
## Activamos entorno virtual 

```sh
.\venv\Scripts\activate
```
## instalamos django (teniendo activado entorno virtual)
```sh
 pip install django
```

## Creamos el proyecto

```sh
django-admin startproject clinica .
```

## Instalamos el driver de conexión
```sh
pip install django psycopg2-binary
```

## Instalamos los "motores" de encriptación a utilizar en el proyecto
```sh
pip install bcrypt
```

```sh
pip install argon2-cffi
```

## Creamos archivos de dependencias (requirements.txt)
```sh
pip freeze > requirements.txt
```

## Creamos base de datos desde PostgreSQL
```sh
CREATE DATABASE clinica;
```

## Creamos la carpeta "templates" dentro de la raíz del proyecto
![alt text](img/image.png)

## Primeras configuraciones de archivo "settings.py"

### Configuramos el acceso a la carpeta "templates".
![alt text](img/image-2.png)

### Configuramos acceso a la base de datos.
![alt text](img/image-3.png)

### Incluimos PASWORD_HASHERS para su uso en encriptación.
![alt text](img/image-4.png)

### Camiamos idioma y zona horaria.
![alt text](img/image-5.png)