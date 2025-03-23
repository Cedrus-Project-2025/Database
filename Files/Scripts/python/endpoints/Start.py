import subprocess
from flask_restful import Resource


class Start_Rclone(Resource):
    def get(self):
        try:
            # ===== Ejecutar script install_rclone.sh
            result = subprocess.run(
                ["bash", "./Files/Scripts/bash/install_rclone.sh"],
                capture_output=True,
                text=True
            )

            # Log del resultado (opcional)
            print("STDOUT:\n", result.stdout)
            print("STDERR:\n", result.stderr)

            if result.returncode != 0:
                return {
                    "status": "failed",
                    "reason": "Rclone installation script failed.",
                    "details": result.stderr.strip()
                }, 500

            # ===== Confirmación
            return {"status": "Rclone started!", "log": result.stdout.strip()}, 200

        except Exception as ex: return {"status": "failed!", "reason": f"{ex}"}, 500
