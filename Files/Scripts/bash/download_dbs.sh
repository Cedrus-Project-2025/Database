#!/bin/bash

# Variables de configuración
RCLONE_BIN="/opt/render/project/src/./installation/rclone"           # Ruta personalizada de Rclone
RCLONE_CONFIG="/opt/render/project/src/./.config/rclone/rclone.conf" # Ruta de las configuraciones de Rclone
RCLONE_REMOTE_NAME="drive"                                           # Nombre del remoto configurado en Rclone
DRIVE_FOLDER="/UPY/Estancias_Enero_2025/cedrus_db"                   # Ruta en Google Drive
LOCAL_DEST="/opt/render/project/src/./Files/Data"                    # Ruta de destino local

if [ ! -f "$RCLONE_BIN" ]; then
    echo "Error: Rclone no está instalado en $RCLONE_BIN."
    exit 1
fi

# Especificar explícitamente archivo de configuración
echo "Ubicación del archivo de configuración: $RCLONE_CONFIG"
mkdir -p "$LOCAL_DEST"

echo "Descargando archivos desde Google Drive..."
"$RCLONE_BIN" --config "$RCLONE_CONFIG" copy "$RCLONE_REMOTE_NAME:$DRIVE_FOLDER" "$LOCAL_DEST" --progress

if [ $? -eq 0 ]; then
    echo "Descarga completada en $LOCAL_DEST."
else
    echo "Error en la descarga. Revisa la configuración de Rclone."
    exit 1
fi
