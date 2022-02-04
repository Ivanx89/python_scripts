import csv
import os

contador = 0

with open("usuariosgrupos.csv", "r") as file:
    reader = csv.reader(file)
    for each_row in reader:
        if contador == 1:
            usuario = each_row[0]
            uousuario = each_row[1]
            grupo = each_row[2]
            uogrupo = each_row[3]
            os.system(f"dsmod group \"CN={grupo}, CN={uogrupo}, dc=dominio13, dc=local\" -addmbr \"CN={usuario}, CN={uousuario}, dc=dominio13, dc=local\"")
            print(f"Grupo {grupo} creado correctamente")
        else:
            contador = 1;

        
