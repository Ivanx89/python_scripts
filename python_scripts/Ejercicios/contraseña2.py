#Verificación de contraseña en bucle.
pwd  = "contraseña"



correcto = False;
#Check

while correcto == False:
    pwdv = input("Escriba la contraseña:")
    if pwdv == pwd:
        correcto = True;
    else:
        print("La contraseña no es correcta")
print("La contraseña es correcta")