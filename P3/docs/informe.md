> **Borrador.** Las respuestas sobre la auditoría (paso 2) usan los resultados del notebook. Las que dependen de las valoraciones del lector (pasos 3 a 8) están marcadas como pendientes.

## 1. ¿Qué detectores usamos, qué contaminación encontró cada uno y qué costo tiene un falso positivo?

Medimos cada detector en la parte de prueba de la muestra etiquetada (150 libros, 30 contaminados):

| Detector | Qué contaminación encuentra | Precisión | Recall |
|---|---|---|---|
| Regex de enlaces, correos y teléfonos | Enlaces explícitos (`https://`, `www.`, correos, teléfonos) | 1,00 | 0,40 |
| Regex sobre el texto normalizado | Además, enlaces disimulados: letras cirílicas, caracteres invisibles, «punto» en lugar de «.», letras separadas | 1,00 | 0,63 |
| Idioma por oración (`langdetect`) | Mensajes en inglés y portugués | 0,89 | 0,27 |
| Clasificador de oraciones con TF-IDF | Frases promocionales que repiten las de la muestra | 1,00 | 0,90 |
| Clasificador de oraciones con embeddings | Frases promocionales por su sentido, también las nuevas | 1,00 | 0,63 |
| Libros copiados (vecino más cercano y Jaccard) | Libros inventados que copian la sinopsis de otro | 1,00 | 0,10 |
| **Combinación** (todos menos el de idioma) | | **1,00** | **1,00** |

El reconocimiento de entidades (spaCy) no lo usamos para detectar: en el texto insertado aparecen sobre todo entidades MISC (formatos y marcas, como *PDF* o *EpubMax*), pero MISC también es frecuente en las sinopsis limpias. Sirve para explicar qué promociona un libro que ya marcó otro detector.

**El costo de un falso positivo:** cada libro legítimo que marcamos sale del catálogo y nunca se va a recomendar. Por eso:

- **Pedimos precisión 0,97 en desarrollo** para elegir el umbral de los clasificadores, y no 0,90. La muestra tiene un 20 % de contaminados y el catálogo, bastante menos, así que con la misma regla en el catálogo hay más falsos positivos por cada acierto.
- **Dejamos afuera el detector de idioma.** En prueba no encuentra ningún contaminado que no encuentren los demás, y en el catálogo, por su cuenta, marca 64 libros que son falsos positivos: oraciones en español con títulos en inglés o escritas en mayúsculas.

Con esas decisiones marcamos **406 de los 8.625 libros del catálogo (4,7 %)**. En una primera versión, con umbrales a precisión 0,90 y con el detector de idioma, marcábamos 694.

## 2. ¿Qué representa la etiqueta `interes` y quién realizó las valoraciones?

`interes` es la respuesta del lector a «¿Me interesaría leer este libro?», después de leer el título y la sinopsis: 1 si le interesaría, 0 si no. Cuando no pudo decidir, el libro queda sin valorar: es una preferencia desconocida, no un 0. Representa la intención de leer **antes** de leer el libro: no mide su calidad ni si le gustaría al terminarlo.

> **Pendiente:** quién fue el lector, cuántos libros vio y cuántos 1, 0 y abstenciones dio.

## 3. ¿Cómo se compararon TF-IDF y embeddings? ¿En qué tarea fue mayor la diferencia y por qué?

**Al detectar contaminación**, a igual precisión en desarrollo, TF-IDF encontró más contaminados de prueba (recall 0,90 contra 0,63). En la muestra el spam repite plantillas literales, y TF-IDF las reconoce palabra por palabra, incluso con una dirección disimulada adentro. En el catálogo, en cambio, cada uno mostró su límite:

- Lo que marcó **solo el de embeddings** (84 libros) incluye mensajes que no estaban en la muestra, como «Join millions of readers and claim your free premium membership…» o «Promoción exclusiva para nuevos usuarios…»: reconoce el sentido promocional aunque cambien las palabras.
- Lo que marcó **solo TF-IDF** (38 libros) son en su mayoría contratapas legítimas en segunda persona («¡Tu bebé te lo agradecerá!»): aprendió que «tu» y «te» son señal de spam.

**Al clasificar preferencias:**

> **Pendiente:** F1 de cada modelo en prueba y en la validación cruzada, y en qué tarea fue mayor la diferencia.

## 4. ¿Algún clasificador mejoró las recomendaciones por similitud?

> **Pendiente:** precision@5 de las tres listas frente al azar.

## 5. ¿Qué error encontraron y qué límite tiene el experimento?

**Errores de la auditoría:**

- El clasificador TF-IDF confunde la segunda persona con spam.
- El detector de idioma confunde con otro idioma las oraciones en mayúsculas o con títulos en inglés.
- El detector de copias marcó dos libros legítimos que tienen casi la misma sinopsis que otro atribuido a otro autor (*Richard P. Feynman. La física de las palabras* y *Las grandes preguntas de los niños*).

> **Pendiente:** un error del recomendador (por ejemplo, un falso positivo en prueba) y qué lo explica.

**Límites:**

- **La precisión y el recall de 1,00 de la combinación son optimistas.** La muestra está enriquecida y sus mensajes son los mismos con los que desarrollamos los detectores. En el catálogo hay mensajes nuevos (ver la pregunta 3), y los que no se parezcan a ninguno de la muestra pueden haber quedado sin detectar.
- **El criterio de versiones del paso 1 es conservador:** dos ediciones de una obra con contratapas distintas quedan como libros separados.

> **Pendiente:** los límites del recomendador (un solo lector, pocas valoraciones, 20 libros de prueba).

## Uso de asistentes de IA

Usamos un asistente de IA para explorar los datos, armar el código del notebook y redactar un primer borrador de las interpretaciones y de este informe. El grupo revisó el procedimiento, los resultados y las conclusiones, y es responsable de su contenido. Las valoraciones del paso 3 son del lector elegido: el asistente no intervino en ellas.
