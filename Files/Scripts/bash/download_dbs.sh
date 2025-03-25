#!/bin/bash

# Variables de configuración
RCLONE_BIN="/opt/render/project/src/./installation/rclone"  # Ruta personalizada de Rclone
RCLONE_REMOTE_NAME="[gdrive]"                               # Nombre del remoto configurado en Rclone
DRIVE_FOLDER="/UPY/Estancias Enero 2025/cedrus-db"          # Ruta en Google Drive
LOCAL_DEST="/opt/render/project/src/./Files/Data"           # Ruta de destino local

# Verificar si Rclone está instalado
echo "Verificando Rclone en $RCLONE_BIN..."
if [ ! -f "$RCLONE_BIN" ]; then
    echo "Error: Rclone no está instalado en $RCLONE_BIN. Por favor, instálalo antes de ejecutar este script."
    exit 1
fi

# Crear la carpeta de destino si no existe
mkdir -p "$LOCAL_DEST"

# Descargar los archivos desde Google Drive
echo "Descargando archivos desde Google Drive..."
"$RCLONE_BIN" copy "$RCLONE_REMOTE_NAME:$DRIVE_FOLDER" "$LOCAL_DEST" --progress

if [ $? -eq 0 ]; then
    echo "Descarga completada en $LOCAL_DEST."
else
    echo "Error en la descarga. Revisa la configuración de Rclone."
    exit 1
fi
