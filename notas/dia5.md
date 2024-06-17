
PROGRAMA Python
    Abrir conexión con un cluster de spark (nos lo regala Databricks)
    Le mandamos los datos al cluster... y las operaciones que debe hacer sobre los datos

    MI-PROGRAMA(1) ---> SPARK-CLUSTER (maestro) ----> SPARK-WORKER (esclavo) 
                                                    JVM Spark < hashtags_eliminados = 1
                                             ----> SPARK-WORKER (esclavo) 
                                                    JVM Spark < hashtags_eliminados = 2
                                             ----> SPARK-WORKER (esclavo)
                                                    JVM Spark < hashtags_eliminados = 1
                     JVM Spark                      
     ^                                              
     hashtags_eliminados = 0

    Capturamos el resultado... si es que lo hay, a nivel de este programa.

    Necesito una variable MUY ESPECIAL... que esté compartida entre todas las máquinas.
    Realmente eso no va a ser así... solo en apariencia

    Un ACCUMULATOR es una variable que existe SOLO a nivel de mi programa(1).
    Desde mi programa, yo puedo consultarla... y los workers pueden incrementarla.

    Un BROADCAST es una variable que existe a nivel de todas las máquinas trabajadoras.
    Pero ellas solo pueden consultarla... no modificarla.
    La relleno desde mi programa (1)
        Nos sirve para evitar continuos envíos de datos a las máquinas trabajadoras.

---

Vamos a partir de un fichero de Personas (JSON)

    ID; Nombre; Apellidos; Edad; DNI; CP

Vamos a querer validar los datos... y consolidarlos de alguna forma:

    Quiero solo los nombres (paso de los apellidos) y la suma de las edad por nombre

Eso en SQL qué tal sería?
    Si tuviera una tabla personas:
    
        SELECT Nombre, SUM(Edad) FROM personas GROUP BY Nombre

En Spark, tenemos una librería llamada spark-sql, que me permite escribir este tipo de sentencias SQL 
y que Spark las convierta a operaciones sobre RDDs (operaciones de tipo map-reduce de la libreria spark-core)

Problema!
Nos falta algo en esa query... Validar los datos
Qué valido? EL DNI
12345678T
12345.678-T
12.345.678-T
00001234T
1234 t

Además, quiero validar la letra del DNI

La letra del DNI es una huella del número.
Se saca de una función de Huella (HASH)
Una función HASH es una función que recibe un dato y:
- Me devuelve otro dato, de forma que:
  - A. Siempre se obtiene el mismo resultado para el mismo dato de partida
  - B. La probabilidad de obtener el mismo resultado para dos datos distintos de partida sea lo "suficientemente baja"
  - C. No se pueda obtener el dato de partida a partir del resultado (el dato resultado es un RESUMEN del dato de partida)
  
Para la letra del DNI, tomamos el número del DNI y lo dividimos entre 23. Pero no me quedo con el resultado de la división... sino con el RESTO

    23.000.012 | 23
               +-----------
            12   1.000.000
            **
            Esto es lo me interesa... ESE RESTO en nuestro caso estará entre [0-22]
    El ministerio del interior ofrece una tabla, donde a cada valor del resto 0-22 le asigna una letra.
    Que probabilidad hay de que 2 DNIs compartan letra? 1/24 = 4.16%

import re

letras_posibles="TRWAGMYFPDXBNJZSQVHLCKE"

def letra_correspondiente(numero_dni):
    return letras_posibles[numero_dni % 23]

def validar_dni(dni_como_texto):
    """                             VALIDACION                    -->   FORMATEO
    Me llegará algo como:       NUMERO          LETRA     VALIDO
        12345678T           ->  12345678        T           √           --> 12345678-T | 12345678T | 12345678 T | 12.345.678-T
        12345.678-T             12345678        T           x
        12.345.678 T            12345678        T           √
        00001234T               1234            T           x
        1234t                   1234            T           x
    """
    numero = None
    letra = None
    # Aplico una expresion regular
    valido = re.match(r'^[0-9]{1,8}[ -]?[a-zA-Z]$', dni_como_texto)
    if(valido):
        # Extraer la letra 
        letra = dni_como_texto[-1].upper()
        # Extraer el número
        dni_como_texto = dni_como_texto.replace(". -","") # Me como los espacios, puntos y guiones
        numero = int(dni_como_texto[:-1])
        # Validar la letra
        if letra_correspondiente(numero) != letra:
            valido = False
    return (valido, numero, letra)

def tratar_de_arreglar_el_dni(dni_como_texto):
    """
        Si me vienen puntos en mal sitio, lo ignoro...                          [^a-zA-Z0-9]
        Si me viene algun caracter que no sea letras o numeros... los ignoro
    """
    dni_como_texto = dni_como_texto.sub(r'[^a-zA-Z0-9]','',dni_como_texto)
    return validar_dni(dni_como_texto)

Una cosa es validar el DATO... y otra cosa es dejar el dato como a mi me interesa que esté. NO ME INTERESA ENFRENTARME A ESTE PROBLEMA DE UNA.
SON 2 PROBLEMAS DISTINTOS

    EXPRESIONES REGULARES
    ^[0-9]{1,8}[ -]?[a-zA-Z]$

Nunca programa contra los datos
Se programa contra requisitos


----


Las librerias, como tal, en python se distribuyen mediante un comando que se llama pip:


$ python -m pip install spark:1.0
---

```json
    {
        "nombre":"Juan",
        "apellidos":"García",
        "edad":25, 
        "dni": "23000000T", 
        "cp": "28001", 
        "email": "juan@garcia.es"
    },
    {"nombre":"Juan","apellidos":"Ruiz","edad":17, "dni": "23000023T", "cp": "28006", "email": "juan@ruiz.es"},
    {"nombre":"María","apellidos":"García","edad":43, "dni": "23000046T", "cp": "28006", "email": "maria@garcia.com"},
    {"nombre":"Menchu","apellidos":"Ruiz","edad":33, "dni": "23000002T", "cp": "28002", "email": "menchu@ruiz.net"}
```

UNION 
-> DISTINCT 
    -> ORDER BY

En la medida que pueda, debería limitar los joins en Spark a Simples lookups, de tablas con 4 datos (400)


Columna que ocupa 10 Mbs en una tabla... Su indice puede ocupar fácilmente 50Mbs... por los huecos

La gracia de tener un índice es que puedo aplicar un algoritmo de búsqueda binaria.
De hecho,... cuando hago (yo humano) esa búsqueda en un diccionario: ZAPATO. Abro el diccionario por la mitad? NO... por el final
Yo abro por el final porque en mi cabeza tengo la distribución de los datos (de las palabras)

Las BBDD también aprenden la distribución de los datos: ESTADISTICAS -> Para afinar el primer corte de la búsqueda binaria... igual que un humano.

El problema es que necesito datos ordenados para hacer esta búsqueda. Los índices son una copia preordenada de los datos.
Pero se dejan un montón de hueco entre medias de los datos.

ETL
E(SQL Server) -> Transformar -> Enriquecer -> L(Parquet)

E(SQL Server) -> Transformar -> L(Hive, Cassandra, SQL Server) -> Enriquecer 