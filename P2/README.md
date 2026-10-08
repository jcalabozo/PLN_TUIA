# Práctica 2 — Embeddings y búsqueda semántica

Representación de las sinopsis del corpus del TP1 con TF-IDF, Word2Vec (propio y pre-entrenado)
y modelos de oración, y evaluación de cuál recupera mejor los libros relevantes para consultas
en lenguaje natural.

## Integrantes del grupo

* Josías Calabozo
* Sharo Giuntoli
* Ismael Darruiz
* Sebastián Di Carlo

## Estructura del proyecto

```
README.md
requirements.txt                              dependencias
.gitignore
TP2_calabozo_giuntoli_darruiz_dicarlo.ipynb   notebook del TP (entregable)
enunciado/
  Enunciado_TP2_embeddings.md                 enunciado de la cátedra
  Enunciado_TP2_embeddings_marcado.docx       el mismo, con lo que no va marcado en rojo
data/
  queries.json                                conjunto de evaluación (entregable)
docs/
  informe.md                                  borrador del informe
  listado_corpus.md                           listado del corpus para escribir queries.json
src/
  listado_corpus.py                           genera docs/listado_corpus.md
```

El corpus se lee de `../P1/data/libros.csv`, el dataset del TP1. Al ejecutar el notebook aparecen
además `models/` (SBW) y los embeddings calculados en `data/*.npy`; ninguno de los dos se versiona.

## Instalación

Probado con **Python 3.12**.

```bash
# 1. Crear y activar un entorno virtual (desde la carpeta P2/)
py -3 -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux / macOS

# 2. Instalar las dependencias
pip install -r requirements.txt

# 3. Descargar SBW, el Word2Vec pre-entrenado en español (~1 GB, una sola vez)
mkdir models
curl -L -o models/SBW-vectors-300-min5.bin.gz https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5.bin.gz
```

> En PowerShell, `curl` es otro comando: hay que escribir `curl.exe`.

Los dos modelos de oración, `distiluse-base-multilingual-cased-v1` (~540 MB) y
`intfloat/multilingual-e5-small` (~490 MB), no hace falta bajarlos: `sentence-transformers`
los descarga solo la primera vez que el notebook los usa y los guarda en la caché de Hugging
Face (ver más abajo).

## Ejecución

Abrir `TP2_calabozo_giuntoli_darruiz_dicarlo.ipynb` con el entorno creado como kernel y ejecutar
todas las celdas. El notebook se ejecuta con **`P2/` como carpeta de trabajo**, porque lee y
escribe con rutas relativas (`data/queries.json`, `models/`, `../P1/data/libros.csv`). Es lo que
hacen Jupyter y VS Code por defecto, ya que el notebook está en `P2/`.

La corrida completa tarda unos dos minutos una vez descargados los modelos; cargar SBW es lo
más lento (alrededor de un minuto y 1,2 GB de memoria). Los embeddings de los modelos de oración
se guardan en `data/embeddings_*.npy` y se reutilizan en las corridas siguientes: para
recalcularlos, borrar esos archivos.

### En Colab

```python
!git clone https://github.com/jcalabozo/PLN_TUIA.git
%cd PLN_TUIA/P2
!pip install -r requirements.txt
!mkdir -p models && wget -P models https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5.bin.gz
```

### Listado del corpus

`docs/listado_corpus.md` se regenera con:

```bash
python src/listado_corpus.py
```

## Caché de Hugging Face

Los modelos de oración quedan en la caché de Hugging Face, por defecto en
`~/.cache/huggingface/hub` (en Windows, `C:\Users\<usuario>\.cache\huggingface\hub`). Se puede
mover a otra carpeta definiendo la variable de entorno `HF_HOME` antes de abrir el notebook.

Para ver qué hay y liberar espacio, con el entorno activado:

```bash
# Ver los modelos guardados y cuánto ocupan
hf cache ls

# Borrar solo los dos modelos del TP (pide confirmación)
hf cache rm model/sentence-transformers/distiluse-base-multilingual-cased-v1 model/intfloat/multilingual-e5-small
```

Con versiones viejas de `huggingface_hub` el comando `hf` no existe: en su lugar, `huggingface-cli delete-cache` abre un menú para elegir qué borrar.

Si se borran, se vuelven a descargar la próxima vez que se ejecute el notebook. SBW no está en
esa caché: para borrarlo, eliminar la carpeta `models/`.
