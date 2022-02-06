#Mostrar resultado de un .txt del ejercicio tabladen.py


n = input("Introduzca un número: ")


try:
    f = open(f'tabla-{n}.txt', 'r')

except FileNotFoundError:
    print(f"No existe el fichero tabla-{n}.txt")
else:
    for l in f:
        print(l)
    f.close()
