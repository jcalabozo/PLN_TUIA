# Plan de trabajo — TP2: embeddings y búsqueda semántica

> Documento vivo: se actualiza a medida que avanzamos o que la cátedra comparte material. Última actualización: 2026-10-07.
>
> Enunciado: [Enunciado_TP2_embeddings.md](../Enunciado_TP2_embeddings.md) · Notebook: [TP2_calabozo_giuntoli_darruiz_dicarlo.ipynb](../TP2_calabozo_giuntoli_darruiz_dicarlo.ipynb) · Listado del corpus: [listado_corpus.md](listado_corpus.md)
>
> Los apuntes de la materia (exportados de Notion) y las prácticas resueltas están en [jcalabozo/tuia-nlp](https://github.com/jcalabozo/tuia-nlp).
>
> **2026-10-07 — La cátedra marcó en rojo lo que no hay que hacer:** las partes E y F (Postgres, pgvector, HNSW y búsqueda en SQL), las opciones de parte avanzada Clustering, Búsqueda híbrida, RAG y Chunking, las recomendaciones sobre el Anexo A y Supabase, y las filas «Uso de pgvector» (20 %) y «Parte avanzada» (15 %) de los criterios de evaluación. El clustering ya estaba hecho: esa versión del TP quedó guardada en la carpeta `TP2_BKP_Clustering/` de tuia-nlp.

## 1. En pocas palabras

El TP pide representar las sinopsis del corpus del TP1 con **embeddings** (palabra y oración), compararlos contra **TF-IDF** y, sobre todo, **demostrar con una evaluación honesta** si la representación nueva es mejor que la vieja.

| # | Entregable | Contenido |
|---|---|---|
| 1 | `TP2_apellido1_apellido2.ipynb` | Notebook ejecutado, con las salidas visibles |
| 2 | `queries.json` | Al menos 10 consultas, con los libros relevantes de cada una |
| 3 | `informe.pdf` | Hasta 3 páginas |
| 4 | ~~Base en Supabase~~ | No está en rojo, pero depende de la parte E, que sí: entendemos que no va (ver la sección 9) |

**Lo que más pesa:** el rigor de la evaluación (30 %): líneas de base, límites de la métrica y una interpretación que los resultados sostengan. Un pipeline que corre, sin piso de azar y sin discusión, saca menos que uno con peores resultados bien analizados.

## Estado del avance

- **Notebook:** [`TP2_calabozo_giuntoli_darruiz_dicarlo.ipynb`](../TP2_calabozo_giuntoli_darruiz_dicarlo.ipynb), ejecutado y con las salidas visibles.
- **Consultas:** [`queries.json`](../queries.json).
- **Borrador del informe:** [informe.md](informe.md).

**El notebook está completo.** Faltan la revisión del grupo, el informe en PDF y confirmar si se pide otra parte avanzada (sección 7).

| Parte | Estado |
|---|---|
| 0 · Análisis inicial (las cuatro preguntas) | ✅ |
| A · Corpus en dos versiones | ✅ |
| Línea de base TF-IDF y `buscar(consulta, modelo, k, genero)` | ✅ |
| B · Word2Vec propio contra SBW | ✅ |
| C · SBERT (`distiluse`) y e5-small, con el truncado de cada uno | ✅ |
| D · Similitudes al azar, ediciones repetidas, proyección 2D y rankings lado a lado | ✅ |
| `queries.json` (13 consultas) y evaluación con precision@5 | ✅ |
| Dos casos de falla analizados | ✅ |
| Parte avanzada | ❓ El clustering quedó afuera (backup en tuia-nlp). Falta confirmar si se pide Recomendación o Doc2Vec |
| Borrador del informe | ✅ Falta la revisión del grupo y pasarlo a PDF |
| E, F · pgvector, HNSW y SQL | ❌ Fuera del alcance |

**Resultados principales** (detallados en el notebook y en el informe):

- **precision@5 promedio:** SBERT y E5 0,400; TF-IDF 0,385; SBW 0,338; Word2Vec propio 0,277; azar 0,027. **Los modelos de oración empatan con TF-IDF**: la diferencia es de un solo libro en 65 posiciones evaluadas.
- **Sin palabras en común**, TF-IDF saca 0 y SBERT 0,40. **Con vocabulario compartido**, TF-IDF es muy fuerte: saca 1,0 en "amor prohibido".
- **`distiluse` trunca 178 de 200 sinopsis (89 %)**; **e5-small**, con 512 tokens de límite, solo 3.
- **El Word2Vec propio aprende co-ocurrencias de cada libro, no significado.** Con SBW, todo se parece a todo (0,87 ± 0,04 entre libros al azar).
- **Casos de falla:** con "el amor por los libros", SBERT y E5 devuelven solo novelas románticas. Con "un crimen en un lugar aislado", fallan todos.

**Próximos pasos:**

1. **El grupo revisa `queries.json`:** las consultas, los criterios y los casos límite, como *Cadáver exquisito* en q03. Si se cambia algo, se reejecuta la evaluación.
2. **El grupo revisa y completa el informe**, en especial el párrafo de uso de IA.
3. **Confirmar con la cátedra** si la parte avanzada sigue en pie (sección 9).
4. Pasar el informe a PDF, en hasta 3 páginas.

## 2. Qué tenemos y qué falta

| Material | Estado |
|---|---|
| Corpus (`P1/data/libros.csv`) | ✅ 200 libros, 13 columnas |
| Entorno (`P2/requirements.txt`) | ✅ gensim, sentence-transformers, nltk y `langdetect` (Unidad 3). `psycopg`, `pgvector` y `python-dotenv` eran para la parte E: se pueden sacar |
| Modelo `SBW-vectors-300-min5` (~1 GB) | ✅ Bajado en `P2/models/` (ignorado por git) desde [SBWCE](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5.bin.gz) |
| **Notebook guía** `TP2_embeddings_busqueda_semantica.ipynb` | ❌ **No fue compartido** (ver abajo) |
| Fecha de entrega | ❌ El enunciado la deja en blanco |

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
   → **Resuelto el 2026-10-07:** la cátedra marcó en rojo las partes E y F y las recomendaciones sobre Supabase. Todo se hace con el CSV y DataFrames. Quedaron sin marcar cosas que dependen de la base (el objetivo 4, la sección 3, el entregable 4, el requisito de la *opclass* y los descuentos por el índice y por insertar `NaN`): entendemos que caen con la parte E, pero lo preguntamos (sección 9).
4. **"El corpus del TP1 cargado en la tabla `books` de su csv"** mezcla tabla y CSV.
   → DataFrame desde `libros.csv`. La tabla `books` era de la parte E, que no va.
5. **El modelo de oración:** el TP pide arrancar con `distiluse-base-multilingual-cased-v1` (el del apunte), pero la práctica de U2 usa `intfloat/multilingual-e5-small`.
   → Usamos `distiluse` como modelo principal. e5-small queda como segundo modelo opcional: está en MTEB y ya lo conocemos.
6. **Los géneros vienen en orden alfabético** en el 100 % de los libros (pasa lo mismo en el dataset de las prácticas). "El primer género" no significa nada, y "Novela" (83 libros) es un formato, no un tema.
   → Para colorear la proyección (parte D) hay que **elegir la etiqueta a propósito** (ver la sección 8).
7. **La parte avanzada "Doc2Vec"** dice que es "el modelo de la Unidad 2" que entrena vectores de documento, pero el apunte solo lo menciona como hito histórico, sin código.
   → Si la elegimos, usamos `gensim.models.Doc2Vec` (gensim sí es de la cátedra), sabiendo que no hay ejemplo en el material.
8. **No fijar el `numpy==1.23.5` del apunte:** el enunciado lo aclara y `P2/requirements.txt` ya está así.

## 4. Lo que ya sabemos del corpus

| Dato | Valor | Por qué importa |
|---|---|---|
| Libros | 200 (categoría "Los más comentados") | Corpus chico: TF-IDF y Word2Vec propio van a sufrir |
| Géneros por libro | 1 → 31 libros · 2 → 103 · 3 → 56 · 4 o más → 10 | **Multi-etiqueta**: afecta la proyección y la definición de "relevante" |
| Géneros más frecuentes | Novela 83, Fantástico 51, Intriga 33, Terror 27, Romántico 27, Ciencia ficción 26, Drama 26, Juvenil 25 | El piso de azar depende de esto (sección 7) |
| Largo de la sinopsis | mediana 136 palabras · p90 218 · máximo 455 | Medido en la parte C: con su límite de 128 tokens, **`distiluse` trunca 178 de las 200 sinopsis (89 %)** |
| Tamaño total | ~29.800 tokens, ~6.900 palabras distintas | Muy poco para entrenar Word2Vec: SBW se entrenó con miles de millones de palabras |
| Series | 89 libros en 67 series (Harry Potter: 4 tomos) | El problema del "tomo 1 → tomos 2 a 7" de la parte avanzada de recomendación |
| Autores | Stephen King 12, Brandon Sanderson 9, Sarah J. Maas 5 | Riesgo de que "similar" signifique "del mismo autor" |
| Gallego o catalán | Ninguna: `langdetect` (U3) detecta español en las 200 | La pregunta del enunciado no aplica a nuestro corpus |
| Libros repetidos | 5 pares: *1984*, *Cien años de soledad* y *Rebelión en la granja* (dos ediciones, con sinopsis distintas); *El imperio final* (y su edición revisada); *Sapiens* = *De animales a dioses* (sinopsis idéntica) | En `queries.json`, las dos ediciones son relevantes. Los pares con sinopsis distintas son una **prueba natural** para la parte D: un buen modelo semántico debería ponerlos cerca. En recomendación, la otra edición es lo primero que hay que excluir |

## 5. Plan por partes

### Parte 0 — Análisis inicial del corpus
- Responder las cuatro preguntas del bloque pegado, **con nuestros datos**:
  1. **Estabilidad de TF-IDF:** comparar los términos característicos con submuestras de distinto tamaño (por ejemplo, 50, 100 y 200 libros) y ver cuánto cambian.
  2. **Sesgo promocional:** frases de marketing ("best seller", "la saga que…") que un clasificador aprendería en lugar del género.
  3. **Multi-etiqueta:** por qué la accuracy de multi-clase no alcanza (una predicción puede acertar a medias).
  4. **Idioma:** detectarlo con `langdetect`, como en U3, y reportar si hay sinopsis en otros idiomas.
- Documentar las decisiones de preprocesamiento como **pérdidas deliberadas de información** (minúsculas, tildes, puntuación, stopwords).

### Parte A — Corpus en dos versiones
- **Limpia** (minúsculas, sin puntuación, sin stopwords de NLTK y tokenizada): para TF-IDF y Word2Vec.
- **Cruda** (texto natural): para el modelo de oración, que usa el orden y las palabras funcionales.
- Escribir en el notebook **por qué** cada modelo recibe una versión distinta: el preprocesamiento pertenece al modelo, no al corpus.

### Parte B — Word2Vec propio contra SBW
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
  - Decidir qué hacer con las palabras fuera del vocabulario: si **ninguna** palabra de un documento está en el vocabulario, el promedio no existe (vector nulo o `NaN`). Hay que detectarlo: los requisitos técnicos piden manejar los vectores nulos o `NaN`.

### Parte C — Modelo de oración (SBERT)
- `SentenceTransformer("distiluse-base-multilingual-cased-v1")` sobre el texto **crudo**.
- Reportar:
  - la **dimensión** (512);
  - el **límite de tokens** (`model.max_seq_length`; según la ficha del modelo, 128);
  - **cuántos documentos se truncan.** El modelo no lo avisa: hay que tokenizar cada sinopsis con `model.tokenizer` y contar cuántas superan el límite.
- Guardar los embeddings en disco (`.npy`), como recomienda el enunciado.

### Parte D — Comparación y visualización
- **Rankings lado a lado** para al menos 3 consultas, con TF-IDF, el promedio de word vectors y SBERT. La práctica de U2 (ejercicio 6) tiene el formato.
- **Distribución de similitudes entre pares al azar** para cada modelo: media, desvío y rango.
  - Ya vimos en la práctica de U2 que en E5 todo se parece a todo (0,86 a 0,89): un espacio así ordena, pero no discrimina.
  - Comparar si centrar los embeddings cambia algo, como en la práctica.
- **Proyección 2D** coloreada por género:
  - Con **PCA**, informar la varianza explicada (en la práctica de U2 fue del 5,8 % con 384 dimensiones).
  - Con **t-SNE**, informar la `perplexity` y advertir que las distancias entre clusters no se interpretan.
  - Con 200 libros, t-SNE corre en segundos. Usar una `perplexity` menor que la habitual de 30, porque hay pocos puntos.

### Partes E y F — Fuera del alcance
La cátedra las marcó en rojo: no se persiste en Postgres ni se busca en SQL. `buscar(consulta, modelo, k, genero)` resuelve la similitud con numpy y filtra por género sobre el DataFrame. Con eso cubrimos el requisito técnico «búsqueda que combine similitud y filtro por metadata», que no fue marcado.

## 6. Evaluación — el núcleo del TP

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

| Opción | Estado | Comentario |
|---|---|---|
| Clustering | ❌ En rojo | Lo habíamos hecho: quedó en `TP2_BKP_Clustering/` de tuia-nlp |
| **Recomendación** | Sin marcar | Hay 89 libros en series y 5 ediciones repetidas: la discusión de "qué excluir" sale con datos reales. `buscar()` y los embeddings ya están |
| Doc2Vec | Sin marcar | Sin ejemplo en el material, y `infer_vector()` es estocástico |
| Chunking, Búsqueda híbrida, RAG | ❌ En rojo | — |

**Duda:** la fila «Parte avanzada (15 %)» de los criterios también está en rojo, pero Recomendación y Doc2Vec no. Puede querer decir que la parte avanzada ya no se pide, o que solo quedan esas dos. Hay que confirmarlo (sección 9). Si se pide, conviene **Recomendación**: es la que más aprovecha lo que ya tenemos.

## 8. Decisiones

**Tomadas:**
- **Libros repetidos:** se dejan los 5 pares en el corpus y se anotan juntos en `queries.json` (el notebook lo valida). Los pares con sinopsis distintas se usan como prueba en la parte D.
- **Etiqueta para la proyección:** un panel por género presente, en lugar de elegir un solo género por libro. Respeta la multi-etiqueta y evita depender del orden alfabético.
- **k de precision@k:** 5 (es un parámetro del notebook).

- **Parte avanzada:** clustering, hasta que la cátedra lo sacó (2026-10-07). Está guardado en `TP2_BKP_Clustering/` de tuia-nlp.
- **Segundo modelo de oración:** e5-small. Con su límite de 512 tokens evita casi todo el truncado de la parte C.
- **`queries.json`:** 13 consultas, con el criterio de relevancia escrito en cada una, definidas leyendo las sinopsis y commiteadas antes de correr la evaluación.

**Pendientes:**
1. **Reparto del trabajo** de lo que queda (revisión e informe) entre los cuatro integrantes.
2. **Parte avanzada:** si se sigue pidiendo, elegir entre Recomendación y Doc2Vec.

## 9. Preguntas para la cátedra

1. ¿Pueden compartir el **notebook guía** `TP2_embeddings_busqueda_semantica.ipynb`?
2. ¿Cuál es la **fecha de entrega**?
3. La fila «Parte avanzada (15 %)» está en rojo, pero las opciones Recomendación y Doc2Vec no: ¿hay que hacer una de esas dos, o la parte avanzada ya no se pide? ¿Cómo se reparte el 35 % de las filas marcadas?
4. El bloque del principio de la sección 4 (12 documentos y preguntas sueltas), ¿hay que responderlo?
5. ¿Se puede usar `multilingual-e5-small` como segundo modelo de oración?
6. El entregable 4 (base en Supabase), la sección 3 y algunos requisitos y descuentos (la *opclass*, insertar `NaN`) no están en rojo, pero dependen de la parte E: ¿también quedan afuera?

## 10. Orden de trabajo sugerido

| Paso | Qué | Depende de | Paralelizable |
|---|---|---|---|
| 1 | Bajar SBW · leer el corpus · **escribir `queries.json`** | — | Sí: las consultas se reparten. Para elegir consultas y relevantes está el **[listado del corpus](listado_corpus.md)**, con un índice por género y una ficha por libro |
| 2 | Parte 0 y parte A | 1 | — |
| 3 | TF-IDF, `buscar()` en numpy y evaluación con el piso de azar | 2 | Sí, con el paso 4 |
| 4 | Parte B (Word2Vec y SBW) y parte C (SBERT) | 2 | Sí: una persona cada una |
| 5 | Parte D y precision@k de todos los modelos | 3, 4 | — |
| 6 | Parte avanzada, si se pide | 4 | — |
| 7 | Informe | Todo | Ir anotando **casos de falla** desde el paso 3 |

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
| Clasificación con TF-IDF contra embeddings | Parte 0: el sesgo promocional |
| Búsqueda semántica y recomendación (`util.semantic_search`, ejercicio 6.4) | `buscar()` y la parte avanzada de recomendación |
