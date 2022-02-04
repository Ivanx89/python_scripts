import sys

stdout = sys.stdout

with open('prova2.txt', 'w') as f:
    sys.stdout = f
    print("Hola al fichero')
    sys.stdout = stdout

print("Hola a pantalla")
