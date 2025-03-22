# ========== Comando para crear y levantar docker
# docker build -t cedrus-db .
# docker run -p 10000:10000 cedrus-db
# ========== 

# Usa una imagen base de Python 3.11
FROM python:3.11

WORKDIR /app

COPY . /app

# Instala dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Instala rclone
RUN curl https://rclone.org/install.sh | bash

# Exponer el puerto
EXPOSE 10000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:10000", "app:app"]

