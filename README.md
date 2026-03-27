# Teciman

Prueba técnica para Teciman.

Aplicación web desarrollada con Flask para la gestión de partes de obra, usando SQLite como base de datos.

## Requisitos

- Python 3.11 o superior
- Entorno virtual recomendado

## Instalación

Desde la raíz del proyecto:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r src/requirements.txt
```

## Puesta en marcha

Para ejecutar el proyecto desde cero hay que seguir este orden:

### 1. Crear la base de datos

Este script crea las tablas necesarias en SQLite:

```powershell
python src/database/init_db.py
```

### 2. Insertar datos de ejemplo

Este script carga datos iniciales en las tablas maestras para poder probar los formularios:

```powershell
python src/database/inserciondatos.py
```

### 3. Ejecutar la aplicación

Una vez creada la base de datos y cargados los datos de ejemplo, se lanza la aplicación desde el archivo principal:

```powershell
python app.py
```

La aplicación quedará disponible en:

```text
http://127.0.0.1:5000/
```

## Estructura básica

```text
app.py
src/
	database/
		init_db.py
		inserciondatos.py
		teciman.db
	models/
	routes/
	static/
	templates/
```

## Notas

- `init_db.py` debe ejecutarse antes que `inserciondatos.py`.
- `inserciondatos.py` inserta datos de prueba solo si las tablas maestras están vacías.
- La base de datos se genera en `src/database/teciman.db`.
