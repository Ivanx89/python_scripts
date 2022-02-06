#Realizar un ping a la red mencionada.

import os
import sys

red = sys.argv[1]
message = "Host de destino inaccesible"

for i in range(1,255):
    ping = os.popen(f"ping -c 1 {red}.{i}").readlines()
    if message in str(ping):
         print(f"El host {i}, no está activo o hay algún fallo en la conexión.")
    else:
        print(f"El host {i} está activo")