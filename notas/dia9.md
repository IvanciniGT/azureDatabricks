
DATABRICKS
    CLUSTER PRO
    CLUSTER DEV

    WORKSPACE
        shared <--- Clonado del repo de git         DATABRICKS
        repos
            carlos <--- Clonado del repo de git     DATABRICKS
            jorge  <--- Clonado del repo de git     DATABRICKS
            oscar  <--- Clonado del repo de git     DATABRICKS

---

DATABRICKS
    CLUSTER PRO
    CLUSTER DEV

    WORKSPACE
        shared <--- Clonado del repo de git 
        repos
            carlos <--- Clonado del repo de git 
            jorge  <--- Clonado del repo de git 
            oscar  <--- Clonado del repo de git 

---

AZURE DEVOPS
    REPO PRINCIPAL: Curso_spark
        Pipeline de despliegue
        etl_dnis
    REPOS ADICIONALES (de segundo nivel):
        library_dni_utils
            Pipeline de despliegue  ---> Deja ya instalada la librería en DATABRICKS (PRE/PRO)

---

AZURE DEVOPS
    REPO PRINCIPAL: DATABRICKS
        Dentro tiene todo en carpetas
        Asociado a ese repo tenéis un pipeline de despliegue

# ESCENARIO 1: Lo mio está listo para subir

---- main       C10
      ^         /
---- pre    --C10
      ^         \
---- dev        C10 ------------> C12 ----> C11
                  \            /         /
---- feature_jorge C10 -> C11-/--------+/
                    \        /
---- feature_fer    C10 -> C12

## Escenario 2: Lo mio no está listo aún, necesito cosas que ha hecho fernando

---- main       C10
      ^         /
---- pre    --C10
      ^         \
---- dev        C10 ------------> C12
                  \            /
---- feature_jorge C10 -> C11 /
                    \        /
---- feature_fer    C10 -> C12



---




---- main       C1                                          | * PROTEGIDA y SOLO AZURE DEVOPS TRAER COMMITS A ESTA RAMA
                 \                                           > RAMAS DE PROYECTO
---- dev          C1 --------> CJ1 ---------> CF1           | * PROTEGIDA y SOLO LOS GUAYS PUEDEN TRAER COMMITS A ESTA RAMA
                    \       /    \         /   *TAG 1.1.0
---- jorge          C1 -> CJ1     \       /
                      \            \     /
---- oscar             C1 -> CO1 ---> CF1

PROCEDIMIENTO DESPUES DEL CAMBIO DE JORGE:
1. En rama jorge merge de rama dev (para ver si hay algo nuevo en dev)
2. En rama dev merge de rama jorge (para llevar mis cambios a rama dev)

PROCEDIMIENTO DESPUES DEL CAMBIO DE OSCAR:
0. PULL de rama dev
1. En rama jorge merge de rama dev (para ver si hay algo nuevo en dev)
2. En rama dev merge de rama jorge (para llevar mis cambios a rama dev)