
GIT
Diseño / Arquitectura Orientada a componentes desacoplados
DEVOPS / Pruebas / CI

ETLs MULTIPLES
ORQUESTACION de esas ETLs

---
# Situación actual

Un único REPO DE GIT donde están todos los cuadernos.
A partir de aquí ya se complica todo!
Problemas:
- Cuando quiere alguien hacer un paso... hay que avisar a todo el mundo: CUIDAO
  Dejad el proyecto "más o menos" estable: VAMOS A INTENTARLO porque no tenemos forma de saber si va a funcionar o no (PRUEBAS).

---
# Situación deseada

Queremos un repo de git para cada COMPONENTE... y tenemos MUCHOS componentes de MUCHOS TIPOS DISTINTOS.
- Funciones/Librerías que podríais reutilizar: DNI
- Funciones ETL: FUNCIONES QUE RECIBEN UNOS DATOS , LOS TRANSFORMAN Y GENERAN OTRO CONJUNTO DE DATOS
  - TRANSFORMACION: la transformación en si misma es una función.
    - ENTRADA, TRANSFOMACION, SALIDA 
        def historificar_tabla(nombre_tabla_actual, nombre_tabla_historificada):
            # Codigo que hace la historificación de una tabla
            pass
    En cuanto quiero hacer pruebas ya necesito trabajar con 2 conjuntos de datos: EL BUENO y el PRUEBA 
- CUADERNOS: Ya uso las funciones ETLs para trabajar con mis datos
   for(tabla_a_procesar in tablas_a_procesar):
       historificar_tabla(tabla_a_procesar, f'{tabla_a_procesar}_historica')

   historificar_tabla('tabla_prueba', 'tabla_prueba_historica')
- SCRIPTS DE ORQUETACION

---

# Cuando tengo repos distintos:
- El trabajar con ellos se vuelve mucho más sencillo:
  Tendré pocas ramas 
  Los cambios que haga en una no afectarán a otros repositorios
- Podemos empezar a automatizar trabajos (DEVOPS: CI/CD)
  - Todo esto empieza con tener pruebas AUTOMATIZADAS. PASO 1. Si no hay esto, no hay nada.
  - AZURE DEVOPS es un servidor de automatización de tareas (permite orquestar y automatizar la ejecución de trabajos)
    Pero no automatiza trabajos. 
    - Cuando alguien publique nuevo contenido en un repo (nuevo commit de una versión actualizada del proyecto):
      - Se lanzan las pruebas
      - Si las pruebas pasan, se despliega en un entorno de pruebas integrado
      - Si las pruebas pasan, se despliega en un entorno de producción

Python: UNIT TEST
    Esto es lo que se usa en python para hacer pruebas automáticas.

---

GIT:
    REPO 1: Librería para trabajar con DNIS
            Esa librería debe tener su propio conjunto de pruebas
            Y asociaré un flujo automatizado de tareas en ese repo.

            dev -> C1 -> C2 -> C3

            A lo largo de ese trabajo, cada vez que lo necesite ejecuto mi juego de pruebas automatizadas.
            Para ver qué tal voy!

            Cuando creo que el trabajo ya está listo -> main
            Asociado a esa tarea: Pasar un commit de la rama dev a la rama main,
            AZURE DEVOPS: 
                SE FUERZA LA EJECUCION DE LAS PRUEBAS (yo no me fío de lo que ha hecho el desarrollador , ni de mi mismo)
                Si va bien, entonces es cuando realmente el commit se pasa a la rama main
                Y en automático, genero un package (module) de python, que despliego en el cluster de databricks

            Microsoft ha deprecado tfs en favor de git. Una de las cosas más horribles que había en tfs, igual que en otros SCM era el bloqueo de archivos.
                TFS: 
                    Un sistema de control de versiones (SCM) 
                    Una app de gestión de proyectos: JIRA
                    Una herramienta de automatización de tareas
                TFS como herramienta de automatización de tareas se ha rebautizado como AZURE DEVOPS
                Pero como SCM se ha eliminado y se ha reemplazado por GIT
            
            En git es fundamental definir un claro flujo de trabajo... ese flujo de trabajo depende de:
            - El tipo de proyecto
            - El tamaño del proyecto
            - El número de personas que trabajan en el proyecto
  
            En umn caso como éste, el de la librería de los DNI, podemos optar por un flujo muy simple:

                main: Todo lo que está en main es apto para producción
                dev:  Donde estamos trabajando
                    Cuando esté listo en dev, lo paso a main
            
            Si tengo un proyecto pequeño (como es éste) y donde previsiblemente va a haber poca gente trabajando (hay poca probabilidad de que simultáneamente haya 2 personas trabajando en el mismo proyecto), puedo optar por un flujo de trabajo tan simple como este.

            Y en un momento dado puede ser que haya 2 personas... y lidiaré con ello. Me costará un poquito... a cambio uso el 99% del tiempo un flujo de trabajo sencillo.






---

# Cuaderno de databricks

En databricks me meten este concepto de los cuadernos. No es nada especifico de databricks... es un aherramienta llamada JUPYTER que llevamnos usando años en python. Y SON GUAY: para análisis de datos.
Me permiten meter código en bloques, ir viendo resultados... siendo capaces de ejecutar cada bloque de forma independiente.
Reuitilizar las salidas de un bloque en otro bloque.
E ir intercalando texto entre el código, con explicaciones de los hallazgos.

---

La gran diferencia de git con respecto a otros SCM es que git es un sistema de control de versiones DISTRIBUIDO.
Qué significa eso:
NO EXISTE EL CONCEPTO DE REPO CENTRAL, como existía en otros SCM: TFS, SVN, CVS
Cada persona tiene su propio repositorio de git, totalmente independiente del resto de repositorios que tengan el resto de compañeros.

    IvanPC
        miproyecto
            carpeta/
            REPO IVAN   
                dev: C1-> C2 -> CM1 -> CI1 -+------> CF
    
    Servidor que permita alojar REPOS REMOTOS (AZURE DEVOPS, GITHUB, GITLAB)
        REPO REMOTO
            dev: C1-> C2 -> CM1 -> CI1 -+------> CF                 AZURE DEVOPS : dev: C1-> C2 -> CM1 -> CI1 -> CF -> Monte en el cluster de Databricks

    MenchuPC
        miproyecto
            carpeta/
            REPO MENCHU
                remoto/dev: C1-> C2 -> CM1 -> CI1 -+------> CF
                                                    \    /
                dev:        C1-> C2 -> CM1 -> CM2 ----> CF
                Git me echará una mano a unir el código de Ivan con el de Menchu.
                Pero puede ser que ambos hayan tocado exactamente el mismo trozo de código... y git entonces NO TOMA LA DECISION 
                de cuál de los 2 cambios es el correcto. Eso lo tengo que hacer yo: CONFLICTO (que no es malo... es una situación que se da al trabajar)

Un commit de git es una copia completa de la carpeta del proyecto en un momento dado del tiempo (ESTO ES MENTIRA... pero de momento nos vale)
En git existe el concepto de REPO REMOTO... que no REPO CENTRAL
    En un REPO CENTRAL: cuando alguien quiere trabajar se bloquea el archivo... y nadie más puede trabajar en él.
    En git, yo trabajo en mi REPO local... no le afecta a nadie lo que hago!
    Para compartir lo que hago, subo RAMAS a un REPO REMOTO... o a otro o a 4 a la vez.
    En git puedo tener 10 repos remotos asociados a mi repo local.
    Los remotos se usan para compartir RAMAS entre personas.


---

Lo que acabo es con un montón de librerías, y funciones de ETL (T) que quiero controlar y que pueden evolucionar de forma INDEPENDIENTE EN EL TIEMPO.
Para resolver este problema uso una herramienta como GIT.
Pero la clave no está en GIT... si no en el problema real que quiero resolver.
Y necesito una herramienta, que me permita resolver ese problema... Y DEBERE usar esa herramienta de forma que me permita resolver el problema.

El tener un UNICO REPO no me resuelve el problema.
---
Tengo una ETL (cuaderno) en la que estoy haciendo unos cambios...
Pero en parallello tengo otra ETL (cuaderno) en la que también estoy haciendo cambios.
DA IGUAL QUE HAYA UNA O VARIAS PERSONAS en este sentido.

Cuando un cuaderno está listo y lo quiero pasar a producción... necesito haber acabado los cambios que estaba haciendo en el otro?
NO DEBERIA SER ASI.
    Si tengo en mi proyecto 2 cuadernos
    Y uno esta a medias, no puedo subir el otro.
        ES TODO UN PACK, un bloque. O SUBO TODO o no subo nada.
        Y ESTE ES EL PROBLEMA.
En git hay un tema que nos ayuda mucho con esto: SUBMODULOS
Puedo tener un repo cuyas carpetas apunten realmente otros repos.
Y tengo un repo de más alto nivel en la jerarquía que apunta a los repos de más bajo nivel.

Viene una persona nueva a trabajar en algo... y le doy acceso a ese algo!

La configuración de todo esto es más compleja... MUCHO MAS COMPLEJA.
La operativa va a ser trivial.... y sin dolores de cabeza.

---

CLUSTER EN DATABRICKS


WORKSPACE EN DATABRICKS
    shared---> REPO GIT
        cuaderno1 
        cuaderno2 
        cuaderno3 
    repos
        ivan ---> REPO GIT
            cuaderno1
            cuaderno2
            cuaderno3
        menchu ---> REPO GIT
            cuaderno1
            cuaderno2
            cuaderno3

--

WORKSPACE EN DATABRICKS
    shared---> REPO GIT principal
        cuaderno1 ---> REPO GIT (como submodulo del repo principal)
        cuaderno2 ---> REPO GIT (como submodulo del repo principal)
        cuaderno3 ---> REPO GIT (como submodulo del repo principal)
    repos
        ivan ---> REPO GIT principal 
            cuaderno1 ---> REPO GIT (como submodulo del repo principal)
            cuaderno2 ---> REPO GIT (como submodulo del repo principal) *
            cuaderno3 ---> REPO GIT(como submodulo del repo principal)
        menchu ---> REPO GIT principal
            cuaderno1 ---> REPO GIT (como submodulo del repo principal) *
            cuaderno2 ---> REPO GIT (como submodulo del repo principal)
            cuaderno3 ---> REPO GIT (como submodulo del repo principal)
        felipe 
            cuaderno3 ---> REPO GIT (como submodulo del repo principal)

Si teneis mucha gente externa, en la que teneis poca confianza podeis usar otro concepto que hay en azure devops (NO ES UN CONCEPTO DE GIT)
    Merge Request / Pull Request
        En este caso el procedimiento cambia un poco:
            Un externo lo que hace es FORKEAR UN REPO DE GIT
                Hacerse una copia completa del repo de AZUREDEVOPS asociada a su cuenta de azure devops
                    PROPIETARIO JEFE SUPREMO     Propietario: Felipe
                    ------------------------     ------------------------
                    REPO CUADERNO OFICIAL <----- REPO CUADERNO FORKEADO
                                                 Felipe hace sus cambios aquí
                                                 Y cuando cree que están listos, HACE UN PULL REQUEST (solicitud de fusión de cambios)
                    El jefe supremo recibe la solicitud de fusión de cambios
                    Y decide aprobarla, y que esos cambios vayan al repo oficial o no.
                    Eso implica más gestión (hay que hacer trabajos manuales (APROBACIONES)                                                 
                    pero de eso se trata precisamente de que haya un control de calidad en los cambios que se hacen en el proyecto.


Cuando hay un cambio
    - Trabajamos exactamente igual que antes
      - Voy a mi carpeta,
      - Voy a la subcarpeta del cuaderno que quiero cambiar
      - Y voy haciendo mis commits ahí. ( 1 o 20 los que hagan falta)
        - Pero la gracia es que al tenerlo como submodulos, los commits se hacen en el repo del cuaderno
      - Llega un momento en que tengo eso listo para producción... Y el último commit que tengo en ese cuaderno lo etiqueto como v1.1.0
      - Y acto seguido, en el repo principal, digo que ahora para el cuaderno1 quiero la versión v1.1.0 en lugar de la v1.0.0 que tenía antes.
      - Los cambios que se estén haciendo en otros submodulos no de despliegan, ni se toman aún en el repo principal.
