
def sumar(numero1, numero2):
     # Si existe una variable global con el mismo nombre, se puede modificar su valor o acceder a ella
                     # Si no existe, se crea una variable global con ese nombre
    global resultado
    resultado = numero1 + numero2


sumar(5, 7)

print("Resultado:", resultado)