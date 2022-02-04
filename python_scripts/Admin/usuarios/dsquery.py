import os

usuarios = os.popen("dsquery user").read().split()

for i in usuarios:
    i = i.strip()
    campos = i.split(",")
    nombre = campos[0].split("=")
    if (len(nombre) > 1):
        print(nombre[1])