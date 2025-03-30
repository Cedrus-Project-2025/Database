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
                raise RuntimeError("\n".join([
                    "status: failed",
                    "reason: Rclone installation script failed.",
                    f"details:  {inst_result.stderr.strip()}",
                    f"log: {inst_result.stdout.strip()}",
                    f"location_path: {location_path}"
                ]))

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

                raise RuntimeError('\n'.join(
                    "status: failed",
                    "reason: Download Databases script failed.",
                    f"config: {config_str}",
                    f"details: {down_result.stderr.strip()}",
                    f"log: {down_result.stdout.strip()}",
                    f"location_path: {location_path}"
                ))

        except Exception as ex: return {"status": "failed from Start_Rclone!", "reason": str(ex)}, 500

