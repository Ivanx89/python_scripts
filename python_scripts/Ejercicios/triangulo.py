#Realizar un triangulo según la altura introducida.

altura = int(input("Introduce la altura del triángulo: "))

for i in range(altura):
    for j in range(i+1):
        print("*", end="")
    print("")
    