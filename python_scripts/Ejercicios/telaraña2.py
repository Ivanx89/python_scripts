import sys

try:
    peso = int(input("Peso: "))
except:
    print("El peso máximo tiene que ser de un entero positivo")
    sys.exit()

if peso > 0:
    l = input("Indica el peso de los elefantes: ").split()
    peso_total = 0
    n_elefantes = 0
    for p_e in l:
        try:
            p_e = int(p_e)
        except:
            print("Error: Los pesos de los elefantes tienen que ser enteros positivos")
            sys.exit()