# Práctica 3. Recomendador personalizado de libros

Auditoría de un catálogo de libros contaminado con spam (enlaces, mensajes promocionales y libros
inventados) y construcción de un recomendador que aprende las preferencias de un lector a partir
de las sinopsis, comparando TF-IDF y embeddings.

## Integrantes del grupo

* Josías Calabozo
* Sharo Giuntoli
* Ismael Darruiz
* Sebastián Di Carlo

## Estructura del proyecto

```
README.md
requirements.txt                              dependencias, con versiones fijas
.gitignore
TP3_grupo02.ipynb                             notebook del TP (entregable)
enunciado/                                    archivos de la cátedra
  TP3_Recomendador_personalizado_de_libros.pdf   enunciado (también en .docx)
  ejemplo_preferencias.csv, ejemplo_sospechosos.csv   ejemplos de formato
data/                                         datos que usa el notebook
  catalogo_tp3.jsonl                          catálogo de la cátedra (8.747 libros)
  muestra_etiquetada.csv                      500 libros etiquetados por la cátedra
  catalogo_limpio.csv                         catálogo sin los sospechosos: lo usan los pasos 3 a 8
entregables/                                  lo que pide entregar la consigna
  grupo02_sospechosos.csv                     libros marcados en la auditoría
  grupo02_preferencias.csv                    valoraciones del lector, con la columna conjunto
  informe.pdf                                 informe de hasta 3 páginas
informe/                                      archivos auxiliares del informe
  informe.md                                  texto del informe, del que sale el PDF
embeddings/                                   embeddings cacheados (no se versionan)
```

`grupo02` es el prefijo que pide el enunciado («grupoNN», con el número de grupo). Se define en la
constante `GRUPO`, al principio del notebook.

## Instalación

Probado con **Python 3.12**.

```bash
# 1. Crear y activar un entorno virtual (desde la carpeta P3/)
py -3.12 -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux / macOS

# 2. Instalar las dependencias
pip install -r requirements.txt

# 3. Descargar el modelo de spaCy en español (~570 MB, una sola vez)
python -m spacy download es_core_news_lg

# 4. Registrar el entorno como kernel de Jupyter (el notebook lo pide por ese nombre)
python -m ipykernel install --user --name pln-tp3 --display-name "Python 3.12 (PLN TP3)"
```

El modelo de oración `intfloat/multilingual-e5-small` (~490 MB), el mismo del TP2, no hace falta
bajarlo: `sentence-transformers` lo descarga la primera vez y lo guarda en la caché de Hugging
Face (ver el [README del TP2](../P2/README.md#caché-de-hugging-face)).

## Ejecución

Abrir `TP3_grupo02.ipynb` con el kernel **Python 3.12 (PLN TP3)** y
ejecutar todas las celdas. En VS Code está en **Select Kernel → Jupyter Kernel…**, aunque la
carpeta abierta no sea `P3/`. El notebook se ejecuta con **`P3/` como carpeta de trabajo**, porque
lee y escribe con rutas relativas (`data/...`, `entregables/...`). Es lo que hacen Jupyter y VS Code
por defecto.

La primera corrida tarda unos 20 minutos en CPU: lo más lento son los embeddings de las más de
50 mil oraciones del catálogo (paso 2.7, unos 9 minutos) y de las sinopsis del catálogo limpio
(paso 5, unos 7). Quedan guardados en `embeddings/` y las corridas siguientes los reutilizan, con
lo que el notebook completo tarda unos 5 minutos. Si cambia el catálogo limpio, hay que borrar
`embeddings/sinopsis_limpio.npy` para que se vuelva a calcular.

### Completar las preferencias (paso 3)

El notebook se detiene en el paso 3 hasta que el lector complete sus valoraciones:

1. La primera corrida crea `entregables/grupo02_preferencias.csv` con los primeros 300 libros del
   orden del enunciado (el catálogo limpio mezclado con `random_state=42`) y la columna `interes`
   vacía.
2. El lector elegido abre la planilla, lee el título y la sinopsis de cada libro **en orden, sin
   saltear filas**, y completa `interes` con `1` (me interesaría leerlo), `0` (no me interesaría) o
   la deja vacía si no puede decidir. Hacen falta al menos 100 respuestas y 20 de cada clase. Si se
   detiene antes de la última fila, borra las filas que no llegó a ver: una fila vacía cuenta como
   abstención.
3. Si encuentra un libro contaminado que la auditoría no detectó, lo deja vacío. En esta entrega no
   hubo ninguno; si lo hubiera, hay que sumar al paso 3 el código que lo agrega a los sospechosos
   con motivo `revision_manual`.
4. Guarda la planilla como CSV en UTF-8, separado por comas y con el mismo nombre, y vuelve a
   ejecutar el notebook completo.

> Con Excel en español, el CSV puede quedar separado por punto y coma. Conviene usar Google
> Sheets (Archivo → Descargar → CSV) o LibreOffice Calc (Guardar como → CSV, UTF-8, separador coma).

La misma persona da todas las respuestas, antes de ver cualquier predicción.

### En Colab

```python
!git clone https://github.com/jcalabozo/PLN_TUIA.git
%cd PLN_TUIA/P3
!pip install -r requirements.txt
!python -m spacy download es_core_news_lg
```

Después de instalar el modelo de spaCy hay que reiniciar la sesión (Entorno de ejecución →
Reiniciar sesión) para que `spacy.load` lo encuentre.
