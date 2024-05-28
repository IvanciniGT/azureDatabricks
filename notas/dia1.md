
# Qué es BigData?

## Ejemplo 1. Pincho  USB de 16 Gbs... recién sacado de la caja

Tengo un archivo de 5Gbs... puedo guardarlo en ese pincho? DEPENDE
Del sistema de archivos con el que tenga formateado el pincho: 
- FAT16: 2Gbs
En NTFS si podría... a no ser que quiera meter un archivos de 6Pb... el NTFS se hace caquita!!!

## Ejemplo 2: Voy a haver la compra al Mercadona.

- Tablita con 100 productos y la cantidad. Qué programa uso:EXCEL
- Y si tengo 300.000 datos? Excel se hace caquita!!!
- Siempre me quedará el MYSQL... y si tengo 10.000.000 de datos? Se hace caquita!!!
- Siempre tendremos el MS SQL Server.... y si tengo 1km de datos... El SQL Server... 
- No pasa nada... ORACLE Al rescate !
- Y si tengo 1b de datos... Y AHORA QUE???

## Ejemplo 3: Clash royale! 2v2

Cuando un movimiento , de mi teléfono en última instancia deben llegar 3 mensajes a los teléfonos de mis compañero/contrincantes. Lo normal es una media de 2 mov/segundo... = 6 mensajes
4 jugando = 24 mensajes/segundo
50k partidas = 1.200.000 mensajes/segundo

### Que hago entonces? en todos estos escenarios.

Cambio de enfoque: Adopto un enfoque BIGDATA (computación distribuida)
No voy a tener un MEGA-SERVIDOR = BARATO
Voy a trabajar con una granja de mierda-máquinas (commodity hardware), trabajando como si fueran 1 sola.

- Alto volumen de datos
- Complejidad de los datos
- Variedad de fuentes
- Velocidad de procesamiento
Cuando las opciones tradicionales no me sirven... he de optar por otro enfoque: BIG-DATA

Sea lo que sea que quiero hacer con los datos:
- Análisis de datos
- Almacenarlos
- Transmitirlos

La idea es usar la CPU, RAM y HDD de un montón de máquinas, como si fueran 1.

Y el primero que se mete en esta guerra es GOOGLE: BIG-TABLE. Para montar ese producto inventan algunas cosas.. y las comparten en un paper (2 papers):
- Un sistema de archivos distribuido: GFS (google file system... equivalente a FAT-16, NTFS, EXT4, ZSF)
    Donde un archivo se trocea en bloques... y esos bloques se almacenan en computadoras diferentes.
    - Me permite almacenar archivos de tamaño gigantesco
    - El rendimiento... Puedo escribir un archivo o leer un archivo de/hacia 200HDD simultáneamente
- Una forma nueva de plantear los algoritmos que trabajan con colecciones de datos: MAP-REDUCE
  - La gracia de esta forma de plantear un programa es que es fácilmente paralelizable / distribuible
  
Basado en los papers de Google, nace APACHE HADOOP. Qué nos da Apache Hadoop?
- Un sistema de archivos (basado en los diseños de Google): HDFS (Hadoop Distributed File System)
- Una implementación de MAP-REDUCE (Un motor de procesamiento de programas MAP-REDUCE) que permite paralelizar el trabajo usando granjas de máquinas.

Apache Hadoop es el equivalente a un sistema operativo para el mundo BIG-DATA.
Una de las principales funciones de un SO es :
- Controlar la CPU, RAM, HDD
- Determinar qué procesos hacen uso de esos recursos

GRANJA (CLUSTER) Hadoop:

    -+--------------+---------+---------------red
     |              |         |
     Maquina 1    Maquina 2   Maquina n
     (Hadoop*)    (Hadoop)    (Hadoop)
     MAESTRA

MAESTRA: La que recibe las peticiones de trabajo y las reparte entre las esclavas (workers).

CUIDADO: Cuando aplicamos MAP-REDUCE... lo que hacemos es repartir los datos sobre distintas máquinas... 
En todas ellas aplicamos el mismo trabajo sobre su parte de los datos.. Y al final CONSOLIDAMOS el resultado.

- Archivo de DNIs: 100.000 DNIs... Y he de validarlos                      ----> Apacha Hadoop / apache Spark
  Tengo 10 máquinas... reparto los 100.000 datos en 10 partes... y en cada máquina valido 10.000 DNIs
  Esto me da una forma de mejorar el rendimiento de mi programa... 
- En otros escenarios, este tipo de paralelización no es posible...        ----> Apache STORM
  Tengo que hacer 7 tareas sobre los datos que recibo...
    Y en una máquina hago la tarea 1 (sobre TODOS LOS DATOS) . 
    Su resultado lo paso a la máquina 2... que hace la tarea 2... y así sucesivamente.

Apache: Es una fundación que se dedica a desarrollar software libre... recibe donaciones de empresas y particulares. Fundamentalmente (y sobre todo para ciertos productos) de empresas grandes.

Hubo un problema... La implementación del motor de procesamiento MAP-REDUCE que se implementó en HADOOP es lenta de narices. Ya que cadas vez que un conjunto de datos se va a mandar a una máquina, primero se guarda en HDD (En serio??) SIP... y cada vez que recibe en un nodo de trabajo, se hace lo mismo (Se guarda en HDD)

Para resolver este problema, nace APACHE SPARK.
Apache Spark es una implementación ALTERNATIVA al motor de procesamiento MAP-REDUCE de Hadoop, que evita la persistencia en HDD de los datos intermedios.... utilizando solamente memoria RAM... y por ende mejorando un huevo y medio el rendimiento.

Apache Hadoop os comentaba que es como un SO para granjas de máquinas.... y básicamente me ofrece lo mismo que cualquier SO... na'
Para sacar partido a mi computadora, necesito instalarle programas de más valor: POWEBI, EXCEL, WORD

Eso mismo ocurre en el mundo BIGDATA... hay programas que pueden instalarse por encima de máquinas que tienen instalado Apache Hadoop...
- Guardar datos: BASES DE DATOS: 
  - HBASE: Base de datos NoSQL
  - HIVE: Base de datos SQL
  - CASSANDRA: Base de datos NoSQL
- Transmitir datos: 
  - APACHE KAFKA: Sistema de mensajería
- Transformar datos:
  - APACHE SPARK: Motor de procesamiento de datos
  - APACHE STORM: Motor de procesamiento de datos
- Análisis de datos:
  - Apache mahout: Machine learning
  - Apache Spark: Machine learning
- Ingesta de datos: 
  - SQOOP: Importar/exportar datos de bases de datos relacionales
  - FLUME: Ingesta de datos en tiempo real
  
## Preguntas:
- Si tengo 10 millones de datos... Me interesa más un Oracle / SQL Server para almacenarlos o esta parafernalia del mundo BIGDATA? A priori... un SQL Server... una BBDD tradicional
- Cuando cargáis datos, vosotros, trabajáis con ese volumen de datos.

Y al final tengo miles de millones de registros? NO... ni de coña!!!
Y pa' que entonces este fregao'.

...
PERO...

> Estoy con el juego del CLASH ROYALE.... que tengo que mandar un huevo de mensajes...
Qué servidor/es compro?
    1 servidor me da hasta para 100.000 mensajes por segundo.
    Pico de trabajo que hemos tenido es de 10m de mensajes por segundo: 100 servidores
    GUAY!!!!.. pero los voy a tener en uso 24x7? Ah.. no... Eso es para el pico... 2 veces al mes... que hay liga... el resto pues con 15-20 te sobran...

> Voy a hacer una carga de datos... por la noche... y voy a mandar ... npi de cuantos registros..
    
    Dia n: 10000 datos... y con un servidorcito de tipo A me apaño... en 1 hora
    Dia n+1: 1000000 datos... el servidorcito de tipo A se lleva 24 horas para procesarlo... no me vale...
    Ah no... pues entonces vamos a comprar mejor un servidor de tipo B... GUAY .. pastizal... para usarlo 1 vez al mes...

ESTA ES OTRA GRACIA... y posiblemente la mayor del ENFOQUE BIGDATA: FLEXIBILIDAD + CLOUD

# CLOUD?

El conjunto de todos los servicios que una empresa (en el mundo IT) ofrece de forma automatizada a través de Internet se demonina CLOUD. 
Tipos de servicios:
- Infraestructura   IaaS
- Plataforma        PaaS
- Software          SaaS

Esos servicios se ofrecen:
- De forma automatizada. No hay humano al otro lado
- De pago por uso: FLEXIBILIDAD ENORME

En el mundo de BIGDATA, al sumarle el concepto de CLOUD... obtengo una flexibilidad sin precedentes.

Mi programa siempre lo ejecuto en una granja que me da un cloud...
Cómo de grande? Lo que necesite en cada momento... o nada... si no estoy ejecutando nada!

# Qué es Apache Spark?

Es un framework de computación distribuida dentro de lo que llamamos el mundo BIG-DATA.
Es una implementación alternativa a MAP REDUCE con respecto a la que me ofrece Apache Hadoop.
Tenemos APIS (librerías para usar una granja de máquinas donde he montado Apache Spark) para crear programas usando:

- R (esto es menos habitual)
- PYTHON: Es un chorri-lenguaje creado para montar chorri-aplicaciones.
- SCALA
- JAVA

Con estos 4 lenguajes... trabajar con Spark... es duro de cojones!
La programación MAP-REDUCE es dura de cojones!!!

PERO... La gente de SPARK en un momento dado, se dio cuenta que poca genet tenía conocimiento/capacidad para montar algoritmos MAP-REDUCE. Lo que hicieron fue montar una librería adicional en Apache Spark: SQL.
Básicamente esa librería nos permite escribir sentencias SQL, y en automático convertirlas a un algoritmo MAP-REDUCE... que gestiona ya directamente Apache SPARK.
ESTO ES GUAY !!!!! y queremos aprenderlo... AUNQUE... No todo escenario lo podré resolver de esta forma.
Y cuando no pueda, me tocará rebajarme al barro... y trabajar con MAP-REDUCE

Al final... Apache Spark lo usamos para desarrollo de ETLs... en concreto la T de ETL...
Por cierto... entendiendo ETL con un concepto un poco más amplio:
ETL:
- E: Extraer
- T: Transformar
- L: Cargar
Pero... hay muchas varientes de SCRIPTS ETLs:
- ETL
- TEL
- ELT
- TELT
Y esas T... son crhorriprogramas. Un puñetero SCRIPT que coge unos datos... les aplica N transformaciones y pa'lante

# Qué es Databricks?

Es una plataforma cloud, basada en Spark (computación distribuida)
Databricks es una EMPRESA, que no es AZURE(Microsoft) ni AMAZON... Son independientes.
Pues resulta que son los creadores de Apache Spark... hay que sacarle pasta a esto.
os creadores de Apache Spark montaron una plataforma llamada Databriks... en colaboración con:
- Microsoft: AZURE
- Amazon: AWS


Lo que nos ofrece es una forma de:
- Crear clusters de máquinas con Apache Spark instalado, con un click... usando la infraestructura de AZURE o AWS
- Ese cluster se gestiona en automático... y se paga por uso:
- Mnto, instalaciones, actualizaciones, backups, apagados, inicios... todo en automático por el cloud =
    Me ahorro una pasta en Administradores de sistemas.

Además, me ofrecen:
- Un entorno de desarrollo colaborativo (JUPYTER NOTEBOOK)
- Integraciones con otros productos del cloud de marras: DataFactory, DataLake, DataBricks, PowerBI.

----
Apache Spark...está desarrollado con SCALA.
Es una sintaxis alternativa a la de JAVA (que es una mierda enorme)... pero la arquitectura del lenguaje es brutal. Es un lenguaje de tipado estático... que se compila e interpreta a la vez.. 
    .java   -compilación-> .class (bytecode) -interpretación-> JVM
    .scala  -compilación-> .class (bytecode) -interpretación-> JVM
    .kotlin -compilación-> .class (bytecode) -interpretación-> JVM

A efectos de los que os voy a contar... lo mismo me da scala, que java (o que python)

Pregunta... ¿qué tal gestiona JAVA la Memoria RAM? COMO EL CULO !!!!
JAVA es un lenguaje que come RAM que te cagas...
El mismo programa hecho en JAVA o en C, necesita 3/4 veces más RAM en JAVA. que si lo haces en C.
Eso es bueno o malo? ES UN FEATURE !!!
Fue parte de los criterios de diseño de JAVA: VAMOS A HACER UN LENGUAJE QUE DESTROCE LA RAM!

La cuestión es que gestionar la RAM es harto complejo... y de hecho hacer un programa que la gestione adecuadamente en lenguajes como C  o C++ es complicado.
El programa guay en C, me requiere 300 horas de tios/as a 70€/hora = 21.000€
El mismo programa en JAVA... me requiere 200 horas de tios/as a 50€/hora = 10.000€
Y comparo... en esta opción me ahorro: 11.000€
Cuánto me cuesta Más pastillas de RAM para el servidor? 3000€
Está claro!

En muchas oicasiones, la deción más barate, no necesariamente es la mejor desde el punto de vista técnicco.. ni de rendimiento.
----
# DEVOPS: es la cultura de la automatización.
----
- PYTHON
- PROGRAMACION FUNCIONAL: MAP-REDUCE se basa en el concepto de PROGRAMACION FUNCIONAL.
- MAP-REDUCE -> PYTHON
- APACHE SPARK... desde PYTHON
- APACHE SPARK... desde SQL
- Hablaremos acuerda de la arquitectura/diseño de Apache Spark/Apache Hadoop... ---> 
  - Buenas prácticas y escenarios de uso.
- Formatos de archivos: PARQUET, AVRO
- Empezaremos a meternos con caractarísticas propias de Databricks ... y de AZURE Databricks
---

# MARKDOWN

Es una sintaxis para escribir documentación.
Posteriormente podemos convertir esos documentos markdown en HTML, PDF, WORD...




---

> Quiero guardar un DNI de ESPAÑA en una BBDD... estructura???

- OPCIÓN 1: VARCHAR(9)...
Pregunta que me hago? Cuánto ocupa un VARCHAR(9) en un HDD
DEPENDE... del juego de caracteres que use: ASCII, UTF-8, UTF-16, UTF32, ISO-8859-1
Los caracteres de los DNI: (números y letras simplonas) : 1 byte por carácter: 9 bytes

- OPCIÓN 2: NUMERO (INTEGER- 4 bytes) + CHAR(1) (1 byte)
Integer 4 bytes: 
0000 0000: 2^8 = 256 posibles valores
2 bytes: 256x256 = 65536 posibles valores
4 bytes: 65536x65536 = 4.294.967.296 posibles valores
Con esta opción: 5 bytes
1 millón de DNIs: Ahorro 4 millones de bytes... 4Mb

- OPCIÓN 3: NUMERO (INTEGER- 4 bytes) paso de la letra.... Se genera desde el número... es una huella.
Si quiero primar almacenamiento, esta es mi opción.. eso si, en cada consulta necesito regenerarla.

Si trabajo con un fichero CSV, JSON.... TODO ES TEXTO:
- Edad de una persona
- Años que ha estudiado
- Número de hijos
TODAS ellas se guardan como texto... porque el formato solo permite guardar TEXTOS: CSV, JSON

>> El almacenamiento a dia de hoy es barato o caro?
Pero... sigue siendo lo más caro en un entorno de producción.
Para mi casa, me voy a mediamark que no soy tonto y compro un wester blue de 3Tbs.: 100€
Para la empresa elijo los Westerd red-pro o gold... que triplican precio... 300€

Pero... Cuántas copias se hace de un dato en un entorno de prod? mínimo 3
Y al final... para conseguir los 3Tbs.,.. necesito 9Tbs... pero de los caros.. 900€

Y los backups? 3Tbs.. les haré varios backups...Y al final.. esos 3Tbs en prod: 20Tbs de los caros... 2000€