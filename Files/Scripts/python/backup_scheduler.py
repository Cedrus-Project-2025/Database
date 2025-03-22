import time
import subprocess
from Files.Scripts.python.inactivity_tracker import is_time_to_backup

def monitor_and_backup():
    while True:
        if is_time_to_backup():
            print("Subiendo .db a Google Drive...")
            # Usa rclone para subir los archivos de base de datos
            result = subprocess.run([
                "rclone", "copy", "/app/Files/Data", "gdrive:/cedrus-db", "--update"
            ])
            if result.returncode == 0:
                print("Backup completado correctamente.")
            else:
                print("Error durante el backup.")

            # Espera un poco más antes de volver a intentar, para evitar múltiples subidas
            time.sleep(60)
        time.sleep(30)

if __name__ == "__main__":
    monitor_and_backup()
