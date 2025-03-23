#!/bin/bash

echo "Inicializando el contenedor..."

# Crear directorio para las bases de datos
mkdir -p ./Files/Data

# Iniciar el monitor de inactividad en segundo plano
echo "🕒 Iniciando monitor de inactividad..."
if [ -f ./Files/Scripts/python/scheduler/backup_scheduler.py ]; then
    python3 -u ./Files/Scripts/python/scheduler/backup_scheduler.py &
else
    echo "⚠️  No se encontró el archivo backup_scheduler.py"
fi

# Lanzar la API con Gunicorn
echo "🚀 Iniciando la API..."
gunicorn -w 4 -b 0.0.0.0:10000 app:app
