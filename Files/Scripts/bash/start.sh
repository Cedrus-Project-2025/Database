#!/bin/bash

echo "Inicializando el contenedor..."

# Crear carpeta de configuración de rclone en un lugar seguro (no en /root)
mkdir -p ./.config/rclone
export RCLONE_CONFIG=./.config/rclone/rclone.conf

# Crear archivo rclone.conf usando variables de entorno
echo "Configurando Rclone desde variables de entorno..."
cat <<EOF > ./.config/rclone/rclone.conf
${RCLONE_name}
type = ${RCLONE_type}
scope = ${RCLONE_scope}
token = ${RCLONE_token}
team_drive = 
EOF

echo "Rclone configurado."

# Crear directorio para las bases de datos
mkdir -p ./Files/Data

# Descargar las bases de datos desde Google Drive
echo "Descargando bases de datos desde Google Drive..."
if command -v rclone &> /dev/null; then
    rclone copy "gdrive:/UPY/Estancias Enero 2025/cedrus-db" ./Files/Data --create-empty-src-dirs
    echo "Bases de datos descargadas."
else
    echo "Rclone no está instalado o no se encuentra en el PATH."
fi

# Iniciar el monitor de inactividad en segundo plano (verifica si el archivo existe)
echo "Iniciando monitor de inactividad..."
if [ -f ./Files/Scripts/python/scheduler/backup_scheduler.py ]; then
    python3 -u ./Files/Scripts/python/scheduler/backup_scheduler.py &
else
    echo "No se encontró el archivo backup_scheduler.py"
fi

# Lanzar la API con Gunicorn
echo "Iniciando la API..."
gunicorn -w 4 -b 0.0.0.0:10000 app:app
