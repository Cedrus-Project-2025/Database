#!/bin/bash

echo "Inicializando el contenedor..."

# Crear directorio para las bases de datos
mkdir -p ./Files/Data

# Lanzar la API con Gunicorn
echo "🚀 Iniciando la API..."
gunicorn -w 4 -b 0.0.0.0:10000 app:app
