# Práctica 1 — Extracción de metadatos y sinopsis con Playwright y BeautifulSoup

Construcción de un corpus de libros a partir de la información pública de
[Lectulandia](https://ww3.lectulandia.co/), para su uso posterior en actividades de
procesamiento de texto y en un recomendador de libros.

## Integrantes del grupo

* Josías Calabozo
* Sharo Giuntoli
* Ismael Darruiz
* Sebastián Di Carlo

## Categoría seleccionada

| | |
| :---- | :---- |
| **Categoría** | Los más comentados |
| **URL** | https://ww3.lectulandia.co/mas-comentados/ |
| **Criterio de recorrido** | Secuencial; la cantidad de páginas se lee del paginador |
| **Libros disponibles en la categoría** | 206 distintos (216 tarjetas en 9 páginas, ~10 repetidas) |
| **Libros extraídos** | 200 |

## Estructura del proyecto

```
README.md
requirements.txt          dependencias
.gitignore
src/
  scraper.py              programa de extracción
data/
  libros.csv              dataset final (único CSV de la entrega)
docs/
  diseno_extraccion.md    análisis previo (Parte 1)
  como_funciona.md        cómo funciona el scraper, explicado desde cero
```

> Si es la primera vez que ves un scraper, empezá por
> [docs/como_funciona.md](docs/como_funciona.md): explica qué hace cada herramienta, cómo se
> encontraron los selectores y por qué el código tiene la forma que tiene.

## Instalación

Requiere **Python 3.10 o superior** (probado con 3.11). El piso lo impone Playwright; si además
se instala la versión más reciente de pandas, el mínimo sube a 3.11.

```bash
# 1. Crear y activar un entorno virtual
py -3 -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux / macOS

# 2. Instalar las dependencias
pip install -r requirements.txt

# 3. Descargar el navegador que utiliza Playwright (~190 MB, una sola vez)
playwright install chromium
```

## Ejecución

```bash
python src/scraper.py
```

El programa abre Chromium sin mostrar la ventana, recorre el listado de la categoría,
visita cada ficha junto con las páginas de su autor y de su serie, y genera
`data/libros.csv` con los 200 libros y todos sus campos. No recibe parámetros.

Todo lo que informa por pantalla queda también en **`data/scraper.log`**, con la hora al
principio de cada línea. El archivo se abre en modo "agregar", así que una corrida reanudada
continúa el registro anterior en lugar de pisarlo, y cada una arranca con una línea separadora.
Sirve para revisar después qué libros fallaron o dónde se demoró. No se versiona.

La corrida completa demora alrededor de 20 minutos, por la pausa de 1 a 2 segundos que se
respeta entre peticiones.

### Reanudación

El avance se guarda cada 10 libros sobre el propio `data/libros.csv`. Si la ejecución se
corta, basta con volver a lanzar el mismo comando: el programa lee ese archivo y saltea los
libros que ya tiene. Para empezar de cero, borrar `data/libros.csv`.

## Campos del dataset

| Campo | Descripción |
| :---- | :---- |
| `titulo` | Título del libro |
| `autores` | Autor o autores, separados por `\|` |
| `generos` | Género o géneros, separados por `\|` |
| `serie` | Serie a la que pertenece, si corresponde |
| `num_serie` | Número de orden dentro de la serie |
| `sinopsis` | Texto completo de la sinopsis |
| `url_libro` | Dirección de la ficha |
| `categoria_origen` | Categoría de la que se obtuvo el libro |
| `fecha_extraccion` | Fecha y hora en que se leyó la ficha, en ISO (`2026-09-01T14:23:45`) |
| `portada` | URL de la imagen de portada |
| `cant_comentarios` | Cantidad de comentarios publicados |
| `otros_libros_autor` | Otros libros del autor |
| `libros_serie` | Otros libros de la serie |

Los campos ausentes se representan siempre como cadena vacía. El archivo se guarda en
UTF-8 con BOM, de modo que los acentos se vean correctamente también al abrirlo con Excel.

## Controles de calidad

Al terminar, el programa informa por pantalla el resultado de seis controles y devuelve un
código de salida distinto de cero si alguno falla:

| Control | Criterio |
| :---- | :---- |
| Sin duplicados | `url_libro` no se repite |
| Título presente | ningún `titulo` vacío |
| URL válida | todas empiezan con `https://ww3.lectulandia.co/book/` |
| Cobertura de sinopsis | más de la mitad tiene `sinopsis` |
| Texto limpio | sin espacios dobles ni saltos de línea |
| Cantidad obtenida | exactamente 200 libros |

El último control compara contra el objetivo y no contra el rango del enunciado, a propósito:
una corrida que pierde libros por un corte de red igual quedaría "entre 100 y 200" y pasaría
inadvertida. Si falla, basta con volver a ejecutar el programa, que retoma los faltantes.

## Principales dificultades encontradas

**El sitio devuelve páginas vacías con código 200 después de un centenar de peticiones.**
Fue el problema más difícil de detectar, porque no se manifiesta como un error. La primera
corrida completa terminó sin una sola excepción y con todos los controles en verde, pero el
dataset tenía 168 libros en lugar de 200: a partir del registro 101, de forma intermitente,
el servidor respondía `200` con una página sin contenido, y esos registros vacíos entraban
en silencio. El reintento original sólo actuaba ante excepciones, así que no los alcanzaba.
La solución fue detectar el fallo por el **resultado** en lugar de por la excepción: si la
ficha vuelve sin título, se espera bastante más de lo habitual (5 y 10 segundos) y se vuelve
a pedir. Además, al reanudar se descartan los registros sin título para que se soliciten
otra vez, en lugar de darlos por extraídos.

Vale la pena señalar que los controles mínimos no bastaron para detectarlo: el rango de
"entre 100 y 200 libros" se cumplía con 168. Conviene comparar siempre la cantidad obtenida
contra la cantidad **pedida**, y no sólo contra el rango.

**La primera página del listado no está numerada.** El paginador del sitio enlaza
`/mas-comentados/page/1`, pero esa URL responde con un `301` que redirige a
`/mas-comentados/`. Asumir el patrón `page/{n}` para todas las páginas funciona, pero
agrega una redirección innecesaria en cada corrida. El scraper construye la primera URL
sin sufijo.

**El div de la serie sólo existe si el libro pertenece a una serie.** En los libros sueltos
`#serie` directamente no está en el DOM, así que acceder a él sin comprobar antes cortaba
la ejecución. El número de orden, además, no está en el enlace sino en el rótulo
`<span class="tagTitle">Libro 4 de: </span>`, del que hay que extraerlo con una expresión
regular.

**Los libros del autor y de la serie no están en la ficha.** La única grilla de relacionados
que ofrece la página del libro es por género. Para completar esos dos campos hubo que
visitar `/autor/<slug>/` y `/serie/<slug>/`, con un caché por URL para no repetir peticiones
cuando varios libros comparten autor o serie.

**Los rótulos se mezclaban con los datos.** Autores y géneros conviven en su div con un
`<span class="tagTitle">` que contiene el texto "Autor: " o "Generos: ". Tomar el texto
completo del div arrastraba ese rótulo; hubo que seleccionar únicamente los
`<a class="dinSource">`.

**El tipo de `num_serie` se corrompía al reanudar.** Al releer el CSV parcial, pandas
infería la columna como numérica (mezcla de vacíos y números) y el `1` volvía al archivo
final como `1.0`. Se resolvió leyendo el parcial con `dtype=str`.

**El margen de la categoría es acotado.** "Los más comentados" tiene alrededor de 216 libros
en total, apenas por encima de los 200 propuestos, de modo que casi no hay reserva si
algunos registros se descartan en la validación.

## Alcance y uso responsable

Se extraen **únicamente metadatos y sinopsis públicas**. No se descargan libros ni archivos
EPUB, PDF u otros contenidos: los enlaces de descarga de la ficha se ignoran por completo.
Se respeta una pausa entre peticiones y se evita la concurrencia, para mantener una carga
baja sobre el servidor. El dataset se destina exclusivamente a fines académicos.
