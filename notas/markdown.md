# Título del documento (nivel 1)

## Sección (nivel 2)

### Subsección (nivel 3)

#### Nivel 4

## Vista previa

Abrimos cualquier .md en VS Code y:

**Ctrl + Shift + V** (Cmd + Shift + V en macOS): abre la vista previa en una pestaña nueva.  
**Ctrl + K y después V**: abre la vista previa al lado, que se actualiza mientras escribimos. Es la forma más cómoda de trabajar.

## Párrafos y saltos de línea

Esto es un párrafo. Aunque lo escribamos
en dos líneas, se verá como una sola.

Una línea en blanco separa párrafos.

Es la regla que más sorprende: un salto de línea simple no se respeta; hace falta una línea en blanco para empezar un párrafo nuevo. Si necesitamos un salto de línea dentro de un párrafo, terminamos la línea con una barra invertida \ (o con dos espacios, que funcionan pero son invisibles; por eso en la sesión 3 configuramos VS Code para no borrarlos en Markdown).

## Énfasis

*cursiva*  
**negrita**  
***negrita y cursiva***  
~~tachado~~

Convención recomendada: asteriscos para todo. Y con moderación: si todo está en negrita, nada destaca.

## Listas

- Elemento
- Otro elemento
  - Elemento anidado (dos espacios de sangría)
  - Otro anidado

1. Primer paso
2. Segundo paso
3. Tercer paso

Las listas sin orden empiezan con - (también valen * o +; usamos siempre -).  
En las numeradas, Markdown renumera solo: podríamos escribir 1. en todas y se mostrarían 1, 2, 3.  
Deja una línea en blanco antes de la lista. Sin ella, algunas herramientas la pegan al párrafo anterior.  

## Listas de tareas (GFM)

- [x] Instalar Git
- [x] Publicar el portfolio
- [ ] Escribir el README

## Enlaces

[Documentación de pandas](https://pandas.pydata.org/docs/)  
Enlace externo: texto entre corchetes y URL entre paréntesis.

[Mi chuleta de terminal](notas/terminal.md)  
Enlace relativo: a otro archivo del repositorio, con una ruta relativa como las de la sesión 1. Funciona en GitHub y en VS Code, y sigue funcionando aunque se mueva o se renombre el repositorio. Es la forma correcta de enlazar archivos del propio proyecto.

[Ir a la sección de resultados](#resultados)  
Enlace a una sección: # y el título en minúsculas, con guiones en lugar de espacios y sin signos de puntuación (las tildes se mantienen: ## Instalación → #instalación). GitHub genera estos anclajes automáticamente para cada encabezado.

<https://github.com>  
URL entre < >: se muestra tal cual y es clicable.  

## Imágenes

![Gráfico de ventas por región](img/ventas_region.png)
Igual que un enlace, con ! delante. El texto entre corchetes es el texto alternativo: lo lee un lector de pantalla a una persona ciega y aparece si la imagen no carga. Escribimos qué muestra la imagen, no "imagen" ni "captura".

## Código

Para código dentro de una frase, comillas invertidas (backticks):  
Usamos la función `groupby()` sobre la columna `region`.

Para bloques de código, tres comillas invertidas antes y después, indicando el lenguaje para que se coloree:

```sql
SELECT region, SUM(importe) AS ventas
FROM pedidos
GROUP BY region;
```

Los lenguajes que usaremos: sql, python, bash, powershell, json, markdown. Nombres de columnas, tablas, archivos, funciones y comandos siempre en formato código: así se distinguen del texto y no se confunden con palabras normales.

## Tablas (GFM)

| Región    | Ventas(€)  | Variación |
|:----------|-----------:|:---------:|
| Madrid    |    125.300 |    +12 %  |
| Barcelona |     98.450 |     +8 %  |
| Valencia  |     54.120 |     -3 %  |

La primera fila son los encabezados; la segunda, obligatoria, separa encabezados y datos.  
Los dos puntos de la fila separadora controlan la alineación: :--- izquierda, ---: derecha (la adecuada para números), :---: centro.  
No hace falta alinear las barras verticales: es solo para que se lea mejor en texto plano. Esta tabla funcionaría igual:  

| Región | Ventas(€) | Variación |
|:--|--:|:-:|
| Madrid | 125.300 | +12 % |

## Citas

> Sin datos, solo eres otra persona con una opinión.  
> — W. Edwards Deming

Además de citas literales, en documentación se usan para destacar avisos, como hacemos en este manual.

## Separadores

---
Tres guiones en una línea (con una línea en blanco antes) dibujan una línea horizontal. En este manual separan las secciones.

## Escapar caracteres especiales

Si queremos mostrar un símbolo que Markdown interpretaría (un asterisco, una almohadilla al principio de línea), lo precedemos de una barra invertida:

El precio sube un 5 \* 2 = 10%.  
\# Esto no es un título

## Bloques desplegables

Para esconder contenido largo (una solución, un log de error) que el lector puede abrir si quiere.  
Markdown permite HTML dentro del texto. \<details> es el caso más útil. Conviene dejar líneas en blanco alrededor del contenido para que el Markdown interior se interprete.

<details>
<summary>Ver la solución</summary>

La consulta correcta es...  

</details>

## Notas al pie

El dataset procede del INE[^1].

[^1]: Instituto Nacional de Estadística, encuesta de 2024.
