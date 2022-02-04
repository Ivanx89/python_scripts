#De un .csv Crear los directorios listados y compartirlos con permisos de modificar

#Importar las librerías:

import csv
import os

#--------------------------#
#---------INICIO-----------#
#--------------------------#

#Leer CSV
with open("directorios.csv", "r") as file:
    reader = csv.reader(file)
    for each_row in reader:
        #Pasar las filas a string
        carpeta = ''.join(each_row)
        directorio = ''.join(each_row)
        print(directorio)
        directorio = directorio.split("\\")       
        print(directorio)
        nombre = directorio[-1]
        #Crear directorios listados en el fichero csv:
        os.popen(f"mkdir {carpeta}")
        print(f"Directorio {directorio} creado")
        os.popen(f"net share {nombre}=s:\{directorio} /GRANT:Change")