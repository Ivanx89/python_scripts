

# NO FUNCIONA

import sys


try:
    numero = int(input("Introduce un número entero positivo: "))
    if numero >=0:
        for i in range(numero, -1, -1):
            if i == 0:
                print(i)
            else:
                print(i, end=", ")
    else:
        print("No ha escrito un número entero positivo")
except:
    print("No ha escrito ningún número")
