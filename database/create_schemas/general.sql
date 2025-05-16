-- Crear base de datos
DROP DATABASE IF EXISTS general;
CREATE DATABASE general;
\connect general;

-- Crear esquema público (opcional)
CREATE SCHEMA IF NOT EXISTS public;

-- Tabla proyectos_contacto_config
CREATE TABLE public.proyectos_contacto_config (
    id SERIAL PRIMARY KEY,
    proyecto_id INTEGER NOT NULL,
    titulo TEXT,
    descripcion TEXT,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

-- Tabla proyectos_contacto_opciones
CREATE TABLE public.proyectos_contacto_opciones (
    id SERIAL PRIMARY KEY,
    proyecto_id INTEGER NOT NULL,
    id_opcion TEXT,
    icono TEXT,
    titulo TEXT,
    descripcion TEXT,
    boton_texto TEXT,
    modal TEXT,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

-- Tabla proyectos_contacto_modal
CREATE TABLE public.proyectos_contacto_modal (
    id SERIAL PRIMARY KEY,
    id_opcion TEXT,
    contenido_modal TEXT,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

-- Tabla proyectos_contacto_planes
CREATE TABLE public.proyectos_contacto_planes (
    id SERIAL PRIMARY KEY,
    id_opcion TEXT,
    titulo TEXT,
    icono TEXT,
    beneficios TEXT,
    destacado BOOLEAN DEFAULT FALSE,
    tag TEXT,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

-- Tabla proyectos_about
CREATE TABLE public.proyectos_about (
    id SERIAL PRIMARY KEY,
    proyecto_id INTEGER NOT NULL,
    titulo TEXT,
    subtitulo TEXT,
    descripcion TEXT,
    imagen TEXT,
    imagen_alt TEXT,
    conclusion TEXT,
    valores_titulo TEXT,
    es_activo INTEGER DEFAULT 1,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Índices y claves foráneas (opcional, si tienes las tablas referenciadas)
-- Por ejemplo, para proyecto_id FK (si existe tabla proyectos)
-- ALTER TABLE public.proyectos_contacto_config
--   ADD CONSTRAINT fk_proyecto FOREIGN KEY(proyecto_id) REFERENCES public.proyectos(id);
--
-- ALTER TABLE public.proyectos_contacto_opciones
--   ADD CONSTRAINT fk_proyecto_opciones FOREIGN KEY(proyecto_id) REFERENCES public.proyectos(id);
