#Insertar frases en un fichero

import sys

with open('prova2.txt', 'w') as f:
    s = input("Escribe una frase (enter para acabar)")
    while (len(s) > 0):
            f.write(s + "\n")
            s=input("Escribe una frase (enter para acabar)")
