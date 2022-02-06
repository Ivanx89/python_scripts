#Realizar copia de seguridad quitando el atributo "A" en Windows y que tenga la fecha actual como nombre

from datetime import datetime
import os
import zipfile
from zipfile import ZipFile
import datetime

fecha = datetime.date.today()


files = os.popen("dir /aa /b").readlines()
with ZipFile(f"{fecha}.zip", "w") as archivo:
    for each_file in files:
        each_file = each_file.strip()
        archivo.write(each_file)
        os.system(f"attrib -a {each_file}")
