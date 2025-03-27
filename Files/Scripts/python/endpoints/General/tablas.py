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
            data = dict(request.json) if request.is_json else dict()
            endpoint = request.endpoint
            
            # ===== Valores Peticion
            db_name = self.__get_db_name(endpoint)

            # Columnas
            cols = data.get('columnas',['all',])
            if type(cols) != list: raise RuntimeError("El valor del arg 'columnas' tiene que ser una lista.")
            
            if len(cols) == 1 and cols[0] == 'all': cols = '*'
            elif len(cols) == 1: cols = f"{cols[0]}"
            elif len(cols) > 1: cols = ', '.join(cols)
            else: raise RuntimeError("El valor del arg 'columnas' no puede estar vacio. Tiene que tener el nombre de las columnas a revisar o, en su defecto, omitir arg para mostrar todas las columnas.")

            # Nombre tabla
            tb_name = data.get('nombre_tabla',None)
            if tb_name == None: raise KeyError("No se encontró el arg 'nombre_tabla' en la petición.")
            elif type(tb_name) != str: raise RuntimeError("El valor del arg 'nombre_tabla' no puede ser diferente a un string.")
            
            # Condiciones
            conditions = data.get('condiciones',['None',])
            if type(conditions) != list: raise RuntimeError("El valor del arg 'condiciones' tiene que ser una lista.")
            
            if len(conditions) == 1 and conditions[0] == 'None': conditions = ''
            elif len(conditions) == 1: conditions = conditions[0]
            elif len(conditions) > 1: conditions = ' '.join(conditions)
            else: raise RuntimeError("El valor del arg 'condiciones' no puede estar vacio. Tiene que tener una lista con las condiciones tipo SQL para procesar o, en su defecto, omitir arg para no condicionar la consulta.")

            # Tipo Orden
            orden = data.get('tipo_orden',dict())
            if type(orden) != dict: raise RuntimeError("El valor del arg 'tipo_orden' tiene que ser un diccionario con el nombre de la columna como key y si es 'asc' o 'desc' como valor.")
            
            if len(orden) > 0:
                texto = " ORDER BY "
                index = 0
                for key,value in orden.items():
                    if not(value in ['asc','desc']): raise RuntimeError(f"Dentro del valor del arg 'tipo_orden', para la columna '{key}', no se puede ordenar por '{value}', tiene que ser 'asc' o 'desc'.")
                    
                    if index == 0: texto += f"{key} {value.upper()}"
                    elif index > 0: texto += f", {key} {value.upper()}"
                    
                    index += 1
                orden = texto
            else: orden = ""

            # Registros
            registros = data.get('registros',-1)
            if (type(registros) != int) or registros < -1: raise KeyError("El valor del arg 'registros' tiene que ser un entero positivo.")

            if registros == -1: registros = ''
            else: registros = f' LIMIT {registros}'

            # ===== Consulta BD
            query = f"SELECT {cols} FROM {tb_name} {conditions}{orden}{registros};"
            result = self.db.fetch_all(db_name,query)

            # ===== Confirmación
            return {"status":"fetched!","query":query,"result":result}, 200
        
        # ===== Manejor de errores
        except KeyError as ex: return {"status":"failed!","reason":f"The key {ex} was not in request."}, 400

        except RuntimeError as ex: return {"status":"failed","reason":f"{ex}"}, 400

        except Exception as ex: return {"status":"failed!","reason":f"{ex}"}, 500

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
        except KeyError as ex: return {"status":"failed!","reason":f"Falta la clave: {ex}"}, 400
        except Exception as ex: return {"status":"failed!","reason":f"{ex}"}, 500

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
        except KeyError as ex: return {"status":"failed!","reason":f"Falta la clave: {ex}"}, 400
        except Exception as ex: return {"status":"failed!","reason":f"{ex}"}, 500

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
        except KeyError as ex: return {"status":"failed!","reason":f"Falta la clave: {ex}"}, 400
        except Exception as ex: return {"status":"failed!","reason":f"{ex}"}, 500