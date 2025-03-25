#!/bin/bash

echo "Instalando Rclone en ./installation si no está presente..."

# Ruta personalizada de instalación
INSTALL_DIR="/opt/render/project/src/./installation"
RCLONE_BIN="$INSTALL_DIR/rclone"

# Verifica si rclone ya está instalado en el directorio deseado
if [ ! -f "$RCLONE_BIN" ]; then
    echo "Descargando e instalando Rclone..."
    curl -Of https://downloads.rclone.org/rclone-current-linux-amd64.zip
    unzip rclone-current-linux-amd64.zip
    cd rclone-*-linux-amd64 || exit 1
    mkdir -p "$INSTALL_DIR"
    cp rclone "$RCLONE_BIN"
    chmod +x "$RCLONE_BIN" 
    cd ..
    rm -rf rclone-*-linux-amd64 rclone-current-linux-amd64.zip
    echo "Rclone instalado correctamente en $RCLONE_BIN."
else
    echo "Rclone ya está instalado en $RCLONE_BIN."
fi

# Crear carpeta de configuración
export RCLONE_CONFIG="./.config/rclone/rclone.conf"
mkdir -p "$(dirname "$RCLONE_CONFIG")"

# Generar archivo de configuración (si no existe)
if [ ! -f "$RCLONE_CONFIG" ]; then
    echo "Configurando Rclone en $RCLONE_CONFIG..."
    cat <<EOF > "$RCLONE_CONFIG"
[${RCLONE_name}]
type = ${RCLONE_type}
scope = ${RCLONE_scope}
token = ${RCLONE_token}
team_drive = 
EOF
    echo "Archivo de configuración creado."
else
    echo "Archivo de configuración ya existe en $RCLONE_CONFIG."
fi

# Agregar ./installation al PATH temporalmente (aunque no se usará en Python)
export PATH="$INSTALL_DIR:$PATH"
echo "PATH temporal actualizado para usar Rclone desde $INSTALL_DIR"

# Verificar que Rclone se instaló correctamente
"$RCLONE_BIN" version
