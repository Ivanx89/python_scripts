


#Variables

nombre = input("Indica tu nombre: ")
sexo = input("Indica tu sexo [M/H]: ")


#Condiciones

if sexo == "M":
    if nombre.lower() < "m":
        grupo = "A"
        print("Perteneces al grupo " + grupo)
    else:
        grupo = "B"
        print("Perteneces al grupo " + grupo)
elif sexo == "H":
    if nombre.lower() > "n":
        grupo = "A"
        print("Perteneces al grupo " + grupo)
    else:
        grupo = "B"
        print("Perteneces al grupo " + grupo)
else:
    #Grupo
    print("Algun dato introducido no es correcto.")


