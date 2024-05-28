En markdown escribimos textos.
Si yo escribo dos lineas, como estas, tengo un único párrafo.. y al formatearse, ambas se ponen juntas...
Una a continuación de otra... Se separan por un espacio en blanco.

Esto ya sería otro párrafo.

# Título de primer nivel #########################
## Título de segundo nivel
###### Título de séptimo nivel

Esto es otro título (equivale a # )
====================================

Un subtítulo (equivale a ## )
-------------------------------

## Listas
### Listas no ordenadas:
- Elemento 1
  Esta es otra fase dentro de este apartado.

  Este es otro párrafo dentro del mismo elemento.
- Elemento 2
- Elemento 3

+ Elemento 1
+ Elemento 2
+ Elemento 3

* Elemento 1
* Elemento 2
* Elemento 3
  * Elemento 3.1
  * Elemento 3.2
    * Elemento 3.2.1 

Las buenas prácticas es:
- No mezclar caracteres dentro de un nivel de lista.
- Usar los distintos caracteres para los distintos niveles de lista.

- Item 1
- Item 2
    + Item 2.1
      * Item 2.1.1 
    + Item 2.2

### Listas ordenadas:

1. Elemento 1
1. Elemento 2
1. Elemento 3

1) Elemento 1
2) Elemento 2
   1) Elemento 2.1

# Formatos de texto:

- Resaltado:  *cursiva* o _cursiva_
- Enfatizado: **negrita** o __negrita__
- Ambos: ***negrita y cursiva*** o ___negrita y cursiva___
- Tachado: ~~tachado~~
- Operaciones matemáticas sintaxis latex
  $x^2 + y^2 = z^2$
- Código: `palabra reservada`

## Código en bloque:

```python
def hola_mundo():
    print("Hola mundo")
```

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

```mermaid
```

## Tablas

| Cabecera 1 | Cabecera 2 | Cabecera 3 |
|------------|-----------:|:----------:|
| valor 1    | valor 2    | valor 3    |
| valor 4    | valor 5    | valor 6    |
| valor 7    | valor 8    | valor 9    |

## Enlaces

[Texto del enlace](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)

## Imágenes
![](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)
