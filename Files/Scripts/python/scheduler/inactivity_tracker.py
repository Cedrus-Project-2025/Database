import os
from datetime import datetime, timedelta

# =============== RUTAS ===============
time_file_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
    "Temp",
    "time_file.txt"
)
updt_file_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
    "Temp",
    "update_file.txt"
)



# =============== FUNCIONES ===============
def update_last_access():
    last_access = datetime.now()
    with open(time_file_path,'w') as file: file.write(f"{last_access}")
    with open(updt_file_path,'w') as file: file.write("True")
    print('Se actualizo la hora')
    

def is_time_to_backup():
    '''Valida si ya pasaron 4 minutos después de la última actualizacion a la BD.'''
    now = datetime.now()

    # ===== Evaluando existencia de archivos temporales
    if not(os.path.isfile(time_file_path)):
        with open(time_file_path,'w') as file: file.write(f"{now}")
    
    if not(os.path.isfile(updt_file_path)):
        with open(updt_file_path,'w') as file: file.write(f"False")

    # ===== Validacion de Hora Actual Vs. Última Actualizacion
    with open(time_file_path,'r') as file: last_access = file.read()
    last_access = datetime.strptime(last_access, "%Y-%m-%d %H:%M:%S.%f")
    diff = now - last_access
    print(f"\tHan pasado {diff}")

    # ===== Validacion si se tiene que subir la info a Drive
    with open(updt_file_path,'r') as file: update = file.read()
    update = True if update == 'True' else False

    return bool((diff > timedelta(minutes=1)) and update)
