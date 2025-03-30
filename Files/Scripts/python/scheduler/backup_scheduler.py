import time, subprocess, os
from inactivity_tracker import is_time_to_backup

# =============== RUTAS ===============
location_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

RCLONE_BIN = os.path.join(location_path, "Files", "Temp", "installation", "rclone")
RCLONE_CONFIG = os.path.join(location_path, "Files", "Temp", "config", "rclone", "rclone.conf")
data_dir = os.path.join(location_path, "Files", "Data")
updt_file_path = os.path.join(location_path, "Files", "Temp", "update_file.txt")





# =============== FUNCIONES ===============
def monitor_and_backup():
    while True:
        print("Validando si es momento de subir la BD...")

        if not os.path.isfile(RCLONE_BIN):
            print(f"Error: Rclone no encontrado en {RCLONE_BIN}")
            time.sleep(60)
            continue

        if is_time_to_backup():
            print("Subiendo .db a Google Drive...")

            result = subprocess.run([
                RCLONE_BIN, "--config", RCLONE_CONFIG, "copy",
                data_dir,
                "drive:/UPY/Estancias_Enero_2025/cedrus_db",
                "--update"
            ], cwd=location_path)

            if result.returncode == 0:
                print("Backup completado correctamente.")
                with open(updt_file_path, 'w') as file:
                    file.write("False")
            else:
                print(f"Error durante el backup. Código de error: {result.returncode}")
                print(f"result.stdout.strip(): {result.stdout.strip()}\nresult.stderr.strip(): {result.stderr.strip()}")

            time.sleep(60)

        time.sleep(30)





# =============== MAIN ===============
if __name__ == "__main__":
    monitor_and_backup()
