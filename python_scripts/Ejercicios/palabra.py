palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for i in vocales: 
    veces = 0
    for j in palabra: 
        if j == i:
            veces += 1
    print("La vocal " + i + " aparece " + str(veces) + " veces")