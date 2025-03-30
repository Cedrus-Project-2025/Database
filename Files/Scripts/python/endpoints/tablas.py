import os, sys
from flask import request
from flask_restful import Resource

location_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
sys.path.append(location_path)

from Files.Scripts.python.Database.manager import DatabaseManager


class Tables(Resource):
    def __init__(self):
        self.db = DatabaseManager()

    def __get_db_name(self, endpoint:str) -> str:
        if 'business' in endpoint: return 'bi.db'
        elif 'chat' in endpoint:   return 'asistente.db'
        elif 'web' in endpoint:    return 'web.db'
        else:                      return 'general.db'

    def get(self):
        try:
            # ===== Peticion
            endpoint = request.endpoint
            
            # ===== Valores Peticion
            db_name = self.__get_db_name(endpoint)

            # ===== Consulta BD
            tablas_query = "SELECT name FROM sqlite_master WHERE type='table';"
            tablas = self.db.fetch_all(db_name, tablas_query)

            resultado = {}

            for tabla in tablas:
                nombre_tabla = tabla[0]
                if nombre_tabla == 'sqlite_sequence': continue

                columnas_query = f"PRAGMA table_info('{nombre_tabla}');"
                columnas = self.db.fetch_all(db_name, columnas_query)

                # Convertimos a un formato tipo diccionario
                columnas_resultado = [
                    {"column_name": col[1], "data_type": col[2]}  # name y type
                    for col in columnas
                ]
                resultado[nombre_tabla] = columnas_resultado

            # ===== Confirmación
            return {"status":"fetched!","tablas": resultado}, 200
        
        # ===== Manejor de errores
        except KeyError as ex: return {"status":"failed from Tables!","reason":f"The key {ex} was not in request."}, 400

        except RuntimeError as ex: return {"status":"failed from Tables!","reason":f"{ex}"}, 400

        except Exception as ex: return {"status":"failed from Tables!","reason":f"{ex}"}, 500

    def post(self):
        try:
            # ===== Peticion
            data = dict(request.json) if request.is_json else dict()
            endpoint = request.endpoint

            # ===== Valores Peticion
            db_name = self.__get_db_name(endpoint)
            tb_name = data['nombre_tabla']
            columnas = data['columnas']

            if type(columnas) != dict or not columnas: raise RuntimeError("El arg 'columnas' debe ser un diccionario no vacío.")

            cols_defs = ', '.join([f"{col} {definition}" for col, definition in columnas.items()])
            
            # ===== Consulta BD
            query = f"CREATE TABLE IF NOT EXISTS {tb_name} ({cols_defs});"
            self.db.execute_query(db_name, query)

            # ===== Confirmación
            return {"status":"created!","query":query}, 201

        # ===== Manejor de errores
        except KeyError as ex: return {"status":"failed from Tables!","reason":f"Falta la clave: {ex}"}, 400
        except Exception as ex: return {"status":"failed from Tables!","reason":f"{ex}"}, 500

    def patch(self):
        try:
            # ===== Peticion
            data = dict(request.json) if request.is_json else dict()
            endpoint = request.endpoint

            # ===== Valores Peticion
            db_name = self.__get_db_name(endpoint)
            tb_name = data['nombre_tabla']
            accion = data['accion']  # 'agregar', 'renombrar', 'eliminar'

            if accion == 'agregar':
                columna = data['columna']          # ej: "edad"
                tipo_columna = data['tipo_columna'] # ej: "INTEGER"
                query = f"ALTER TABLE {tb_name} ADD COLUMN {columna} {tipo_columna};"

            elif accion == 'renombrar':
                viejo_nombre = data['columna_vieja'] # ej: "edad"
                nuevo_nombre = data['columna_nueva'] # ej: "edad_usuario"
                query = f"ALTER TABLE {tb_name} RENAME COLUMN {viejo_nombre} TO {nuevo_nombre};"

            elif accion == 'eliminar':
                columna = data['columna'] # ej: "edad"
                temp_table = f"{tb_name}_temp"

                cols_actuales = [col[1] for col in self.db.fetch_all(
                    db_name, f"PRAGMA table_info({tb_name});"
                ) if col[1] != columna]

                if not cols_actuales:
                    raise RuntimeError("No se pueden eliminar todas las columnas de una tabla.")

                cols_str = ', '.join(cols_actuales)
                queries = [
                    f"CREATE TABLE {temp_table} AS SELECT {cols_str} FROM {tb_name};",
                    f"DROP TABLE {tb_name};",
                    f"ALTER TABLE {temp_table} RENAME TO {tb_name};"
                ]

                for q in queries:
                    self.db.execute_query(db_name, q)

                return {"status":"updated!","queries":queries}, 200

            else:
                raise RuntimeError("La 'accion' debe ser 'agregar', 'renombrar' o 'eliminar'.")

            # ===== Consulta BD
            self.db.execute_query(db_name, query)

            # ===== Confirmación
            return {"status":"updated!","query":query}, 200

        # ===== Manejor de errores
        except KeyError as ex: return {"status":"failed from Tables!","reason":f"Falta la clave: {ex}"}, 400
        except Exception as ex: return {"status":"failed from Tables!","reason":f"{ex}"}, 500

    def delete(self):
        try:
            # ===== Peticion
            data = dict(request.json) if request.is_json else dict()
            endpoint = request.endpoint

            # ===== Valores Peticion
            db_name = self.__get_db_name(endpoint)
            tb_name = data['nombre_tabla']

            # ===== Consulta BD
            query = f"DROP TABLE IF EXISTS {tb_name};"
            self.db.execute_query(db_name, query)

            # ===== Confirmación
            return {"status":"deleted!","query":query}, 200

        # ===== Manejor de errores
        except KeyError as ex: return {"status":"failed from Tables!","reason":f"Falta la clave: {ex}"}, 400
        except Exception as ex: return {"status":"failed from Tables!","reason":f"{ex}"}, 500