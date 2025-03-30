import os, sys
from flask import request
from flask_restful import Resource

location_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
sys.path.append(location_path)

from Files.Scripts.python.Database.manager import DatabaseManager

class Registers(Resource):
    # =============== MÉTODOS PRIVADOS ===============
    def __init__(self):
        self.db = DatabaseManager()

    def __get_db_name(self, endpoint:str) -> str:
        if 'business' in endpoint: return 'bi.db'
        elif 'chat' in endpoint:   return 'asistente.db'
        elif 'web' in endpoint:    return 'web.db'
        else:                      return 'general.db'

    # =============== MÉTODOS PUBLICOS ===============
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
            result = self.db.fetch_all(db_name,query,as_dict=True)

            # ===== Confirmación
            return {"status":"fetched!","query":query,"result":result}, 200
        
        # ===== Manejor de errores
        except KeyError as ex: return {"status":"failed from Registers!","reason":f"The key {ex} was not in request."}, 400

        except RuntimeError as ex: return {"status":"failed from Registers!","reason":f"{ex}"}, 400

        except Exception as ex: return {"status":"failed from Registers!","reason":f"{ex}"}, 500

    def post(self):
        try:
            # ===== Peticion
            data = dict(request.json) if request.is_json else dict()
            endpoint = request.endpoint
            
            # ===== Valores Peticion
            db_name = self.__get_db_name(endpoint)
            
            tb_name = data.get("nombre_tabla")
            if not isinstance(tb_name, str): raise RuntimeError("El valor de 'nombre_tabla' debe ser un string.")
            
            registros = data.get("registros")
            if not registros or not isinstance(registros, list): raise RuntimeError("El valor de 'registros' debe ser una lista de diccionarios.")

            columnas = list(registros[0].keys())
            columnas_str = ", ".join(columnas)
            placeholders = ", ".join(["?"] * len(columnas))

            values = []
            for fila in registros:
                if not isinstance(fila, dict): raise RuntimeError("Cada registro debe ser un diccionario.")
                fila_valores = [fila.get(col) for col in columnas]
                values.append(tuple(fila_valores))
                
            # ===== Consulta BD
            query = f"INSERT INTO {tb_name} ({columnas_str}) VALUES ({placeholders})"
            self.db.execute_many(db_name, query, values)

            # ===== Confirmación
            return {"status": "inserted!", "registros_insertados": len(values)}, 201
        
        # ===== Manejor de errores
        except KeyError as ex: return {"status":"failed from Registers!","reason":f"The key {ex} was not in request."}, 400

        except RuntimeError as ex: return {"status":"failed from Registers!","reason":f"{ex}"}, 400

        except Exception as ex: return {"status":"failed from Registers!","reason":f"{ex}"}, 500

    def patch(self):
        try:
            # ===== Peticion
            data = dict(request.json) if request.is_json else dict()
            endpoint = request.endpoint
            
            # ===== Valores Peticion
            db_name = self.__get_db_name(endpoint)

            tb_name = data.get("nombre_tabla")
            if not isinstance(tb_name, str): raise RuntimeError("El valor de 'nombre_tabla' debe ser un string.")

            cambios = data.get("cambios")
            if not cambios or not isinstance(cambios, dict): raise RuntimeError("El valor de 'cambios' debe ser un diccionario.")

            condiciones = data.get("condiciones", "")
            if not isinstance(condiciones, str): raise RuntimeError("El valor de 'condiciones' debe ser un string.")

            # ===== Consulta BD
            set_clause = ", ".join([f"{col} = ?" for col in cambios])
            values = list(cambios.values())

            query = f"UPDATE {tb_name} SET {set_clause} {condiciones};"
            self.db.execute_query(db_name, query, tuple(values))

            # ===== Confirmación
            return {"status": "updated!", "query": query}, 200
        
        # ===== Manejor de errores
        except KeyError as ex: return {"status":"failed from Registers!","reason":f"The key {ex} was not in request."}, 400

        except RuntimeError as ex: return {"status":"failed from Registers!","reason":f"{ex}"}, 400

        except Exception as ex: return {"status":"failed from Registers!","reason":f"{ex}"}, 500

    def delete(self):
        try:
            # ===== Peticion
            data = dict(request.json) if request.is_json else dict()
            endpoint = request.endpoint
            
            # ===== Valores Peticion
            db_name = self.__get_db_name(endpoint)

            tb_name = data.get("nombre_tabla")
            if not isinstance(tb_name, str): raise RuntimeError("El valor de 'nombre_tabla' debe ser un string.")

            condiciones = data.get("condiciones", "")
            if not isinstance(condiciones, str): raise RuntimeError("El valor de 'condiciones' debe ser un string.")
            if condiciones.strip() == "":
                raise RuntimeError("Por seguridad, DELETE requiere condiciones explícitas.")

            # ===== Consulta BD
            query = f"DELETE FROM {tb_name} {condiciones};"
            self.db.execute_query(db_name, query)

            # ===== Confirmación
            return {"status":"fetched!","query":query}, 200
        
        # ===== Manejor de errores
        except KeyError as ex: return {"status":"failed from Registers!","reason":f"The key {ex} was not in request."}, 400

        except RuntimeError as ex: return {"status":"failed from Registers!","reason":f"{ex}"}, 400

        except Exception as ex: return {"status":"failed from Registers!","reason":f"{ex}"}, 500