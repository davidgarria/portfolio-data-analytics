"""Verificación del entorno del curso: Python, librerías y conexión a PostgreSQL."""

import getpass
import sys

import matplotlib
import numpy
import pandas
import psycopg
import seaborn
import sklearn
import sqlalchemy

print(f"Python        {sys.version.split()[0]}")
print(f"Ejecutable    {sys.executable}")
print()

for libreria in (numpy, pandas, matplotlib, seaborn, sklearn, sqlalchemy, psycopg):
    print(f"{libreria.__name__:<14}{libreria.__version__}")
print()

contrasena = getpass.getpass("Contraseña del usuario postgres: ")

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="curso_data_analytics",
    user="postgres",
    password=contrasena,
) as conexion:
    version = conexion.execute("SELECT version();").fetchone()[0]
    filas = conexion.execute("SELECT mensaje FROM prueba_entorno;").fetchall()

print(f"PostgreSQL    {version}")
print(f"prueba_entorno: {len(filas)} fila(s) -> {filas[0][0]}")
print()
print("Entorno listo para el curso.")
