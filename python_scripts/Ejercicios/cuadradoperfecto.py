import math

try:
    x = 1
    numero = int(input("Introduce un número: "))
    n = int(math.sqrt(numero))

    if n * n == numero:
        print("Es un cuadrado perfecto")
    else:
        while x >= 1 and x <=2 ** 31:
            if n * n == numero:
                print(x)
                break
            else:
                y = numero * x
                k = int(math.sqrt(y))
                if k * k == y:
                    print(x)
                    break
            x += 1

except ValueError:
    print("No has escrito nungún número")