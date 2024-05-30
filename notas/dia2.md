# Python

Lenguaje de programación.

## Tipado: Dinámico vs estático

Cualquier programa al final trabaja con datos. Y esos datos serán de un determinado tipo (naturaleza):
- Números enteros
- Números decimales
- Texto
- Fechas
- Valores lógicos (True/False)
  
```python
5.7 # Coloca en memoria un número decimal
```

En todo programa, utilizamos el concepto de variable.
NADA: Una variable es un espacio en memoria que almacena un valor = RUINA !!!!!

En estos lenguajes (js, python, java) una variable es una referencia a un dato que tengo en memoria RAM

```python
numero = 5.7
```
Cómo se ejecuta este código:
- 5.7       Coloca un dato de tipo float en memoria... con valor 5.7
- numero    Definimos una variable... llamada numero.
- =         Pegar el post-it al lado del valor en el cuaderno(RAM)
            Asigno la variable numero al valor 5.7

```python
numero = 10
```
- 10        Coloca un dato de tipo int en memoria... con valor 10
            Pregunta: En qué sitio de la RAM? en el mismo donde estaba el 5.7? NO... en otro sitio
            En este punto, tengo 2 datos en RAM: 5.7 y 10
- numero    Arranca el postit de donde estaba pegado
- =         Pegar el post-it al lado del nuevo valor (10)
            En este momento, el dato 5.7 queda huérfano de variables (no hay variable que le apunte)
            Y por ende.. ese dato es irrecuperable en python. Y entonces python lo marca como BASURA (GARBAGE)
            Y quizás (o no) en algún momento entre el recolector de basura (GARBAGE COLLECTOR) y lo elimina de la RAM... Pero es algo de lo que no tengo control.

En todos los lenguajes, los datos tienen una determinada naturaleza (tipo).
Algunos lenguajes me permiten (obligan) a definir un tipo de dato en las variables

```java
int numero = 10;
```
Ese int, lo aplico a la variable...La variable TIENE TAMBIÉN UN TIPO DE DATO. De forma que solo podre usar esa variable para apuntar a datos de ese tipo. TIPADO ESTATICO.
Otros lenguajes no.. como python... o js... TIPADO DINÁMICO, en los que las variables NO TIENEN TIPO.


## Lenguajes compilados vs interpretados

En el caso de python es un lenguaje interpretado.
El SO es el que última instancia se encarga de la ejecución de un programa.
Cada SO tiene su  propio lenguaje... SU API.
Es necesario traducir mi programa, del lenguaje que yo he elegido al lenguaje del SO.
- Compilación: traducción estática previa a la distribución del programa.
  - Ventajas:   Da lugar a programas que se ejecutan más rápido.
                Tenemos la oportunidad al hacer esa compilación de revisar el código.
  - Inconvenientes:
                Voy a necesitar traducir (compilar) mi programa a cada lenguaje (SO) de destino
- Interpretación: traducción dinámica en tiempo de ejecución.
  - Inconvenientes:   Da lugar a programas que se ejecutan más lento... requieren de traducción (interpretación) en tiempo real
                Perdemos la oportunidad por no hacer esa compilación de revisar el código.
  - Ventajas:
                Distribuyo el programa en mi lenguaje

También hemos dicho que python es el lenguaje del Machine learning... deep learning...
Las librerias que usamos en python para estos temas: pytorch, sklearn... numpy están montadas en C.
Lo único que hago desde python... es llamar a esas librerías y pasarles datos.

## Paradigmas que soportan

Un paradigma es una forma de usar el lenguaje para expresar un concepto.
- Imperativo            Lo que damos es una secuencia de instrucciones/órdenes que se ejecutan una tras otra.
                        En ocasiones me interesa/necesito romper esa secuencialidad... y usamos las típicas palabras de control de flujo (if, else, for, while)
- Procedural            Cuando el lenguaje me permite declarar funciones(métodos, procedimientos, subrutinas)... 
                        y ejecutarlas posteriormente.
                        Las funciones me permiten:
                        - Organizar mejor mi programa
                        - Reutilizar código: Ejecutar el mismo código en varios puntos del programa
- Funcional             Cuando el lenguaje me permite que una variable apunte a una función
                        Y posteriormente ejecutar la función desde la variable... decimos que el lenguaje soporta el paradigma funcional
                        La cuestión no es lo que es la programación funcional... sino lo que puedo hacer cuando se permiten estas operaciones en un lenguaje. Y AQUI ES DONDE LA CABEZA EXPLOTA !
                        Porque ahora que puedo hacer esto.. puedo comenzar a crear funciones que reciban funciones como argumentos...
                        O puedo crear funciones que retornen funciones como resultado...
- Orientado a objetos   Cuando el lenguaje me permite definir mis propios tipos de datos, con sus características... y su s operaciones

                    Lo caracteriza                  Operaciones
        String      Una cadena de caracteres        Ponte en mayúscula.. o minúscula
        Fecha       dia, mes, año                   Súmale 3 días, cae en bisiesto. Cae entre semana.
        DNI         Número, letra                   Comprueba si es válido, formatea
    
- Declarativo

En español... me pasa igual:

> Felipe, pon una silla debajo de la ventana.   (Imperativo)
> Felipe, debajo de la ventana tiene que haber una silla. (Declarativo)
---

# Programación Map-Reduce

> Quiero calcular los trending topis de un listado de tweets... leídos de un fichero
# En la playa con mis amigos #SummerLove#GoodVibes
# En la playa con mis otros amigos #MierdaDeVerano...#BadVibes
# En la cafetería de la uni #GoodVibes#MierdaDeClases

GoodVibes 2
SummerLove 1
MierdaDeVerano NO ESTE NO... 

> Tengo un diccionario con palabras en español

Me dan una palabra: "manana"
Y he de buscar las similares : Corrector ortográfico -> "manzana", "mañana", "ananá", "banana"

Distancia de levensthein:
Función que dadas 2 palabras calcula el número de caracteres que he de añadir, quitar o modificar para pasar de una palabra a la otra

Con una linea de código, puedo retornar el listado de palabras más similares, mediante un enfoque MAP-REDUCE

## MAP-REDUCE

Un algoritmo Map reduce se basa en aplicar sobre una colección de datos de partida funciones tipo MAP (n) para acabar siempre con una función tipo REDUCE

### Funciones tipo MAP

Son funciones que se aplican sobre una colección de datos... y devuelven otra colección de datos... Colecciones de datos que soporten programación funcional.
Las funciones tipo MAP se ejecutan en modo LAZY: PEREZOSO... es decir, realmente no se ejecutan hasta que no se requiere su resultado.
Hay muchas funciones tipo MAP:
- MAP... Recibe una función, que aplica sobre cada elemento de la colección de partida... generando una nueva colección de salida, donde cada dato es el resultado de aplicar la función suministrada sobre el correspondiente elemento de la colección de entrada.
- ORDER  Aplicada sobre una colección, devuelve otra colección ordenada según un criterio
- FILTER Aplicada sobre una colección, devuelve otra colección con los elementos para los que la función de filtrado suministrada devuelve True
- y otras 50

### Funciones tipo REDUCE

Son funciones que se aplican sobre una colección de datos... y devuelven algo que no es otra colección de datos que soporte programación funcional.
Las funciones tipo REDUCE se ejecutan en modo EAGER: ANSIOSO... es decir, se ejecutan en cuanto se les llama.
Hay muchas funciones de reducción:
- REDUCE... Recibe una función, que aplica sobre pares de datos... para ir reduciéndolos a un único dato final, que es el que devuelve
- SUM
- AVG
- COUNT
- ... y otras 50
De hecho, en un algoritmo implementado con un diseño MAP-REDUCE, acabamos siempre con una función tipo REDUCE... que hace efecto dominó... Es la función que fuerza la ejecución de todas las funciones tipo MAP.

    Pero este trabajo aún no se ejecuta
    (solo se ha anotado... pte de ejecución)
    -----------------------------------------
     -> Filter ->               RESULTADO    -----> REDUCE (potencial opción 1)... otra opción
    1               False  ---> 2                   a, b -> a+b
    2    es_par?    True        4                   2 \                         2 \ 8 \ 16  \ 20
    3               False       6                   4 / 6    \ 20               6 /   /     /
    4               True        8                   6 \      /                  8    /     /
    5               False                           8 / 14  /                   4         /
    6               True
    7               False
    8               True


Los reduce, se aplican como los playoffs... o la copa del rey... eliminatorias... hasta que solo queda uno.

El trabajar de esta forma, permite PARALELIZAR LOS TRABAJOS

Me da igual que los datos 1,2,3,4,5,6,7,8 se filtren en una máquina
O que una máquina filtre los datos 1,2,3,4 -> 2,4 -> REDUCE  -> 6  \ 20
   Y otra máquina filtre los datos 5,6,7,8 -> 6,8 -> REDUCE  -> 14 /
