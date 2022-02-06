#Copiar los archivos como argumento del directorio actual a un directorio que pasa como argumento

import sys
import os
import shutil



directorio = sys.argv[-1]
longitud = len(sys.argv)
n = 0

if len(sys.argv) >= 3:
    if not os.path.exists(directorio):
            print("No existe el directorio")
            print("Directorio creado")
            os.mkdir(directorio)
            for i in range(1, (longitud -1)):
                shutil.copy(sys.argv[i], directorio)
                n += 1
            print(f"{n} fichero(s) copiado(s)")   
    else:
            for i in range(1, (longitud -1)):
                shutil.copy(sys.argv[i], directorio)
                n += 1 
            print(f"{n} fichero(s) copiado(s)")
            
else:
    print("Introduzca más argumentos")

