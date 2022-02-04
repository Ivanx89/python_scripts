
alpha = input("Introduzca un número: ")


if str.isnumeric(alpha):
    alpha = int(alpha)
    if (alpha % 2) == 0:
        print(f"El número {alpha} es par")
    else:
        print(f"El número {alpha} es impar")
else:
    print("No ha introducido es un número")
