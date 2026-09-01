# Parte 1 — Diseño de la extracción

**Práctica 1 — Procesamiento de Lenguaje Natural**
Extracción de metadatos y sinopsis de Lectulandia con Playwright y BeautifulSoup.

---

## 1. Categoría seleccionada

* **Nombre de la categoría:** "Los más comentados"
* **URL de la categoría:** https://ww3.lectulandia.co/mas-comentados/
* **Cantidad de libros que se propone extraer:** 200
* **Criterio utilizado para seleccionar las páginas:** Secuencial

### Justificación y verificación previa

Se inspeccionó el listado para confirmar que la categoría alcanza para el objetivo:

| Observación | Valor verificado |
| :---- | :---- |
| Libros por página (`article.card`) | 24 |
| Cantidad de páginas del listado | 9 al momento del análisis |
| Tarjetas en total (24 × 9) | 216 |
| **Libros distintos disponibles** | **206** |
| Patrón de paginación | `/mas-comentados/page/{n}` (n ≥ 2; la página 1 no lleva sufijo) |

El recorrido es **secuencial**: se parte de la página 1 y se avanza hasta reunir 200 fichas
únicas o hasta agotar el listado.

El total de páginas **no se fija en el código**: se lee del paginador
(`div.page-nav .page-numbers`) al abrir la primera página. Eran 9 durante el análisis, pero
la categoría crece a medida que se publican libros, y un valor escrito a mano dejaría de
recorrer las páginas nuevas sin dar ningún aviso.

Conviene distinguir las 216 tarjetas de los 206 libros **distintos**: unos 10 títulos aparecen
repetidos en más de una página, porque el orden del ranking se recalcula entre una petición y la
siguiente. Por eso la deduplicación no es un detalle de cierre sino parte del recorrido: sin ella
no se llegaría a 200 libros únicos. El margen real es de apenas 6 libros sobre la meta.

> **Nota sobre la consigna:** en "Controles mínimos" se menciona un rango de 50 a 100 libros,
> mientras que el resto del enunciado indica 100 a 200. Se adopta el rango de **100 a 200**,
> que es el criterio general del trabajo.

---

## 2. Datos que se extraerán

### Campos mínimos requeridos

| Campo | Descripción |
| :---- | :---- |
| `titulo` | Título del libro |
| `autores` | Autor o autores |
| `generos` | Género o géneros |
| `serie` | Serie a la que pertenece, si corresponde |
| `sinopsis` | Texto completo de la sinopsis |
| `url_libro` | Dirección de la ficha |
| `categoria_origen` | Categoría seleccionada por el grupo |
| `fecha_extraccion` | Fecha y hora en que se obtuvo el registro |

### Campos adicionales que incorpora el grupo

| Campo | Descripción | Origen |
| :---- | :---- | :---- |
| `portada` | URL de la imagen de portada (versión `big.jpg`) | Ficha individual |
| `num_serie` | Número de orden del libro dentro de la serie | Ficha individual |
| `cant_comentarios` | Cantidad de comentarios/reseñas publicados | Ficha individual |
| `otros_libros_autor` | Lista de libros del autor principal | Página de autor |
| `libros_serie` | Lista de libros de la serie, si corresponde | Página de serie |

`cant_comentarios` es especialmente pertinente en esta categoría, porque es la variable que
define el propio ranking de "Los más comentados".

Los campos `otros_libros_autor` y `libros_serie` **no están disponibles en la ficha del libro**:
la ficha sólo ofrece una grilla de recomendados por género. Obtenerlos exige visitar dos páginas
adicionales (`/autor/<slug>/` y `/serie/<slug>/`) por cada libro, que se piden a continuación de
la ficha dentro del mismo recorrido (ver sección 4). Como muchos libros comparten autor o serie,
esas páginas se cachean para no repetir peticiones.

### Convenciones de formato

* Campos multivaluados (`autores`, `generos`, `otros_libros_autor`, `libros_serie`): se guardan como texto con separador `" | "`.
* Campos ausentes: cadena vacía `""` de manera uniforme (nunca `None`, `"N/A"` ni `"-"` mezclados).
* `fecha_extraccion`: fecha **y hora** en formato ISO (`2026-09-01T14:23:45`). Se guarda el momento
  en que se leyó cada ficha, no el de la corrida: una extracción larga o reanudada deja registros
  con distintos valores, y eso es lo correcto según la definición del campo.
* `cant_comentarios`: entero, `0` cuando el libro no tiene comentarios.
* `num_serie`: número de orden dentro de la serie, `""` cuando no aplica. **No siempre es entero**:
  las series numeran con decimales las novelas cortas y las precuelas, de modo que hay valores como
  `3.1` o `0.5`. Se guarda tal como aparece en el sitio.

---

## 3. Localización de los datos

Los selectores se obtuvieron inspeccionando el HTML del sitio con las herramientas de
desarrollo del navegador. La ficha individual estructura la información dentro de
`div#book`, con un `div` de id propio por cada dato.

### 3.1 Página de listado (`/mas-comentados/page/{n}`)

| Dato | Etiqueta HTML | Selector propuesto | Observaciones |
| :---- | :---- | :---- | :---- |
| Tarjeta de libro | `<article class="card">` | `article.card` | 24 por página |
| URL de la ficha | `<a class="title">` | `article.card h2 a.title["href"]` | Ruta relativa `/book/<slug>/`; se completa con `urljoin` |
| Paginación | `<a class="page-numbers">` | `div.page-nav .page-numbers` | Da el total de páginas. Se leen `<a>` y `<span>`: el número de la página actual va en un `<span>` |

Del listado **sólo se toma la URL de la ficha**. Todos los metadatos se extraen de la ficha
individual, porque la tarjeta muestra la sinopsis truncada (termina en `[…]`).

### 3.2 Ficha individual (`/book/<slug>/`)

| Dato | Tipo de página | Etiqueta HTML | Selector propuesto |
| :---- | :---- | :---- | :---- |
| Título | Ficha individual | `<div id="title"><h1>` | `#title h1` |
| Autores | Ficha individual | `<div id="autor">` con `<a class="dinSource">` | `#autor a.dinSource` (lista) |
| Géneros | Ficha individual | `<div id="genero">` con `<a class="dinSource">` | `#genero a.dinSource` (lista) |
| Serie | Ficha individual | `<div id="serie">` con `<a class="dinSource">` | `#serie a.dinSource` |
| Nº en la serie | Ficha individual | `<span class="tagTitle">` | `#serie span.tagTitle` → regex `Libro (\d+) de:` |
| Sinopsis | Ficha individual | `<div id="sinopsis">` → `<div class="ali_justi"><span>` | `#sinopsis` con `get_text(" ", strip=True)` |
| Portada | Ficha individual | `<div id="cover"><img>` | `#cover img["src"]` |
| Cant. comentarios | Ficha individual | `<span class="commentCount">` | `span.commentCount` |
| URL del libro | — | — | Conocida desde el listado; no se extrae del HTML |

**Notas de implementación relevadas en el HTML:**

* `#serie` **sólo existe si el libro pertenece a una serie.** En libros sueltos el `div` no está
  presente, por lo que `serie` y `num_serie` quedan vacíos. Todo acceso debe ir precedido de una
  comprobación `if nodo:`.
* El texto de la sinopsis se envuelve en `div.ali_justi > span` y usa `<br>` como separador de
  párrafos. Se selecciona directamente `#sinopsis` con `get_text(" ", strip=True)` para ser
  robustos ante variaciones del envoltorio interno y para que los `<br>` no peguen palabras.
* `span.commentCount` no aparece cuando el libro no tiene comentarios; en ese caso se registra `0`.
* Las etiquetas `<span class="tagTitle">` ("Autor: ", "Generos: ", "Libro N de: ") son rótulos
  fijos: hay que excluirlas del texto extraído seleccionando únicamente los `a.dinSource`.
* La portada de la ficha (`#cover img`) apunta a `big.jpg`, de mayor resolución que la `small.jpg`
  de la tarjeta del listado.

### 3.3 Páginas de autor y de serie

| Dato | Tipo de página | Etiqueta HTML | Selector propuesto |
| :---- | :---- | :---- | :---- |
| Otros libros del autor | `/autor/<slug>/` | `<a class="title">` | `div.books-grid h2 a.title` |
| Libros de la serie | `/serie/<slug>/` | `<a class="title">` | `div.books-grid h2 a.title` |

Los slugs se obtienen del `href` de `#autor a.dinSource` y `#serie a.dinSource` en la ficha.
Como varios libros comparten autor o serie, se **cachea** el resultado por URL para no repetir
peticiones. El libro en curso se excluye de su propia lista.

Una lista vacía es un valor legítimo: significa que el autor o la serie tienen un solo libro
publicado en el sitio.

---

## 4. Estrategia de extracción

### 4.1 Procedimiento

1. **Abrir la página de la categoría con Playwright.** Se inicia Chromium en modo *headless* y se
   navega a `https://ww3.lectulandia.co/mas-comentados/`, esperando el estado `domcontentloaded`.
2. **Recorrer las páginas necesarias.** La primera página **no lleva sufijo de numeración**: se
   solicita como `/mas-comentados/`. A partir de la segunda se avanza secuencialmente por
   `/mas-comentados/page/{n}`. El recorrido se detiene al reunir 200 URL únicas o al agotar el
   listado, cuya cantidad de páginas se lee del paginador al abrir la primera.

   ```python
   URL_CATEGORIA = "https://ww3.lectulandia.co/mas-comentados/"

   def url_pagina(n):
       return URL_CATEGORIA if n == 1 else f"{URL_CATEGORIA}page/{n}"

   def paginas_del_listado(html):
       numeros = [int(e.get_text()) for e in html.select("div.page-nav .page-numbers")
                  if e.get_text(strip=True).isdigit()]
       return max(numeros) if numeros else 1
   ```

   Aunque el propio paginador del sitio enlaza `/mas-comentados/page/1`, esa URL responde con un
   **301** que redirige a `/mas-comentados/`. Construirla así evita una redirección innecesaria en
   cada ejecución.
3. **Obtener el HTML mediante Playwright.** Con `page.content()` se captura el HTML ya renderizado.
4. **Analizar ese HTML con BeautifulSoup.** Se instancia `BeautifulSoup(html, "html.parser")`.
5. **Extraer las URL de las fichas.** Se recorren los `article.card`, se lee `h2 a.title["href"]`
   y se normaliza con `urljoin` contra el dominio base. Las URL se acumulan en un conjunto para
   descartar repeticiones ya en esta etapa.
6. **Visitar cada ficha con Playwright.** Se reutiliza la misma página del navegador y se navega
   una por una, con una **pausa de 1 a 2 segundos** entre visitas para no sobrecargar el servidor.
7. **Extraer los metadatos y la sinopsis con BeautifulSoup**, aplicando los selectores de la
   sección 3.2 sobre el HTML de cada ficha. A continuación, y para ese mismo libro, se visitan
   las páginas de su autor y de su serie (sección 3.3) para completar los dos campos que la ficha
   no ofrece. Ambas quedan cacheadas para los libros siguientes.
8. **Limpiar y validar los datos** (detalle en 4.3).
9. **Eliminar libros duplicados** por `url_libro` (detalle en 4.4).
10. **Guardar el resultado** en `data/libros.csv` con pandas, en UTF-8 con BOM (`utf-8-sig`) para
    que los acentos se vean correctamente también al abrir el archivo en Excel.

### 4.2 Manejo de errores y guardado incremental

* Cada ficha se procesa dentro de un `try/except`: si falla la navegación o el parseo, se informa
  la URL y el programa **continúa con la siguiente**, sin interrumpirse.
* Las navegaciones usan `timeout` explícito y hasta **2 reintentos** con espera creciente antes de
  dar la página por perdida.
* Además del error con excepción, se contempla que el sitio responda `200` con una **página vacía**
  cuando se acumulan muchas peticiones. Como ese caso no lanza excepción, se detecta por el
  resultado: cada pedido declara qué selector debería estar presente (`article.card` en el listado,
  `#title h1` en la ficha, `div.books-grid` en las páginas de autor y de serie) y, si no aparece,
  se espera bastante más de lo habitual y se vuelve a pedir.
* Todo lo que el programa informa se escribe a la vez por pantalla y en `data/scraper.log`,
  con la hora al principio de cada línea, usando el módulo `logging`. El archivo se abre en modo
  "agregar", de modo que una corrida reanudada continúa el registro anterior. Permite revisar
  después qué fichas fallaron y en qué momento aparecieron los reintentos.
* El guardado es **incremental**: cada 10 libros se vuelca lo acumulado sobre el propio
  `data/libros.csv`. Si la ejecución se corta, al reiniciar se lee ese mismo archivo y se
  **saltean las URL ya extraídas**, de modo que el trabajo previo no se pierde. Se trabaja siempre
  sobre un único CSV, que es el que pide la entrega.

### 4.3 Limpieza y validación

* Se colapsan espacios múltiples, tabulaciones y saltos de línea con `re.sub(r"\s+", " ", texto).strip()`.
* Las entidades HTML (`&hellip;`, `&nbsp;`, `&rsquo;`) quedan convertidas a sus caracteres
  correspondientes, porque el texto se toma con `get_text()` de BeautifulSoup y no del HTML crudo.
* La validación se hace **en el origen**: si la ficha no devuelve título, el libro no se agrega al
  dataset y su URL se informa al final. Así no hay registros a medio llenar que haya que limpiar
  después.
* Los registros sin sinopsis sí se conservan con el campo vacío, y el control de cierre verifica
  que sean una minoría.
* Los campos ausentes se representan de manera uniforme según las convenciones de la sección 2.

### 4.4 Deduplicación

* **Durante el recorrido del listado:** las URL se acumulan en un `set`, evitando visitar dos veces
  la misma ficha. Este paso no es opcional: de las 216 tarjetas del listado sólo 206 corresponden a
  libros distintos.
* **Al guardar:** `drop_duplicates(subset="url_libro")` sobre el DataFrame, como control de cierre.
* **Al reanudar:** las URL ya presentes en el CSV se saltean, de modo que una segunda corrida no
  vuelve a agregar los libros que ya están.

### 4.5 Controles finales

Al terminar, el programa ejecuta estos seis controles e informa el resultado de cada uno por
pantalla. Si alguno falla, termina con código de salida distinto de cero:

| Control | Criterio |
| :---- | :---- |
| Sin duplicados | `url_libro` no se repite |
| Título presente | ningún `titulo` vacío |
| URL válida | todas empiezan con `https://ww3.lectulandia.co/book/` |
| Cobertura de sinopsis | más de la mitad de los registros tiene `sinopsis` |
| Texto limpio | sin espacios dobles ni saltos de línea |
| Cantidad obtenida | exactamente 200 libros |

Sobre el último control: el enunciado sólo pide un rango, pero comparar contra el **objetivo**
en lugar del rango es lo que permite detectar una extracción incompleta. Una corrida que pierde
libros por un corte de red igual cae dentro de "entre 100 y 200", así que un control por rango la
daría por buena; exigir los 200 obliga a volver a ejecutar el programa, que retoma los faltantes
gracias a la reanudación.

La consistencia de los campos ausentes no se comprueba al final porque está garantizada en el
origen: cada campo se inicializa en `""` al construir el registro, y los libros cuya ficha no se
pudo leer no se agregan al dataset en lugar de entrar con los campos vacíos.

### 4.6 Consideraciones éticas y de uso responsable

* Se extraen **únicamente metadatos y sinopsis públicas**. No se descargan libros, ni archivos
  EPUB, PDF ni ningún otro contenido; los enlaces de descarga de la ficha se ignoran por completo.
* Se respeta una pausa entre peticiones y se evita la concurrencia, manteniendo una carga baja
  sobre el servidor.
* El dataset resultante se destina exclusivamente a fines académicos, dentro de las actividades de
  procesamiento de texto y del recomendador de libros de la materia.

---

## 5. Estructura de entrega prevista

```
README.md                 integrantes, categoría, instalación y ejecución
requirements.txt          dependencias
.gitignore
src/
  scraper.py              programa de extracción
data/
  libros.csv              dataset final (único CSV de la entrega)
docs/
  diseno_extraccion.md    este documento
  como_funciona.md        explicación conceptual del scraper
```
