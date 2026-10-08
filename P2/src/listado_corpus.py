"""Genera docs/listado_corpus.md: el listado de los libros del corpus que usamos para escribir
y revisar queries.json, con un índice por género y una ficha por libro.

Uso, desde la carpeta P2/:
    python src/listado_corpus.py
"""
import unicodedata
from collections import Counter

import pandas as pd

RUTA_CORPUS = "../P1/data/libros.csv"
RUTA_SALIDA = "docs/listado_corpus.md"
PALABRAS_EXTRACTO = 35   # palabras del comienzo de la sinopsis que se muestran en cada ficha

# Mismo libro con otro título o en otra edición (los encontramos revisando el corpus)
REPETIDOS = [
    ("1984", "1984 (Trad. Miguel Temprano García)"),
    ("Cien años de soledad (Edición conmemorativa)", "Cien años de soledad (Ed. Ilustrada)"),
    ("Rebelión en la granja", "Rebelión en la granja (trad. Marcial Souto y Miguel Temprano García)"),
    ("El imperio final", "El Imperio Final. (Ed. revisada)"),
    ("Sapiens", "De animales a dioses"),
]

COMO_USARLO = """## Cómo usarlo

1. **Escribir las consultas antes de correr cualquier modelo.** Definir qué es relevante después de ver qué devolvió el buscador es hacerse trampa.
2. Para cada consulta, anotar **todos** los libros relevantes del corpus, no solo los primeros que aparezcan. El índice por género ayuda a no olvidarse de ninguno, pero la relevancia se decide leyendo la sinopsis: el género solo no alcanza.
3. Variar los tipos de consulta: temáticas ("un mundo mágico con dragones"), de trama ("una investigación de asesinato"), de tono ("algo que dé miedo").
4. Incluir **al menos una consulta que no comparta ninguna palabra** con las sinopsis de sus libros relevantes. Es el caso donde TF-IDF no puede ganar.
5. **Ojo con el piso de azar:** el azar acierta, en promedio, `relevantes / 200`. Una consulta con 50 libros relevantes tiene un piso de 0,25, y casi cualquier modelo la "aprueba". Conviene que la mayoría tenga pocos relevantes (de 2 a 15).
6. Usar el **título exacto**, tal como figura acá, para identificar cada libro en `queries.json`."""


def sin_tildes(texto):
    """Quita las tildes, como en el apunte de la Unidad 1: NFKD separa "á" en "a" + tilde."""
    descompuesto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in descompuesto if not unicodedata.combining(c))


def comparar_sinopsis(a, b):
    """Qué tan parecidas son las sinopsis de dos ediciones, según la similitud de Jaccard de sus palabras."""
    if a == b:
        return "**sinopsis idéntica**"
    palabras_a, palabras_b = set(a.lower().split()), set(b.lower().split())
    jaccard = len(palabras_a & palabras_b) / len(palabras_a | palabras_b)
    return "sinopsis parecidas" if jaccard >= 0.5 else "sinopsis distintas"


def ficha(numero, libro):
    generos = " · ".join(libro["generos"].split(" | "))
    datos = f"**{libro['autores']}** · *{generos}*"
    if pd.notna(libro["serie"]):
        datos += f" · Serie: {libro['serie']}, tomo {int(libro['num_serie'])}"
    palabras = libro["sinopsis"].split()
    extracto = " ".join(palabras[:PALABRAS_EXTRACTO])
    if len(palabras) > PALABRAS_EXTRACTO:
        extracto += " …"
    return (f"### {numero}. {libro['titulo']}\n\n{datos}\n\n{extracto}\n\n"
            f"<details><summary>Sinopsis completa</summary>\n\n{libro['sinopsis']}\n\n</details>")


libros = pd.read_csv(RUTA_CORPUS)

# Fichas en orden alfabético, sin distinguir tildes ni mayúsculas, numeradas desde 1
libros["orden"] = libros["titulo"].apply(lambda titulo: sin_tildes(titulo).lower())
libros = libros.sort_values("orden").reset_index(drop=True)
libros.index += 1
numero = {titulo: n for n, titulo in libros["titulo"].items()}
sinopsis = dict(zip(libros["titulo"], libros["sinopsis"]))
assert all(a in numero and b in numero for a, b in REPETIDOS)

repetidos = [f"- {a} ({numero[a]}) = {b} ({numero[b]}): {comparar_sinopsis(sinopsis[a], sinopsis[b])}"
             for a, b in REPETIDOS]

# Índice por género. most_common() ordena por cantidad de libros; los empates quedan
# en el orden en que aparece cada género al recorrer las fichas
generos_por_libro = libros["generos"].str.split(" | ", regex=False)
conteo = Counter(genero for generos in generos_por_libro for genero in generos)
indice = []
for genero, cantidad in conteo.most_common():
    titulos = [f"{titulo} ({n})" for n, titulo, generos in zip(libros.index, libros["titulo"], generos_por_libro)
               if genero in generos]
    indice.append(f"- **{genero}** ({cantidad}): " + ", ".join(titulos))

partes = [
    "# Listado del corpus del TP2",
    "> Generado con [`src/listado_corpus.py`](../src/listado_corpus.py) a partir de "
    f'`P1/data/libros.csv` ({len(libros)} libros, categoría "Los más comentados" de '
    "Lectulandia). Sirve para escribir `queries.json`: elegir consultas y decidir qué libros son relevantes "
    "para cada una.",
    COMO_USARLO,
    "## ⚠️ Libros repetidos",
    "Estos pares son **el mismo libro** con otro título o en otra edición. Si un libro de un par es relevante "
    "para una consulta, el otro también lo es: hay que anotar los dos en `queries.json`.",
    "\n".join(repetidos),
    "Los pares con sinopsis distintas sirven además como prueba: un buen modelo semántico debería ponerlos "
    "cerca aunque las palabras no coincidan.",
    "## Índice por género",
    "Cada libro aparece en todos sus géneros. Entre paréntesis, la cantidad de libros; al lado de cada título, "
    "su número de ficha.",
    "\n".join(indice),
    "## Fichas",
] + [ficha(n, libro) for n, libro in libros.iterrows()]

with open(RUTA_SALIDA, "w", encoding="utf-8", newline="\n") as archivo:
    archivo.write("\n\n".join(partes) + "\n")
print(f"{RUTA_SALIDA}: {len(libros)} fichas, {len(conteo)} géneros")
