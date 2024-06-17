
Hay 2 formas grande s de trabajar con Spark... Y SON MUY INDEPENDIENTES ENTRE SI

Core: RDD
SQL:  DataFrame <-> RDD[Row]
                <-> RDD[Persona] <-> DataFrame

---

COLECCION DE PARTIDA
---------------------
"Fiesta en la playa #BeachParty#SunFun#CacaSun, bronceado extremo!",
"#CaféEnLaMañana con un libro... #Relax pero mi café está frío :(",
"Noche de estudio (#StudyHard)#NoSleep, ¿quién inventó los exámenes?",
"#Running#FitnessGoals, corriendo bajo la lluvia... totalmente empapado",
"Pizza con amigos, #PizzaNight #Chill, pero ¿quién tomó mi trozo?",
"Perdido en la ciudad #CityLife#Lost pero descubriendo lugares nuevos",
"#GymTime#Workout, pero realmente odio las sentadillas" 

vvvv ??????

Para a una lista de tokens
"Fiesta","en","la","playa","#BeachParty","#SunFun","#CacaSun","bronceado","extremo",

PERO CONSOLIDAMOS LOS TOKENS EN UNA UNICA LISTA (flatMap)

["Fiesta","en","la","playa","#BeachParty","#SunFun","#CacaSun","bronceado","extremo",
"#CaféEnLaMañana","con","un","libro","...","#Relax","pero","mi","café","está","frío",":(",
"Noche","de","estudio","(#StudyHard)","#NoSleep",",","¿quién","inventó","los","exámenes","?",]

vvv
FILTRO (lo que empiece por #)

["#BeachParty","#SunFun","#CacaSun","#Sunfun","#sunFun","#SUNFUN","#StudyHard","#Running","#FitnessGoals","#PizzaNight","#Chill","#CityLife","#Lost","#GymTime","#Workout"]

vvvv

NORMALIZAR HASHTAGS -> map

vvvv
Me vale ya para algo el # ??? NO .... los quito: map

vvvv
[
    "beachparty",
    "sunfun",
    "cacasun",
    "sunfun",
    "sunfun",
    "sunfun",
]

Quitar palabras prohibidas (FILTER)
    No quiero mirar que el hashtag esté en la lista de palabras prohibidas...
    Que ninguna palabra prohibida aparezca en el hashtag

vvvv
[
    ("beachparty",1)
    ("sunfun",1)
    ("sunfun",1)
    ("sunfun",1)
    ("sunfun",1)
    ("sunfun",1)
]
reduceByKey (para aplicar esta función, necesito tener un key y un value)
[
    ("beachparty", 1)
    ("sunfun", 5)
]

vvvv
ORDENAR POR APARICIONES (SORT)
[
    ("sunfun", 5)
    ("beachparty", 1)
]
vvvv
Quedarme con los top ten!!!


COLECCION DE SALIDA
---------------------
CaféEnLaMañana 17
Chill 16
...
10 en total


split()

----

a   1
a   1
b   1
a   1
b   1
c   1

vvvvvv
a   [1] numero1
a   [1] numero2 -> [2] numero1
a   [1]                numero2 -> [3]
b   [1] numero1 -> [2]
b   [1] numero2
c   [1] 