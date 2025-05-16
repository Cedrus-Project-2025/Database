-- business.sql
-- Elimina la base de datos si existe y crea una nueva llamada "business"
DROP DATABASE IF EXISTS business;
CREATE DATABASE business;
\connect business;

-- Tabla publicaciones
CREATE TABLE public.publicaciones (
    post_id INTEGER PRIMARY KEY,
    page_id TEXT,
    page_name TEXT,
    title TEXT,
    description TEXT,
    duration_sec INTEGER,
    publish_time TEXT,
    caption_type TEXT,
    permalink TEXT,
    is_crosspost INTEGER,
    is_share INTEGER,
    post_type TEXT,
    languages TEXT,
    custom_labels TEXT,
    funded_content_status TEXT,
    data_comment TEXT,
    date TEXT,
    views INTEGER,
    reach INTEGER,
    reactions INTEGER,
    comments INTEGER,
    shares INTEGER,
    total_clicks INTEGER,
    other_clicks INTEGER,
    link_clicks INTEGER,
    matc_pc REAL,
    seconds_viewed INTEGER,
    average_seconds_viewed REAL,
    estimated_earnings_usd REAL,
    ad_cpm_usd REAL,
    ad_impressions INTEGER
);

-- Tabla audiencia
CREATE TABLE public.audiencia (
    fecha DATE,
    edad_promedio REAL,
    porcentaje_hombres REAL,
    porcentaje_mujeres REAL,
    ubicacion_principal TEXT
);
