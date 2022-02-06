#Números hasta el indicado.

import sys


try:
    numero = int(input("Introduce un número entero positivo: "))
    if numero >=0:
        for i in range(1, numero + 1):
            if i % 2 != 0:
                print(i, end=", ")
    else:
        print("No ha escrito un número entero positivo")
except:
    print("No ha escrito ningún número")
