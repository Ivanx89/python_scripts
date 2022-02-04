#Escribir una función que pida un número entero y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.

n = int(input("Escribe un número del 1 al 10: "))

if n > 1 and n <= 10:
    with open(f"tabla-{n}.txt", 'w') as f:
        for i in range(1, 11):
            f.write(f"{n}X{i}={n*i} \n")
else:
    print("Introduzca un número del 1 al 10")
