

try:

    numero = int(input("Escribe un número entero positivo: "))

    if numero > 2:
        if numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")
    elif numero <= 2:
        print("No ha escrito un número mayor a 2.")

except ValueError:
    print("No ha introducido un número entero positivo.")




