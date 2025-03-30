import subprocess, os

location_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))

class Start_Rclone:
    def start(self):
        try:

            # ===== Scripts de Instalacion
            inst_script_path = os.path.abspath(os.path.join(location_path, 'Files','Scripts','bash','install_rclone.sh'))
            inst_result = subprocess.run(
                ["bash", inst_script_path],
                capture_output=True,
                text=True,
                cwd=os.path.dirname(inst_script_path)
            )

            if inst_result.returncode != 0:
                return {
                    "status": "failed",
                    "reason": "Rclone installation script failed.",
                    "details": inst_result.stderr.strip(),
                    "log": inst_result.stdout.strip(),
                    "location_path": location_path
                }, 500

            # ===== Scripts de Descarga
            down_script_path = os.path.abspath(os.path.join(location_path, 'Files','Scripts','bash','download_dbs.sh'))
            down_result = subprocess.run(
                ["bash", down_script_path],
                capture_output=True,
                text=True,
                cwd=os.path.dirname(down_script_path)
            )

            if down_result.returncode != 0:
                config_path = os.path.join(location_path,'Files','Temp','.config','rclone','rclone.conf')
                if not os.path.isfile(config_path):
                    config_str = 'No se encontró el archivo'
                else:
                    with open(config_path,'r') as file:
                        config_str = file.read()

                return {
                    "status": "failed",
                    "reason": "Download Databases script failed.",
                    ".config": config_str,
                    "details": down_result.stderr.strip(),
                    "log": down_result.stdout.strip(),
                    "location_path": location_path
                }, 500

            # ===== Confirmacion
            return {
                "status": "Rclone installed and configured!",
                "log": inst_result.stdout.strip(),
                "base_dir": f"{os.listdir(location_path)}",
                "data_dir": f"{os.listdir(os.path.join(location_path,'Files','Data'))}",
                "temp_dir": f"{os.listdir(os.path.join(location_path,'Files','Temp'))}",
            }, 200

        except Exception as ex: return {"status": "failed!", "reason": str(ex)}, 500

