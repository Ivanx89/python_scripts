#Crear grupos en el DC mencionados en un .csv

import csv
import os

contador = 0

with open("listagrupos.csv", "r") as file:
    reader = csv.reader(file)
    for each_row in reader:
        if contador == 1:
            grupo = each_row[0]
            ou      = each_row[1]
            os.system(f"dsadd group \"CN={grupo}, CN={ou}, dc=dominio13, dc=local\" -secgrp yes")
            print(f"Grupo {grupo} creado correctamente")
        else:
            contador = 1;

        
