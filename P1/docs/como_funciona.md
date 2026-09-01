# Cómo funciona el scraper

Guía para entender el programa sin haber hecho web scraping antes. Explica las ideas
y el recorrido; los selectores concretos están en [diseno_extraccion.md](diseno_extraccion.md).

---

## 1. La idea de fondo

Un sitio web le manda al navegador un archivo de texto llamado **HTML**, que describe la página:
qué es un título, qué es un enlace, qué es un párrafo. El navegador lo interpreta y dibuja lo que
vemos. Hacer *scraping* es saltearse la parte visual: pedir ese mismo HTML y leerlo con un
programa para quedarnos con los datos.

No hay nada mágico. La dificultad real es que el HTML está pensado para dibujar una página, no
para entregar datos ordenados, así que hay que ir a buscar cada dato donde el sitio lo puso.

## 2. Por qué dos herramientas

| Herramienta | Se ocupa de |
| :---- | :---- |
| **Playwright** | Abrir un navegador de verdad y traer el HTML de una dirección |
| **BeautifulSoup** | Leer ese HTML y encontrar los datos adentro |

La división es estricta: **Playwright navega, BeautifulSoup lee**. Playwright nunca busca datos y
BeautifulSoup nunca pide páginas.

¿Por qué un navegador entero y no una simple descarga? Porque muchos sitios arman parte de su
contenido con JavaScript *después* de entregar el HTML inicial. Una descarga simple se quedaría
con la página a medio construir; un navegador real ejecuta ese JavaScript y entrega la página ya
terminada. En el programa, Chromium se abre en modo *headless*, que significa sin ventana: hace
todo lo que haría un navegador, pero sin mostrarse.

## 3. Cómo se le pide un dato al HTML

Con un **selector CSS**: una cadena corta que describe *dónde* está algo. Los que usamos:

| Selector | Quiere decir |
| :---- | :---- |
| `#title` | el elemento cuyo `id` es `title` |
| `.card` | los elementos cuya `class` es `card` |
| `#title h1` | el `<h1>` que esté adentro de `#title` |
| `article.card h2 a.title` | el `<a class="title">` dentro de un `<h2>` dentro de `<article class="card">` |

BeautifulSoup ofrece dos maneras de usarlos, y la diferencia importa:

- `soup.select_one(sel)` → **un** resultado, o `None` si no encuentra nada.
- `soup.select(sel)` → una **lista**, vacía si no encuentra nada.

Ese `None` es la causa de la mayoría de los errores al empezar: si se pide el título de una serie
en un libro que no pertenece a ninguna, `select_one` devuelve `None` y el programa se cae. Por eso
en el código todo el texto se pide a través de `texto_de()`, que devuelve cadena vacía cuando el
nodo no existe.

### De dónde salieron los selectores

No se adivinan: se leen del sitio. En el navegador, clic derecho sobre el dato → **Inspeccionar**.
Se abre el HTML posicionado en ese elemento, y ahí se ve su `id` o su `class`. Por ejemplo, al
inspeccionar el título de un libro aparece `<div id="title"><h1>La chica del tren</h1></div>`, de
donde sale el selector `#title h1`.

## 4. Las páginas del sitio

El programa trabaja con tres tipos de página, y conviene tenerlos claros:

**El listado** (`/mas-comentados/`, `/mas-comentados/page/2`, …). Muestra 24 tarjetas por página.
De acá sacamos **sólo las direcciones** de los libros, porque la tarjeta muestra la sinopsis
cortada (termina en `[…]`).

**La ficha de cada libro** (`/book/la-chica-del-tren/`). Acá está casi todo: título, autores,
géneros, serie, sinopsis completa, portada y cantidad de comentarios.

**Las páginas de autor y de serie** (`/autor/…`, `/serie/…`). Hacen falta porque dos campos que
pedimos —los otros libros del autor y los de la serie— no están en la ficha: lo único que la ficha
ofrece como relacionados es una grilla por género.

## 5. El recorrido del programa

```
main()
 └─ cargar_previos()      ¿ya hay libros de una corrida anterior? se saltean
 └─ recolectar_urls()     recorre el listado y junta 200 direcciones
 │    └─ paginas_del_listado()   cuántas páginas hay, leído del paginador
 └─ para cada dirección:
      └─ extraer_libro()  abre la ficha y saca todos los campos
      │    └─ titulos_del_indice()   visita las páginas de autor y de serie
      └─ guardar()        cada 10 libros, escribe el CSV
 └─ controles()           verifica el resultado
```

Todo pasa por una sola función para pedir páginas, **`pedir()`**, que hace las tres cosas juntas:
navega con Playwright, parsea con BeautifulSoup y reintenta si algo sale mal. Si después de los
reintentos no lo logra, devuelve `None` y quien la llamó decide qué hacer. Por eso casi no hay
bloques `try/except` desperdigados.

## 6. Los dos problemas reales que aparecieron

Vale la pena conocerlos porque explican por qué el código tiene partes que, de otro modo,
parecerían de más.

### El sitio devuelve páginas vacías sin avisar

Pasadas unas cien peticiones, el servidor empieza a responder con código **200 (todo bien)** pero
una página **sin contenido**. Como no hay ningún error, un programa ingenuo guarda el libro con
todos los campos vacíos y sigue tan tranquilo.

Nos pasó: la primera corrida completa terminó sin una sola excepción, con todos los controles en
verde, y con **168 libros en vez de 200**.

La solución es que cada pedido declare qué debería contener la página. Si eso no aparece, se
considera fallida aunque el código HTTP diga que salió bien:

```python
html = pedir(page, url, HAY_FICHA)   # HAY_FICHA = "#title h1"
```

**La lección:** cuando se scrapea, "no hubo error" no significa "salió bien". Hay que verificar el
resultado, no confiar en la ausencia de excepciones.

### Las corridas largas se cortan

Son unas 400 peticiones con pausas: cerca de 20 minutos. En ese lapso cualquier cosa puede fallar.

Por eso el avance se guarda cada 10 libros sobre el propio `libros.csv`, y al arrancar el programa
lee ese archivo y saltea lo que ya tiene. Si una corrida termina con menos de 200, alcanza con
volver a ejecutarla: va a pedir únicamente los que faltan. Para empezar de cero, se borra el CSV.

## 7. El registro de la corrida

Todo lo que el programa informa sale por dos lados a la vez: la pantalla y el archivo
`data/scraper.log`. En el código eso no cuesta nada, porque en vez de `print(...)` se escribe
`log.info(...)` y el módulo `logging` se encarga del resto.

Cada línea lleva la hora adelante, que es lo que permite ver después dónde se demoró la
extracción o en qué momento empezaron los reintentos. El archivo se abre en modo "agregar":
una corrida reanudada continúa el registro anterior en lugar de borrarlo, y por eso cada una
arranca con una línea separadora.

## 8. Para experimentar

Todo lo ajustable está arriba de todo en `src/scraper.py`:

| Constante | Para qué |
| :---- | :---- |
| `TOTAL_LIBROS` | cuántos libros extraer — bajarlo a 5 para hacer una prueba rápida |
| `PAUSA_MIN`, `PAUSA_MAX` | segundos de espera entre peticiones |
| `REINTENTOS` | cuántas veces reintentar una página |
| `GUARDAR_CADA` | cada cuántos libros se escribe el CSV |

Para ver el navegador trabajando, en `main()` cambiar `headless=True` por `headless=False`.

Y una advertencia sobre la pausa: bajarla hace que el programa termine antes, pero también que el
sitio empiece a devolver páginas vacías mucho más temprano. No es cortesía nada más, es lo que
hace que la extracción funcione.
