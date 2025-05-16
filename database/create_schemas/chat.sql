-- Elimina la base de datos si existe y crea una nueva llamada "chat"
DROP DATABASE IF EXISTS chat;
CREATE DATABASE chat;
\connect chat;

-- Tabla chatbot_interacciones
CREATE TABLE public.chatbot_interacciones (
    id SERIAL PRIMARY KEY,
    pregunta TEXT,
    respuesta TEXT,
    tiempo_respuesta INTEGER,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

-- Tabla configuraciones
CREATE TABLE public.configuraciones (
    id SERIAL PRIMARY KEY,
    clave TEXT,
    valor TEXT,
    descripcion TEXT,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);
