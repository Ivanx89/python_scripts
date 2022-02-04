import sys
import os
import shutil

directorio = sys.argv[-1]

if not os.path.exists(directorio):
        print("No existe el directorio")
        print("Directorio creado")
        os.mkdir(directorio)
        os.system(f"xcopy . {directorio}") 
else:
        os.system(f"xcopy . {directorio}")