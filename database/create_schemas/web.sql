-- web.sql
-- Elimina la base de datos si existe y crea una nueva llamada "web"
DROP DATABASE IF EXISTS web;
CREATE DATABASE web;
\connect web;

-- Tabla main_home_slides_config
CREATE TABLE public.main_home_slides_config (
    id SERIAL PRIMARY KEY,
    titulo_seccion TEXT,
    subtitulo_seccion TEXT,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_home_slides
CREATE TABLE public.main_home_slides (
    id SERIAL PRIMARY KEY,
    subtitulo TEXT,
    titulo_parte1 TEXT,
    titulo_parte2 TEXT,
    boton_texto TEXT,
    boton_link TEXT,
    imagen TEXT,
    alt TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_about_config
CREATE TABLE public.main_about_config (
    id SERIAL PRIMARY KEY,
    subtitulo TEXT,
    titulo_parte1 TEXT,
    titulo_parte2 TEXT,
    descripcion TEXT,
    imagen1 TEXT,
    imagen2 TEXT,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_about_stats
CREATE TABLE public.main_about_stats (
    id SERIAL PRIMARY KEY,
    tipo TEXT,
    cantidad TEXT,
    texto TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_services_config
CREATE TABLE public.main_services_config (
    id SERIAL PRIMARY KEY,
    subtitulo TEXT,
    titulo_parte1 TEXT,
    titulo_parte2 TEXT,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_services_items
CREATE TABLE public.main_services_items (
    id SERIAL PRIMARY KEY,
    icono TEXT,
    titulo TEXT,
    descripcion TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_testimonials_config
CREATE TABLE public.main_testimonials_config (
    id SERIAL PRIMARY KEY,
    subtitulo TEXT,
    titulo_parte1 TEXT,
    titulo_parte2 TEXT,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_testimonials_items
CREATE TABLE public.main_testimonials_items (
    id SERIAL PRIMARY KEY,
    avatar TEXT,
    rating INTEGER,
    descripcion TEXT,
    nombre TEXT,
    ubicacion TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_social_links
CREATE TABLE public.main_social_links (
    id SERIAL PRIMARY KEY,
    tipo TEXT,
    url TEXT,
    icono TEXT,
    texto TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_contact_config
CREATE TABLE public.main_contact_config (
    id SERIAL PRIMARY KEY,
    subtitulo TEXT,
    titulo_parte1 TEXT,
    titulo_parte2 TEXT,
    descripcion TEXT,
    telefono TEXT,
    horario TEXT,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_contact_options
CREATE TABLE public.main_contact_options (
    id SERIAL PRIMARY KEY,
    icono TEXT,
    titulo TEXT,
    descripcion TEXT,
    modal TEXT,
    aria_label TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_contact_modals_schedule
CREATE TABLE public.main_contact_modals_schedule (
    id SERIAL PRIMARY KEY,
    valor TEXT,
    texto TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_contact_modals_advisor_sucursales
CREATE TABLE public.main_contact_modals_advisor_sucursales (
    id SERIAL PRIMARY KEY,
    valor TEXT,
    texto TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_contact_modals_advisor_horas
CREATE TABLE public.main_contact_modals_advisor_horas (
    id SERIAL PRIMARY KEY,
    valor TEXT,
    texto TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_mapa_config
CREATE TABLE public.main_mapa_config (
    id SERIAL PRIMARY KEY,
    titulo TEXT,
    subtitulo TEXT,
    zoom_inicial INTEGER,
    latitud_central REAL,
    longitud_central REAL,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_mapa_marcadores
CREATE TABLE public.main_mapa_marcadores (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    latitud REAL,
    longitud REAL,
    descripcion TEXT,
    imagen TEXT,
    link TEXT,
    icono TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_footer_enlaces
CREATE TABLE public.main_footer_enlaces (
    id SERIAL PRIMARY KEY,
    texto TEXT,
    url TEXT,
    orden INTEGER,
    activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_contact_schedule_requests
CREATE TABLE public.main_contact_schedule_requests (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    telefono TEXT,
    fecha TEXT,
    horario TEXT,
    estado TEXT,
    notas_admin TEXT,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_contact_data_requests
CREATE TABLE public.main_contact_data_requests (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    email TEXT,
    estado TEXT,
    notas_admin TEXT,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla main_contact_advisor_visits
CREATE TABLE public.main_contact_advisor_visits (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    telefono TEXT,
    sucursal TEXT,
    fecha TEXT,
    hora TEXT,
    comentarios TEXT,
    estado TEXT,
    notas_admin TEXT,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla proyectos
CREATE TABLE public.proyectos (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    slug TEXT,
    descripcion TEXT,
    logo TEXT,
    imagen_principal TEXT,
    estado TEXT,
    es_visible BOOLEAN DEFAULT FALSE,
    fecha_inicio DATE,
    fecha_fin DATE,
    orden INTEGER,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla proyectos_slides
CREATE TABLE public.proyectos_slides (
    id SERIAL PRIMARY KEY,
    proyecto_id INTEGER,
    subtitulo TEXT,
    titulo_parte1 TEXT,
    titulo_parte2 TEXT,
    boton_texto TEXT,
    boton_link TEXT,
    imagen TEXT,
    alt TEXT,
    es_activo BOOLEAN DEFAULT FALSE,
    orden INTEGER,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla proyectos_valores
CREATE TABLE public.proyectos_valores (
    id SERIAL PRIMARY KEY,
    proyecto_about_id INTEGER,
    icono TEXT,
    titulo TEXT,
    descripcion TEXT,
    es_activo BOOLEAN DEFAULT FALSE,
    orden INTEGER,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla proyectos_mapa_locations
CREATE TABLE public.proyectos_mapa_locations (
    id SERIAL PRIMARY KEY,
    proyecto_mapa_id INTEGER,
    name TEXT,
    coords TEXT,
    img TEXT,
    link TEXT,
    description TEXT,
    es_activo BOOLEAN DEFAULT FALSE,
    orden INTEGER,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla proyectos_amenidades
CREATE TABLE public.proyectos_amenidades (
    id SERIAL PRIMARY KEY,
    proyecto_id INTEGER,
    titulo TEXT,
    descripcion TEXT,
    es_activo BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla proyectos_amenidad_items
CREATE TABLE public.proyectos_amenidad_items (
    id SERIAL PRIMARY KEY,
    proyecto_amenidades_id INTEGER,
    titulo TEXT,
    descripcion TEXT,
    icono TEXT,
    imagen TEXT,
    alt TEXT,
    es_activo BOOLEAN DEFAULT FALSE,
    orden INTEGER,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla proyectos_diseno_caracteristicas
CREATE TABLE public.proyectos_diseno_caracteristicas (
    id SERIAL PRIMARY KEY,
    proyecto_diseno_id INTEGER,
    titulo TEXT,
    descripcion TEXT,
    icono TEXT,
    imagen TEXT,
    alt TEXT,
    es_activo BOOLEAN DEFAULT FALSE,
    orden INTEGER,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla proyectos_diseno_materiales
CREATE TABLE public.proyectos_diseno_materiales (
    id SERIAL PRIMARY KEY,
    proyecto_diseno_id INTEGER,
    nombre TEXT,
    descripcion TEXT,
    icono TEXT,
    es_activo BOOLEAN DEFAULT FALSE,
    orden INTEGER,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla proyectos_diseno_propuestas
CREATE TABLE public.proyectos_diseno_propuestas (
    id SERIAL PRIMARY KEY,
    proyecto_diseno_id INTEGER,
    imagen TEXT,
    alt TEXT,
    caption TEXT,
    es_activo BOOLEAN DEFAULT FALSE,
    orden INTEGER,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla proyectos_diseno_estilos
CREATE TABLE public.proyectos_diseno_estilos (
    id SERIAL PRIMARY KEY,
    proyecto_diseno_id INTEGER,
    nombre TEXT,
    icono TEXT,
    es_activo BOOLEAN DEFAULT FALSE,
    orden INTEGER,
    fecha_creacion TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fecha_modificacion TIMESTAMP WITHOUT TIME ZONE
);
