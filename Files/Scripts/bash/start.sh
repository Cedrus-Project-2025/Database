#!/bin/bash

echo "Inicializando el contenedor..."

# Crear carpeta de configuración de rclone si no existe
mkdir -p /root/.config/rclone

# Crear archivo rclone.conf usando variables de entorno
echo "Configurando Rclone desde variables de entorno..."
cat <<EOF > /root/.config/rclone/rclone.conf
${RCLONE_name}
type = ${RCLONE_type}
scope = ${RCLONE_scope}
token = ${RCLONE_token}
team_drive = 
EOF

echo "Rclone configurado."

# Crear directorio para las bases de datos si no existe
mkdir -p /app/Files/Data

# Descargar las bases de datos desde Google Drive
echo "Descargando bases de datos desde Google Drive..."
rclone copy "gdrive:/UPY/Estancias Enero 2025/cedrus-db" /app/Files/Data --create-empty-src-dirs
echo "Bases de datos descargadas."

# Iniciar el monitor de inactividad en segundo plano
echo "Iniciando monitor de inactividad..."
python3 -u /app/Files/Scripts/python/scheduler/backup_scheduler.py &

# Lanzar la API con Gunicorn
echo "Iniciando la API..."
gunicorn -w 4 -b 0.0.0.0:10000 app:app
