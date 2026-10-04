# Plan de trabajo — TP2: embeddings y búsqueda semántica

> Documento vivo: se actualiza a medida que avanzamos o que la cátedra comparte material. Última actualización: 2026-10-04.
>
> Enunciado: [Enunciado_TP2_embeddings.md](../Enunciado_TP2_embeddings.md) · Notebook: [TP2_calabozo_giuntoli_darruiz_dicarlo.ipynb](../TP2_calabozo_giuntoli_darruiz_dicarlo.ipynb) · Listado del corpus: [listado_corpus.md](listado_corpus.md)
>
> Los apuntes de la materia (exportados de Notion) y las prácticas resueltas están en [jcalabozo/tuia-nlp](https://github.com/jcalabozo/tuia-nlp).

## 1. En pocas palabras

El TP pide representar las sinopsis del corpus del TP1 con **embeddings** (palabra y oración), compararlos contra **TF-IDF** y, sobre todo, **demostrar con una evaluación honesta** si la representación nueva es mejor que la vieja.

| # | Entregable | Contenido |
|---|---|---|
| 1 | `TP2_apellido1_apellido2.ipynb` | Notebook ejecutado, con las salidas visibles |
| 2 | `queries.json` | Al menos 10 consultas, con los libros relevantes de cada una |
| 3 | `informe.pdf` | Hasta 3 páginas |
| 4 | Base en Supabase | Poblada y accesible (ver la sección 3, problema 3) |

**Lo que más pesa:** el rigor de la evaluación (30 %): líneas de base, límites de la métrica y una interpretación que los resultados sostengan. Un pipeline que corre, sin piso de azar y sin discusión, saca menos que uno con peores resultados bien analizados.

## Estado del avance

Notebook: [`TP2_calabozo_giuntoli_darruiz_dicarlo.ipynb`](../TP2_calabozo_giuntoli_darruiz_dicarlo.ipynb) (ejecutado, con las salidas visibles).

| Parte | Estado |
|---|---|
| 0 · Análisis inicial (las cuatro preguntas) | ✅ |
| A · Corpus en dos versiones | ✅ |
| Línea de base TF-IDF y `buscar(consulta, modelo, k, genero)` | ✅ |
| B · Word2Vec propio contra SBW | ✅ |
| C · SBERT (`distiluse`) y truncado | ✅ |
| D · Similitudes al azar, prueba de las ediciones y proyección 2D | ✅ |
| D · Rankings lado a lado para 3 consultas | ⏳ Necesita `queries.json` |
| Evaluación con precision@k | ⏳ Código listo; necesita `queries.json` |
| E, F · pgvector y SQL | ⏳ Fase 2 |
| Parte avanzada | ⏳ A definir |

**Hallazgos hasta ahora** (detallados en el notebook):
- **SBERT trunca 178 de las 200 sinopsis (89 %)** con su límite de 128 tokens, y en las truncadas no ve, en promedio, el 39 % final del texto.
- **El Word2Vec propio aprende co-ocurrencias de cada libro, no significado.** Los vecinos de "guerra" salen todos de una sola saga de Sanderson.
- **SBW tiene el sesgo de su corpus:** los vecinos de "familia" son familias biológicas.
- **Con SBW, todo se parece a todo:** dos libros al azar dan 0,87 de similitud media, con un desvío de 0,04. SBERT es el espacio más repartido (0,22 ± 0,09).
- **TF-IDF encuentra las cinco ediciones repetidas en el puesto 1**, por los nombres propios compartidos (*Winston*, *Smith*). Es un caso legítimo donde TF-IDF gana.
- **En PCA, solo SBERT muestra regiones por género** (Fantástico, Romántico, Ciencia ficción). En TF-IDF, las dos componentes capturan solo duplicados.
- **Los términos característicos de TF-IDF no se estabilizan con 200 sinopsis.** Además, el 88 % de los top 10 tienen empates que hay que desempatar de forma fija.

**Próximo paso: escribir `queries.json`** (ver la sección 6 y el [listado del corpus](listado_corpus.md)). Con eso se completan los rankings de la parte D y la evaluación.

## 2. Qué tenemos y qué falta

| Material | Estado |
|---|---|
| Corpus (`P1/data/libros.csv`) | ✅ 200 libros, 13 columnas |
| Entorno (`P2/requirements.txt`) | ✅ gensim, sentence-transformers, nltk, psycopg, pgvector, python-dotenv; se sumó `langdetect` (Unidad 3) |
| Modelo `SBW-vectors-300-min5` (~1 GB) | ✅ Bajado en `P2/models/` (ignorado por git) desde [SBWCE](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5.bin.gz) |
| **Notebook guía** `TP2_embeddings_busqueda_semantica.ipynb` | ❌ **No fue compartido** (ver abajo) |
| **Anexo A** (cuenta y proyecto en Supabase) | ❌ No fue compartido |
| Fecha de entrega | ❌ El enunciado la deja en blanco |
| Teoría de pgvector, HNSW y Supabase | ❌ Todavía no se vio en clase |

**Dónde se buscó el notebook guía, sin resultado:** las prácticas de U2 y U3, los Notion de U2 y U3 (reexportados el 2026-10-04: no cambiaron) y los Colab enlazados en los apuntes (el "cuaderno práctico" de U1 y el de POS tags de U3). La página de Notion que agrupa las unidades no es pública.

Todo indica que la guía existe y no se compartió. El bloque mal pegado al principio de la sección 4 del enunciado ("Primer análisis del corpus…", "Con 12 documentos…") tiene formato de celdas de notebook y no aparece en ningún material del curso: seguramente sale de ahí, de una versión que trabaja con una muestra de 12 libros.

**Mientras tanto, lo más parecido que tenemos:**

| Para… | Usar |
|---|---|
| Cargar SBW con gensim y ver vecinos | Apunte U2, sección *Word2Vec* (`KeyedVectors.load_word2vec_format`, `most_similar`) |
| Entrenar Word2Vec propio | Apunte U2, sección *Word2Vec* (`Word2Vec(sentences, vector_size, window, min_count, sg)`) |
| Embeddings de oración con `distiluse` | Apunte U2, sección *Sentence-BERT* |
| Buscar, recomendar, clustering, PCA y t-SNE sobre Lectulandia | Práctica *Embeddings semánticos* de U2 ([resuelta en tuia-nlp](https://github.com/jcalabozo/tuia-nlp/blob/main/U2/practicas/practica_embeddings_semanticos_resuelta.ipynb)) |
| TF-IDF y sus parámetros | Práctica *Vectorización frecuentista* de U2 ([resuelta en tuia-nlp](https://github.com/jcalabozo/tuia-nlp/blob/main/U2/practicas/practica_vectorizacion_frecuentista_resuelta.ipynb)) |
| `util.semantic_search` y un recomendador | Práctica de U3, sección 6 (ejercicio 6.4) |

## 3. Problemas del enunciado y cómo los resolvemos

1. **La sección 4 empieza con un bloque pegado de otro material:** markdown escapado (`\*\*`, `\#`), "12 documentos" (el corpus tiene 200) y cuatro preguntas sueltas (cuántos documentos hacen falta, sesgo de las sinopsis promocionales, multi-etiqueta, gallego o catalán).
   → Las tomamos como **preguntas de reflexión del análisis inicial** y las respondemos en el notebook con nuestros datos (parte 0).
2. **Pide comparar contra "el TF-IDF del TP1", que no existe:** el TP1 fue solo el scraper.
   → Construimos el TF-IDF en este TP, con `TfidfVectorizer`, como en la práctica de U2.
3. **Las partes E y F, el entregable 4 y la sección 3 piden Postgres, pgvector, HNSW y Supabase**, que todavía no se vieron, y el Anexo A no se compartió. La propia sección 3 dice: "por el momento solo utilizan el csv y el DataFrame".
   → Trabajamos en **dos fases**: la **fase 1** (ahora) usa el CSV y DataFrames; la **fase 2** (cuando se vea el tema) agrega la base. La búsqueda de la fase 1 se escribe para que pasar a SQL sea reemplazar una sola función.
4. **"El corpus del TP1 cargado en la tabla `books` de su csv"** mezcla tabla y CSV.
   → Fase 1: DataFrame desde `libros.csv`. Fase 2: tabla `books` en Supabase.
5. **El modelo de oración:** el TP pide arrancar con `distiluse-base-multilingual-cased-v1` (el del apunte), pero la práctica de U2 usa `intfloat/multilingual-e5-small`.
   → Usamos `distiluse` como modelo principal. e5-small queda como segundo modelo opcional: está en MTEB y ya lo conocemos.
6. **Los géneros vienen en orden alfabético** en el 100 % de los libros (pasa lo mismo en el dataset de las prácticas). "El primer género" no significa nada, y "Novela" (83 libros) es un formato, no un tema.
   → Para colorear la proyección (parte D) o evaluar el clustering hay que **elegir la etiqueta a propósito** (ver la sección 8).
7. **La parte avanzada "Doc2Vec"** dice que es "el modelo de la Unidad 2" que entrena vectores de documento, pero el apunte solo lo menciona como hito histórico, sin código.
   → Si la elegimos, usamos `gensim.models.Doc2Vec` (gensim sí es de la cátedra), sabiendo que no hay ejemplo en el material.
8. **No fijar el `numpy==1.23.5` del apunte:** el enunciado lo aclara y `P2/requirements.txt` ya está así.

## 4. Lo que ya sabemos del corpus

| Dato | Valor | Por qué importa |
|---|---|---|
| Libros | 200 (categoría "Los más comentados") | Corpus chico: TF-IDF y Word2Vec propio van a sufrir |
| Géneros por libro | 1 → 31 libros · 2 → 103 · 3 → 56 · 4 o más → 10 | **Multi-etiqueta**: afecta la proyección, el clustering y la definición de "relevante" |
| Géneros más frecuentes | Novela 83, Fantástico 51, Intriga 33, Terror 27, Romántico 27, Ciencia ficción 26, Drama 26, Juvenil 25 | El piso de azar depende de esto (sección 7) |
| Largo de la sinopsis | mediana 136 palabras · p90 218 · máximo 455 | Medido en la parte C: con su límite de 128 tokens, **`distiluse` trunca 178 de las 200 sinopsis (89 %)** |
| Tamaño total | ~29.800 tokens, ~6.900 palabras distintas | Muy poco para entrenar Word2Vec: SBW se entrenó con miles de millones de palabras |
| Series | 89 libros en 67 series (Harry Potter: 4 tomos) | El problema del "tomo 1 → tomos 2 a 7" de la parte avanzada de recomendación |
| Autores | Stephen King 12, Brandon Sanderson 9, Sarah J. Maas 5 | Riesgo de que "similar" signifique "del mismo autor" |
| Gallego o catalán | Ninguna: `langdetect` (U3) detecta español en las 200 | La pregunta del enunciado no aplica a nuestro corpus |
| Libros repetidos | 5 pares: *1984*, *Cien años de soledad* y *Rebelión en la granja* (dos ediciones, con sinopsis distintas); *El imperio final* (y su edición revisada); *Sapiens* = *De animales a dioses* (sinopsis idéntica) | En `queries.json`, las dos ediciones son relevantes. Los pares con sinopsis distintas son una **prueba natural** para la parte D: un buen modelo semántico debería ponerlos cerca. En recomendación, la otra edición es lo primero que hay que excluir |

## 5. Plan por partes

**Fase 1** = ahora, con CSV y DataFrames. **Fase 2** = cuando se vea pgvector y llegue el Anexo A.

### Parte 0 — Análisis inicial del corpus · Fase 1
- Responder las cuatro preguntas del bloque pegado, **con nuestros datos**:
  1. **Estabilidad de TF-IDF:** comparar los términos característicos con submuestras de distinto tamaño (por ejemplo, 50, 100 y 200 libros) y ver cuánto cambian.
  2. **Sesgo promocional:** frases de marketing ("best seller", "la saga que…") que un clasificador aprendería en lugar del género.
  3. **Multi-etiqueta:** por qué la accuracy de multi-clase no alcanza (una predicción puede acertar a medias).
  4. **Idioma:** detectarlo con `langdetect`, como en U3, y reportar si hay sinopsis en otros idiomas.
- Documentar las decisiones de preprocesamiento como **pérdidas deliberadas de información** (minúsculas, tildes, puntuación, stopwords).

### Parte A — Corpus en dos versiones · Fase 1
- **Limpia** (minúsculas, sin puntuación, sin stopwords de NLTK y tokenizada): para TF-IDF y Word2Vec.
- **Cruda** (texto natural): para el modelo de oración, que usa el orden y las palabras funcionales.
- Escribir en el notebook **por qué** cada modelo recibe una versión distinta: el preprocesamiento pertenece al modelo, no al corpus.

### Parte B — Word2Vec propio contra SBW · Fase 1
- **Propio:** `gensim.models.Word2Vec` sobre las 200 sinopsis limpias. Justificar cada parámetro:
  - `vector_size`: chico (por ejemplo, 100), porque hay pocos datos.
  - `window`: del orden de 5.
  - `min_count`: bajo (1 o 2); si no, el vocabulario desaparece.
  - `sg=1`: skip-gram suele andar mejor que CBOW con corpus chicos.
  - Aclarar qué hace `negative` (negative sampling), que el enunciado marca como tema nuevo.
- **SBW:** `KeyedVectors.load_word2vec_format(..., binary=True)`, como en el apunte.
- **Vecinos de al menos 4 palabras del dominio** (por ejemplo, *dragón*, *asesinato*, *amor*, *magia*), **lado a lado** en los dos modelos. Lo esperable es que el modelo propio dé vecinos pobres por falta de datos: hay que decirlo y explicarlo.
- **Vector de documento:** promedio de los vectores de palabra.
  - Explicar qué se pierde: el orden, las negaciones y el peso relativo de las palabras.
  - Decidir qué hacer con las palabras fuera del vocabulario: si **ninguna** palabra de un documento está en el vocabulario, el promedio no existe (vector nulo o `NaN`). Hay que detectarlo, y es lo que pide la parte E.

### Parte C — Modelo de oración (SBERT) · Fase 1
- `SentenceTransformer("distiluse-base-multilingual-cased-v1")` sobre el texto **crudo**.
- Reportar:
  - la **dimensión** (512);
  - el **límite de tokens** (`model.max_seq_length`; según la ficha del modelo, 128);
  - **cuántos documentos se truncan.** El modelo no lo avisa: hay que tokenizar cada sinopsis con `model.tokenizer` y contar cuántas superan el límite.
- Guardar los embeddings en disco (`.npy`), como recomienda el enunciado.

### Parte D — Comparación y visualización · Fase 1
- **Rankings lado a lado** para al menos 3 consultas, con TF-IDF, el promedio de word vectors y SBERT. La práctica de U2 (ejercicio 6) tiene el formato.
- **Distribución de similitudes entre pares al azar** para cada modelo: media, desvío y rango.
  - Ya vimos en la práctica de U2 que en E5 todo se parece a todo (0,86 a 0,89): un espacio así ordena, pero no discrimina.
  - Comparar si centrar los embeddings cambia algo, como en la práctica.
- **Proyección 2D** coloreada por género:
  - Con **PCA**, informar la varianza explicada (en la práctica de U2 fue del 5,8 % con 384 dimensiones).
  - Con **t-SNE**, informar la `perplexity` y advertir que las distancias entre clusters no se interpretan.
  - Con 200 libros, t-SNE corre en segundos. Usar una `perplexity` menor que la habitual de 30, porque hay pocos puntos.

### Parte E — Persistencia e indexado · Fase 2
Lo que pide: una tabla por modelo (`vector(300)` para word vectors, `vector(512)` para SBERT), índice HNSW con la *opclass* del operador que se use (coseno: `vector_cosine_ops` con `<=>`) y manejo de nulos antes de insertar.

**Lo que se puede dejar listo en la fase 1:**
- vectores normalizados;
- una función que descarte o corrija los vectores con norma 0 o valores no finitos (`np.isfinite`);
- los embeddings guardados en `.npy`.

**Para el informe:** por qué no pueden convivir dos dimensiones en la misma columna indexada (el tipo `vector(n)` fija `n`, y el índice compara vectores del mismo largo).

### Parte F — Búsqueda semántica · Fase 1 → Fase 2
- **Fase 1:** `buscar(consulta, k, genero=None)` con numpy (coseno contra la matriz de embeddings) y un filtro opcional por género sobre el DataFrame. Es la referencia para validar la versión SQL.
- **Fase 2:** la misma función, pero con la similitud **en SQL** (`ORDER BY embedding <=> %s LIMIT k`) y el filtro en el `WHERE`. Las credenciales van en `P2/.env`, con `python-dotenv` (ya está en los requirements).
- **Para el informe:** con un índice aproximado (HNSW) y un filtro selectivo, el índice devuelve sus candidatos más cercanos y **después** se filtra, así que pueden quedar menos de `k` resultados (se pierde recall). Opciones: subir `hnsw.ef_search` o buscar sin índice cuando el filtro es muy selectivo. Con 200 libros, la búsqueda exacta es instantánea, y conviene decirlo.

## 6. Evaluación — el núcleo del TP · Fase 1

1. **Escribir `queries.json` ANTES de ver resultados.** Es lo único que no se automatiza y lo que más pesa. Definir qué es relevante después de ver qué devolvió el modelo es hacerse trampa.
2. **Al menos 10 consultas**, de tipos variados:
   - temáticas ("un mundo mágico con dragones");
   - de trama ("una investigación de asesinato en un pueblo");
   - **al menos una sin ninguna palabra en común con los libros relevantes.** Es el caso donde TF-IDF no puede ganar.
3. Formato propuesto:
   ```json
   [
     {"id": "q01",
      "consulta": "una historia de piratas en el Caribe",
      "relevantes": ["Título exacto 1", "Título exacto 2"],
      "tipo": "sin palabras en común"}
   ]
   ```
   Los títulos sirven como identificador, porque en el corpus no hay títulos repetidos.
4. **precision@k** (proponemos k = 5) para TF-IDF, el promedio de word vectors, SBERT y **el azar**.
   - El piso de azar de una consulta con `R` libros relevantes es `R / 200`: es lo que acierta, en promedio, un ranking aleatorio. Con "Novela" en 83 libros, una consulta genérica de novela tiene un piso altísimo.
5. **Discutir qué NO mide precision@k:**
   - no mira el orden dentro del top-k;
   - ignora los relevantes que quedan fuera del top-k (recall);
   - depende de cuántos relevantes tenga cada consulta.

   Si TF-IDF empata o gana en algunas consultas, se explica por qué: no se cambia la métrica.

## 7. Parte avanzada (elegir una)

| Opción | ¿Se puede en la fase 1? | Comentario |
|---|---|---|
| **Clustering** | ✅ | Ya practicado en U2 (K-Means, silhouette, ARI). La multi-etiqueta da para discutir por qué un clustering duro sale penalizado |
| **Recomendación** | ✅ | Hay 89 libros en series y autores con muchos libros: la discusión de "qué excluir" (mismos tomos, mismo autor) sale con datos reales |
| Chunking | ✅ | Ataca el truncado de la parte C (más de la mitad del corpus) |
| Doc2Vec | ✅ | Sin ejemplo en el material, y `infer_vector()` es estocástico |
| Búsqueda híbrida | ❌ fase 2 | Necesita el full-text de Postgres (`ts_rank`) |
| RAG | ⚠️ | Necesita un LLM; U3 usa LLMs para sentimiento y traducción |

**Recomendación:** Clustering o Recomendación. Las dos se pueden hacer ya, tienen base en las prácticas y generan discusión con nuestros propios datos.

## 8. Decisiones

**Tomadas:**
- **Libros repetidos:** se dejan los 5 pares en el corpus y se anotan juntos en `queries.json` (el notebook lo valida). Los pares con sinopsis distintas se usan como prueba en la parte D.
- **Etiqueta para la proyección:** un panel por género presente, en lugar de elegir un solo género por libro. Respeta la multi-etiqueta y evita depender del orden alfabético.
- **k de precision@k:** 5 (es un parámetro del notebook).
- **Promedio de word vectors para la fase 2:** SBW. La parte B mostró que el Word2Vec propio no aprende significado con 200 sinopsis.

**Pendientes:**
1. **Parte avanzada:** Clustering o Recomendación. Las dos se pueden hacer en la fase 1; la decisión puede esperar a la evaluación.
2. **Segundo modelo de oración:** ¿agregamos e5-small, además de `distiluse`? Su límite de 512 tokens evitaría casi todo el truncado de la parte C.
3. **Reparto del trabajo** entre los cuatro integrantes (sección 10).

## 9. Preguntas para la cátedra

1. ¿Pueden compartir el **notebook guía** `TP2_embeddings_busqueda_semantica.ipynb` y el **Anexo A** de Supabase?
2. ¿Cuál es la **fecha de entrega**?
3. Las partes E y F y la base en Supabase, ¿se exigen en esta entrega o cuando se vea el tema?
4. El bloque del principio de la sección 4 (12 documentos y preguntas sueltas), ¿hay que responderlo?
5. ¿Se puede usar `multilingual-e5-small` como segundo modelo de oración?

## 10. Orden de trabajo sugerido

| Paso | Qué | Depende de | Paralelizable |
|---|---|---|---|
| 1 | Bajar SBW · leer el corpus · **escribir `queries.json`** | — | Sí: las consultas se reparten. Para elegir consultas y relevantes está el **[listado del corpus](listado_corpus.md)**, con un índice por género y una ficha por libro |
| 2 | Parte 0 y parte A | 1 | — |
| 3 | TF-IDF, `buscar()` en numpy y evaluación con el piso de azar | 2 | Sí, con el paso 4 |
| 4 | Parte B (Word2Vec y SBW) y parte C (SBERT) | 2 | Sí: una persona cada una |
| 5 | Parte D y precision@k de todos los modelos | 3, 4 | — |
| 6 | Parte avanzada | 4 | — |
| 7 | **Fase 2:** Supabase, partes E y F | Material de la cátedra | — |
| 8 | Informe | Todo | Ir anotando **casos de falla** desde el paso 3 |

**Para el informe, juntar desde el principio:**
- casos donde la búsqueda falló, con una hipótesis del porqué (sin esto, el informe está incompleto);
- consultas donde TF-IDF gana o empata;
- criterios para elegir el modelo de producción: costo, privacidad, reproducibilidad y dependencia de terceros;
- un párrafo que declare para qué usamos asistentes de IA (lo pide la sección 9 del enunciado).

## 11. Relación con U3

| Tema de U3 | Dónde ayuda en el TP2 |
|---|---|
| Métricas de similitud (coseno, Jaccard) | Parte D: Jaccard sobre conjuntos de palabras como otra línea de base léxica |
| Detección de idioma (`langdetect`) | Parte 0: la pregunta de las sinopsis en gallego o catalán |
| NER (spaCy, Stanza) | Parte A: el ejemplo de `Madrid` contra `madrid` al pasar a minúsculas |
| Clasificación con TF-IDF contra embeddings | Parte 0: el sesgo promocional; parte avanzada: clustering |
| Búsqueda semántica y recomendación (`util.semantic_search`, ejercicio 6.4) | Parte F y parte avanzada: recomendación |
| LLMs de propósito general | Parte avanzada: RAG |
