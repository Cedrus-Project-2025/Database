# ========== Comando para crear y levantar docker
# clear; docker build -t cedrus-db .; docker run --name CedusDB --env-file .env -p 10000:10000 cedrus-db
# ========== 


# Imagen base
FROM python:3.11

# Instalar herramientas necesarias
RUN apt-get update && apt-get install -y \
    nano \
    curl \
    unzip \
    && apt-get clean

# Instalar Rclone manualmente (compatible con Render)
RUN curl -Of https://downloads.rclone.org/rclone-current-linux-amd64.zip && \
    unzip rclone-current-linux-amd64.zip && \
    cd rclone-*-linux-amd64 && \
    cp rclone /usr/local/bin/ && \
    chmod 755 /usr/local/bin/rclone && \
    cd .. && rm -rf rclone-*-linux-amd64 rclone-current-linux-amd64.zip

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Dar permisos al script de inicio
RUN chmod +x /app/Files/Scripts/bash/start.sh

# Exponer el puerto para Render (Render detecta automáticamente el puerto)
EXPOSE 10000

# Comando por defecto
CMD ["./Files/Scripts/bash/start.sh"]
