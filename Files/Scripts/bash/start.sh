#!/bin/bash

echo "Inicializando el contenedor..."

# Crear carpeta de configuración de rclone si no existe
mkdir -p /root/.config/rclone

# Crear archivo rclone.conf usando variables de entorno
echo "Configurando Rclone desde variables de entorno..."
cat <<EOF > /root/.config/rclone/rclone.conf
${RCLONE_NAME}
type = ${RCLONE_TYPE}
scope = ${RCLONE_SCOPE}
token = ${RCLONE_TOKEN}
team_drive = ${RCLONE_TEAM_DRIVE}
EOF

echo "Rclone configurado."

# Crear directorio para las bases de datos si no existe
mkdir -p /app/Files/Data

# Descargar las bases de datos desde Google Drive
echo "Descargando .db desde Google Drive..."
rclone copy gdrive:/cedrus-db /app/Files/Data --create-empty-src-dirs
echo "Bases de datos descargadas."

# Iniciar el monitor de inactividad en segundo plano
echo "Iniciando monitor de inactividad..."
python3 -u /app/Files/Scripts/python/backup_scheduler.py &

# Lanzar la API con Gunicorn
echo "Iniciando la API..."
gunicorn -w 4 -b 0.0.0.0:10000 app:app
