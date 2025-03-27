import sqlite3
import os
import subprocess
from typing import List, Tuple, Any

class DatabaseManager:
    def __init__(self) -> None:
        """
        Inicializa la conexión con la base de datos y verifica la existencia de las tablas.
        """

        self.location_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))


    # =============== MÉTODOS PRIVADOS ===============
    def __upload_db_to_drive(self,db_name:str) -> None:
        """
        Sube la base de datos a Google Drive después de cada modificación.
        """
        # try:
        path = os.path.join(
            self.location_path,
            'Files',
            'Data',
            db_name
        )
        result = subprocess.run(
            ["rclone", "copy", path, "[drive]"],
            capture_output=True,
            text=True,
            cwd=self.location_path
        )
        if result.returncode != 0:
            raise RuntimeError(f"Wtf checa qpd con el log: {result.stdout.strip()}/******/Wtf checa qpd con el detail: {result.stderr.strip()}")

        return "Base de datos subida a Google Drive correctamente."
        
        # except Exception as e:
        #     raise RuntimeError(f"Error al subir la base de datos con Rclone, Saltando proceso: {e}")

    def __connect(self,db_name) -> sqlite3.Connection:
        """
        Crea y devuelve una conexión a la base de datos.
        """
        # try:
        path = os.path.join(
            self.location_path,
            'Files',
            'Data',
            db_name
        )
        return sqlite3.connect(path, timeout=10, check_same_thread=False)
        
        # except sqlite3.Error as e:
        #     raise RuntimeError(f"Error al conectar a la base de datos: {e}")

    # =============== MÉTODOS PUBLICOS ===============
    def execute_query(self, db_name:str, query: str, params: Tuple[Any, ...] = ()) -> None:
        """
        Ejecuta una consulta SQL (INSERT, UPDATE, DELETE) y sube la BD a Google Drive.
        """
        # try:
        conn:sqlite3.Connection = self.__connect(db_name)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()
        self.__upload_db_to_drive(db_name)
        # except Exception as ex:
        #     raise ex

    def fetch_all(self, db_name:str, query: str, params: Tuple[Any, ...] = ()) -> List[Tuple[Any, ...]]:
        """
        Ejecuta una consulta SELECT y devuelve todos los resultados.
        """
        # try:
        conn:sqlite3.Connection = self.__connect(db_name)
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
        # except Exception as ex:
        #     raise ex
    