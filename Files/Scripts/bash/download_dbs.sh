#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
RCLONE_BIN="$SCRIPT_DIR/../../Temp/installation/rclone"
RCLONE_CONFIG="$SCRIPT_DIR/../../Temp/.config/rclone/rclone.conf"
RCLONE_REMOTE_NAME="drive"
DRIVE_FOLDER="/UPY/Estancias_Enero_2025/cedrus_db"
LOCAL_DEST="$SCRIPT_DIR/../../Data"

if [ ! -f "$RCLONE_BIN" ]; then
    echo "Error: Rclone no está instalado en $RCLONE_BIN."
    exit 1
fi

mkdir -p "$LOCAL_DEST"

echo "Descargando archivos desde Google Drive..."
"$RCLONE_BIN" --config "$RCLONE_CONFIG" copy "$RCLONE_REMOTE_NAME:$DRIVE_FOLDER" "$LOCAL_DEST" --progress

if [ $? -eq 0 ]; then
    echo "Descarga completada en $LOCAL_DEST."
else
    echo "Error en la descarga. Revisa la configuración de Rclone."
    exit 1
fi
