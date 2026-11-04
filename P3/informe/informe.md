## 1. ¿Qué detectores usamos, qué contaminación encontró cada uno y qué costo tiene un falso positivo?

Medimos cada detector en la parte de prueba de la muestra etiquetada (150 libros, 30 contaminados):

| Detector | Qué contaminación encuentra | Precisión | Recall | F1 |
|---|---|---|---|---|
| Regex | Enlaces con `http` o `www`, correos y teléfonos | 1,00 | 0,40 | 0,57 |
| Regex sobre el texto normalizado | Además, enlaces disimulados | 1,00 | 0,63 | 0,78 |
| Idioma por oración | Mensajes en otro idioma | 0,89 | 0,27 | 0,41 |
| Clasificador con TF-IDF | Frases que repiten palabras de la muestra | 1,00 | 0,90 | 0,95 |
| Clasificador con embeddings | Frases promocionales por su sentido | 0,95 | 0,60 | 0,73 |
| Libros copiados | Libros que copian la sinopsis de otro | 1,00 | 0,10 | 0,18 |
| Combinación (sin el de idioma) | | 0,97 | 1,00 | 0,98 |

El reconocimiento de entidades (spaCy) sirve para explicar y no para detectar: en el texto insertado predominan las entidades MISC (formatos y marcas, como *PDF* o *EpubMax*), pero MISC también es frecuente en las sinopsis limpias.

Un falso positivo es un libro legítimo que sale del catálogo y nunca se va a recomendar. Por eso elegimos el umbral de los clasificadores con precisión 0,97 en desarrollo, y no 0,90: la muestra tiene un 20 % de contaminados y el catálogo bastante menos, así que ahí la misma regla marca más libros legítimos por cada contaminado. Por la misma razón dejamos afuera el detector de idioma: en desarrollo tiene precisión 0,80 y encuentra solo 8 de los 70 contaminados, y ninguno de los 82 libros que marca por su cuenta en el catálogo tiene un mensaje insertado. En el catálogo, los detectores marcan 363 de 8.588 libros (4,2 %). Con 11 más que tienen una plantilla promocional que encontramos a mano, sin medir en prueba, quedan 374 sospechosos y un catálogo limpio de 8.214 libros.

## 2. ¿Qué representa la etiqueta `interes` y quién realizó las valoraciones?

`interes` es la respuesta del lector a «¿Me interesaría leer este libro?» después de leer el título y la sinopsis: 1 si le interesaría y 0 si no. Un libro sin valorar tiene preferencia desconocida, no un 0. Representa la intención de leer, no si el libro le gustaría al terminarlo.

Las valoraciones las hizo Josías Calabozo, integrante del grupo. Recorrió en orden los primeros 300 libros del catálogo limpio mezclado con `random_state=42` y dio 283 respuestas, 44 con 1 y 239 con 0; otros 17 quedaron sin valorar. No encontró libros contaminados que la auditoría no hubiera detectado.

## 3. ¿Cómo se compararon TF-IDF y embeddings? ¿En qué tarea fue mayor la diferencia y por qué?

En las dos tareas comparamos el F1 en prueba. Al detectar contaminación, a igual precisión en desarrollo, TF-IDF fue mejor: F1 de 0,95 contra 0,73, con recall 0,90 contra 0,60. Encontró 10 contaminados de prueba que el de embeddings no encontró, y el de embeddings, uno solo que TF-IDF no. El spam de la muestra repite plantillas, y TF-IDF las reconoce palabra por palabra, incluso con una dirección disimulada adentro. El de embeddings generaliza mejor a frases nuevas con el mismo sentido: en el catálogo, 60 de los libros que marca solo él tienen seis plantillas promocionales que no están en la muestra, en español, inglés y portugués.

Al clasificar preferencias el resultado se invierte y la diferencia es mayor: el F1 de la clase 1 en prueba es de 0,44 con embeddings y de 0 con TF-IDF, que predijo un solo 1 y se equivocó; en la validación cruzada, la media es de 0,29 contra 0,03. El spam repite palabras literales, y TF-IDF las aprovecha. El interés del lector depende del tema y no de palabras exactas: con 226 libros de entrenamiento, TF-IDF tiene 9.083 columnas y el 68 % de las palabras aparece en un solo libro, mientras que los embeddings resumen el sentido de cada sinopsis en 384 dimensiones aprendidas antes, con muchos otros textos.

## 4. ¿Algún clasificador mejoró las recomendaciones por similitud?

Sí, los dos. Sobre los 57 libros de prueba, la precision@5 fue de 0,60 con embeddings, de 0,20 con TF-IDF y de 0,00 con la similitud con el perfil (el promedio de los embeddings de los 35 libros de interés de entrenamiento), contra 0,16 del azar. Con el perfil, el primer libro de interés queda séptimo. Cada posición vale 0,20: el de embeddings supera al perfil por tres libros y el de TF-IDF, por uno. Con 9 libros de interés en prueba, el resultado es orientativo.

## 5. ¿Qué error encontraron y qué límite tiene el experimento?

En la auditoría, los clasificadores marcan algunas oraciones legítimas que le hablan al lector: en prueba, el de embeddings marca *Diario emprendedor* por «…que encontrarás al final de cada capítulo.». La regex marca cuatro libros que citan sitios reales, como `www.xkcd.com`, y el detector de copias, dos libros legítimos cargados dos veces con autores distintos. Ningún detector encontró la plantilla «Aprovechá el descuento del 70 % solo por hoy…»: es un mensaje de precio, sin enlace y distinto de los de la muestra.

En el recomendador, *Imperium*, una novela sobre Cicerón, es un falso positivo del clasificador de embeddings, que acertó 4 de los 9 libros que marcó con 1. El resumen de *Trilogía Mistborn* perdió de qué trata la saga y se quedó con una cita de prensa.

Los límites:

- Las métricas de la auditoría son optimistas: la muestra está enriquecida y sus mensajes son los mismos con los que desarrollamos los detectores. En el catálogo la precisión es menor, y un mensaje que no se parezca a los de la muestra puede quedar sin detectar.
- Hay un solo lector, con 283 valoraciones y 44 de interés. En prueba quedan 9, y cada uno mueve el recall en 0,11: las métricas son orientativas, y en la validación cruzada el F1 del clasificador de embeddings tiene un desvío de 0,14.
- `interes` mide la intención de leer antes de hacerlo, no si el libro le gustó al lector.

## Uso de asistentes de IA

Usamos un asistente de IA para explorar los datos, armar el código del notebook y redactar un primer borrador de las interpretaciones y de este informe. El grupo revisó el procedimiento, los resultados y las conclusiones, y es responsable de su contenido. Las valoraciones del paso 3 son del lector elegido: el asistente no intervino en ellas.
