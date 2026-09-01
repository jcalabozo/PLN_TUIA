"""
Extracción de metadatos y sinopsis de Lectulandia.

Práctica 1 — Procesamiento de Lenguaje Natural.
Categoría: "Los más comentados" (https://ww3.lectulandia.co/mas-comentados/)

Playwright se encarga de la navegación y BeautifulSoup de interpretar el HTML.
Sólo se extraen metadatos y sinopsis públicas: no se descarga ningún libro.

Uso:
    py -3 src/scraper.py

El programa extrae 200 libros con todos sus campos y genera data/libros.csv.
El avance se guarda cada 10 libros sobre ese mismo archivo, así que si la
ejecución se corta basta con volver a lanzarla: los libros ya extraídos se
saltean. Para empezar de cero, borrar data/libros.csv.
"""

import logging
import random
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# --------------------------------------------------------------------------
# Configuración
# --------------------------------------------------------------------------

BASE = "https://ww3.lectulandia.co/"
CATEGORIA = "Los más comentados"
URL_CATEGORIA = urljoin(BASE, "mas-comentados/")
PREFIJO_FICHA = urljoin(BASE, "book/")   # así empiezan las URL de los libros

TOTAL_LIBROS = 200         # cantidad de libros a extraer
PAUSA_MIN, PAUSA_MAX = 1.0, 2.0   # segundos de espera entre peticiones
REINTENTOS = 2             # reintentos por página antes de darla por perdida
ESPERA = 5                 # segundos base de espera antes de reintentar
GUARDAR_CADA = 10          # cada cuántos libros se vuelca el avance a disco

# El sitio a veces devuelve páginas vacías (ver pedir()). Para darse cuenta,
# cada tipo de página declara un selector que debería estar presente si llegó
# completa.
HAY_LISTADO = "article.card h2 a.title"     # tarjetas del listado
HAY_FICHA = "#title h1"                     # título en la ficha de un libro
HAY_INDICE = "div.books-grid h2 a.title"    # grilla en páginas de autor y serie

DATOS = Path(__file__).resolve().parent.parent / "data"
SALIDA = DATOS / "libros.csv"      # el dataset
LOG = DATOS / "scraper.log"        # registro de lo que hizo el programa

COLUMNAS = [
    "titulo", "autores", "generos", "serie", "num_serie", "sinopsis",
    "url_libro", "categoria_origen", "fecha_extraccion", "portada",
    "cant_comentarios", "otros_libros_autor", "libros_serie",
]

SEPARADOR = " | "   # separador de los campos con varios valores

log = logging.getLogger("scraper")


def configurar_log():
    """Hace que todo lo que el programa informa vaya a la pantalla y al archivo.

    En el código se escribe `log.info(...)` en lugar de `print(...)`: el mismo
    mensaje sale por los dos lados, sin repetirlo. Cada línea lleva la hora
    adelante, que es lo que después permite ver dónde se demoró una corrida.

    El archivo se abre en modo "agregar", así que una corrida reanudada continúa
    el registro anterior en vez de borrarlo. Por eso cada una arranca con una
    línea separadora.
    """
    DATOS.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.FileHandler(LOG, encoding="utf-8"),   # al archivo
            logging.StreamHandler(),                      # a la pantalla
        ],
    )
    log.info("=" * 60)
    log.info(f"Nueva corrida: {datetime.now().isoformat(timespec='seconds')}")


# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------

def url_pagina(n):
    """Arma la URL de la página n del listado.

    La primera página no lleva sufijo: se pide como /mas-comentados/. El sitio
    enlaza /mas-comentados/page/1, pero esa URL responde con un 301 que redirige
    a la anterior, así que la evitamos.
    """
    return URL_CATEGORIA if n == 1 else f"{URL_CATEGORIA}page/{n}"


def texto_de(nodo):
    """Devuelve el texto de un nodo, ya limpio.

    Hace dos cosas a la vez porque siempre se necesitan juntas:

    - Si el nodo no existe (BeautifulSoup devuelve None cuando el selector no
      encuentra nada) devuelve cadena vacía en lugar de romper. Esto es lo que
      permite pedir campos que pueden no estar, como la serie.
    - Colapsa espacios, tabulaciones y saltos de línea en un solo espacio, que
      es la limpieza que pide el enunciado.
    """
    if not nodo:
        return ""
    return re.sub(r"\s+", " ", nodo.get_text(" ", strip=True)).strip()


def pausa():
    """Espera un momento entre peticiones para no sobrecargar el servidor."""
    time.sleep(random.uniform(PAUSA_MIN, PAUSA_MAX))


def pedir(page, url, selector):
    """Pide una página con Playwright y la devuelve parseada con BeautifulSoup.

    Devuelve None si no se pudo obtener. Reintenta en dos situaciones que
    conviene no confundir:

    - La navegación falla y lanza una excepción (timeout, error de red).
    - La página llega "bien" pero vacía. El sitio, cuando se le acumulan muchas
      peticiones, responde con código 200 y una página sin contenido. Eso no
      lanza ninguna excepción, así que sólo se detecta mirando el resultado:
      por eso quien llama indica con `selector` qué debería contener la página.

    Ese segundo caso es el que hace falta vigilar. Si se ignora, los libros
    entran al dataset con todos los campos vacíos y el programa no se entera.
    """
    for intento in range(REINTENTOS + 1):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            html = BeautifulSoup(page.content(), "html.parser")
            if html.select_one(selector):
                return html
            motivo = "página vacía"
        except Exception as error:
            motivo = error.__class__.__name__

        if intento < REINTENTOS:
            espera = ESPERA * (intento + 1)     # espera creciente: 5s, 10s
            log.info(f"    {motivo} en {url}, reintento {intento + 1} en {espera}s")
            time.sleep(espera)

    return None


# --------------------------------------------------------------------------
# Listado de la categoría
# --------------------------------------------------------------------------

def paginas_del_listado(html):
    """Lee del paginador cuántas páginas tiene el listado.

    El número de la página actual va en un <span> y los demás en <a>, así que se
    miran ambos: eso hace que la cuenta salga bien desde cualquier página. Las
    flechas de anterior/siguiente se descartan porque su texto no es un número.
    Si no hubiera paginador, se asume que el listado tiene una sola página.
    """
    numeros = [int(e.get_text()) for e in html.select("div.page-nav .page-numbers")
               if e.get_text(strip=True).isdigit()]
    return max(numeros) if numeros else 1


def recolectar_urls(page):
    """Recorre el listado página por página hasta juntar TOTAL_LIBROS URL únicas.

    Del listado sólo tomamos la dirección de cada ficha: la tarjeta muestra la
    sinopsis truncada, así que los metadatos se leen después en la ficha.
    """
    urls = []
    vistas = set()
    total = 1     # provisorio: se corrige al leer el paginador de la página 1
    n = 1

    while n <= total and len(urls) < TOTAL_LIBROS:
        html = pedir(page, url_pagina(n), HAY_LISTADO)
        if html is None:
            # Si falla justo la primera página nunca se conoce el total y el
            # recorrido termina sin libros; los controles finales lo detectan.
            log.info(f"[listado] !! no se pudo leer la página {n}")
            n += 1
            continue

        if n == 1:
            total = paginas_del_listado(html)
            log.info(f"[listado] el paginador indica {total} páginas")

        for enlace in html.select(HAY_LISTADO):
            url = urljoin(BASE, enlace.get("href", ""))
            if url not in vistas:          # deduplicación temprana
                vistas.add(url)
                urls.append(url)

        log.info(f"[listado] página {n}/{total}: {len(urls)} libros acumulados")
        n += 1
        pausa()

    return urls[:TOTAL_LIBROS]


# --------------------------------------------------------------------------
# Extracción de un libro
# --------------------------------------------------------------------------

def titulos_del_indice(page, url, cache):
    """Devuelve los títulos listados en una página de autor o de serie.

    Como varios libros comparten autor o serie, el resultado se cachea por URL
    para no repetir peticiones.
    """
    if not url:
        return []
    if url not in cache:
        html = pedir(page, url, HAY_INDICE)
        cache[url] = [texto_de(a) for a in html.select(HAY_INDICE)] if html else []
        pausa()
    return cache[url]


def extraer_libro(page, url, cache):
    """Extrae todos los campos de un libro: ficha, autor y serie.

    Devuelve None si la ficha no se pudo obtener después de los reintentos.
    """
    soup = pedir(page, url, HAY_FICHA)
    if soup is None:
        return None

    titulo = texto_de(soup.select_one(HAY_FICHA))

    # Autores y géneros: varios <a class="dinSource"> dentro de su div. Se
    # seleccionan sólo los enlaces para dejar afuera el rótulo
    # <span class="tagTitle"> ("Autor: ", "Generos: ").
    # Guardamos los nodos, no sólo el texto, porque de ellos sale también el
    # enlace a la página del autor.
    nodos_autor = soup.select("#autor a.dinSource")
    autores = [texto_de(a) for a in nodos_autor]
    generos = [texto_de(a) for a in soup.select("#genero a.dinSource")]

    # Serie: el div #serie sólo existe si el libro pertenece a una serie, así
    # que nodo_serie puede ser None y todo lo que dependa de él queda vacío.
    nodo_serie = soup.select_one("#serie a.dinSource")
    serie = texto_de(nodo_serie)

    # El número de orden no está en el enlace sino en el rótulo, con la forma
    # "Libro 4 de:", de donde lo saca esta expresión regular. Admite decimales
    # porque las series numeran así las novelas cortas y las precuelas: hay
    # libros rotulados "Libro 3.1 de:" o "Libro 0.5 de:".
    rotulo = texto_de(soup.select_one("#serie span.tagTitle"))
    numero = re.search(r"Libro\s+(\d+(?:\.\d+)?)\s+de", rotulo)
    num_serie = numero.group(1) if numero else ""

    # Sinopsis: se toma el contenedor completo en lugar del <span> interno, para
    # ser robustos ante variaciones del envoltorio. El separador " " evita que
    # los <br> peguen la última palabra con la primera del renglón siguiente.
    sinopsis = texto_de(soup.select_one("#sinopsis"))

    # Portada: la imagen de la ficha apunta a big.jpg (mayor resolución que la
    # small.jpg que usa la tarjeta del listado).
    imagen = soup.select_one("#cover img")
    portada = imagen["src"] if imagen and imagen.get("src") else ""

    # Cantidad de comentarios: el <span> no aparece si el libro no tiene ninguno.
    digitos = re.sub(r"\D", "", texto_de(soup.select_one("span.commentCount")))
    cant_comentarios = int(digitos) if digitos else 0

    # Los libros del autor y de la serie no están en la ficha (la única grilla de
    # relacionados que trae es por género), así que hay que visitar esas páginas.
    # Sus direcciones salen de los mismos enlaces que ya seleccionamos arriba.
    # Para el autor se usa el primero de la lista, que es el principal.
    url_autor = urljoin(BASE, nodos_autor[0]["href"]) if nodos_autor else ""
    url_serie = urljoin(BASE, nodo_serie["href"]) if nodo_serie else ""

    del_autor = titulos_del_indice(page, url_autor, cache)
    de_serie = titulos_del_indice(page, url_serie, cache)

    return {
        "titulo": titulo,
        "autores": SEPARADOR.join(autores),
        "generos": SEPARADOR.join(generos),
        "serie": serie,
        "num_serie": num_serie,
        "sinopsis": sinopsis,
        "url_libro": url,
        "categoria_origen": CATEGORIA,
        # Fecha y hora del momento en que se leyó esta ficha, en formato ISO
        # (2026-09-01T14:23:45). Una corrida larga o reanudada deja registros
        # con distintos valores, y eso es correcto: cada uno guarda cuándo se
        # obtuvo ese libro.
        "fecha_extraccion": datetime.now().isoformat(timespec="seconds"),
        "portada": portada,
        "cant_comentarios": cant_comentarios,
        "otros_libros_autor": SEPARADOR.join(t for t in del_autor if t != titulo),
        "libros_serie": SEPARADOR.join(t for t in de_serie if t != titulo),
    }


# --------------------------------------------------------------------------
# Guardado y controles
# --------------------------------------------------------------------------

def guardar(registros):
    """Escribe los registros en data/libros.csv, sin duplicados por url_libro.

    Se usa utf-8-sig (UTF-8 con BOM) para que los acentos se vean bien también
    al abrir el archivo con Excel.
    """
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(registros, columns=COLUMNAS).drop_duplicates(subset="url_libro")
    df.to_csv(SALIDA, index=False, encoding="utf-8-sig")
    return df


def cargar_previos():
    """Recupera los libros extraídos en una corrida anterior, si los hay.

    Se lee todo como texto (dtype=str) a propósito: si dejáramos que pandas
    infiriera los tipos, una columna como num_serie (que mezcla vacíos con
    números) se leería como float y el "1" volvería al CSV como "1.0".
    """
    if not SALIDA.exists():
        return []
    df = pd.read_csv(SALIDA, encoding="utf-8-sig", dtype=str).fillna("")
    registros = df.to_dict("records")
    for r in registros:
        r["cant_comentarios"] = int(r["cant_comentarios"] or 0)
    log.info(f"[reanudar] {len(registros)} libros ya extraídos en {SALIDA.name}")
    return registros


def controles(df):
    """Ejecuta los controles mínimos y muestra el resultado de cada uno."""
    if df.empty:
        log.info("[controles] no se extrajo ningún libro")
        return False

    con_sinopsis = (df["sinopsis"].str.len() > 0).sum()

    pruebas = [
        ("Sin duplicados por url_libro", df["url_libro"].duplicated().sum() == 0),
        ("Todos los registros tienen título", (df["titulo"].str.len() > 0).all()),
        ("Todas las URL son válidas", df["url_libro"].str.startswith(PREFIJO_FICHA).all()),
        ("La mayoría tiene sinopsis", con_sinopsis > len(df) / 2),
        ("Sin espacios ni saltos sobrantes", not df["titulo"].str.contains(r"\s{2,}|\n").any()),
        ("Se obtuvieron los 200 libros", len(df) == TOTAL_LIBROS),
    ]

    log.info("=" * 60)
    log.info("CONTROLES MÍNIMOS")
    log.info("=" * 60)
    for descripcion, ok in pruebas:
        log.info(f"  [{'OK' if ok else '--'}] {descripcion}")

    log.info(f"  Libros extraídos:  {len(df)}")
    log.info(f"  Con sinopsis:      {con_sinopsis} ({con_sinopsis / len(df):.0%})")
    log.info(f"  Con serie:         {(df['serie'].str.len() > 0).sum()}")
    log.info(f"  Autores distintos: {df['autores'].nunique()}")
    log.info("=" * 60)

    return all(ok for _, ok in pruebas)


# --------------------------------------------------------------------------
# Programa principal
# --------------------------------------------------------------------------

def main():
    configurar_log()
    registros = cargar_previos()
    ya_extraidas = {r["url_libro"] for r in registros}
    cache = {}      # páginas de autor y de serie ya visitadas
    fallidas = []

    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        page = navegador.new_page()

        urls = recolectar_urls(page)
        pendientes = [u for u in urls if u not in ya_extraidas]
        log.info(f"[fichas] {len(urls)} URL recolectadas, {len(pendientes)} pendientes")

        for i, url in enumerate(pendientes, start=1):
            try:
                libro = extraer_libro(page, url, cache)
            except Exception as error:
                # Los errores de red ya los maneja pedir(), que devuelve None.
                # Este try/except es la red de seguridad para lo inesperado (por
                # ejemplo, un cambio de HTML que rompa el parseo): se anota el
                # libro como fallido y el programa sigue con el siguiente.
                libro = None
                log.info(f"[{i}/{len(pendientes)}] !! {url}: {error.__class__.__name__}")

            if libro:
                registros.append(libro)
                log.info(f"[{i}/{len(pendientes)}] {libro['titulo']}")
            else:
                fallidas.append(url)

            # Guardado incremental sobre el mismo CSV: si la corrida se corta,
            # el avance no se pierde y la próxima ejecución lo retoma.
            if i % GUARDAR_CADA == 0:
                guardar(registros)

            pausa()

        navegador.close()

    df = guardar(registros)
    log.info(f"[salida] {len(df)} libros guardados en {SALIDA}")

    if fallidas:
        log.info(f"[salida] {len(fallidas)} fichas no se pudieron extraer:")
        for url in fallidas:
            log.info(f"    {url}")

    return 0 if controles(df) else 1


if __name__ == "__main__":
    sys.exit(main())
