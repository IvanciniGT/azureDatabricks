
- Tablas paralelo (24 en paralelo en lotes)
- En cada tabla hacéis paralelización  (SPARK)


24 tablas -> CLUSTER a procesar
Cada tabla se parte en trozos y esos trozos se mandan a nodos del cluster


24 tablas en paralelo, posiblemente no interesa que cada tabla además se procese en paralelo

JOINS
Necesito las tablas de cruce en todas las máquinas

9 tablas a la vez x historico = 18 tablas
TABLA x TABLA_HISTORICO
 ^
 Parto en 10 trozos porque tengo 10 cores
 Al mandarla a esos 10 nodos, la tabla histórico la tengo que mandar a los 10 nodos.

---

24 tablas: 20 tablas acaban en 1 min
4 tablas que se pasa 5 hora
TRATAR DE LANZAR DENTRO DE UN BATCH TABLAS DE TAMAÑO SIMILAR !
COLA y ejecutores

COLA en programación es una estructura de datos (lista, matriz, árbol), que sigue lo que llamamo un modelo FIFO (First In First Out), es decir, el primer elemento que entra es el primero en salir.

        COLA DE PROCESAMIENTO                         POOL DE EJECUTORES 24

    +--------------------------------------+            EJECUTOR 1 (CORE De un nodo del cluster de Spark) P1
    | P1                                   |            EJECUTOR 2 (CORE De un nodo del cluster de Spark) P2√ P4
    +--------------------------------------+            EJECUTOR 3 (CORE De un nodo del cluster de Spark) P3
---
Apache spark

1 trabajo que son 10 tareas (map +map+filter+map+orderby+map+reduce)... y tengo 1000 datos

    Divido los datos en 30 trozos y lanzo 10 trabajos en paralelo, que cada unbo hace las 10 tareas
    CORE1 (100 datos + 10 tareas)
    Nodo2 (100 datos + 10 tareas)
    ...
    Nodo10 (100 datos + 10 tareas)

Apache STORM
    
    Divide las tareas y no los datos
    Nodo1 (1000 datos + 1 tarea) -> Nodo2 (1000 datos + 1 tarea) -> Nodo3 (1000 datos + 1 tarea) -> Nodo4 (1000 datos + 1 tarea) -> Nodo5 (1000 datos + 1 tarea) -> Nodo6 (1000 datos + 1 tarea) -> Nodo7 (1000 datos + 1 tarea) -> Nodo8 (1000 datos + 1 tarea) -> Nodo9 (1000 datos + 1 tarea) -> Nodo10 (1000 datos + 1 tarea)

Los JOINS DE SPARK están pensados para hacer lookups (enriquecer datos) y no para hacer joins masivos

De hecho muy habitual con spark cuando hago joins es hacer un broadcast de la tabla de join para que esté en todos los nodos y se mantenga en memoria.

15m                            9m
ORIGEN (datos de un dia N)  -> HISTORICA (acumulado de cambios)
                            -> TABLA con todas las tablas de origen unidas (empalmadas) 2kM

15 trozos para mandarla a 15 trabajadores (CORE)
A cada core le mando 333k x 1 de datos de la tabla origen y en cada paquete de trabajo, mando la tabla 2
Y de la tabla histórica? ENTERA

---
Para qué particino -> PARALELIZAR 
Para qué paralelizo? Para usar al máximo las capacidades del HW (CPU/RAM) Vuestro cluster está ABURRIO !!!!
Si el cluster está aburrido:
- Le estoy mandando poco trabajo (lotes de 24)
- Que tenga un cuello de botella (CPU no limita, RAM no limita, PRESION DE DISCO, **COMUNICACIONES POR RED ENTRE NODOS**)