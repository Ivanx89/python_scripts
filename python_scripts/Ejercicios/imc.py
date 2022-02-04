
#IMC = peso / altura^2


peso = float(input("Introduce tu peso: "))

altura = float(input("Introduce tu altura: "))

imc = round(float(peso / altura ** 2),2)

print(imc)