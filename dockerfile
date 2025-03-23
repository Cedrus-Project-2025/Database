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

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Dar permisos a los scripts
RUN chmod +x /app/Files/Scripts/bash/start.sh \
    && chmod +x /app/Files/Scripts/bash/install_rclone.sh

# Exponer el puerto para Render
EXPOSE 10000

# Comando por defecto
CMD ["./Files/Scripts/bash/start.sh"]
