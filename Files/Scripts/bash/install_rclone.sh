#!/bin/bash

echo "Instalando Rclone si no está presente..."

# Verifica si rclone ya está instalado
if command -v rclone &> /dev/null; then
    echo "Rclone ya está instalado."
else
    echo "Descargando e instalando Rclone..."
    curl -Of https://downloads.rclone.org/rclone-current-linux-amd64.zip
    unzip rclone-current-linux-amd64.zip
    cd rclone-*-linux-amd64
    cp rclone /usr/local/bin/
    chmod 755 /usr/local/bin/rclone
    cd ..
    rm -rf rclone-*-linux-amd64 rclone-current-linux-amd64.zip
    echo "Rclone instalado correctamente."
fi

# Crear carpeta de configuración
export RCLONE_CONFIG=./.config/rclone/rclone.conf
mkdir -p ./.config/rclone

# Generar archivo de configuración
echo "Configurando Rclone..."
cat <<EOF > "$RCLONE_CONFIG"
${RCLONE_name}
type = ${RCLONE_type}
scope = ${RCLONE_scope}
token = ${RCLONE_token}
team_drive = 
EOF

echo "Configuración de Rclone lista en $RCLONE_CONFIG"
