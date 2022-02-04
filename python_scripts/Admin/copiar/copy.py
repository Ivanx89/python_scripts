import sys
import os
import shutil


fichero = sys.argv[1]
directorio = sys.argv[2]

if len(sys.argv) == 3:
    if not os.path.exists(directorio):
        print("No existe el directorio")
        print("Directorio creado")
        os.mkdir(directorio)
        os.system(f"copy {fichero} {directorio}")
    else:
        os.system(f"copy {fichero} {directorio}")
elif len(sys.argv) == 3:
    print("Indique un fichero y un directorio")
else:
    print("Ha introducido un dato no válido")