import os
import time
import stake_axs
from os import system


def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

f = open("sync.txt", "r")
syncini = float(f.readline())
f.close()
minutes = 0
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
file_path = os.path.join(script_dir, 'counter.txt')
ciclo = True
time.sleep(syncini)
while (ciclo):
    with open(file_path,'r+') as f:
        minutes = int(f.read())

        print(f'Sleeping for {minutes} minutes')
        time.sleep(minutes*60)
        output = stake_axs.main()
        minutes+=1
        if output!=0:
            print("Issues, sleeping 1 minute")
            time.sleep(60)
            output = stake_axs.main()
            minutes+=1
        f.seek(0)
        f.write(str(minutes))
        f.close()
        cantidad_segundos = 86400
        while (cantidad_segundos  > 0):
            time.sleep(1)
            convertido = segundos_a_segundos_minutos_y_horas(cantidad_segundos)
            system("clear")
            print(convertido)
            cantidad_segundos = cantidad_segundos - 1
