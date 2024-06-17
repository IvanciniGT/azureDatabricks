
--- pro         ---> Producción                                 PRODUCCION
            ^^^
--- pre         ---> Pruebo es la integración (ORQUESTACION)    PREPRODUCCION
            ^^^                                                     TEST, Q&A, INTEGRACION
--- dev         ---> Pruebo cada Notebook                       DESARROLLO
    -- featureN

Flujos grandes en DATABRICKS
Montón de cuadernos.
Cada cuaderno es un proyecto de GIT o todo está en un proyecto?


GIT Sub-módulos
REPO PRINCIPAL
    -carpeta1 -> OTRO REPO
    -carpeta2 -> OTRO REPO
    -carpeta3 -> OTRO REPO

Nos falta definir / establecer un Flujo de trabajo en GIT <<< CRITICO

Lo que montamos son SCRIPT
---

PIPELINES que ejecuto diariamente: ETLs
    SCRIPTS DE ORQUESTACIÓN
        Muchos cuadernos: SCRIPTS

Cada script puede evolucionar en el tiempo... de forma independiente a otros scripts.
    CUADERNO                                                                 CUADERNO

Necesito controlar versiones a nivel de CADA CUADERNO
    - Ingesta de datos desde una TABLA
    - Programa que determina que TABLAS son las que he de ingestar
    - Genera una tabla histórica (delta) 

Parece que tiene sentido NO USAR UN UNICO REPO DE GIT
    - Cada cuaderno es un proyecto de GIT que va generando versiones del CUADERNO / SCRIPT
        v.1.0.0
            -> v.1.0.1 

PROGRAMA DE ORQUESTACION: v2.0.0
    - Ingesta de datos desde una TABLA  v1.0.0
    - Programa que determina que TABLAS son las que he de ingestar v1.3.0
    - Genera una tabla histórica (delta)  v1.2.0

---
## OPCION ACTUAL
MONOLITO        <<<   Metodologías de trabajo tradicionales (WATERFALL)
    - Un único repositorio
    - Un único proyecto
    - Y cuando paso o paso todo o no paso nada
  
## OPCION DESEADA
COMPONENTES DESACOPLADOS     <<<<<   Metodologías de trabajo modernas (AGILE)
    - Cada componente tiene su propio repositorio
    - Cada componente tiene su propio ciclo de vida
    - Cada componente tiene su propia versión
+ INTEGRACION / ORQUESTACION
    - Un único repositorio
      - Dentro apunta a cada uno de los repositorios de los componentes
    - Un único proyecto
    - Y cuando paso o paso todo o no paso nada

Me gustaría que una persona pueda hacer un cambio en un cuaderno (nuevo requisito, arreglo de un bug) y que no tenga que esperar a que se aprueben los cambios de otros cuadernos.

----

DEVOPS <- AZURE DEVOPS PROGRAMITA QUE TOMA LA DECISION

Cultura, movimiento, filosofía en pro de AUTOMATIZACION
- Integración Continua
  Quiero tener continuamente en el entorno de integración lo último que han ido haciendo 
  los desarrolladores, sometido a pruebas automáticas.
- Entrega Continua  : CD: Continuous Delivery
  Quiero poner en la mano de mi cliente la última versión probada de mi software.
- Despliegue continuo : CD: Continuous Deployment
  Quiero que mi software se despliegue automáticamente en producción, desde la última versión probada.

Parte siempre de un REPO DE GIT ! << O ESTO ESTA MUY GUAY o no hay NADA QUE HACER !

MLOPS

---

Quién dice que el producto está OK? Nunca el cliente
El cumplimiento de un requerimiento: ¿quién lo dice? LAS PRUEBAS


---

# Gestión del ciclo de vida de un cuaderno

Ese cuaderno tiene versiones:
v.1.2.3
            ¿Cuándo suben?
1 MAJOR     Breaking changes: Cambios que no respetan RETRO-COMPATIBILIDAD
2 MINOR     Nueva funcionalidad
            Una funcionalidad se marca como obsoleta (pnte. de eliminación-deprecated)
3 PATCH     Arreglo de bug


## RAMAS en git

pro:
- Todo lo que hay aquí se considera apto para producción.
- En la vida hago un commit en esta rama.
    ^^^ AZURE DEVOPS
pre:
- Hago pruebas de sistema en su conjunto
    ^^^ AZURE DEVOPS
dev:
- Aquí es donde hago commits, hasta tener una versión que considero LISTA: Release Candidate

---

- Los cuadernos son responsabilidad de 1 persona o de varias?
- En un momento dado del tiempo trabajo en varias features en paralelo o no, que voy a querer subir de forma independiente a producción?
  
pro               C2 (v1.0.0)       C5
                 / auto (SE        /        REQUIEREN LAS PRUEBAS DE SISTEMA)
pre             C2 (v1.0.0-RC1)  C5
               /   auto         /
dev -> C1 -> C2 ------------> C5 --------> C6
              \             /   \       /
requisito1     C2 -> C3 -> C5    \     /
                \                 \   /
requisito2       C2 -> C4 ---------> C6


pro               C2 (v1.0.0)   
                 / auto     
pre             C2 (v1.0.0-RC1) 
               /   auto         
dev -> C1 -> C2 ---> C3(R1-70%) -> C4(R1-70%+R2 acabao)


---

# Qué es un commit?

- Un commit es una copia del estado del proyecto en un momento dado. COPIA DE SEGURIDAD

---

## Para qué creo commits y uso git?

Puedo crear commit para muchas cosas:
- Tener un histórico del proyecto... pero 
  - Para qué quiero un histórico? 
    - Para poder dar marcha atrás en un momento dado.                   git checkout <commit>
    - Para añadir una funcionalidad que quitamos en un momento dado.    git cherry-pick <commit>
    - Para buscar en qué momento o qué persona introdujo un bug.        git blame <archivo>
                                                                        git bisect   
Y en este sentido trato de dejar un histórico de commits limpio.
Y para ello no genero commits por generarlos.
    Estoy trabajando... y lo tengo a medias... NO GENERO COMMIT !
    He terminado una funcionalidad... GENERO COMMIT ! -> Para compartirlo con el resto del equipo
                                                         Para compartirlo con el AZURE DEVOPS (de turno)
                                                         y que pase a producción
Y si estamos trabajando 2 en algo?
Si quiero ir generando un commit, para que mi compi pueda ver lo que llego y seguir a partir de ahí...
o usar lo que estoy haciendo en su desarrollo.

# REFACTORIZACION DE CODIGO

Tengo ya el código listo y PROBADO ! Y funciona GUAY
Como ya sabemos este no era el problema. El problema es que en cuantito suba lo que hecho a producción, la empresa contrae una hipoteca con mi código.
Desde este momento ese código hay que mantenerlo, arreglarlo, evolucionarlo, etc. PROBLEMON !!!!
La refactorización es cuando todo esta PROBADO, dedicarle un rato extra para dejar ese código de forma que sea más fácil de mantener en el futuro.

Si estoy trabajando:
- Tengo listo -> Commit
- Quiero un commit porque me voy a poner a reorganizar todo el código.. y con alta probabilidad la cagaré
- Y quiero en ese momento poder volver atrás y tener un punto de partida.
Y en este caso genero un commit para tener una COPIA DE SEGURAR (punto de restauración) no porque quiera compartirlo.
En estos caso, lo ideal y que esos tipos de commits los creen en sus ramas


---

# LIBRERIAS PYTHON PROPIAS
- Genero un proyecto independiente en GIT
    proyecto/
        libreria/
            __init__.py
            modulo1.py
        setup.py (nombre: libreria + version)
        README.md
- Ejecuto: python setup.py sdist bdist_wheel (genera un archivo .whl)
- En el cluster en shared clono el repo de la librería
- En el cluster> librerias > cargar archivo .whl

Lo guay de nuevo es AUTOMATIZAR TRABAJOS = AZURE DEVOPS
Le pido a azure devops que cuando haya un nuevo commit en la rama pro/master/main (como la quiera haber llamado) de mi repo de la libreria, en auto:
- Genera el .whl
- Y por otro lado, creo lo que llamamos un init script en el cluster de databricks que se encarga de:
- Al arrancar el cluster:
    - Clonar el repo de la librería
    - Instalar la ultima versión que exista

# DEL ENTORNO DE PRO 
1 M                               100k   1k
DATOS -> FILTRADOS Y LIMPIADOS -> PRE -> DEV
Y de vez en cuando o a petición regenerar entorno de PRE y DEV
AUTOMATIZADO

# AUTOMATIZAR LAS PRUEBAS

# AUTOMATIZAR PASOS: DEV-> PRE -> PRO

# REPOSITORIOs para LIBRERIAS PROPIAS
Automatizar la generación de la librería
Y la instalación de la librería en el cluster