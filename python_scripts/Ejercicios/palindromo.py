

palabra = input("Introduce una palabra: ")

palabra_inversa = palabra

palabra = list(palabra)

palabra_inversa = list(palabra_inversa)

palabra_inversa.reverse()


if palabra == palabra_inversa:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")