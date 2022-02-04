

dni = int(input("Escriba su dni sin letra: "))

letra = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E",]

resto = (dni % 23)

print(f"Tu DNI sería {dni}{letra[resto]}")