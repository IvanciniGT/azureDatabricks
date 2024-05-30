
Apache Spark, lo que hace es esto...
Yo le doy una colección de datos, de partida [1,2,3,4,5,6,7,8]... y le digo que sobre esos datos quiero aplicar un filter (dándole una función de filtrado)... y un reduce (dándole una función de reducción)

Spark, toma esas anotaciones... y los datos... y los manda a una granja
En la granja, un maestro recibe los datos y las anotaciones... y reparte el trabajo entre los trabajadores
A un trabajador le mandará una parte de los datos... y las anotaciones ... y que curre...
A otro trabajador le mandará otra parte de los datos... y las anotaciones ... y que curre...
Y al final, cada uno de esos trabajadores acabará su parte... y el maestro recogerá los resultados... y los unirá... y me los devolverá

Los datos van a viajar por la red... y el código va a viajar por la red.
Ese proceso puede tener una penalización... pero si el trabajo es lo suficientemente grande... el gasto (tiempo) invertido en transporte compensa. Si el proceso es muy ligero... posiblemente no compense.

----

1M datos a procesar... y tengo 10 máquinas: 100k datos por máquina.. 1000 partes
Y si... una máquina se cae... pues no pasa nada... el maestro le manda la parte que le tocaba a otra máquina. Y ESTO ES CIERTO.
Pero... si la máquina iba por el dato 99.999... me jodo que ese trabajo lo he perdido.

---

> Tengo un diccionario con palabras en español

Me dan una palabra: "manana"
Y he de buscar las similares : Corrector ortográfico -> "manzana", "mañana", "ananá", "banana"

Distancia de levensthein:
Función que dadas 2 palabras calcula el número de caracteres que he de añadir, quitar o modificar para pasar de una palabra a la otra

Con una linea de código, puedo retornar el listado de palabras más similares, mediante un enfoque MAP-REDUCE

PALABRA OBJETIVO: "manana"
UMBRAL_DE_SIMILITUD: 2

Algoritmo de Levensthein: FUNCION(palabra1,palabra2)-> distancia (int)

            ---> MAP ---->                              ----> SORT   ----> TOMAR LAS 3 primeras (EXTRAER) REDUCE
manzana       distancia(palabra, palabra_objetivo)     ("manzana",1)           ("manzana",1)       "manzana"
albaricoque                                            ("albaricoque",5)       ("banana",1)        "banana"
banana                                                 ("banana",1)            ("mañana",1)        "mañana"
manzano                                                ("manzano",2)           ("manzano",2)       
mañana                                                 ("mañana",1)            
...
650000 palabras


```py

palabras_existentes = ("manzana", "banana", "mañana", "manzano", "albaricoque", ...)

def distancia(palabra1, palabra2):
    # Algoritmo de Levensthein
    return 3

palabras_existentes = filter(  lambda palabra: abs(len(palabra) - len("manana")) >= UMBRAL_DE_SIMILITUD    , palabras_existentes) # Filtrar por longitud
palabras_puntuadas = map(      lambda otra_palabra: ( otra_palabra, distancia(otra_palabra, "manana") )    , palabras_existentes) # Puntuar por distancia
palabras_puntuadas = filter(   lambda palabra_puntuada:  palabra_puntuada[1] <= UMBRAL_DE_SIMILITUD        , palabras_puntuadas)  # Filtrar por similitud
palabras_puntuadas.sort(       lambda palabra_puntuada: palabra_puntuada[1]) # Se ejecuta inplace                                 # Ordenar por similitud
palabras_mas_similares = map(  lambda palabra_puntuada: palabra_puntuada[0]                                , palabras_puntuadas)  # Extraer palabras

#nueva_coleccion= []
#for palabra in palabras_existentes:
#    if(similar_en_longitud(palabra)):
#        palabra_opuntuada = puntuar_palabra(palabra)
#        if(es_similar(palabra_opuntuada)):
#            nueva_coleccion.append(palabra_opuntuada)

```

La función que debo de pasar a la función MAP, debe ser una función que reciba solo UN PARAMETRO (cada valor de la coleeción suministrada al map)