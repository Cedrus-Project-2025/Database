# ========== Comando para crear y levantar docker
# clear; docker build -t cedrus-db .; docker run --name CedusDB --env-file .env -p 10000:10000 cedrus-db
# ========== 


# Imagen base
FROM python:3.11

# Instala nano y dependencias necesarias
RUN apt-get update && apt-get install -y nano curl && apt-get clean

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos de la app
COPY . /app

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Instalar rclone
RUN curl https://rclone.org/install.sh | bash

# Dar permisos al script de inicio
RUN chmod +x /app/Files/Scripts/bash/start.sh

# Exponer el puerto de la API
EXPOSE 10000

# Comando de inicio
CMD ["./Files/Scripts/bash/start.sh"]
