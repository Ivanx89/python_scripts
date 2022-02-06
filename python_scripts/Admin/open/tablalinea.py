#Leer la línea especificada de un fichero resultante de tabladen.py


n = input("Introduzca un número: ")
m = int(input("Escribe el nº de línea: "))
j = 0
try:
    f = open(f'tabla-{n}.txt', 'r')

except FileNotFoundError:
    print(f"No existe el fichero tabla-{n}.txt")
else:
    for l in f:
        j = j + 1 
        if j == m:
            print(l)
    f.close()


