#Configurar interfaz de red y nombre del equipo.

import os

interface = input("Introduzca el nombre de su interfaz de red: ")

ipaddress = input("Introduzca su dirección IP: ")

mask = input("Introduzca la máscara: ")

gateway = input("Introduzca la puerta de enlace: ")

dns = input("Introduzca el servidor DNS: ")

os.system(f"netsh interface ipv4 set address name=\"{interface}\" static {ipaddress} {mask} {gateway}")

os.system(f"netsh interface ipv4 set dns name=\"{interface}\" source=static address={dns} primary")


nombrepc = input("Introduce un nombre de equipo: ")

os.system(f"netdom renamecomputer %COMPUTERNAME% /newname:{nombrepc}")
