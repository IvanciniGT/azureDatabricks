# En python podemos poner comentarios con el simbolo #
# Pueden aparecer al principio de una linea.. o al final

# Desgraciadamente en python no tenemos comentarios en bloque como existen en otros lenguajes de programación: como C

# Datos ... y tipos de datos:

# Tipos simples:
## Enteros
10
-10

## Reales
3.1416
-3.1416

## Cadenas de texto
"Hola mundo"
'Hola mundo'

# Cadenas de texto multilinea
"""
Esto es una cadena de texto
multilinea
"""

'''
Esto es otra cadena de texto
multilinea
'''

# Y nos aprovechamos de esto para poner comentarios en bloque

## Booleanos

True
False

# Tipos compuestos: Colecciones de datos

## Tupla

(1, 2, 3, 4, 5)

## Lista

[1, 2, 3, 4, 5]

# La tupla es un objeto inalterable... ni puedo añadir, ni quitar ni modificarle elementos
# Por contra la lista es un objeto mutable... puedo añadir, quitar y modificar elementos

############################################
# Variables

numero = 10
numero = 11
# Y además, como python es de tipado dinámico, es decir, las variables no tienen un tipo de dato asociado, puedo hacer cosas como:
numero = "Hola mundo"
numero = True

numero1 = 10
numero2 = 20
resultado = numero1 + numero2

############################################
# funciones: Nos permiten reestructurar nuestro código en bloques de código que podemos reutilizar
# Yo puedo definir mis propias funciones... y python tiene muchas funciones predefinidas

# Para llamar a una función, pongo su nombre y paréntesis detrás... 
# Si la función requiere argumentos, los pongo dentro de los paréntesis

# Función print: Imprime en la consola
print( "Hola mundo" )
print(resultado)

# Creacion de funciones propias
def saluda(): # Esta función ni recibe argumentos ni devuelve nada... tan solo hace un trabajo
    print("Hola mundo")

# Ejecutar la función
saluda()

# Función con argumentos
def genera_saludo(nombre): # Esta función recibe un dato y devuelve un dato
    return "Hola " + nombre

saludo_generado = genera_saludo("Pepe")

print(saludo_generado)

def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print(sumar(10, 20))

def imprimir_informe():
    print("Linea 1")
    print("Linea 2")
    print("Linea 3")
    print("Linea 4")

imprimir_informe()
imprimir_informe()
imprimir_informe()

# Operadores

## Operadores sobre números
1 + 1
1 - 1
2 * 2
10 / 3                                 # 3.33333333
2 ** 3 # Potencia
10 // 3 # División entera              # 3
10 % 3 # Resto de la división entera   # 1

## Operadores sobre cadenas de texto

"Hola " + "mundo" # "Hola mundo"
"Hola " * 10 # "Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola "

## Operadores sobre booleanos

True and True # True
True or False # True
not True # False

## Operadores relacionales: Trabajan sobre datos que no son booleanos y devuelven un booleano
2 == 2 # True 
2 != 2 # False
2 > 2 # False
2 < 2 # False
2 >= 2 # True
2 <= 2 # True

## Operadores para actualizar el valor de una variable (Operadores de asignación)
numero = 10
numero += 1
numero += 17
numero -= 10
numero *= 2
numero /= 3
numero //= 3

# Estructuras de control de flujo:

## Condicional: if

edad = 17 #int(input("Introduce tu edad: ")) # La función input, que lee de la consola, devuelve una cadena de texto
                                         # La función int convierte una cadena de texto en un número entero
                                         # Hay un monton de funciones de conversión de tipos en python: int, float, str, bool
                                         # bool("True") -> True

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print ("Estas en el límite")
elif edad == 17:
    print ("El año que viene te toca")
else:
    print("Eres menor de edad")

# Este es un tipo de condicional.. Un condicional controlado por las palabras if, else, elif usadas como un statement (sentencia)
# Hay otro tipo de condicional...  Un condicional como expresión ( es algo así como un operador ternario en otros lenguajes de programación)

resultado = "Eres mayor de edad" if edad > 18 else "Eres menor de edad"

# Bucles: while
# Es como un if... solo que el bloque de código se ejecuta mientras la condición sea verdadera... en lugar de una sola vez

cuenta = 10
while cuenta > 0:
    print(cuenta)
    cuenta -= 1
    #break
    #continue

# Bucles: for... realmente es un foreach... Itera sobre una coleccion de datos

personas = ["Pepe", "Juan", "Maria", "Ana"]
for persona in personas:
    print(persona)

personas = ("Pepe", "Juan", "Maria", "Ana")
for persona in personas:
    print(persona)

for i in range(100,10,-5): #(Desde, hasta, paso): (100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15)
    print(i)


## Programacion funcional

def generar_saludo_formal(nombre):
    return "Estimad@ " + nombre

def generar_saludo_informal(nombre):
    return "Hola " + nombre

saludo_generado = generar_saludo_formal("Pepe")

print(saludo_generado)
mi_variable = generar_saludo_formal # Mi variable ahora referencia a esa función
saludo_generado = mi_variable("Juan")

print(saludo_generado)

def imprimir_saludos(funcion_generadora_de_saludos, lista_nombres ):
    for nombre in lista_nombres:
        print(funcion_generadora_de_saludos(nombre))

imprimir_saludos(generar_saludo_formal, ["Pepe", "Juan", "Maria", "Ana"])
imprimir_saludos(generar_saludo_informal, ["Pepe", "Juan", "Maria", "Ana"])

# El propio python ya me ofrece funciones de este tipo... funciones que reciben funciones como argumentos.

# Función MAP... es una función que recibe una función... y una colección de datos... y genera como resultado 
# una nueva colección de datos... compuesta por el resultado de aplicar la función a cada uno de los elementos de la colección original

# Colección de partida      Función de mapeo    Colección de resultado
#       1                       *2                      2
#       2                                               4
#       3                                               6
#       4                                               8

numeros = [1, 2, 3, 4]

def doblar(numero):
    return numero * 2

dobles_numeros = map(doblar, numeros)
print(list(dobles_numeros))

def mapear(funcion, coleccion):
    listado_nuevo = [ funcion(dato) for dato in coleccion ]
    return listado_nuevo

dobles_numeros = mapear(doblar, numeros)
print(list(dobles_numeros))

# Esto está guay

# Apache Spark es una reimplementación del motor de procesamiento MAP-REDUCE que viene por defecto en Apache Hadoop
# En Apache Spark... lo que hacemos uso es de un paradigma de programación funcional... 
# basado en una nueva forma de escribir programas según un modelo MAP-REDUCE (iniciado por la gente de Google)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_impar(numero):
    return numero % 2 != 0

impares = filter(es_impar, numeros) # Apunta por ahí, que hay que filtrar los elementos de la colección, quedándote con los impares.
print(list(impares))


# EXPRESIONES LAMBDA
# De entrada las expresiones lambda son expresiones.

numero = 17; # statement: Sentencia/Enunciado/Oracion/Frase
numero = 17 + 5; # Otro statement
         ######  Expresión
         # Una expresión es un trozo de código que devuelve un valor

# Expresion lambda, es un trozo de código que devuelve un valor... qué valor?
# El valor que devuelve es una función anónima declarada dentro de la propia expresión.

def triplar(numero):
    return numero * 3

# Declaro una función, llamada triplar... que recibe un dato "numero" y devuelve "numero * 3"

referencia_a_nueva_funcion = lambda numero: numero * 3
# Es otra alternativa

# Las funciones, las usamos para:
# - Reutilizar código
# - Organizar código y hacerlo más legible
# - Para pasar código a una función (PROGRAMACION FUNCIONAL)

