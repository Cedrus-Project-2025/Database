# ========== Comando para crear y levantar docker
# clear; docker build -t permont-db .; docker run --name PermontDB -p 10000:10000 permont-db
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
