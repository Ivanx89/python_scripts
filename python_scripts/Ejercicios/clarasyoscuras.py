#Sin enunciado

try:
    alto, ancho = list(map(int,input().split()))
    suelo = alto * ancho
    negras = suelo // 2
    blancas = suelo - negras
    
    print(blancas, negras)

except ValueError:
    print("Hay algún dato no permitido")