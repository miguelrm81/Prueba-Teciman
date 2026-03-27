import sqlite3
from datetime import datetime

conn = sqlite3.connect("src/database/teciman.db")
cursor = conn.cursor()

# Datos de prueba para tablas maestras, solo inserta si están vacias las tablas

if cursor.execute("SELECT COUNT(*) FROM Personal").fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO Personal (nombre, activo) VALUES (?, ?)", [
        ("Juan", 1),
        ("Marta", 1),
        ("Miguel", 1),
        ("Eusebio", 1),
    ])

if cursor.execute("SELECT COUNT(*) FROM TipoTerreno").fetchone()[0] == 0:
    cursor.executemany("INSERT INTO TipoTerreno (descripcion) VALUES (?)", [
        ("Arcilloso",),
        ("Hormigón",),
        ("Arena",),
    ])

if cursor.execute("SELECT COUNT(*) FROM SeccionTipo").fetchone()[0] == 0:
    cursor.executemany("INSERT INTO SeccionTipo (descripcion) VALUES (?)", [
        ("Seccion A",),
        ("Seccion B",),
        ("Seccion C",),
    ])

if cursor.execute("SELECT COUNT(*) FROM MotivoExcesoHoras").fetchone()[0] == 0:
    cursor.executemany("INSERT INTO MotivoExcesoHoras (descripcion) VALUES (?)", [
        ("Avería",),
        ("Mal tiempo",),
        ("Tráfico",),
    ])

if cursor.execute("SELECT COUNT(*) FROM EstadoParte").fetchone()[0] == 0:
    cursor.executemany("INSERT INTO EstadoParte (descripcion) VALUES (?)", [
        ("Activo",),
        ("Cerrado",),
        ("En curso",),
    ])

conn.commit()
print("Datos de ejemplo insertados correctamente.")