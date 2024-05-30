
# Quiero calcular los trending topis de un listado de tweets... leídos de un fichero
# En la playa con mis amigos #SummerLove#GoodVibes
# En la playa con mis otros amigos #MierdaDeVerano...#BadVibes
# En la cafetería de la uni #GoodVibes#MierdaDeClases

# GoodVibes 2
# SummerLove 1
# MierdaDeVerano NO ESTE NO... 

import random # Esta librería viene de serie con python... y me da funciones para generar números aleatorios

NUMERO_DARDOS_TOTALES = 100 * 1000 * 1000
numero_dardos_circulo = 0

for numero_de_dardo in range(0,NUMERO_DARDOS_TOTALES):
    # Tiro dardo
    x = random.random() # Me da un aleatorio equiprobable entre 0 y 1
    y = random.random() # Me da un aleatorio equiprobable entre 0 y 1
    # Calculo distancia(al cuadrado) al centro de la diana
    d = x*x + y*y # x
    # Miro si ha caido dentro
    if d <= 1:
        numero_dardos_circulo += 1

# Calculo PI
PI = 4 * numero_dardos_circulo / NUMERO_DARDOS_TOTALES
print(PI)