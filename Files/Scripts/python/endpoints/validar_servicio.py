import subprocess, os
from flask_restful import Resource

location_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))

class Start_Rclone(Resource):
    def get(self):
        try:
            # ===== Ruta completa al script
            inst_script_path = os.path.join(location_path, 'Files','Scripts','bash','install_rclone.sh')
            inst_script_path = os.path.abspath(inst_script_path)
            down_script_path = os.path.join(location_path, 'Files','Scripts','bash','download_dbs.sh')
            down_script_path = os.path.abspath(down_script_path)

            # ===== Ejecutar script de instalación
            inst_result = subprocess.run(
                ["bash", inst_script_path],
                capture_output=True,
                text=True
            )

            if inst_result.returncode != 0:
                return {
                    "status": "failed",
                    "reason": "Rclone installation script failed.",
                    "details": inst_result.stderr.strip()
                }, 500

            # ===== Ejecutar script de descarga de bases de datos
            down_result = subprocess.run(
                ["bash",down_script_path],
                capture_output=True,
                text=True
            )

            if down_result.returncode != 0:
                config_path = os.path.join(location_path,'.config','rclone','rclone.conf')
                if not(os.path.isfile(config_path)): config_str = 'No se encontró el archivo'
                else:
                    with open(config_path,'r') as file: config_str = file.read()
                
                return {
                    "status"  : "failed",
                    "reason"  : "Download Databases script failed.",
                    ".config" : config_str,
                    "details" : down_result.stderr.strip(),
                    "log"     : down_result.stdout.strip()
                }, 500

            # ===== Confirmación
            return {
                "status": "Rclone installed and configured!",
                "log": inst_result.stdout.strip(),
                "base_dir":f"{os.listdir(location_path)}",
                "data_dir":f"{os.listdir(os.path.join(location_path,'Files','Data'))}",
                "temp_dir":f"{os.listdir(os.path.join(location_path,'Files','Temp'))}",
            }, 200

        except Exception as ex: return {"status": "failed!", "reason": str(ex)}, 500
