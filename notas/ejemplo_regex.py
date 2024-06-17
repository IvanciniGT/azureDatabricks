import re

texto = "#hola mio,amigo #federico#lucas que nooooo!!!!"
texto = texto.replace("#", " #")
salida = re.split(r'[ ,.;:()=!¿?_-]', texto) 
print(salida)

lista = (1,2,3,4,5,6,7,8,9,10)
print(lista[3])
print(lista[3:7])
print(lista[3:7:2])
print(lista[3:])
print(lista[:7])
print(lista[-1])
print(lista[-3])
print(lista[-3:])
print(lista[3:-3])
# Y esto mismo, lo puedo aplicar a textos.. ya que en python, los textos son listas de caracteres

texto = "Hola mundo"
print(texto[3])
print(texto[3:7])
print(texto[3:7:2])
print(texto[3:])
print(texto[:7])
print(texto[-1])
print(texto[-3])
print(texto[-3:])
print(texto[3:-3])