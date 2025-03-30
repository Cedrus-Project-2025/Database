#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Ahora installation y .config están dentro de Files/Temp/
INSTALL_DIR="$SCRIPT_DIR/../../Temp/installation"
RCLONE_BIN="$INSTALL_DIR/rclone"
CONFIG_DIR="$SCRIPT_DIR/../../Temp/config/rclone"
RCLONE_CONFIG="$CONFIG_DIR/rclone.conf"

echo "Instalando Rclone en $INSTALL_DIR..."

rm -rf "$INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

echo "Descargando e instalando Rclone..."
curl -Of https://downloads.rclone.org/rclone-current-linux-amd64.zip
unzip -o rclone-current-linux-amd64.zip
cd rclone-*-linux-amd64 || exit 1
cp rclone "$RCLONE_BIN"
chmod +x "$RCLONE_BIN" 
cd ..
rm -rf rclone-*-linux-amd64 rclone-current-linux-amd64.zip
echo "Rclone instalado correctamente en $RCLONE_BIN."

# Crear carpeta y archivo de configuración en Temp/.config
mkdir -p "$CONFIG_DIR"

echo "Configurando Rclone en $RCLONE_CONFIG..."
cat <<EOF > "$RCLONE_CONFIG"
[drive]
type = ${RCLONE_type}
scope = ${RCLONE_scope}
token = ${RCLONE_token}
team_drive = 
EOF
echo "Archivo de configuración creado en $RCLONE_CONFIG."

export PATH="$INSTALL_DIR:$PATH"
echo "PATH temporal actualizado para usar Rclone desde $INSTALL_DIR"

# Verificar instalación
"$RCLONE_BIN" version
