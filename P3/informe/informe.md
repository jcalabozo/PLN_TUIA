## 1. ¿Qué detectores usamos, qué contaminación encontró cada uno y qué costo tiene un falso positivo?

Medimos cada detector en la parte de prueba de la muestra etiquetada (150 libros, 30 contaminados):

| Detector | Qué contaminación encuentra | Precisión | Recall | F1 |
|---|---|---|---|---|
| Regex de enlaces, correos y teléfonos | Enlaces explícitos (`https://`, `www.`), correos y teléfonos | 1,00 | 0,40 | 0,57 |
| Regex sobre el texto normalizado | Además, enlaces disimulados: letras cirílicas, caracteres invisibles, «punto» en lugar de «.», letras separadas | 1,00 | 0,63 | 0,78 |
| Idioma por oración (`langdetect`) | Mensajes en otro idioma | 0,89 | 0,27 | 0,41 |
| Clasificador de oraciones con TF-IDF | Frases promocionales que repiten palabras de la muestra | 1,00 | 0,90 | 0,95 |
| Clasificador de oraciones con embeddings | Frases promocionales por su sentido, también las nuevas | 0,95 | 0,60 | 0,73 |
| Libros copiados (vecino más cercano y Jaccard) | Libros inventados que copian la sinopsis de otro | 1,00 | 0,10 | 0,18 |
| Combinación (todos menos el de idioma) | | 0,97 | 1,00 | 0,98 |

El reconocimiento de entidades (spaCy) no lo usamos para detectar: en el texto insertado predominan las entidades MISC (formatos y marcas, como *PDF* o *EpubMax*), pero MISC también es frecuente en las sinopsis limpias. Sirve para explicar qué promociona un libro que ya marcó otro detector.

Un falso positivo es un libro legítimo que sale del catálogo y nunca se va a recomendar. Por eso elegimos el umbral de los clasificadores con precisión 0,97 en desarrollo, y no 0,90: la muestra tiene un 20 % de contaminados y el catálogo bastante menos, así que ahí la misma regla marca más libros legítimos por cada contaminado. Por la misma razón dejamos afuera el detector de idioma: en desarrollo tiene precisión 0,80 y encuentra solo 8 de los 70 contaminados, y ninguno de los 82 libros que marca por su cuenta en el catálogo tiene un mensaje insertado. También limitamos los dominios sin `http` ni `www` a las terminaciones de los fragmentos de desarrollo (`.test`, `.invalid` y `.example`), porque la única `.com` de desarrollo estaba en una sinopsis limpia. Los detectores marcan 363 de los 8.588 libros del catálogo (4,2 %). Al revisar las oraciones repetidas en libros no marcados encontramos una plantilla promocional que ninguno detectó, en 11 libros, que marcamos a mano (este paso no está medido en la parte de prueba): en total quedan 374 sospechosos y un catálogo limpio de 8.214 libros.

## 2. ¿Qué representa la etiqueta `interes` y quién realizó las valoraciones?

`interes` es la respuesta del lector a «¿Me interesaría leer este libro?» después de leer el título y la sinopsis: 1 si le interesaría y 0 si no. Cuando no pudo decidir, el libro queda sin valorar: es una preferencia desconocida, no un 0. Representa la intención de leer antes de leer el libro, no su calidad ni si le gustaría al terminarlo.

Las valoraciones las hizo Josías Calabozo, integrante del grupo. Recorrió en orden los primeros 300 libros del catálogo limpio mezclado con `random_state=42` y dio 283 respuestas: 44 con 1 y 239 con 0. Otros 17 quedaron sin valorar, y no encontró libros contaminados que la auditoría no hubiera detectado.

## 3. ¿Cómo se compararon TF-IDF y embeddings? ¿En qué tarea fue mayor la diferencia y por qué?

En las dos tareas comparamos el F1 en prueba. Al detectar contaminación, a igual precisión en desarrollo (0,97), TF-IDF fue mejor: F1 de 0,95 contra 0,73, con recall 0,90 contra 0,60. De los contaminados de prueba, TF-IDF encontró 10 que el de embeddings no encontró, y el de embeddings, uno solo que TF-IDF no. El spam de la muestra repite plantillas, y TF-IDF las reconoce palabra por palabra, incluso con una dirección disimulada adentro. En el catálogo encontró dos libros con «Si te gustó esta reseña, compartila…» pegado sin punto a la oración anterior, que el de embeddings no marcó porque la frase queda dentro de una oración más larga. El de embeddings generaliza mejor a frases nuevas: marca las tres frases promocionales que inventamos, y en el catálogo, 60 de los libros que marca solo él tienen seis plantillas que no están en la muestra, como «Sumate a la comunidad…», en español, inglés y portugués.

Al clasificar preferencias el resultado se invierte y la diferencia es mayor: el F1 de la clase 1 en prueba es de 0,44 con embeddings y de 0 con TF-IDF, que predijo un solo 1 y se equivocó, y en la media de la validación cruzada, de 0,29 contra 0,03. La explicación es la misma, vista desde lados opuestos. El spam repite palabras literales, y TF-IDF las aprovecha. El interés del lector depende del tema y no de palabras exactas: con 226 libros de entrenamiento, TF-IDF tiene 9.083 columnas y el 68 % de las palabras aparece en un solo libro, mientras que los embeddings resumen el sentido de cada sinopsis en 384 dimensiones aprendidas antes, con muchos otros textos.

## 4. ¿Algún clasificador mejoró las recomendaciones por similitud?

Sí, los dos. Sobre los 57 libros de prueba, la precision@5 fue de 0,60 con embeddings, de 0,20 con TF-IDF y de 0,00 con la similitud con el perfil, contra 0,16 del azar. El perfil, el promedio de los embeddings de los 35 libros de interés de entrenamiento, casi no separa unos libros de otros: las similitudes de los 57 van de 0,868 a 0,932, y el primer libro de interés queda séptimo. Los clasificadores aprenden además de los 191 libros sin interés. Con cinco posiciones cada libro vale 0,20: el de embeddings supera al perfil por tres libros y el de TF-IDF, por uno, y con 9 libros de interés en prueba el resultado es orientativo.

## 5. ¿Qué error encontraron y qué límite tiene el experimento?

En la auditoría, el clasificador de embeddings marca en prueba un libro legítimo, *Diario emprendedor*, por una oración que le habla al lector («…que encontrarás al final de cada capítulo.»), y en el catálogo los dos clasificadores, sobre todo el de embeddings, marcan oraciones legítimas que le hablan al lector del libro. La regex marca cuatro libros que citan sitios reales (`www.perezreverte.com`, `www.xkcd.com` y `www.depechemode.com`), y el detector de copias, dos libros legítimos cargados dos veces con autores distintos. Ningún detector encontró la plantilla «Aprovechá el descuento del 70 % solo por hoy…»: es un mensaje de precio, sin enlace y distinto de los de la muestra, y el de embeddings le da 0,69, debajo de su umbral de 0,774.

En el recomendador, *Imperium*, una novela sobre Cicerón, es un falso positivo del clasificador de embeddings, que acertó 4 de los 9 libros que marcó con 1. El resumen de *Trilogía Mistborn*, una de las recomendaciones del catálogo, perdió de qué trata la saga y se quedó con una cita de prensa.

Los límites:

- Las métricas de la auditoría son optimistas: la muestra está enriquecida y sus mensajes son los mismos con los que desarrollamos los detectores, así que en el catálogo la precisión es menor, y un mensaje que no se parezca a los de la muestra puede quedar sin detectar, como la plantilla del descuento.
- Hay un solo lector y 283 valoraciones, con 44 de interés. En prueba quedan 9, y cada uno que el modelo acierta o falla mueve el recall en 0,11: las métricas son orientativas, y en la validación cruzada el F1 del clasificador de embeddings tiene un desvío de 0,14.
- `interes` mide la intención de leer antes de hacerlo, no si el libro le gustó al lector.

## Uso de asistentes de IA

Usamos un asistente de IA para explorar los datos, armar el código del notebook y redactar un primer borrador de las interpretaciones y de este informe. El grupo revisó el procedimiento, los resultados y las conclusiones, y es responsable de su contenido. Las valoraciones del paso 3 son del lector elegido: el asistente no intervino en ellas.
