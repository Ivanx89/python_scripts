#Realizar copia de seguridad quitando el atributo "A" en Windows

import os
import zipfile
from zipfile import ZipFile


files = os.popen("dir /aa /b").readlines()
with ZipFile("compress.zip", "w") as archivo:
    for each_file in files:
        each_file = each_file.strip()
        archivo.write(each_file)
        os.system(f"attrib -a {each_file}")
    