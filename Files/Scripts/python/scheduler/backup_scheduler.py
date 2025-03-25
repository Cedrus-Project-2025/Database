import time, subprocess, os
from inactivity_tracker import is_time_to_backup

# =============== RUTAS ===============
location_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

os.makedirs(os.path.join(location_path,'installation'),exist_ok=True)
RCLONE_BIN = os.path.join(location_path, "installation/rclone")

updt_file_path = os.path.join(
    location_path,
    "Temp",
    "update_file.txt"
)





# =============== FUNCIONES ===============
def monitor_and_backup():
    while True:
        print(f"Validando si es momento de subir la BD...")

        if not os.path.isfile(RCLONE_BIN):
            print(f"Error: Rclone no encontrado en {RCLONE_BIN}")
            time.sleep(60)  # Esperar antes de volver a intentar
            continue

        if is_time_to_backup():
            print("Subiendo .db a Google Drive...")

            # Ejecuta rclone usando la ruta absoluta
            result = subprocess.run([
                RCLONE_BIN, "copy", "/app/Files/Data", "drive:/UPY/Estancias_Enero_2025/cedrus_db", "--update"
            ])

            if result.returncode == 0:
                print("Backup completado correctamente.")
                with open(updt_file_path, 'w') as file:
                    file.write("False")
            else:
                print(f"Error durante el backup. Código de error: {result.returncode}")

            # Espera un poco más antes de volver a intentar, para evitar múltiples subidas
            time.sleep(60)

        time.sleep(30)





# =============== MAIN ===============
if __name__ == "__main__":
    monitor_and_backup()
