#Crear usuarios en el dominio DC.

import csv
import os

contador = 0

with open("listausuarios.csv", "r") as file:
    reader = csv.reader(file)
    for each_row in reader:
        if contador == 1:
            usuario = each_row[0]
            ou      = each_row[1]
            password= each_row[2]
            os.system(f"dsadd user \"CN={usuario}, CN={ou}, dc=dominio13, dc=local\" -pwd {password} -disabled no")
            print(f"Usuario {usuario} creado correctamente")
        else:
            contador = 1;

        
