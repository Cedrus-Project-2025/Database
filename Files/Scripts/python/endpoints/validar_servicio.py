import subprocess, os
from flask_restful import Resource

location_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))

class Start_Rclone(Resource):
    def get(self):
        try:
            # Ruta completa al script
            script_path = os.path.join(location_path, 'Files','Scripts','bash','install_rclone.sh')
            script_path = os.path.abspath(script_path)

            # Ejecutar script de instalación
            result = subprocess.run(
                ["bash", script_path],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                return {
                    "status": "failed",
                    "reason": "Rclone installation script failed.",
                    "details": result.stderr.strip()
                }, 500

            return {
                "status": "Rclone installed and configured!",
                "log": result.stdout.strip(),
                "base_dir":f"{os.listdir(location_path)}",
                "data_dir":f"{os.listdir(os.path.join(location_path,'Files','Data'))}",
                "temp_dir":f"{os.listdir(os.path.join(location_path,'Files','Temp'))}",
            }, 200

        except Exception as ex: return {"status": "failed!", "reason": str(ex)}, 500
