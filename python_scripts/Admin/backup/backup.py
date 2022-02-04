import os
import zipfile
from zipfile import ZipFile

files = os.listdir(".")
with ZipFile("compress.zip", "w") as archivo:
    for each_file in files:
        archivo.write(each_file)
    