import sqlite3
import os
import subprocess
from typing import List, Union, Tuple, Any, Dict


class DatabaseManager:
    def __init__(self) -> None:
        """
        Inicializa la conexión con la base de datos y verifica la existencia de las tablas.
        """

        self.location_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

    # =============== MÉTODOS PRIVADOS ===============
    def __connect(self,db_name) -> sqlite3.Connection:
        """
        Crea y devuelve una conexión a la base de datos.
        """
        try:
            path = os.path.join(
                self.location_path,
                'Files',
                'Data',
                db_name
            )
            return sqlite3.connect(path, timeout=10, check_same_thread=False)
        
        except Exception as ex:
            raise Exception(f"Fallo DatabaseManager desde __connect debido a: /*{ex}*/")

    # =============== MÉTODOS PUBLICOS ===============
    def execute_query(self, db_name:str, query: str, params: Tuple[Any, ...] = ()) -> None:
        """
        Ejecuta una consulta SQL (INSERT, UPDATE, DELETE) y sube la BD a Google Drive.
        """
        try:
            with self.__connect(db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
        except Exception as ex:
            raise Exception(f"Fallo DatabaseManager desde execute_query debido a: /*{ex}*/")
    
    def fetch_all(self, db_name: str, query: str, params: Tuple[Any, ...] = (), as_dict: bool = False) -> List[Union[Tuple[Any, ...], Dict[str, Any]]]:
        """
        Ejecuta una consulta SELECT y devuelve todos los resultados.
        Si as_dict es True, devuelve los resultados como diccionarios.
        """
        try:
            with self.__connect(db_name) as conn:
                if as_dict:
                    conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(query, params)
                results = cursor.fetchall()
            if as_dict:
                return [dict(row) for row in results]
            return results
        except Exception as ex:
            raise Exception(f"Fallo DatabaseManager desde fetch_all debido a: /*{ex}*/")

    def execute_many(self, db_name: str, query: str, values: List[Tuple[Any, ...]]) -> None:
        """
        Ejecuta una consulta SQL en múltiples registros (INSERT, UPDATE, etc.) y sube la BD.
        """
        try:
            with self.__connect(db_name) as conn:
                cursor = conn.cursor()
                cursor.executemany(query, values)
                conn.commit()
        except Exception as ex:
            raise Exception(f"Fallo DatabaseManager desde execute_many debido a: /*{ex}*/")