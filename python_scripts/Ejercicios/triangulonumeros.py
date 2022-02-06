#Realizar un triangulo según la altura introducida.

n = int(input("Introduce la altura del triángulo: "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")