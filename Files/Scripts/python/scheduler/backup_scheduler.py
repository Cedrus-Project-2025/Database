import time, subprocess, os
from inactivity_tracker import is_time_to_backup

# =============== RUTAS ===============
updt_file_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
    "Temp",
    "update_file.txt"
)





# =============== FUNCIONES ===============
def monitor_and_backup():
    while True:
        print(f"Validando si es momento de subir la BD...")
        if is_time_to_backup():
            print("Subiendo .db a Google Drive...")
            # Usa rclone para subir los archivos de base de datos
            result = subprocess.run([
                "rclone", "copy", "/app/Files/Data", "gdrive:/UPY/Estancias Enero 2025/cedrus-db", "--update"
            ])
            if result.returncode == 0:
                print("Backup completado correctamente.")
                with open(updt_file_path,'w') as file: file.write("False")
            else:
                print("Error durante el backup.")

            # Espera un poco más antes de volver a intentar, para evitar múltiples subidas
            time.sleep(60)
        time.sleep(30)





# =============== MAIN ===============
if __name__ == "__main__":
    monitor_and_backup()
