#Realizar copia de seguridad quitando el atributo "A" en Windows para los archivos que pesen >= a el argumento del comando

from datetime import datetime
import os
import zipfile
from zipfile import ZipFile
import datetime
import sys

fecha = datetime.date.today()
peso_input = int(sys.argv[1])


files = os.popen("dir /aa /b").readlines()
with ZipFile(f"{fecha}.zip", "w") as archivo:
    for each_file in files:
        each_file = each_file.strip()
        if os.stat(f"./{each_file}").st_size >= peso_input:
            archivo.write(each_file)
            os.system(f"attrib -a {each_file}")
        else:
            print(f"Se ha omitido el archivo {each_file}")
