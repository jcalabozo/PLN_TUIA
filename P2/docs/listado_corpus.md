# Listado del corpus del TP2

> Generado con [`src/listado_corpus.py`](../src/listado_corpus.py) a partir de `P1/data/libros.csv` (200 libros, categoría "Los más comentados" de Lectulandia). Sirve para escribir `queries.json`: elegir consultas y decidir qué libros son relevantes para cada una. Ver la sección 6 del [plan de trabajo](plan_de_trabajo.md).

## Cómo usarlo

1. **Escribir las consultas antes de correr cualquier modelo.** Definir qué es relevante después de ver qué devolvió el buscador es hacerse trampa.
2. Para cada consulta, anotar **todos** los libros relevantes del corpus, no solo los primeros que aparezcan. El índice por género ayuda a no olvidarse de ninguno, pero la relevancia se decide leyendo la sinopsis: el género solo no alcanza.
3. Variar los tipos de consulta: temáticas ("un mundo mágico con dragones"), de trama ("una investigación de asesinato"), de tono ("algo que dé miedo").
4. Incluir **al menos una consulta que no comparta ninguna palabra** con las sinopsis de sus libros relevantes. Es el caso donde TF-IDF no puede ganar.
5. **Ojo con el piso de azar:** el azar acierta, en promedio, `relevantes / 200`. Una consulta con 50 libros relevantes tiene un piso de 0,25, y casi cualquier modelo la "aprueba". Conviene que la mayoría tenga pocos relevantes (de 2 a 15).
6. Usar el **título exacto**, tal como figura acá, para identificar cada libro en `queries.json`.

## ⚠️ Libros repetidos

Estos pares son **el mismo libro** con otro título o en otra edición. Si un libro de un par es relevante para una consulta, el otro también lo es: hay que anotar los dos en `queries.json`.

- 1984 (1) = 1984 (Trad. Miguel Temprano García) (2): sinopsis distintas
- Cien años de soledad (Edición conmemorativa) (21) = Cien años de soledad (Ed. Ilustrada) (20): sinopsis distintas
- Rebelión en la granja (168) = Rebelión en la granja (trad. Marcial Souto y Miguel Temprano García) (169): sinopsis distintas
- El imperio final (63) = El Imperio Final. (Ed. revisada) (64): sinopsis parecidas
- Sapiens (173) = De animales a dioses (32): **sinopsis idéntica**

Los pares con sinopsis distintas sirven además como prueba: un buen modelo semántico debería ponerlos cerca aunque las palabras no coincidan.

## Índice por género

Cada libro aparece en todos sus géneros. Entre paréntesis, la cantidad de libros; al lado de cada título, su número de ficha.

- **Novela** (83): 1984 (Trad. Miguel Temprano García) (2), A todos los chicos de los que me enamoré (3), After (5), Alas de sangre (7), Amarilla (8), Antes de que se enfríe el café (10), Asylum (13), Brazales de duelo (16), Cadáver exquisito (17), Cien años de soledad (Ed. Ilustrada) (20), Cien años de soledad (Edición conmemorativa) (21), Cometierra (25), Cuento de hadas (30), Cumbres borrascosas (ed. Alba) (31), Doctor Sueño (35), Edenbrooke (37), El bestiario de Axlin (41), El camino de los reyes – segunda edicion (44), El chico que dibujaba constelaciones (46), El Cuarto Mono (49), El día que dejó de nevar en Alaska (52), El día que el cielo se caiga (53), El día que se perdió la cordura (54), El duque y yo (55), El hombre de tiza (62), El Imperio Final. (Ed. revisada) (64), El instituto (65), El jardín de las mariposas (66), El laberinto de huesos (69), El Laberinto de los Espíritus (70), El monstruo pentápodo (74), El Pozo de la Ascensión. (Ed. revisada) (80), El príncipe cruel (81), El problema de los Tres Cuerpos (83), El secreto de la asistenta (86), El silencio de la ciudad blanca (87), El visitante (91), Elantris. Edición X Aniversario y definitiva del autor (92), Eleanor & Park (93), Escuadrón (97), Indigno de ser humano (107), La asistenta (112), La Biblioteca de la Medianoche (113), La chica del tren (118), La hipótesis del amor (122), La jaula del rey (124), La maldición de Hill House (129), La novia gitana (132), La paciente silenciosa (133), La pareja de al lado (134), La Reina Roja (135), La vegetariana (138), La verdad sobre el caso Harry Quebert (139), Las dos muertes (140), Llámame por tu nombre (142), Los siete maridos de Evelyn Hugo (146), Maze Runner: Correr o morir (147), No culpes al karma de lo que te pasa por gilipollas (154), Nuestra parte de noche (158), Palabras radiantes (160), Patria (163), PD. Todavía te quiero (164), Prohibido (166), Rebelión en la granja (trad. Marcial Souto y Miguel Temprano García) (169), Reina roja (170), Romper el círculo (172), Sueños de piedra (177), Tal vez mañana (178), Tan poca vida (179), Te doy mi corazón (180), Todas las hadas del reino (181), Todo esto te daré (182), Todo lo que nunca fuimos (183), Trenza del mar Esmeralda (185), Un monstruo viene a verme (189), Una corte de alas y ruina (190), Una corte de hielo y estrellas (191), Una corte de niebla y furia (192), Una corte de rosas y espinas (193), Verity. La sombra de un engaño (194), Yo antes de ti (197), Yo soy Eric Zimmerman. Volumen 1 (198), Yo, Simon, Homo Sapiens (200)
- **Fantástico** (51): Alas de sangre (7), Animales fantásticos y dónde encontrarlos (9), Antes de que se enfríe el café (10), Apocalipsis (11), Brazales de duelo (16), Ciudad de hueso (23), Coraline (28), Cuento de hadas (30), El bestiario de Axlin (41), El caballero de la armadura oxidada (43), El camino de los reyes – segunda edicion (44), El castillo ambulante (45), El hobbit (60), El imperio final (63), El Imperio Final. (Ed. revisada) (64), El ladrón del rayo (71), El nombre del viento (78), El Pozo de la Ascensión. (Ed. revisada) (80), El príncipe cruel (81), El principito (82), El temor de un hombre sabio (88), El último deseo (90), Elantris. Edición X Aniversario y definitiva del autor (92), Entrevista con el vampiro (96), Harry Potter y la cámara secreta (102), Harry Potter y la orden del fénix (103), Harry Potter y la piedra filosofal (104), Harry Potter. La colección completa (105), Hush, Hush (106), Juego de tronos (110), La Biblioteca de la Medianoche (113), La comunidad del anillo (120), La divina comedia (Ilustrado) (121), La jaula del rey (124), La Reina Roja (135), Las dos muertes (140), Los jardines de la Luna (143), Maze Runner: Correr o morir (147), Momo (152), Palabras radiantes (160), Soy leyenda (176), Sueños de piedra (177), Todas las hadas del reino (181), Tokio Blues (184), Trenza del mar Esmeralda (185), Trono de cristal (187), Un monstruo viene a verme (189), Una corte de alas y ruina (190), Una corte de hielo y estrellas (191), Una corte de niebla y furia (192), Una corte de rosas y espinas (193)
- **Intriga** (33): Asesinato en el Orient Express (12), Diez negritos (33), El brillo de las luciérnagas (42), El código Da Vinci (47), El Cuarto Mono (49), El cuento número trece (51), El día que se perdió la cordura (54), El guardián invisible (59), El hogar de Miss Peregrine para niños peculiares (61), El jardín de las mariposas (66), El juego del ángel (68), El laberinto de huesos (69), El Laberinto de los Espíritus (70), El nombre de la rosa (77), El psicoanalista (84), El secreto de la asistenta (86), El túnel (89), Harry Potter y la cámara secreta (102), Harry Potter y la orden del fénix (103), Harry Potter y la piedra filosofal (104), Harry Potter. La colección completa (105), La asistenta (112), La chica del tren (118), La novia gitana (132), La paciente silenciosa (133), La pareja de al lado (134), La sombra del viento (137), Los renglones torcidos de Dios (145), No soy un serial killer (155), Origen (159), Reina roja (170), Todo esto te daré (182), Verity. La sombra de un engaño (194)
- **Romántico** (27): A todos los chicos de los que me enamoré (3), After (5), Al final mueren los dos (6), Antes de que se enfríe el café (10), Cincuenta sombras de Grey (22), Ciudad de hueso (23), Como agua para chocolate (26), Cumbres borrascosas (ed. Alba) (31), Divergente (34), Edenbrooke (37), El amor en los tiempos del cólera (39), El chico que dibujaba constelaciones (46), El día que dejó de nevar en Alaska (52), El día que el cielo se caiga (53), El duque y yo (55), Eleanor & Park (93), Hush, Hush (106), La hipótesis del amor (122), La selección (136), PD. Todavía te quiero (164), Prohibido (166), Te doy mi corazón (180), Todo lo que nunca fuimos (183), Tokio Blues (184), Yo antes de ti (197), Yo soy Eric Zimmerman. Volumen 1 (198), Yo, Simon, Homo Sapiens (200)
- **Terror** (27): Apocalipsis (11), Asylum (13), Battle Royale (15), Carrie (18), Cementerio de animales (19), Doctor Sueño (35), El color que cayó del cielo (48), El guardián invisible (59), El hombre de tiza (62), El instituto (65), El jardín de las mariposas (66), El misterio de Salem’s Lot (73), El perfume (79), El resplandor (85), El visitante (91), Entrevista con el vampiro (96), Frankenstein (100), It (108), La larga marcha (126), La llamada de Cthulhu (128), La maldición de Hill House (129), La metamorfosis (131), Misery (151), No soy un serial killer (155), Nuestra parte de noche (158), Soy leyenda (176), Un monstruo viene a verme (189)
- **Ciencia ficción** (26): 1984 (1), 1984 (Trad. Miguel Temprano García) (2), Al final mueren los dos (6), Battle Royale (15), Cadáver exquisito (17), Divergente (34), Dune (36), El cuento de la criada (50), El problema de los Tres Cuerpos (83), En llamas (94), Escuadrón (97), Fahrenheit 451 (98), Flores para Algernon (99), Jerusalén (109), La carretera (115), La Historia Interminable – Color (123), La larga marcha (126), La selección (136), Los juegos del hambre (144), No tengo boca y debo gritar (156), Parque Jurásico (162), Ready Player One (167), Sinsajo (175), Soy leyenda (176), Trilogía Los juegos del hambre (186), Yo, robot (199)
- **Drama** (26): Amarilla (8), Antes de que se enfríe el café (10), Bajo la misma estrella (14), Cadáver exquisito (17), Carrie (18), Cien años de soledad (Ed. Ilustrada) (20), Cien años de soledad (Edición conmemorativa) (21), Cometas en el cielo (24), Crónica de una muerte anunciada (29), Cumbres borrascosas (ed. Alba) (31), El extranjero (57), El niño con el pijama de rayas (76), El perfume (79), El túnel (89), Indigno de ser humano (107), La cabaña (114), La carretera (115), La casa de los espíritus (116), La ladrona de libros (125), Llámame por tu nombre (142), Los renglones torcidos de Dios (145), Los siete maridos de Evelyn Hugo (146), Memorias de una geisha (148), Patria (163), Rebelión en la granja (168), Tokio Blues (184)
- **Juvenil** (25): A todos los chicos de los que me enamoré (3), Al final mueren los dos (6), Asylum (13), El bestiario de Axlin (41), El laberinto de huesos (69), El principito (82), Eleanor & Park (93), En llamas (94), La jaula del rey (124), La Reina Roja (135), Las dos muertes (140), Los juegos del hambre (144), Maze Runner: Correr o morir (147), PD. Todavía te quiero (164), Sinsajo (175), Sueños de piedra (177), Tal vez mañana (178), Todas las hadas del reino (181), Trilogía Los juegos del hambre (186), Un monstruo viene a verme (189), Una corte de alas y ruina (190), Una corte de hielo y estrellas (191), Una corte de niebla y furia (192), Una corte de rosas y espinas (193), Yo, Simon, Homo Sapiens (200)
- **Infantil y juvenil** (21): Bajo la misma estrella (14), Ciudad de hueso (23), Coraline (28), Divergente (34), El castillo ambulante (45), El hogar de Miss Peregrine para niños peculiares (61), El ladrón del rayo (71), Harry Potter y la cámara secreta (102), Harry Potter y la orden del fénix (103), Harry Potter y la piedra filosofal (104), Harry Potter. La colección completa (105), Hush, Hush (106), Jumper (111), La ciudad de las bestias (119), La Historia Interminable – Color (123), La ladrona de libros (125), La lección de August (127), La selección (136), Las ventajas de ser un marginado (141), Momo (152), Trono de cristal (187)
- **Aventuras** (20): Africanus, el hijo del cónsul (4), Brazales de duelo (16), El código Da Vinci (47), El jardín secreto (67), El nombre del viento (78), El temor de un hombre sabio (88), Harry Potter y la cámara secreta (102), Harry Potter y la orden del fénix (103), Harry Potter y la piedra filosofal (104), Harry Potter. La colección completa (105), Jerusalén (109), Juego de tronos (110), La ciudad de las bestias (119), La Historia Interminable – Color (123), La Reina Roja (135), Origen (159), Parque Jurásico (162), Rebelión en la granja (168), Trenza del mar Esmeralda (185), Trono de cristal (187)
- **Histórico** (11): Africanus, el hijo del cónsul (4), Edenbrooke (37), El duque y yo (55), El mundo de Sofía (75), El nombre de la rosa (77), El perfume (79), Jerusalén (109), La casa de los espíritus (116), La catedral del mar (117), Mi Lucha (149), Te doy mi corazón (180)
- **Policíaco** (11): Asesinato en el Orient Express (12), Diez negritos (33), El código Da Vinci (47), El Cuarto Mono (49), El nombre de la rosa (77), El silencio de la ciudad blanca (87), La chica del tren (118), La novia gitana (132), La verdad sobre el caso Harry Quebert (139), Reina roja (170), Yo, robot (199)
- **Otros** (11): Como agua para chocolate (26), El cuento número trece (51), El mundo de Sofía (75), El túnel (89), Ensayo sobre la ceguera (95), Fahrenheit 451 (98), Flores para Algernon (99), La casa de los espíritus (116), La vegetariana (138), Llámame por tu nombre (142), Relatos (171)
- **Ensayo** (9): De animales a dioses (32), El libro negro de la Nueva Izquierda (72), Ensayo sobre la ceguera (95), Hábitos atómicos (101), Mi lucha. La historia del libro que marcó el siglo XX (150), Pinochet (165), Sapiens (173), Sinceramente (174), Últimas noticias del nuevo idiota iberoamericano (188)
- **Autoayuda** (8): Cómo follar con todas (27), El Alquimista (38), El Arte de la Seducción (40), El caballero de la armadura oxidada (43), El cuento de la criada (50), Hábitos atómicos (101), Muchas vidas, muchos maestros (153), Veronika decide morir (195)
- **Realista** (6): Cometierra (25), La vegetariana (138), Noches Blancas (Ilustrado) (157), Patria (163), Romper el círculo (172), Tan poca vida (179)
- **Historia** (6): De animales a dioses (32), La máquina de matar (130), Mi lucha. La historia del libro que marcó el siglo XX (150), Pinochet (165), Sapiens (173), Voces de Chernóbil (196)
- **Divulgación** (5): Cómo follar con todas (27), El Arte de la Seducción (40), El engaño populista (56), El fin de la inflación (58), La máquina de matar (130)
- **Psicológico** (5): Cumbres borrascosas (ed. Alba) (31), El monstruo pentápodo (74), El secreto de la asistenta (86), Indigno de ser humano (107), La asistenta (112)
- **Clásico** (5): El amor en los tiempos del cólera (39), El jardín secreto (67), Frankenstein (100), La metamorfosis (131), Rebelión en la granja (168)
- **Relato** (5): La cabaña (114), No tengo boca y debo gritar (156), Noches Blancas (Ilustrado) (157), Palmeras en la nieve (161), Relatos (171)
- **Ciencias sociales** (4): El engaño populista (56), El libro negro de la Nueva Izquierda (72), Sinceramente (174), Últimas noticias del nuevo idiota iberoamericano (188)
- **Humor** (3): Bajo la misma estrella (14), Las dos muertes (140), No culpes al karma de lo que te pasa por gilipollas (154)
- **Erótico** (2): Cincuenta sombras de Grey (22), Yo soy Eric Zimmerman. Volumen 1 (198)
- **Ciencias naturales** (2): De animales a dioses (32), Sapiens (173)
- **Filosófico** (2): La divina comedia (Ilustrado) (121), Llámame por tu nombre (142)
- **Memorias** (2): Pinochet (165), Sinceramente (174)
- **Economía** (1): El fin de la inflación (58)
- **Política** (1): El fin de la inflación (58)
- **Recopilación** (1): Harry Potter. La colección completa (105)
- **Bélico** (1): Juego de tronos (110)
- **Ficción** (1): Jumper (111)
- **Poesía** (1): La divina comedia (Ilustrado) (121)
- **Biografía** (1): Mi Lucha (149)
- **Esoterismo** (1): Muchas vidas, muchos maestros (153)
- **Sátira** (1): Rebelión en la granja (trad. Marcial Souto y Miguel Temprano García) (169)
- **Crónica** (1): Voces de Chernóbil (196)

## Fichas

### 1. 1984

**George Orwell** · *Ciencia ficción*

Descripción aterradora de la vida bajo la vigilancia constante del "Gran Hermano". 1984 sitúa su acción en un Estado totalitario. Como explica O’Brien, el astuto y misterioso miembro de la dirección del partido dominante, el …

<details><summary>Sinopsis completa</summary>

Descripción aterradora de la vida bajo la vigilancia constante del "Gran Hermano". 1984 sitúa su acción en un Estado totalitario. Como explica O’Brien, el astuto y misterioso miembro de la dirección del partido dominante, el poder es el valor absoluto y único: para conquistarlo no hay nada en el mundo que no deba ser sacrificado y, una vez alcanzado, nada queda de importante en la vida a no ser la voluntad de conservarlo a cualquier precio. La vigilancia despiadada de este Superestado ha llegado a apoderarse de la vida y la conciencia de sus súbditos, interviniendo incluso y sobre todo en las esferas más íntimas de los sentimientos humanos. Todo está controlado por la sombría y omnipresente figura del Gran Hermano, el jefe que todo lo ve, todo lo escucha y todo lo dispone. Winston Smith, el protagonista, aparece inicialmente como símbolo de la rebelión contra este poder monstruoso, pero conforme el relato avanza está cada vez más cazado por este engranaje, omnipotente y cruel. Por su magnífico análisis del poder y de las relaciones y dependencias que crea en los individuos, 1984 es una de las novelas más inquietantes y atractivas de este siglo.

</details>

### 2. 1984 (Trad. Miguel Temprano García)

**George Orwell** · *Ciencia ficción · Novela*

«No creo que la sociedad que he descrito en 1984 necesariamente llegue a ser una realidad, pero sí creo que puede llegar a existir algo parecido», escribía Orwell después de publicar su novela. Corría el …

<details><summary>Sinopsis completa</summary>

«No creo que la sociedad que he descrito en 1984 necesariamente llegue a ser una realidad, pero sí creo que puede llegar a existir algo parecido», escribía Orwell después de publicar su novela. Corría el año 1948, y la realidad se ha encargado de convertir esa pieza —entonces de ciencia ficción— en un manifiesto de la realidad. En el año 1984 Londres es una ciudad lúgubre en la que la Policía del Pensamiento controla de forma asfixiante la vida de los ciudadanos. Winston Smith es un peón de este engranaje perverso y su cometido es reescribir la historia para adaptarla a lo que el Partido considera la versión oficial de los hechos. Hasta que decide replantearse la verdad del sistema que los gobierna y somete.

</details>

### 3. A todos los chicos de los que me enamoré

**Jenny Han** · *Juvenil · Novela · Romántico* · Serie: A todos los chicos de los que me enamoré, tomo 1

Lara Jean guarda sus cartas de amor en una caja. No son cartas que le hayan enviado, las ha escrito ella, una por cada chico de los que se ha enamorado. En ellas se muestra …

<details><summary>Sinopsis completa</summary>

Lara Jean guarda sus cartas de amor en una caja. No son cartas que le hayan enviado, las ha escrito ella, una por cada chico de los que se ha enamorado. En ellas se muestra tal cual es, porque sabe que nadie las leerá. Hasta que un día alguien las envía por equivocación y la vida amorosa de Lara Jean pasa de «imaginaria» a estar totalmente fuera de control.

</details>

### 4. Africanus, el hijo del cónsul

**Santiago Posteguillo** · *Aventuras · Histórico* · Serie: Trilogía de Escipión, tomo 1

Africanus el hijo del Cónsul es el primero libro de la trilogía de Santiago Posteguillo sobre Publio Cornelio Escipión, el único general romano que fue capaz de derrotar en el campo de batalla al genial …

<details><summary>Sinopsis completa</summary>

Africanus el hijo del Cónsul es el primero libro de la trilogía de Santiago Posteguillo sobre Publio Cornelio Escipión, el único general romano que fue capaz de derrotar en el campo de batalla al genial estratega cartaginés Aníbal, uno de los más famosos generales de la historia y el que fuera recordado con pavor por los romanos durante muchas generaciones.

</details>

### 5. After

**Anna Todd** · *Novela · Romántico* · Serie: After, tomo 1

Tessa Young se enfrenta a su primer año en la universidad. Acostumbrada a una vida estable y ordenada, su mundo cambia cuando conoce a Hardin, un chico tan guapo como borde, inquietante, lleno de tatuajes, …

<details><summary>Sinopsis completa</summary>

Tessa Young se enfrenta a su primer año en la universidad. Acostumbrada a una vida estable y ordenada, su mundo cambia cuando conoce a Hardin, un chico tan guapo como borde, inquietante, lleno de tatuajes, y de aparente mala vida. Desde el primer momento se odian. Pertenecen a dos mundos distintos, pero pronto se harán más que amigos y nada volverá a ser igual. Hardin y Tessa deberán enfrentarse a muchas pruebas para estar juntos. La inocencia, el despertar a la vida, el descubrimiento del sexo… las huellas de un amor tan poderoso como la fuerza del destino. Con más de mil millones de impactos, After se ha convertido en el mayor fenómeno de la historia de la plataforma Wattpad. Ahora llega por fin el libro, enriquecido y con nuevo contenido, que pronto será llevado a la gran pantalla.

</details>

### 6. Al final mueren los dos

**Adam Silvera** · *Ciencia ficción · Juvenil · Romántico*

De Adam Silvera, autor superventas de Recuerda aquella vez. Una historia sobre la vida, la amistad y el amor. ¿Puede un solo día albergar toda una vida? En un presente alternativo, en el que es …

<details><summary>Sinopsis completa</summary>

De Adam Silvera, autor superventas de Recuerda aquella vez. Una historia sobre la vida, la amistad y el amor. ¿Puede un solo día albergar toda una vida? En un presente alternativo, en el que es posible predecir la muerte con un plazo de veinticuatro horas, Mateo Torrez y Rufus Emeterio acaban de recibir la llamada más temida: la misma que te avisa de que ha llegado tu hora final. En circunstancias normales, es poco probable que Mateo y Rufus se hubieran conocido. Pero sus circunstancias no son normales en absoluto. Porque les quedan, a lo sumo, veinticuatro horas de vida. Y han decidido recurrir a Último Amigo, la aplicación de citas que te permite contactar con alguien dispuesto a compartir tu carga. Mateo y Rufus tienen un día, puede que menos, para disfrutar de su recién nacida amistad. Para descubrir cuán frágiles y preciosos son los hilos que nos unen. Para mostrar al mundo su verdadero yo. La nueva novela de Adam Silvera, un superventas del New York Times que ha cosechado un éxito arrollador por parte de la crítica y los lectores. Un libro emotivo, original y extremo, que aborda la cercanía de la muerte para plasmar magistralmente la fuerza arrolladora de la vida, la amistad y el amor. «Extraordinario e inolvidable.» ... «Absorbente, profundo y desgarrador» -Kirkus Review.

</details>

### 7. Alas de sangre

**Rebecca Yarros** · *Fantástico · Novela* · Serie: Empíreo, tomo 1

Violet Sorrengail creía que se uniría al Cuadrante de los Escribas para vivir una vida tranquila, sin embargo, por órdenes de su madre, debe unirse a los miles de candidatos que, en el Colegio de …

<details><summary>Sinopsis completa</summary>

Violet Sorrengail creía que se uniría al Cuadrante de los Escribas para vivir una vida tranquila, sin embargo, por órdenes de su madre, debe unirse a los miles de candidatos que, en el Colegio de Guerra de Basgiath, luchan por formar parte de la élite de Navarre: el Cuadrante de los Jinetes de dragones. Cuando eres más pequeña y frágil que los demás tu vida corre peligro, porque los dragones no se vinculan con humanos débiles. Además, con más jinetes que dragones disponibles, muchos la matarían con tal de mejorar sus probabilidades de éxito; y hay otros, como el despiadado Xaden Riorson, el líder de ala más poderoso del Cuadrante de Jinetes, que la asesinarían simplemente por ser la hija de la comandante general. Para sobrevivir, necesitará aprovechar al máximo todo su ingenio. Mientras la guerra se torna más letal Violet sospecha que los líderes de Navarre esconden un terrible secreto…

</details>

### 8. Amarilla

**R. F. Kuang | Rebecca F. Kuang** · *Drama · Novela*

Athena Liu es una escritora famosa y June Hayward es una escritora a la que no conocen ni en su casa. Cuando Athena muere de forma tan inesperada como extraña, June le roba su último …

<details><summary>Sinopsis completa</summary>

Athena Liu es una escritora famosa y June Hayward es una escritora a la que no conocen ni en su casa. Cuando Athena muere de forma tan inesperada como extraña, June le roba su último manuscrito. Y no solo eso: lo publica como si fuera obra suya. Sin embargo, hay evidencias que amenazan con poner en peligro el éxito que June ha conseguido de manera tan (por decirlo finamente) cuestionable. Y es entonces cuando descubre hasta dónde está dispuesta a llegar para conservar la vida que ella cree que merece.

</details>

### 9. Animales fantásticos y dónde encontrarlos

**J. K. Rowling** · *Fantástico*

Hay un ejemplar de Animales Fantásticos y Dónde Encontrarlos en casi todos los hogares de magos del país. Ahora, sólo por cierto tiempo, también los muggles pueden descubrir dónde viven los quintapeds, qué come el …

<details><summary>Sinopsis completa</summary>

Hay un ejemplar de Animales Fantásticos y Dónde Encontrarlos en casi todos los hogares de magos del país. Ahora, sólo por cierto tiempo, también los muggles pueden descubrir dónde viven los quintapeds, qué come el puffskein y por qué es mejor no dejar leche fuera de casa para un knarl.

</details>

### 10. Antes de que se enfríe el café

**Toshikazu Kawaguchi** · *Drama · Fantástico · Novela · Romántico*

Un rumor circula por Tokio… Oculta en uno de sus callejones hay una pequeña cafetería que merece la pena visitar no solo por su excelente café, sino también porque, si eliges bien la silla donde …

<details><summary>Sinopsis completa</summary>

Un rumor circula por Tokio… Oculta en uno de sus callejones hay una pequeña cafetería que merece la pena visitar no solo por su excelente café, sino también porque, si eliges bien la silla donde sentarte, puedes regresar al pasado. Pero como incluso lo increíble está sujeto a limitaciones, no podrás abandonar la cafetería mientras dure el viaje, para volver deberás beberte el café antes de que se enfríe y, hagas lo que hagas, el presente no cambiará. A través de las emocionantes historias de cuatro clientes que deciden embarcarse en esta aventura por motivos diferentes, Antes de que se enfríe el café nos ofrece un relato atemporal sobre el amor, las oportunidades perdidas y la esperanza en un futuro que siempre está por llegar.

</details>

### 11. Apocalipsis

**Stephen King** · *Fantástico · Terror*

Esta narración cuenta cómo un virus gripal, creado artíficíalmente como posible arma bacteriológica, se extiende por Estados Unidos y provoca la muerte de millones de personas. Los supervivientes tienen sueños comunes, en los que aparece …

<details><summary>Sinopsis completa</summary>

Esta narración cuenta cómo un virus gripal, creado artíficíalmente como posible arma bacteriológica, se extiende por Estados Unidos y provoca la muerte de millones de personas. Los supervivientes tienen sueños comunes, en los que aparece una anciana y un hombre joven. La mujer anciana los incita a viajar a Nebraska para combatir a Randall Flagg, un abominable personaje que encarna las fuerzas del mal y posee un arsenal nuclear.

</details>

### 12. Asesinato en el Orient Express

**Agatha Christie** · *Intriga · Policíaco* · Serie: Hércules Poirot, tomo 10

Estambul, pleno invierno. Poirot decide tomar el Orient Express que en esta época suele hacer su recorrido prácticamente vacío. Pero aquel día, el tren va lleno y sólo gracias a una buena amiga consigue una …

<details><summary>Sinopsis completa</summary>

Estambul, pleno invierno. Poirot decide tomar el Orient Express que en esta época suele hacer su recorrido prácticamente vacío. Pero aquel día, el tren va lleno y sólo gracias a una buena amiga consigue una litera en el coche-cama. A la mañana siguiente se despierta, descubre que una tormenta de nieve ha obligado a detener el tren y que un americano, llamado Ratcher, ha sido apuñalado salvajemente. Aparentemente nadie ha entrado ni ha salido del coche-cama. El asesino, sin duda, es alguno de los ocupantes entre los que se encuentra una altiva princesa rusa y una institutriz inglesa.

</details>

### 13. Asylum

**Madeleine Roux** · *Juvenil · Novela · Terror* · Serie: Asylum, tomo 1

Para Dan Crawford, el programa de verano para alumnos sobresalientes es una oportunidad única. Sus amigos nunca comprendieron su fascinación por la historia y la ciencia. Pero en el Colegio Preparatorio New Hampshire, esas preferencias …

<details><summary>Sinopsis completa</summary>

Para Dan Crawford, el programa de verano para alumnos sobresalientes es una oportunidad única. Sus amigos nunca comprendieron su fascinación por la historia y la ciencia. Pero en el Colegio Preparatorio New Hampshire, esas preferencias están a la orden del día. Al llegar al lugar, se encuentra con que la residencia a la que debía ir ha sido cerrada, por lo cual todos los estudiantes se ven forzados a quedarse en Brookline, lo que solía ser un hospital psiquiátrico. Cuando Dan y sus nuevos amigos, Abby y Jordan, comienzan a explorar los pasillos y el sótano oculto del lugar, descubren secretos escalofriantes sobre lo que realmente ocurría allí. Secretos que los vinculan a ellos con el oscuro pasado del hospicio. Brookline nunca fue un instituto para enfermos mentales comunes: alojó tanto a psicópatas como a homicidas, sujetos sumamente peligrosos, y hay hechos y prácticas aberrantes que saldrán a la luz.

</details>

### 14. Bajo la misma estrella

**John Green** · *Drama · Humor · Infantil y juvenil*

Emotiva, irónica y afilada. Una novela teñida de humor y de tragedia que habla de nuestra capacidad para soñar incluso en las circunstancias más difíciles. A Hazel y a Gus les gustaría tener vidas más …

<details><summary>Sinopsis completa</summary>

Emotiva, irónica y afilada. Una novela teñida de humor y de tragedia que habla de nuestra capacidad para soñar incluso en las circunstancias más difíciles. A Hazel y a Gus les gustaría tener vidas más corrientes. Algunos dirían que no han nacido con estrella, que su mundo es injusto. Hazel y Gus son solo adolescentes, pero si algo les ha enseñado el cáncer que ambos padecen es que no hay tiempo para lamentaciones, porque, nos guste o no, solo existe el hoy y el ahora. Y por ello, con la intención de hacer realidad el mayor deseo de Hazel - conocer a su escritor favorito -, cruzarán juntos el Atlántico para vivir una aventura contrarreloj, tan catártica como desgarradora. Destino: Amsterdam, el lugar donde reside el enigmático y malhumorado escritor, la única persona que tal vez pueda ayudarles a ordenar las piezas del enorme puzle del que forman parte... Rebosante de agudeza y esperanza, Bajo la misma estrella es la novela que ha catapultado a John Green al éxito. Una historia que explora cuán exquisita, inesperada y trágica puede ser la aventura de saberse vivo y de querer a alguien.

</details>

### 15. Battle Royale

**Koushun Takami** · *Ciencia ficción · Terror*

En la República del Gran Oriente Asiático está prohibido el rock, esa música decadente. Los jóvenes crecen en un estado totalitario y controlador que promueve la competitividad. Como medida de control de rebeliones, la administración …

<details><summary>Sinopsis completa</summary>

En la República del Gran Oriente Asiático está prohibido el rock, esa música decadente. Los jóvenes crecen en un estado totalitario y controlador que promueve la competitividad. Como medida de control de rebeliones, la administración pone en marcha el Programa: cada año, 50 clases de distintos institutos son elegidas para luchar a muerte en la BATTLE ROYALE. Los alumnos elegidos son aislados en una isla. Las normas del juego son estrictas: no pueden escapar, no pueden contactar con el exterior, y solo puede quedar uno. Todo está permitido para sobrevivir. Empieza el juego. Empieza BATTLE ROYALE.

</details>

### 16. Brazales de duelo

**Brandon Sanderson** · *Aventuras · Fantástico · Novela* · Serie: Nacidos de la bruma, tomo 6

Brandon Sanderson regresa con la sexta entrega de Nacidos de la Bruma (Mistborn) Brazales de Duelo: legendarios brazales que portaba el lord Legislador hace siglos, hasta que la Guerrero de la Ascensión se los arrebató, …

<details><summary>Sinopsis completa</summary>

Brandon Sanderson regresa con la sexta entrega de Nacidos de la Bruma (Mistborn) Brazales de Duelo: legendarios brazales que portaba el lord Legislador hace siglos, hasta que la Guerrero de la Ascensión se los arrebató, precipitando su muerte. Dicen de ellos que contienen un poder increíble, aunque, como todo el mundo sabe, hace tiempo que se perdieron entre las brumas del tiempo. Solo que alguien acaba de encontrarlos. La cuenca de Elendel es un polvorín. El descontento de los trabajadores solo es la punta del iceberg; las diferencias son cada vez más irreconciliables entre la capital y las demás ciudades de la cuenca, ciudades que Elendel asegura gobernar mientras sus habitantes denuncian la opresión a la que se sienten sometidos. En medio de todo esto, llega a oídos de Waxillium Ladrian el rumor de que un académico kandra podría haber localizado los legendarios Brazales de Duelo, un arma capaz de sembrar la destrucción y dar al traste con el actual equilibrio de poder imperante en la cuenca.

</details>

### 17. Cadáver exquisito

**Agustina María Bazterrica** · *Ciencia ficción · Drama · Novela*

La súbita aparición de un virus letal que ataca a los animales modifica de manera irreversible el mundo: desde las fieras hasta las mascotas deben ser sistemáticamente sacrificadas, y su carne ya no puede ser …

<details><summary>Sinopsis completa</summary>

La súbita aparición de un virus letal que ataca a los animales modifica de manera irreversible el mundo: desde las fieras hasta las mascotas deben ser sistemáticamente sacrificadas, y su carne ya no puede ser consumida. Los gobiernos enfrentan la situación con una decisión drástica: legalizando la cría, reproducción, matanza y procesamiento de carne humana. El canibalismo es ley y la sociedad ha quedado dividida en dos grupos: los que comen y los que son comidos. Marcos Tejo, encargado general del frigorífico Krieg, separado de su esposa y a cargo de su padre, es un oscuro burócrata. El día en que recibe como regalo una mujer criada para el consumo, las tentaciones lo transforman en una conciencia peligrosa de pliegues truculentos que lo llevará a transgredir las nuevas normas hasta límites que la sociedad desconoce. ¿Qué resto de humanidad cabe cuando los muertos son cremados para evitar su consumo? ¿Quién es el otro si, de verdad, somos lo que comemos? En esta despiadada distopía —tan brutal como sutil, tan alegórica como realista—, Agustina Bazterrica inspira, con el poder explosivo de la ficción, sensaciones y debates de suma actualidad.

</details>

### 18. Carrie

**Stephen King** · *Drama · Terror*

El escalofriante caso de una joven de apariencia insignificante que se transformó en un ser de poderes anormales, sembrando el terror en la ciudad. Con pulso mágico para mantener la tensión a lo largo de …

<details><summary>Sinopsis completa</summary>

El escalofriante caso de una joven de apariencia insignificante que se transformó en un ser de poderes anormales, sembrando el terror en la ciudad. Con pulso mágico para mantener la tensión a lo largo de todo el libro, Stephen King narra la atormentada adolescencia de Carrie, y nos envuelve en una atmósfera sobrecogedora cuando la muchacha realiza una serie de descubrimientos hasta llegar al terrible momento de la venganza. Esta novela fue llevada al cine con un inmenso éxito de público y crítica.

</details>

### 19. Cementerio de animales

**Stephen King** · *Terror*

"Church" estaba allí otra vez. Temía y deseaba algo semejante. Porque su hijita Ellie le había encargado que cuidara del gato, de "Church", y "Church" había muerto atropellado. Louis Creed era médico, había tenido al …

<details><summary>Sinopsis completa</summary>

"Church" estaba allí otra vez. Temía y deseaba algo semejante. Porque su hijita Ellie le había encargado que cuidara del gato, de "Church", y "Church" había muerto atropellado. Louis Creed era médico, había tenido al gato en los brazos y estaba muerto. Seguro. Pero había cedido ante la insistencia del viejo y había ido a enterrarlo a plena noche, más allá del cementerio de animales. Más allá. Y ahora estaba allí otra vez. Era "Church", no cabía duda, aunque arrastraba los cuartos traseros, apestaba como un condenado, sus ojos eran mucho más verdes y mucho más crueles y su comportamiento era perverso. Pero volvía a estar allí y Ellie no lo echaría de menos. Sin embargo, Louis Creed sí volvería a echar de menos aquel lugar. Porque más allá del cementerio de animales, más allá de la valla de troncos que nadie se atrevía a traspasar, más allá de los cuarenta y cinco escalones, el poder del antiguo cementerio indio le reclamaba y le ofrecía su aberrante consuelo para una espiral de un dolor y un horror cada vez más intensos.

</details>

### 20. Cien años de soledad (Ed. Ilustrada)

**Gabriel García Márquez** · *Drama · Novela*

En ocasión del 50 aniversario de la publicación de Cien años de soledad , llega una edición con ilustraciones inéditas de la artista chilena Luisa Rivera y con una tipografía creada por el hijo del …

<details><summary>Sinopsis completa</summary>

En ocasión del 50 aniversario de la publicación de Cien años de soledad , llega una edición con ilustraciones inéditas de la artista chilena Luisa Rivera y con una tipografía creada por el hijo del autor, Gonzalo García Bacha (versión «en papel»). Una edición conmemorativa de una novela clave en la historia de la literatura, una obra que todos deberíamos tener en nuestras estanterías. « Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo ». Con esta cita comienza una de las novelas más importantes del siglo XX y una de las aventuras literarias más fascinantes de todos los tiempos. Millones de ejemplares de Cien años de soledad leídos en todas las lenguas y el premio Nobel de Literatura coronando una obra que se había abierto paso «boca a boca» -como gustaba decir el escritor- son la más palpable demostración de que la aventura fabulosa de la familia Buendía-Iguarán, con sus milagros, fantasías, obsesiones, tragedias, incestos, adulterios, rebeldías, descubrimientos y condenas, representaba al mismo tiempo el mito y la historia, la tragedia y el amor del mundo entero.

</details>

### 21. Cien años de soledad (Edición conmemorativa)

**Gabriel García Márquez** · *Drama · Novela*

"Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo". Con estas palabras empieza una novela ya …

<details><summary>Sinopsis completa</summary>

"Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo". Con estas palabras empieza una novela ya legendaria en los anales de la literatura universal, una de las aventuras literarias más fascinantes de nuestro siglo. Millones de ejemplares de Cien años de Soledad leídos en todas las lenguas y el premio Nobel de Literatura coronando una obra que se había abierto paso "boca a boca". La Real Academia Española y la Asociación de Academias de la Lengua Española presentan Cien años de soledad , una edición popular conmemorativa cuyo texto ha revisado el propio Gabriel García Márquez. A pesar del esmero con que el propio escritor corrigió las pruebas de la primera edición (Sudamericana, 1967), se deslizaron en ella indeseadas erratas y expresiones dudosas que editores sucesivos han tratado de resolver con mejor o peor fortuna. Un estudio comparativo detallado de cada caso ha permitido ahora presentar una propuesta razonada al propio autor, que ha querido revisar las pruebas de imprenta completas, enriqueciendo así esta edición con su trabajo de depuración y fijación del texto.

</details>

### 22. Cincuenta sombras de Grey

**E. L. James** · *Erótico · Romántico* · Serie: Trilogía de las cincuenta sombras, tomo 1

Cuando la estudiante de Literatura Anastasia Steele recibe el encargo de entrevistar al exitoso y joven empresario Christian Grey, queda impresionada al encontrarse ante un hombre atractivo, seductor y también muy intimidante. La inexperta e …

<details><summary>Sinopsis completa</summary>

Cuando la estudiante de Literatura Anastasia Steele recibe el encargo de entrevistar al exitoso y joven empresario Christian Grey, queda impresionada al encontrarse ante un hombre atractivo, seductor y también muy intimidante. La inexperta e inocente Ana intenta olvidarle, pero pronto comprende cuánto le desea. Cuando la pareja por fin inicia una apasionada relación, Ana se sorprende por las peculiares prácticas eróticas de Grey, al tiempo que descubre los límites de sus propios y más oscuros deseos...

</details>

### 23. Ciudad de hueso

**Cassandra Clare** · *Fantástico · Infantil y juvenil · Romántico* · Serie: Cazadores de sombras, tomo 1

Demonios, hombres lobo, vampiros, ángeles y hadas conviven en esta trilogía de fantasía urbana donde no falta el romance. En el Pandemonium, la discoteca de moda de Nueva York, Clary sigue a un atractivo chico …

<details><summary>Sinopsis completa</summary>

Demonios, hombres lobo, vampiros, ángeles y hadas conviven en esta trilogía de fantasía urbana donde no falta el romance. En el Pandemonium, la discoteca de moda de Nueva York, Clary sigue a un atractivo chico de pelo azul hasta que presencia su muerte a manos de tres jóvenes cubiertos de extraños tatuajes. Desde esa noche, su destino se une al de esos tres cazadores de sombras, guerreros dedicados a liberar a la tierra de demonios y, sobre todo, al de Jace, un chico con aspecto de ángel y tendencia a actuar como un idiota...

</details>

### 24. Cometas en el cielo

**Khaled Hosseini** · *Drama*

Sobre el telón de fondo de un Afganistán respetuoso de sus ricas tradiciones ancestrales, la vida en Kabul durante el invierno de 1975 se desarrolla con toda la intensidad, la pujanza y el colorido de …

<details><summary>Sinopsis completa</summary>

Sobre el telón de fondo de un Afganistán respetuoso de sus ricas tradiciones ancestrales, la vida en Kabul durante el invierno de 1975 se desarrolla con toda la intensidad, la pujanza y el colorido de una ciudad confiada en su futuro e ignorante de que se avecina uno de los periodos más cruentos y tenebrosos que han padecido los milenarios pueblos que la habitan. Cometas en el cielo es la conmovedora historia de dos padres y dos hijos, de su amistad y de cómo la casualidad puede convertirse en hito inesperado de nuestro destino.

</details>

### 25. Cometierra

**Dolores Reyes** · *Novela · Realista* · Serie: Cometierra, tomo 1

Dice Cometierra: «Me acosté en el suelo, sin abrir los ojos. Había aprendido que de esa oscuridad nacían formas. Traté de verlas y de no pensar en nada más, ni siquiera en el dolor que …

<details><summary>Sinopsis completa</summary>

Dice Cometierra: «Me acosté en el suelo, sin abrir los ojos. Había aprendido que de esa oscuridad nacían formas. Traté de verlas y de no pensar en nada más, ni siquiera en el dolor que me llegaba desde la panza. Nada, salvo un brillo que miré con toda atención hasta que se transformó en dos ojos negros. Y de a poco, como si la hubiera fabricado la noche, vi la cara de María, los hombros, el pelo que nacía de la oscuridad más profunda que había visto en mi vida». El escenario ficticio podría ser cualquiera de las barriadas pobres que rodean a la capital argentina, muy distintas a la ciudad a pesar de estar sólo a unos pocos kilómetros. En una de esas casitas precarias que se levantan directamente sobre la tierra viven solos Cometierra y su hermano, el Walter. Cuando era chica, Cometierra tragó tierra y supo en una visión que su papá había matado a golpes a su mamá. Esa fue solo la primera de las visiones. Nacer con un don implica una responsabilidad hacia los otros y a Cometierra le tocó uno que hace su vida doblemente difícil, porque vive en un barrio en donde la violencia, el desamparo y la injusticia brotan en cada rincón y porque allí las principales víctimas son las mujeres. En la persecución de la verdad, en el descubrimiento del amor, en el cuidado entre hermanos, Cometierra buscará su propio camino.

</details>

### 26. Como agua para chocolate

**Laura Esquivel** · *Otros · Romántico*

Una novela sorprendente, inolvidable, cuyo tema gira en torno a un amor imposible para cuya consecución la protagonista recurrirá a las artes culinaras. Bajo la apariencia de un folletín por entregas y encabezando cada capítulo …

<details><summary>Sinopsis completa</summary>

Una novela sorprendente, inolvidable, cuyo tema gira en torno a un amor imposible para cuya consecución la protagonista recurrirá a las artes culinaras. Bajo la apariencia de un folletín por entregas y encabezando cada capítulo con una receta, esta historia mágica convierte la gastronomía en un código de sensualidad cargado de penetrantes aromas, de colores deslumbrantes. Tita es la pequeña, vive en un rancho con sus hermanas y sus sirvientas, y pese a saberse condenada a no poder gozar del amor por tener que hacerse cargo de su madre, no renunciará a Pedro. Él también la ama, pero se casará con su hermana Rosaura para poder seguir cerca de ella. Tita se refugia en la cocina y se entrega a la elaboración de platos mágicos capaces de transformar las emociones y el comportamiento de quienes los prueban, a la espera de que su trágico destino se cumpla.

</details>

### 27. Cómo follar con todas

**Tony Clink** · *Autoayuda · Divulgación*

Ponte a prueba con el Examen de Pardillismo: ¿verdadero o falso? 1. Invitar a cenar a una chica que te gusta es una buena idea. 2. Dejar caer alguna insinuación sexual mientras hablas con una …

<details><summary>Sinopsis completa</summary>

Ponte a prueba con el Examen de Pardillismo: ¿verdadero o falso? 1. Invitar a cenar a una chica que te gusta es una buena idea. 2. Dejar caer alguna insinuación sexual mientras hablas con una chica a la que apenas conoces es una mala idea. 3. Hablar con la más guapa de dos chicas es lo acertado. Si has contestado «falso» a las tres preguntas, seguramente eres un PAS (perfecto artista de la seducción). En el caso contrario, eres un TPF (típico pardillo frustrado). Si te parece una tontería, piensa en lo siguiente: estas dinámicas han sido verificadas cientos de veces por cientos de hombres. Cómo follar con todas puede enseñarle a cualquier tío las técnicas contrastadas de los mejores ligones del mundo, como la regla de los tres segundos, el estilo Gran Maestro o el truco del Discovery Channel. Ya no perderás tiempo y dinero en citas sin futuro. Ya no dudarás a la hora de tirarle los tejos a una belleza. Ya no suplicarás como un pardillo por el simple hecho de estar ante un bombón. Y dejarás de temer el rechazo. Te convertirás en un sensual varón que nunca pedirá disculpas, y tendrás el aplomo, el poder y la destreza para conseguir a cualquier mujer que desees.

</details>

### 28. Coraline

**Neil Gaiman** · *Fantástico · Infantil y juvenil*

El día después de que se mudaran, Coraline se fue a explorar… Cuando Coraline atraviesa una de las puertas de la casa nueva de su familia, se encuentra que hay otra casa extrañamente similar a …

<details><summary>Sinopsis completa</summary>

El día después de que se mudaran, Coraline se fue a explorar… Cuando Coraline atraviesa una de las puertas de la casa nueva de su familia, se encuentra que hay otra casa extrañamente similar a la suya (aunque la nueva sea, definitivamente, mejor). Al principio, todo parece maravilloso: la comida es más sabrosa que la de casa y el cajón de los juguetes está repleto de angelitos de papel que vuelan solos y de calaveras de dinosaurios que parecen vivas y se arrastran haciendo castañetear los dientes. Pero resulta que hay otra madre que vive ahí, y otro padre, y quieren que Coraline se quede con ellos y se convierta en su pequeña. Quieren cambiarla y no dejarla ir jamás. Coraline tendrá que enfrentarse a ellos con todo su ingenio y las herramientas que encuentre, si es que ha de conseguir salvarse y volver a su vida normal.

</details>

### 29. Crónica de una muerte anunciada

**Gabriel García Márquez** · *Drama*

Crónica de una muerte anunciada, novela corta publicada en 1981, es una de Las obras más conocidas y apreciadas de García Márquez. Relata en forma de reconstrucción casi periodística el asesinato de Santiago Nasar a …

<details><summary>Sinopsis completa</summary>

Crónica de una muerte anunciada, novela corta publicada en 1981, es una de Las obras más conocidas y apreciadas de García Márquez. Relata en forma de reconstrucción casi periodística el asesinato de Santiago Nasar a manos de los gemelos Vicario. Desde el comienzo de la narración se anuncia que Santiago Nasar va a morir: es el joven hijo de un árabe emigrado y parece ser el causante de la deshonra de Ángela, hermana de los gemelos, que ha contraído matrimonio el día anterior y ha sido rechazada por su marido. «Nunca hubo una muerte tan anunciada», declara quien rememora los hechos veintisiete años después: los vengadores, en efecto, no se cansan de proclamar sus propósitos por todo el pueblo, como si quisieran evitar el mandato del destino, pero un cúmulo de casualidades hace que quienes pueden evitar el crimen no logren intervenir o se decidan demasiado tarde. El propio Santiago Nasar se levanta esa mañana despreocupado, ajeno por completo a la muerte que le aguarda.

</details>

### 30. Cuento de hadas

**Stephen King** · *Fantástico · Novela*

Charlie Reade parece un estudiante de instituto normal y corriente, pero carga con un gran peso sobre los hombros. Su madre fue víctima de un atropello cuando él tenía solo diez años y la pena …

<details><summary>Sinopsis completa</summary>

Charlie Reade parece un estudiante de instituto normal y corriente, pero carga con un gran peso sobre los hombros. Su madre fue víctima de un atropello cuando él tenía solo diez años y la pena empujó a su padre a la bebida. Aunque era demasiado joven, Charlie tuvo que aprender a cuidarse solo... y también a ocuparse de su padre.) Ahora, con diecisiete años, Charlie encuentra dos amigos inesperados: una perra llamada Radar y Howard Bowditch, su anciano dueño. El señor Bowditch es un ermitaño que vive en una colina enorme, en una casa enorme que tiene un cobertizo cerrado a cal y canto en el patio trasero. A veces, sonidos extraños emergen de él. Mientras Charlie se encarga de hacer recados para el señor Bowditch, Radar y él se hacen inseparables. Cuando el anciano fallece, le deja al chico una cinta de casete que contiene una historia increíble y el gran secreto que Bowditch ha guardado durante toda su vida: dentro de su cobertizo existe un portal que conduce a otro mundo.

</details>

### 31. Cumbres borrascosas (ed. Alba)

**Emily Brontë** · *Drama · Novela · Psicológico · Romántico*

Como dijo Virginia Woolf, Emily Brontë era capaz de liberar la vida de su dependencia de los hechos; con un par de pinceladas podía retratar el espíritu de una cara de modo que no precisara …

<details><summary>Sinopsis completa</summary>

Como dijo Virginia Woolf, Emily Brontë era capaz de liberar la vida de su dependencia de los hechos; con un par de pinceladas podía retratar el espíritu de una cara de modo que no precisara cuerpo; al hablar del páramo, conseguía hacer que el viento soplara y el trueno rugiera. La magnífica traducción de Carmen Martín Gaite vierte al castellano toda la pasión y verdad poética contenidas en esta gran obra. Cumbres borrascosas , que se convertiría en una de las novelas más indiscutibles del siglo XIX, tuvo una acogida decepcionante cuando se publicó en 1847, pues los lectores victorianos se sintieron incomodados por lo que consideraron una descripción demasiado cruda de pasiones sin control. Al igual que Jane Eyre , de la hermana de Emily, Charlotte Brontë, Cumbres borrascosas se basa en la tradición de novela gótica de finales del XVIII, con apariciones sobrenaturales, noches sin luna y efectos de misterio y terror. Pero la novela trasciende ampliamente el género gracias a sus penetrantes observaciones y a su complejidad, así como, por encima de todo, a sus inolvidables caracterizaciones. La trágica historia de amor entre la apasionada Catherine y el atormentado Heathcliff es sin duda uno de los romances más inolvidables de la literatura de todos los tiempos.

</details>

### 32. De animales a dioses

**Yuval Noah Harari** · *Ciencias naturales · Ensayo · Historia*

Hace 100.000 años al menos seis especies de humanos habitaban la Tierra. Hoy solo queda una, la nuestra: Homo sapiens. ¿Cómo logró nuestra especie imponerse en la lucha por la existencia? ¿Por qué nuestros ancestros …

<details><summary>Sinopsis completa</summary>

Hace 100.000 años al menos seis especies de humanos habitaban la Tierra. Hoy solo queda una, la nuestra: Homo sapiens. ¿Cómo logró nuestra especie imponerse en la lucha por la existencia? ¿Por qué nuestros ancestros recolectores se unieron para crear ciudades y reinos? ¿Cómo llegamos a creer en dioses, en naciones o en los derechos humanos; a confiar en el dinero, en los libros o en las leyes? ¿Cómo acabamos sometidos a la burocracia, a los horarios y al consumismo? ¿Y cómo será el mundo en los milenios venideros? En De animales a dioses Yuval Noah Harari traza una breve historia de la humanidad, desde los primeros humanos que caminaron sobre la Tierra hasta los radicales y a veces devastadores avances de las tres grandes revoluciones que nuestra especie ha protagonizado: la cognitiva, la agrícola y la científica. A partir de hallazgos de disciplinas tan diversas como la biología, la antropología, la paleontología o la economía, Harari explora cómo las grandes corrientes de la historia han modelado nuestra sociedad, los animales y las plantas que nos rodean e incluso nuestras personalidades. ¿Hemos ganado en felicidad a medida que ha avanzado la historia? ¿Seremos capaces de liberar alguna vez nuestra conducta de la herencia del pasado? ¿Podemos hacer algo para influir en los siglos futuros? Audaz, ambicioso y provocador, este libro cuestiona todo lo que creíamos saber sobre el ser humano: nuestros orígenes, nuestras ideas, nuestras acciones, nuestro poder... y nuestro futuro.

</details>

### 33. Diez negritos

**Agatha Christie** · *Intriga · Policíaco*

Diez personas reciben sentadas cartas firmadas por un desconocido Mr. Owen, que las invita a pasar unos días en la mansión que tienen en uno de los islotes de la costa de Devon. La primera …

<details><summary>Sinopsis completa</summary>

Diez personas reciben sentadas cartas firmadas por un desconocido Mr. Owen, que las invita a pasar unos días en la mansión que tienen en uno de los islotes de la costa de Devon. La primera noche, después de la cena, una voz los acusa, de ser culpables de un crimen. Lo que parece ser una broma macabra se convierte en una espantosa realidad cuando, uno por uno, los diez invitados son asesinados en una atmósfera de miedo y mutuas recriminaciones. La clave parece estar en una vieja canción infantil: "Diez negritos se fueron a cenar, uno se ahogó y quedaron nueve. Nueve negritos trasnocharon mucho, uno no despertó, y quedaron ocho..."

</details>

### 34. Divergente

**Veronica Roth** · *Ciencia ficción · Infantil y juvenil · Romántico* · Serie: Divergente, tomo 1

Beatrice “Tris” Pior ha alcanzado la fatídica edad de dieciséis años, la etapa en que los adolescentes en el distópico Chicago de Verónica Roth deben seleccionar a cuál de los cinco grupos van a unirse …

<details><summary>Sinopsis completa</summary>

Beatrice “Tris” Pior ha alcanzado la fatídica edad de dieciséis años, la etapa en que los adolescentes en el distópico Chicago de Verónica Roth deben seleccionar a cuál de los cinco grupos van a unirse de por vida. Cada grupo representa una virtud: Verdad, Abnegación, Osadía, Cordialidad y Erudición. Para sorpresa de ella misma y su desinteresada familia Abnegación, ella elige Osadía, el camino de la valentía. Su elección la expone a los exigentes, violentos ritos de Iniciación de este grupo, pero también a la amenaza de exponer un secreto personal que la puede poner en peligro mortal. La trilogía Divergente de Verónica Roth para jóvenes adultos se inicia con una aventura fascinante de amor y lealtad jugando bajo las más extremas circunstancia.

</details>

### 35. Doctor Sueño

**Stephen King** · *Novela · Terror* · Serie: El resplandor, tomo 2

Llega la esperada continuación de El Resplandor. Danny Torrance, aquel niño que recorría en triciclo las siniestras habitaciones del Hotel Overlook, es ahora un adulto con muchos problemas. Ha aprendido a controlar en parte sus …

<details><summary>Sinopsis completa</summary>

Llega la esperada continuación de El Resplandor. Danny Torrance, aquel niño que recorría en triciclo las siniestras habitaciones del Hotel Overlook, es ahora un adulto con muchos problemas. Ha aprendido a controlar en parte sus visiones y trabaja en un asilo de ancianos donde los ayuda a morir en paz cuando llega el momento. Por eso le llaman Doctor Sueño. Pero su don le pone en contacto con otros que comparten «el resplandor» y para salvar a una niña, tendrá que luchar contra los seres malignos más repugnantes.

</details>

### 36. Dune

**Frank Herbert** · *Ciencia ficción* · Serie: Dune, tomo 1

Arrakis: un planeta desértico donde el agua es el bien más preciado, donde llorar a los muertos es el símbolo de máxima prodigalidad. Paul Atreides: un adolescente marcado por un destino singular, dotado de extraños …

<details><summary>Sinopsis completa</summary>

Arrakis: un planeta desértico donde el agua es el bien más preciado, donde llorar a los muertos es el símbolo de máxima prodigalidad. Paul Atreides: un adolescente marcado por un destino singular, dotado de extraños poderes, abocado a convertirse en dictador, mesías y mártir. Los Harkonnen: personificación de las intrigas que rodean el Imperio Galáctico, buscan obtener el control sobre Arrakis para disponer de la melange, preciosa especia y uno de los bienes más codiciados del universo. Los Fremen: seres libres que han convertido el inhóspito paraje de Dune en su hogar, y que se sienten orgullosos de su pasado y temerosos de su futuro. Dune: una obra maestra unánimemente reconocida como la mejor saga de ciencia ficción de todos los tiempos.

</details>

### 37. Edenbrooke

**Julianne Donaldson** · *Histórico · Novela · Romántico*

Marianne Daventry haría cualquier cosa para escapar del aburrimiento de Bath y las atenciones amorosas de un cretino que no le interesa en absoluto. Así que cuando le llega una invitación de su hermana gemela, …

<details><summary>Sinopsis completa</summary>

Marianne Daventry haría cualquier cosa para escapar del aburrimiento de Bath y las atenciones amorosas de un cretino que no le interesa en absoluto. Así que cuando le llega una invitación de su hermana gemela, Cecily, para que se una a ella en una maravillosa casa de campo, aprovecha la oportunidad. Por fin podrá relajarse y disfrutar del campo, que tanto le gusta, mientras su hermana se las arregla para librarse de las atenciones del guapo heredero de Edenbrooke. Sin embargo, Marianne acabará por descubrir que incluso los mejores planes pueden salir mal: primero será un aterrador encuentro con un salteador de caminos, después un coqueteo aparentemente inofensivo... el caso es que, al final, Marianne se verá envuelta en una inesperada aventura llena de intriga y de amor, tan apasionante que no podrá dar descanso a su mente. ¿Será capaz de controlar su corazón traidor o caerá rendida ante un misterioso desconocido? Está claro, el destino quiere para Marianne algo distinto a lo que ella había planeado al ir a Edenbrooke.

</details>

### 38. El Alquimista

**Paulo Coelho** · *Autoayuda*

Este libro relata la historia de un joven pastor andaluz que un día dejó su rebaño de ovejas para emprender un viaje en el que aprendió a escuchar a su corazón y descifrar un lenguaje …

<details><summary>Sinopsis completa</summary>

Este libro relata la historia de un joven pastor andaluz que un día dejó su rebaño de ovejas para emprender un viaje en el que aprendió a escuchar a su corazón y descifrar un lenguaje que está más allá de las palabras. Nos recuerda la incapacidad que las personas tienen para escoger su propio destino. Nos habla de la leyenda personal que cada persona tiene. Vivir la leyenda personal es la razón de vivir. Y cuando quieres algo, todo el Universo conspira para que realices tu deseo, tu sueño. El jóven pastor viaja en busca de su tesoro escondido siguiendo las señales. Dios escribió en el mundo el camino que cada hombre debe seguir. Sólo hay que leer lo que Él escribió para cada uno de nosotros. El Alquimista es comparado con otros libros conocidos como El Principito o Juan Salvador Gaviota. Con este viaje por las arenas del desierto, Paulo Coelho crea un símbolo hermoso y revelador de la vida, el hombre y sus sueños.

</details>

### 39. El amor en los tiempos del cólera

**Gabriel García Márquez** · *Clásico · Romántico*

De jóvenes, Florentino Ariza y Fermina Daza se enamoran apasionadamente, pero Fermina eventualmente decide casarse con un médico rico y de muy buena familia. Florentino está anonadado, pero es un romántico. Su carrera en los …

<details><summary>Sinopsis completa</summary>

De jóvenes, Florentino Ariza y Fermina Daza se enamoran apasionadamente, pero Fermina eventualmente decide casarse con un médico rico y de muy buena familia. Florentino está anonadado, pero es un romántico. Su carrera en los negocios florece, y aunque sostiene 622 pequeños romances, su corazón todavía pertenece a Fermina. Cuando al fin el esposo de ella muere, Florentino acude al funeral con toda intención. A los cincuenta años, nueve meses y cuatro días de haberle profesado amor a Fermina, lo hará una vez más. Con sagacidad humorística y depurado estilo, García Márquez traza la historia excepcional de un amor que no ha sido correspondido por medio siglo. Aunque nunca parece estar propiamente contenido, el amor fluye a través de la novela de mil maneras –alegre, melancólico, enriquecedor, pero siempre sorprendente–.

</details>

### 40. El Arte de la Seducción

**Robert Greene** · *Autoayuda · Divulgación*

Consigue lo que quieras manipulando la más importante debilidad de cualquier persona: el deseo de placer. Se trata de la seducción, una habilidad que está al alcance de cualquiera y que, empleada con destreza, permite …

<details><summary>Sinopsis completa</summary>

Consigue lo que quieras manipulando la más importante debilidad de cualquier persona: el deseo de placer. Se trata de la seducción, una habilidad que está al alcance de cualquiera y que, empleada con destreza, permite manipular, controlar y doblegar la voluntad de los demás sin recurrir a la violencia física ni a la presión psicológica. Con su claridad y amenidad características, Robert Green muestra aquí todo lo que se puede lograr mediante este sutil arte, así como las estrategias, maniobras y reglas más eficaces para conseguirlo. Con este fin se apoya en ejemplos tomados de la historia y en la biografía de algunos de los seductores más célebres del pasado, tales como Cleopatra, Casanova, De Gaulle y John F. Kennedy. Asimismo sintetiza las ideas de aquellos que han analizado el tema, como el poeta Ovidio y el filósofo Soren Kierkegaard. Estamos, sin duda, ante un libro imprescindible para vencer la resistencia del otro y lograr que se rinda a nuestros deseos.

</details>

### 41. El bestiario de Axlin

**Laura Gallego García** · *Fantástico · Juvenil · Novela* · Serie: Guardianes de la Ciudadela, tomo 1

EN UN MUNDO LLENO DE MONSTRUOS, SOLO UN LIBRO PUEDE SALVARNOS. El mundo de Axlin está plagado de monstruos. Algunos atacan a los viajeros en los caminos, otros asedian las aldeas hasta que logran arrasarlas …

<details><summary>Sinopsis completa</summary>

EN UN MUNDO LLENO DE MONSTRUOS, SOLO UN LIBRO PUEDE SALVARNOS. El mundo de Axlin está plagado de monstruos. Algunos atacan a los viajeros en los caminos, otros asedian las aldeas hasta que logran arrasarlas y otros entran en las casas para llevarse a los niños mientras duermen. Axlin ha crecido sabiendo que la próxima puede ser ella, por eso se ha propuesto descubrirlo todo acerca de los monstruos y plasmarlo en un libro que pueda servir de guía y protección a otras personas. Pero pronto se da cuenta de que si realmente quiere salvar a alguien tendrá que salir de su aldea y recorrer el ancho e inseguro mundo de ahí fuera. A lo largo de su viaje descubrirá cosas que jamás habría imaginado cuando partió.

</details>

### 42. El brillo de las luciérnagas

**Paul Pen** · *Intriga*

Tengo diez años y llevo toda mi vida dentro de este sótano. Vivo en la oscuridad con mis padres, mi abuela, mi hermana y mi hermano. Todos están desfigurados por el fuego. Mi hermana lleva …

<details><summary>Sinopsis completa</summary>

Tengo diez años y llevo toda mi vida dentro de este sótano. Vivo en la oscuridad con mis padres, mi abuela, mi hermana y mi hermano. Todos están desfigurados por el fuego. Mi hermana lleva una máscara blanca para tapar sus quemaduras, porque papá dice que su cara podría asustarme. Me gusta mi cactus. Me gusta leer mi libro sobre insectos. Y tocar durante horas el único rayo de sol que se filtra por una rendija del techo. Pero desde que mi hermana tuvo al bebé, todos actúan de forma extraña. Creo que me cuentan mentiras sobre quién es el padre, sobre el Hombre Grillo que acecha por las noches, sobre lo que sucedió antes de que yo naciera, sobre por qué estamos aquí encerrados. Por lo menos tengo a las luciérnagas. Llegaron hace unos días al sótano y las he guardado en un bote. Como dice mi abuela, no existe criatura más fascinante que aquella que es capaz de crear luz por sí misma. Esa luz me anima a conocer el mundo exterior, escapar, descubrir qué le sucedió a mi familia. Lo malo es que aquí todas las puertas están cerradas. Y no sé dónde voy a encontrar una salida…

</details>

### 43. El caballero de la armadura oxidada

**Robert Fisher** · *Autoayuda · Fantástico*

'El caballero de la armadura oxidada' (en inglés, 'The Knight in Rusty Armor') es una novela del escritor estadounidense Robert Fisher, en el género de autoayuda con elementos de ficción. Es un best seller del …

<details><summary>Sinopsis completa</summary>

'El caballero de la armadura oxidada' (en inglés, 'The Knight in Rusty Armor') es una novela del escritor estadounidense Robert Fisher, en el género de autoayuda con elementos de ficción. Es un best seller del que se han vendido más de un millón de copias y ha tenido un gran impacto tanto en niños como en adultos. Este libro refleja el proceso de un ser humano que no expresa sus sentimientos. Los cambios y los sentimientos que un hombre con corazón debería tener están reflejados en los castillos que tiene que atravesar y la confianza que debe tener.

</details>

### 44. El camino de los reyes – segunda edicion

**Brandon Sanderson** · *Fantástico · Novela* · Serie: El archivo de las tormentas, tomo 1

En Roshar, un mundo de piedra y tormentas, extrañas tempestades de increíble potencia barren el rocoso territorio de tal manera que han dado forma a una nueva civilización escondida. Han pasado siglos desde la caída …

<details><summary>Sinopsis completa</summary>

En Roshar, un mundo de piedra y tormentas, extrañas tempestades de increíble potencia barren el rocoso territorio de tal manera que han dado forma a una nueva civilización escondida. Han pasado siglos desde la caída de las diez órdenes consagradas conocidas como los Caballeros Radiantes, pero sus espadas y armaduras aún permanecen. En las Llanuras Quebradas se libra una guerra sin sentido. Kaladin ha sido sometido a la esclavitud, mientras diez ejércitos luchan por separado contra un solo enemigo. El comandante de uno de los otros ejércitos, el señor Dalinar, se siente fascinado por un antiguo texto llamado El camino de los reyes . Mientras tanto, al otro lado del océano, su eminente y hereje sobrina, Jasnah Kholin, forma a su discípula, la joven Shallan, quien investigará los secretos de los Caballeros Radiantes y la verdadera causa de la guerra.

</details>

### 45. El castillo ambulante

**Diana Wynne Jones** · *Fantástico · Infantil y juvenil* · Serie: Howl, tomo 1

Al huir de Ingary bajo los efectos de un terrible maleficio, Sophie Hatter encuentra el castillo del mago Howl. El mago es temido en toda la región y hace que su castillo se traslade de …

<details><summary>Sinopsis completa</summary>

Al huir de Ingary bajo los efectos de un terrible maleficio, Sophie Hatter encuentra el castillo del mago Howl. El mago es temido en toda la región y hace que su castillo se traslade de un sitio a otro. De forma inesperada, el mago y Sophie colaborarán, cambiando el destino de muchas personas. En 2004 se estrenó la película de animación que adaptaba la novela, dirigida por Hayao Miyazaki, que fue nominada a los Óscar

</details>

### 46. El chico que dibujaba constelaciones

**Alice Kellen** · *Novela · Romántico*

Esta es una historia de amor, de sueños y de vida. La de Valentina. La chica que no sabía que tenía el mundo a sus pies, la que creció y empezó a pensar en imposibles. …

<details><summary>Sinopsis completa</summary>

Esta es una historia de amor, de sueños y de vida. La de Valentina. La chica que no sabía que tenía el mundo a sus pies, la que creció y empezó a pensar en imposibles. La que cazaba estrellas, la que anhelaba más, la que tropezó con él. Con Gabriel. El chico que dibujaba constelaciones, el valiente e idealista, el que confió en las palabras «para siempre», y creó los pilares que terminaron sosteniendo el pasado, el ahora, lo que fueron y los recuerdos que se convertirán en polvo.

</details>

### 47. El código Da Vinci

**Dan Brown** · *Aventuras · Intriga · Policíaco* · Serie: Robert Langdon, tomo 2

v 1.0 Antes de morir asesinado, Jacques Saunière, el último Gran Maestre de una sociedad secreta que se remonta a la fundación de los Templarios, transmite a su nieta Sophie una misteriosa clave. Saunière y …

<details><summary>Sinopsis completa</summary>

v 1.0 Antes de morir asesinado, Jacques Saunière, el último Gran Maestre de una sociedad secreta que se remonta a la fundación de los Templarios, transmite a su nieta Sophie una misteriosa clave. Saunière y sus predecesores, entre los que se encontraban hombres como Isaac Newton o Leonardo Da Vinci, han conservado durante siglos un conocimiento que puede cambiar completamente la historia de la humanidad. Ahora Sophie, con la ayuda del experto en simbología Robert Langdon, comienza la búsqueda de ese secreto, en una trepidante carrera que les lleva de una clave a otra, descifrando mensajes ocultos en los más famosos cuadros del pintor y en las paredes de antiguas catedrales. Un rompecabezas que deberán resolver pronto, ya que no están solos en el juego: una poderosa e influyente organización católica está dispuesta a emplear todos los medios para evitar que el secreto salga a la luz. Un apasionante juego de claves escondidas, sorprendentes revelaciones, acertijos ingeniosos, verdades, mentiras, realidades históricas, mitos, símbolos, ritos, misterios y suposiciones en una trama llena de giros inesperados, narrada con un ritmo imparable que conduce al lector hasta el secreto más celosamente guardado del inicio de nuestra era.

</details>

### 48. El color que cayó del cielo

**H. P. Lovecraft** · *Terror*

La historia es contada en primera persona por un ingeniero encargado de hacer un estudio para edificar un lago en un remoto paraje, llamado Arkham. Allí encuentra un área de terreno que es distinta a …

<details><summary>Sinopsis completa</summary>

La historia es contada en primera persona por un ingeniero encargado de hacer un estudio para edificar un lago en un remoto paraje, llamado Arkham. Allí encuentra un área de terreno que es distinta a todas y que le causa extrañas sensaciones. Un anciano vecino del lugar le explica que el motivo del estado de esa parcela es que un meteorito se estrelló cerca de una granja, y, al transcurrir el tiempo, las plantas y árboles primero, y los animales después, empiezan a sufrir mutaciones, cambios de color, olores desagradables, acabando afectando a la familia que habita la granja, enloqueciéndola hasta morir en un trágico final, y el ingeniero decide abandonar su trabajo electrizado por el horror que descubre.

</details>

### 49. El Cuarto Mono

**J. D. Barker** · *Intriga · Novela · Policíaco* · Serie: Detective Porter, tomo 1

El detective de la policía de Chicago Sam Porter investiga el caso de un hombre atropellado, pues los indicios en la escena del crimen apuntan a que se trata de El Cuarto Mono, un asesino …

<details><summary>Sinopsis completa</summary>

El detective de la policía de Chicago Sam Porter investiga el caso de un hombre atropellado, pues los indicios en la escena del crimen apuntan a que se trata de El Cuarto Mono, un asesino en serie que ha estado aterrorizando la ciudad. Su modus operandi consistía en enviar tres cajas blancas a los padres de las víctimas que secuestra y mata: una primera con una oreja, una segunda con los dos ojos, y otra con la lengua; y finalmente dejar abandonado el cuerpo sin vida en algún lugar. El hombre atropellado llevaba una de esas cajas blancas. Se inicia así una frenética carrera contrarreloj para averiguar dónde se encuentra encerrada la próxima víctima.

</details>

### 50. El cuento de la criada

**Margaret Atwood** · *Autoayuda · Ciencia ficción*

Se sitúa en un futuro próximo y describe la vida en lo que antaño fue Estados Unidos, convertido en una teocracia monolítica que ha reaccionado ante los trastornos sociales y ante una disminu­ción progresiva del …

<details><summary>Sinopsis completa</summary>

Se sitúa en un futuro próximo y describe la vida en lo que antaño fue Estados Unidos, convertido en una teocracia monolítica que ha reaccionado ante los trastornos sociales y ante una disminu­ción progresiva del índice de natalidad con un retorno a la intolerancia represiva de la ideología puritana. Comparable a Un mundo feliz de Huxley, 1984 de Orwell o La naranja mecánica de Burgess, la fabulación nos muestra, desde el punto de vista de las mujeres, el horror oculto o latente en el envés de nuestra vida diaria, la trama vibradora que sustenta la cotidianidad en una prosa de admirable y ate­rradora precisión. Una de las novelas más célebres y prestigiosas de Margaret Atwood, constituye una mirada futurista, terrible y lúcida a una sociedad totalitaria que denuncia la barbarie que pueden llegar a alcanzar los puritanismos extremos de toda índole, con sus ansias de dominio sobre los seres humanos, a los que privan del ejercicio del derecho a la libertad.

</details>

### 51. El cuento número trece

**Diane Setterfield** · *Intriga · Otros*

Cuando una vieja escritora acostumbrada a mentir y una joven librera empeñada en saber la verdad se encuentran, regresan los fantasmas del pasado, los secretos de una familia marcada por el exceso, las cenizas de …

<details><summary>Sinopsis completa</summary>

Cuando una vieja escritora acostumbrada a mentir y una joven librera empeñada en saber la verdad se encuentran, regresan los fantasmas del pasado, los secretos de una familia marcada por el exceso, las cenizas de un incendio memorable y el perfil de un ser extraño que aparece y desaparece tras las cortinas de una mansión. Entre mentiras, recuerdos e imaginación se teje la vida de la señora Winter, una famosa novelista ya muy entrada en años que pide ayuda a Margaret, una mujer joven y amante de los libros, para contar por fin la historia de su misterioso pasado. "Cuéntame la verdad", pide Margaret, pero la verdad duele, y solo el día en que Vida Winter muera sabremos qué secretos encerraba El cuento número trece, una historia que nadie se había atrevido a escribir. Después de cinco años de intenso trabajo, Diane Setterfield ha logrado el aplauso de los lectores y el respeto de los críticos con una primera novela que pronto se convertirá en un clásico.

</details>

### 52. El día que dejó de nevar en Alaska

**Alice Kellen** · *Novela · Romántico*

De la autora New Adult más leída en nuestro país. Alice Kellen nos sorprende de nuevo con una gran historia de segundas oportunidades y destinos que se cruzan. Un romance que fundirá hasta el corazón …

<details><summary>Sinopsis completa</summary>

De la autora New Adult más leída en nuestro país. Alice Kellen nos sorprende de nuevo con una gran historia de segundas oportunidades y destinos que se cruzan. Un romance que fundirá hasta el corazón más helado. Un chico con el corazón de hielo. Una chica que huye de sí misma. Dos destinos que se cruzan. Heather cree que solo hay tres cosas que sabe hacer: atraer problemas, salir huyendo y correr. Así es como termina en Alaska, en un pequeño pueblo perdido, trabajando de camarera mientras intenta llevar una vida nueva y tranquila. Su único problema es que uno de los dueños del restaurante parece odiarla y que ella nunca antes ha conocido a nadie que despierte tanto su curiosidad. Nilak es reservado, frío y distante, pero Heather puede ver a través de todas las capas tras las que se esconde y sabe que en ocasiones hay recuerdos que pesan demasiado; como los de sus propios errores, esos que intenta dejar atrás. Pero, a veces, la vida te da una segunda oportunidad. La nieve empieza a derretirse. Y todo encaja.

</details>

### 53. El día que el cielo se caiga

**Megan Maxwell** · *Novela · Romántico*

Alba y Nacho se conocen desde que eran niños. La conexión entre ellos es muy especial y aumenta con el paso de los años, hasta que ella se casa y, obligada por su marido, se …

<details><summary>Sinopsis completa</summary>

Alba y Nacho se conocen desde que eran niños. La conexión entre ellos es muy especial y aumenta con el paso de los años, hasta que ella se casa y, obligada por su marido, se distancia de él. Nacho se marcha a Londres. Allí encontrará al amor de su vida, a quien luego perderá a causa de una desconocida enfermedad. Alba, que no sabe lo mal que lo está pasando su amigo, acude a él tras su fracaso matrimonial. Su reencuentro crea una unión irrompible, pero al cabo de poco tiempo ella descubre que Nacho también está enfermo. En su afán por ayudarlo a luchar contra lo que parece inevitable, Alba conocerá a Víctor. Y lo que en un principio no son más que encuentros fortuitos, se acaba convirtiendo en un amor incondicional que le permitirá superar sus miedos e inseguridades. Esta novela hará que te cuestiones varias cosas: ¿por qué el destino es capaz de hacernos encontrar a nuestra media naranja en el peor momento de nuestra vida? ¿Por qué siempre decimos que se mueren los buenos y los malos se quedan aquí para fastidiarnos? Si quieres conocer el desenlace de esta tierna, emotiva y dura historia de amor y amistad, no te pierdas El día que el cielo se caiga .

</details>

### 54. El día que se perdió la cordura

**Javier Castillo** · *Intriga · Novela*

En el centro de Boston, a las 12 de la mañana de un 24 de diciembre, un hombre camina desnudo con la cabeza decapitada de una joven. El Dr. Jenkins, director del centro psiquiátrico de …

<details><summary>Sinopsis completa</summary>

En el centro de Boston, a las 12 de la mañana de un 24 de diciembre, un hombre camina desnudo con la cabeza decapitada de una joven. El Dr. Jenkins, director del centro psiquiátrico de la ciudad, y Stella Hyden, agente de perfiles del FBI, se adentrarán en una investigación que pondrá en juego sus vidas, su concepción de la cordura, y que viajará atrás 17 años hasta unos eventos fortuitos ocurridos en el misterioso pueblo de Salt Lake. "Narrada magistralmente a tres tiempos, el autor nos sumerge a ritmo de thriller en una historia de amor y odio a partes iguales, en las que se exploran los extremos del ser humano"

</details>

### 55. El duque y yo

**Julia Quinn** · *Histórico · Novela · Romántico* · Serie: Bridgerton, tomo 1

Todos parecían divertirse en aquel baile que reunía a lo más selecto de la sociedad londinense. Todos, excepto ellos dos. Daphne, una hermosa joven agobiada por su madre, y Simon, el huraño nuevo duque de …

<details><summary>Sinopsis completa</summary>

Todos parecían divertirse en aquel baile que reunía a lo más selecto de la sociedad londinense. Todos, excepto ellos dos. Daphne, una hermosa joven agobiada por su madre, y Simon, el huraño nuevo duque de Hastings, tenían el mismo problema: la continua presión para que encontraran pareja. Al conocerse, se les ocurrió el plan perfecto: fingir un compromiso que los liberara de más agobios. Pero no sería sencillo, ya que el hermano de Daphne, amigo de Simon, no es fácil de engañar, ni tampoco lo son las avezadas damas de la alta sociedad. Aunque lo que complicará de verdad las cosas será la aparición de un elemento que no estaba previsto en este juego a dos bandas: el amor. I dearon un plan perfecto en el que el amor no tenía cabida … Desde que fue presentada en sociedad, Daphne no tiene un momento de respiro. La culpa es de su madre, a la que adora, pero que está obsesionada con encontrarle un marido cuanto antes. Lo peor del caso es que los hombres razonablemente deseables no están interesados, y los que sí lo están son unos incansables pesados de los que tiene que librarse… incluso a golpes. Por eso acepta encantada la idea del duque de Hastings de fingir un noviazgo que ahuyente a los pretendientes. Aunque quizá también tenga algo que ver el hecho de que el joven duque comienza a resultarle cada vez más seductor. Pero hay cosas de las que es imposible escapar . Marcado por una infancia llena de soledad y resentimiento, Simon Basset, el nuevo duque de Hastings, no quiere saber nada de la vida social de Londres ni, desde luego, de los intentos de las elegantes damas de «cazarlo» como marido para sus hijas. Cuando conoce a Daphne, cree haber encontrado el plan perfecto: un compromiso ficticio que mantenga alejadas a las pretendientes que lo agobian. Y cuando la atracción fingida comienza a convertirse en algo demasiado real, Simon deberá enfrentarse a los fantasmas del pasado que le impiden disfrutar la felicidad que el destino pone al alcance de su mano.

</details>

### 56. El engaño populista

**Axel Kaiser | Gloria Álvarez** · *Ciencias sociales · Divulgación*

La batalla política tanto en América Latina como en España ya no es tanto entre la izquierda y la derecha, sino entre populismo y Estado. Dos voces jóvenes del pensamiento político latinoamericano realizan un diagnóstico …

<details><summary>Sinopsis completa</summary>

La batalla política tanto en América Latina como en España ya no es tanto entre la izquierda y la derecha, sino entre populismo y Estado. Dos voces jóvenes del pensamiento político latinoamericano realizan un diagnóstico de lo que consideran uno de los grandes males de la política latinoamericana, el populismo, y proponen una receta para la restauración de la república, entendida aquí como la suma de instituciones que garantizan la libertad democrática de los ciudadanos. El engaño populista combina el análisis teórico fundamentado, el estudio de casos concretos y vigentes y la llamada a la acción. Para ello examina las manifestaciones populistas en diversos países de América Latina y los casos emergentes a escala internacional, entre los que incluyen el proyecto de Podemos en España, o las declaraciones públicas del papa Francisco.

</details>

### 57. El extranjero

**Albert Camus** · *Drama*

El extranjero (tí­tulo original francés L'Étranger, 1942) es una novela del escritor francés Albert Camus. El personaje de la obra es un ser indiferente a la realidad por resultarle absurda e inabordable. El progreso tecnológico …

<details><summary>Sinopsis completa</summary>

El extranjero (tí­tulo original francés L'Étranger, 1942) es una novela del escritor francés Albert Camus. El personaje de la obra es un ser indiferente a la realidad por resultarle absurda e inabordable. El progreso tecnológico le ha privado de la participación en las decisiones colectivas y le ha convertido en «extranjero» dentro de lo que deberí­a ser su propio entorno. El protagonista, el señor Meursault, comete un absurdo crimen y, a pesar de sentirse inocente, jamás se manifestará contra su ajusticiamiento ni mostrará sentimiento alguno de injusticia, arrepentimiento o lástima. La pasividad y el escepticismo frente a todo y todos recorre el comportamiento del protagonista: un sentido absurdo de la existencia y aun de la propia muerte.

</details>

### 58. El fin de la inflación

**Alberto Benegas Lynch (h) | Diana Mondino | Domingo Cavallo | Federico Sturzenegger | Héctor Rubini | Javier Milei** · *Divulgación · Economía · Política*

Eliminar el Banco Central, terminar con la estafa del impuesto inflacionario y volver a ser un país en serio Plantándole cara a la casta política, peleando contra un supuesto sentido común de época que está …

<details><summary>Sinopsis completa</summary>

Eliminar el Banco Central, terminar con la estafa del impuesto inflacionario y volver a ser un país en serio Plantándole cara a la casta política, peleando contra un supuesto sentido común de época que está destruyendo la Argentina y retando a duelo de ideas a colegas economistas, el candidato a la presidencia de la Nación presenta aquí tres textos que conforman el núcleo de lo que podría ser leído como un programa de gobierno, y que en realidad es mucho más que eso: se trata de un ataque frontal a la inflación, ese mal que corroe día a día la vida de millones y millones de argentinos. No será una lucha fácil, advierte Javier Milei: demasiados intereses enquistados, privilegios que llevan décadas, miserias corporativas. Pero hay una buena noticia: dar la pelea contra la inflación, recuperar la libertad de elegir qué hacer con nuestro dinero y terminar con las mentiras de una economía intoxicada por la política colocarán los cimientos para volver a ser un gran país.

</details>

### 59. El guardián invisible

**Dolores Redondo** · *Intriga · Terror* · Serie: Trilogía del Baztán, tomo 1

«Ainhoa Elizasu fue la segunda víctima del basajaun, aunque entonces la prensa todavía no lo llamaba así. Fue un poco más tarde cuando trascendió que alrededor de los cadáveres aparecían pelos de animal, restos de …

<details><summary>Sinopsis completa</summary>

«Ainhoa Elizasu fue la segunda víctima del basajaun, aunque entonces la prensa todavía no lo llamaba así. Fue un poco más tarde cuando trascendió que alrededor de los cadáveres aparecían pelos de animal, restos de piel y rastros dudosamente humanos, unidos a una especie de fúnebre ceremonia de purificación. Una fuerza maligna, telúrica y ancestral parecía haber marcado los cuerpos de aquellas casi niñas con la ropa rasgada, el vello púbico rasurado y las manos dispuestas en actitud virginal.» En los márgenes del río Baztán, en el valle de Navarra, aparece el cuerpo desnudo de una adolescente en unas circunstancias que lo ponen en relación con un asesinato ocurrido en los alrededores un mes atrás.La inspectora de la sección de homicidios dela Policía Foral, Amaia Salazar, será la encargada de dirigir una investigación que la llevará de vuelta a Elizondo, una pequeña población de donde es originaria y de la que ha tratado de huir toda su vida. Enfrentada con las cada vez más complicadas derivaciones del caso y con sus propios fantasmas familiares, la investigación de Amaia es una carrera contrarreloj para dar con un asesino que puede mostrar el rostro más aterrador de una realidad brutal al tiempo que convocar a los seres más inquietantes de las leyendas del Norte.

</details>

### 60. El hobbit

**J. R. R. Tolkien** · *Fantástico* · Serie: Legendarium, tomo 4

Bilbo Bolsón es como cualquier hobbit: no mide más de metro y medio, vive pacíficamente en la Comarca, y su máxima aspiración es disfrutar de los placeres sencillos de la vida (comer bien, pasear y …

<details><summary>Sinopsis completa</summary>

Bilbo Bolsón es como cualquier hobbit: no mide más de metro y medio, vive pacíficamente en la Comarca, y su máxima aspiración es disfrutar de los placeres sencillos de la vida (comer bien, pasear y charlar con los amigos). Y es que todos ellos son tan vagos como bonachones, por naturaleza, y porque quieren. Pero una soleada mañana, Bilbo recibe la inesperada visita de Gandalf, el mago de larga barba gris y alto sombrero, que cambiará su vida para siempre. Con Gandalf y una pandilla de trece enanos, y con la ayuda de un mapa misterioso, nuestro héroe partirá hacia la Montaña Solitaria a fin de rescatar el valioso tesoro custodiado por Smaug el Dorado, un terrible y enorme dragón. Para eso tendrán que superar muchísimos peligros y toda clase de aventuras que Bilbo jamás hubiera podido ni imaginar y que lo convertirán en el hobbit más famoso del mundo. Lo que Bilbo no sabe es que el anillo que encontró en el camino será el principio de otra gran aventura... la de EL SEÑOR DE LOS ANILLOS.

</details>

### 61. El hogar de Miss Peregrine para niños peculiares

**Ransom Riggs** · *Infantil y juvenil · Intriga* · Serie: El hogar de Miss Peregrine para niños peculiares, tomo 1

El hogar de Miss Peregrine para niños peculiares es una enigmática historia sobre niños extraordinarios y monstruos oscuros; una fantasía escalofriante ilustrada con inquietantes fotografías vintage que deleitará a jóvenes y adultos. De niño, Jacob …

<details><summary>Sinopsis completa</summary>

El hogar de Miss Peregrine para niños peculiares es una enigmática historia sobre niños extraordinarios y monstruos oscuros; una fantasía escalofriante ilustrada con inquietantes fotografías vintage que deleitará a jóvenes y adultos. De niño, Jacob creó un vinculo muy especial con su abuelo, que le contaba extrañas historias y le enseñaba fotografías de niñas levitando y niños invisibles. Ahora, siguiendo la pista de una misteriosa carta, emprende un viaje hacia la isla remota de Gales en la que su abuelo se crió. Allí, encuentra vivos a los niños y niñas de las fotografías aunque los lugareños afirmen que murieron hace muchos años.

</details>

### 62. El hombre de tiza

**C. J. Tudor** · *Novela · Terror*

Hay juegos que solo tienen un final posible. Echando la vista atrás, todo comenzó el día del terrible accidente durante la feria, cuando Eddie, de doce años, conoció al Hombre de Tiza. Fue el Hombre …

<details><summary>Sinopsis completa</summary>

Hay juegos que solo tienen un final posible. Echando la vista atrás, todo comenzó el día del terrible accidente durante la feria, cuando Eddie, de doce años, conoció al Hombre de Tiza. Fue el Hombre de Tiza quien le dio la idea de los dibujos: una manera de dejar mensajes secretos entre el grupo de amigos. Fue divertido hasta que los dibujos condujeron al cuerpo sin vida de una niña. Sucedió hace treinta años y Ed pensaba que todo había quedado olvidado. Sin embargo, recibe una carta que contiene solo dos cosas: una tiza y el dibujo de un muñeco. La historia se repite y Ed se da cuenta de que el juego en realidad nunca terminó… Todos tenemos secretos. Todos somos culpables de algo. Y los niños no son siempre tan inocentes.

</details>

### 63. El imperio final

**Brandon Sanderson** · *Fantástico* · Serie: Nacidos de la bruma, tomo 1

Durante mil años, han caído las cenizas y nada florece. Durante mil años, los skaa han sido esclavizados y viven sumidos en un miedo inevitable. Durante mil años, el Lord Legislador reina con un poder …

<details><summary>Sinopsis completa</summary>

Durante mil años, han caído las cenizas y nada florece. Durante mil años, los skaa han sido esclavizados y viven sumidos en un miedo inevitable. Durante mil años, el Lord Legislador reina con un poder absoluto gracias al terror y a su divina invencibilidad. Le ayudan los «obligadores» y los «inquisidores», junto a la poderosa magia de la «alomancia», que reside en los nobles. Algunos, sólo algunos, son capaces de «quemar» los metales que han tragado y que les otorgan poderes sobrenaturales. Diferentes metales, actuando en pares, otorgan poderes distintos. Pero los nobles, demasiado a menudo, han tenido trato sexual con jóvenes skaa y, aunque la ley lo prohíbe, algunos de sus bastardos han sobrevivido. Y algunos han heredado los poderes alománticos. Los «brumosos» (mistings) tienen sólo uno de esos poderes, pero los «nacidos de la bruma» (mistborns) son capaces de dominarlos todos. Ahora, Kelsier, el «superviviente», el único que ha logrado huir de los Pozos de Hathsin, ha encontrado a Vin, una pobre chica skaa con mucha Suerte… Tal vez los dos unidos a la rebelión que los skaa intentan desde hace mil años puedan cambiar el mundo y la atroz dominación del Lord Legislador.

</details>

### 64. El Imperio Final. (Ed. revisada)

**Brandon Sanderson** · *Fantástico · Novela* · Serie: Nacidos de la bruma, tomo 1

Durante mil años, han caído las cenizas y nada florece. Durante mil años, los skaa han sido esclavizados y viven sumidos en un miedo inevitable. Durante mil años, el Lord Legislador reina con un poder …

<details><summary>Sinopsis completa</summary>

Durante mil años, han caído las cenizas y nada florece. Durante mil años, los skaa han sido esclavizados y viven sumidos en un miedo inevitable. Durante mil años, el Lord Legislador reina con un poder absoluto gracias al terror, a sus poderes y a su inmortalidad. Le ayudan «obligadores» e «inquisidores», junto a la poderosa magia de la alomancia. Pero los nobles a menudo han tenido trato sexual con jóvenes skaa y, aunque la ley lo prohíbe, algunos de sus bastardos han sobrevivido y heredado los poderes alománticos: son los «nacidos de la bruma» (mistborns). Ahora, Kelsier, el «superviviente», el único que ha logrado huir de los Pozos de Hathsin, ha encontrado a Vin, una pobre chica skaa con mucha suerte… Tal vez los dos, unidos a la rebelión que los skaa intentan desde hace mil años, logren cambiar el mundo y la atroz dominación del Lord Legislador.

</details>

### 65. El instituto

**Stephen King** · *Novela · Terror*

En mitad de la noche, en un barrio tranquilo de Minneapolis, raptan a Luke Ellis, de doce años, tras haber asesinado a sus padres. Una operación que dura menos de dos minutos. Luke se despierta …

<details><summary>Sinopsis completa</summary>

En mitad de la noche, en un barrio tranquilo de Minneapolis, raptan a Luke Ellis, de doce años, tras haber asesinado a sus padres. Una operación que dura menos de dos minutos. Luke se despierta en la siniestra institución conocida como El Instituto, en una habitación que se asemeja a la suya pero sin ventanas. En habitaciones parecidas hay otros niños: Kalisha, Nick, George, Iris y Avery Dixon, entre otros, que comparten capacidades especiales como telequinesia o telepatía. Todos ellos se alojan en la Mitad Delantera de la institución. Los mayores, en cambio, se encuentran en la Mitad Trasera. Como dice Kalisha: «Allí entras pero no sales». La señora Sigsby, la directora, y el resto del personal se dedican a aprovecharse sin compasión del talento paranormal de los chicos. Si te portas bien te premian. Si no, el castigo es brutal. Luke se da cuenta de que las víctimas van desapareciendo y son trasladadas a la Mitad Trasera, así que se obsesiona con escapar y pedir ayuda. Pero nunca nadie ha escapado de El Instituto…

</details>

### 66. El jardín de las mariposas

**Dot Hutchison** · *Intriga · Novela · Terror* · Serie: El coleccionista, tomo 1

Cerca de una aislada mansión existe un jardín donde se cultivan delicadas flores y en él, abrigada por frondosos árboles, habita una exquisita y peculiar colección de mariposas que es resguardada por el Jardinero, un …

<details><summary>Sinopsis completa</summary>

Cerca de una aislada mansión existe un jardín donde se cultivan delicadas flores y en él, abrigada por frondosos árboles, habita una exquisita y peculiar colección de mariposas que es resguardada por el Jardinero, un hombre que desconoce los límites de su obsesión por preservar la belleza. Maya es una sobreviviente del jardín y ahora tendrá que narrar a los agentes del FBI los horrores que vivió mientras permanecía en cautiverio junto con otras chicas que ni siquiera habían alcanzado la mayoría de edad. En su memoria viven las peores pesadillas. En su espalda, como en las de todas las jóvenes mariposas, un tatuaje le recordará por siempre un crimen imperdonable.

</details>

### 67. El jardín secreto

**Frances Hodgson Burnett** · *Aventuras · Clásico*

Mary es una niña inglesa nacida en la India. Sus padres no se preocupan de ella, y como nadie la quiere, es solitaria, antipática y amargada. Sorpresivamente queda huérfana y es enviada a Inglaterra, a …

<details><summary>Sinopsis completa</summary>

Mary es una niña inglesa nacida en la India. Sus padres no se preocupan de ella, y como nadie la quiere, es solitaria, antipática y amargada. Sorpresivamente queda huérfana y es enviada a Inglaterra, a la casa de campo de un tío. Pero éste -un hombre viudo, hosco y triste- casi nunca está allí. La mansión, situada en medio del páramo, es inmensa, con un enorme jardín. En él hay un sector amurallado, cuya puerta, oculta bajo la hiedra, está cerrada con llave. Hace diez años que el tío, luego de la muerte de su mujer, prohibió abrirla. Ese jardín secreto y las voces y los llantos que la niña escucha en las noches, la llenan de curiosidad y la impulsan a descubrir tanto misterio. Otra maravillosa novela de la autora de El pequeño Lord Fauntleroy, cuya interesante trama se entrelaza con el cambio de las estaciones y la llegada de la primavera.

</details>

### 68. El juego del ángel

**Carlos Ruiz Zafón** · *Intriga* · Serie: El cementerio de los libros olvidados, tomo 2

Año: 2008 Sinopsis: El Juego del Ángel es una gran aventura de intriga, romance y tragedia, a través de un laberinto de secretos donde el embrujo de los libros, la pasión y la amistad se …

<details><summary>Sinopsis completa</summary>

Año: 2008 Sinopsis: El Juego del Ángel es una gran aventura de intriga, romance y tragedia, a través de un laberinto de secretos donde el embrujo de los libros, la pasión y la amistad se conjugan en un relato magistral. Con El juego del ángel el autor de La Sombra del Viento regresa al Cementerio de los Libros Olvidados y nos sumerge de nuevo en su fascinante universo. En la turbulenta Barcelona de los años 20 un joven escritor obsesionado con un amor imposible recibe la oferta de un misterioso editor para escribir un libro como no ha existido nunca, a cambio de una fortuna y, tal vez, mucho más. “La próxima vez que quieras salvar un libro, no te juegues la vida… Te llevaré a un lugar secreto donde los libros nunca mueren y donde nadie puede destruirlos.”

</details>

### 69. El laberinto de huesos

**Rick Riordan** · *Intriga · Juvenil · Novela* · Serie: The 39 Clues, tomo 1

¿Qué pasaría si descubrieras que tu familia es una de las más poderosas de toda la historia de la humanidad? ¿Y si te dijeran que la fuente de poder de la familia está escondida por …

<details><summary>Sinopsis completa</summary>

¿Qué pasaría si descubrieras que tu familia es una de las más poderosas de toda la historia de la humanidad? ¿Y si te dijeran que la fuente de poder de la familia está escondida por todo el mundo, bajo la forma de 39 pistas? ¿Y si, además, te dieran a elegir entre tener un millón de dólares... o conseguir la primera de las pistas? Todo comienza al salir a la luz el testamento de la abuela Grace, donde se da a elegir entre mucho dinero o un reto que muy pocos serán capaces de comenzar y menos de terminar. La familia Cahill lleva años enfrentada, y ahora algunos de sus miembros son elegidos para resolver las pistas que llevarán al ganador a ser el miembro de la familia más famoso de la historia. Amy y Dan aceptan el reto, no sin antes dudar si aceptarlo, o coger el dinero. Por varios motivos terminan sumergiéndose en la aventura. Así comienza una carrera muy peligrosa. Repleta de pistas, familiares malévolos, peligros, misterios, secretos del pasado y personas extrañas.

</details>

### 70. El Laberinto de los Espíritus

**Carlos Ruiz Zafón** · *Intriga · Novela* · Serie: El cementerio de los libros olvidados, tomo 4

En la Barcelona de finales de los años 50, Daniel Sempere ya no es aquel niño que descubrió un libro que habría de cambiarle la vida entre los pasadizos del Cementerio de los Libros Olvidados. …

<details><summary>Sinopsis completa</summary>

En la Barcelona de finales de los años 50, Daniel Sempere ya no es aquel niño que descubrió un libro que habría de cambiarle la vida entre los pasadizos del Cementerio de los Libros Olvidados. El misterio de la muerte de su madre Isabella ha abierto un abismo en su alma del que su esposa Bea y su fiel amigo Fermín intentan salvarle. Justo cuando Daniel cree que está a un paso de resolver el enigma, una conjura mucho más profunda y oscura de lo que nunca podría haber imaginado despliega su red desde las entrañas del Régimen. Es entonces cuando aparece Alicia Gris, un alma nacida de las sombras de la guerra, para conducirlos al corazón de las tinieblas y desvelar la historia secreta de la familia… aunque a un terrible precio. El Laberinto de los Espíritus es un relato electrizante de pasiones, intrigas y aventuras. A través de sus páginas llegaremos al gran final de la saga iniciada con La Sombra del Viento , que alcanza aquí toda su intensidad y calado, a la vez que dibuja un gran homenaje al mundo de los libros, al arte de narrar historias y al vínculo mágico entre la literatura y la vida.

</details>

### 71. El ladrón del rayo

**Rick Riordan** · *Fantástico · Infantil y juvenil* · Serie: Percy Jackson y los dioses del Olimpo, tomo 1

¿Qué pasaría si los dioses del Olimpo estan vivos en el siglo 21? ¿Y si aún se enamoraran de los mortales y que los niños-héroes podrían llegar a ser grandes, como Teseo, Jasón y Hércules?. …

<details><summary>Sinopsis completa</summary>

¿Qué pasaría si los dioses del Olimpo estan vivos en el siglo 21? ¿Y si aún se enamoraran de los mortales y que los niños-héroes podrían llegar a ser grandes, como Teseo, Jasón y Hércules?. ¿Qué pasa si tu fueras uno de esos niños?. Tal es el descubrimiento que a los doce años de edad, Percy Jackson, se lanza en la búsqueda más peligroso de su vida. Con la ayuda de un sátiro y una hija de Atenea, Percy viaja a través de los Estados Unidos para atrapar a un ladrón que ha robado el arma original de destrucción masiva - el rayo- del maestro de Zeus. En el camino, debe enfrentar una gran cantidad de enemigos mitológicos decididos a detenerlo. Por encima de todo, debe llegar a un acuerdo con un padre que nunca conoció, y una Oraculo que le ha advertido de la traición de un amigo.

</details>

### 72. El libro negro de la Nueva Izquierda

**Agustín Laje | Nicolás Márquez** · *Ciencias sociales · Ensayo*

Tras la caída de la Unión Soviética en 1992, muchos sectores del mundo libre descansaron en ese triunfalismo que brindaba la sensación de que la utopía colectivista había perdido para siempre. Pero pocos años después, …

<details><summary>Sinopsis completa</summary>

Tras la caída de la Unión Soviética en 1992, muchos sectores del mundo libre descansaron en ese triunfalismo que brindaba la sensación de que la utopía colectivista había perdido para siempre. Pero pocos años después, abrazando nuevas banderas y reinventando su discurso, el hoy llamado neocomunismo (o progresismo cultural) no sólo pasó a dominar la agenda política sino en gran medida la mentalidad occidental. Los viejos principios socialistas de lucha de clases, materialismo dialéctico, revolución proletaria o violencia guerrillera, ahora fueron reemplazados por una rara ingesta intelectual promotora del “indigenismo ecológico”, el “derecho-humanismo” selectivo, el “garantismo jurídico” y por sobre todas las cosas, por aquello que se denomina como “ideología de género”, suerte de pornomarxismo de tinte pansexual, impulsor del feminismo radical, del homosexualismo ideológico, la pedofilia como “alternativa”, el aborto como “libre disposición del cuerpo” y todo tipo de hábitos autodestructivos como forma de rebelión ante “la tradición hetero-capitalista” de Occidente. Toda esta ensalada vanguardista se escuda bajo temas de apariencia noble, tales como el “igualitarismo”, la “inclusión”, la “diversidad” y los “derechos de las minorías”: verdaderas caretas de la ideología de género, cuyo contenido constituye la prioridad militante en esta izquierda desarmada que resolvió canalizar su odio por medio de grupos marginales o conflictuados que aquella captura y adoctrina para sí, con el fin de vehiculizarlos de manera funcional a su causa y, de esta forma, dominar la academia, hegemonizar la literatura, monopolizar las artes, manipular los modos del habla, modificar hábitos e influir en los medios de comunicación. La nueva izquierda ya no busca secuestrar empresarios sino el sentido común; no persigue tomar una fábrica sino la cátedra, y no se trata de confiscar cuentas bancarias sino la manera de pensar: “todo lo demás vendrá por añadidura”, vaticinan sus cultores. El Libro Negro de la Nueva Izquierda: Ideología de género o subversión cultural, escrito por dos autores tan audaces como Nicolás Márquez y Agustín Laje, constituye el primer libro que ataca y cuestiona todos y cada uno de los “dogmas” de un progresismo revolucionario que arrasa buscando destruir la cultura vigente para sobre sus escombros, reproducir aquel “paraíso” que por error o subestimación muchos dieron por muerto y hoy representa una grave amenaza.

</details>

### 73. El misterio de Salem’s Lot

**Stephen King** · *Terror*

Veinte años atrás, por una apuesta infantil, Ben Mears entró en la casa de los Marsten. Y lo que vio entonces aún puebla sus pesadillas. Ahora, como escritor consagrado vuelve a Salem's Lot para exorcisar …

<details><summary>Sinopsis completa</summary>

Veinte años atrás, por una apuesta infantil, Ben Mears entró en la casa de los Marsten. Y lo que vio entonces aún puebla sus pesadillas. Ahora, como escritor consagrado vuelve a Salem's Lot para exorcisar sus fantasmas. Salem's Lot es un pueblo tranquilo y adormilado donde nunca pasa nada, excepto la vieja tragedia de la casa de los Marsten. Y el perro muerto colgado de la verja del cementerio. Y el misterioso hombre que se instaló en la casa de los Marsten. Y los niños que desaparecen, los animales que mueren desangrados. Y la espantosa presencia de Ellos, quienesquiera que sean. Ellos.

</details>

### 74. El monstruo pentápodo

**Liliana Blum** · *Novela · Psicológico*

Raymundo Betancourt es el ciudadano modelo: profesionista honesto y responsable, solidario y comprometido con el bienestar de su comunidad. Pero como la vida no sólo es trabajo, también se permite dos sencillos placeres cotidianos: los …

<details><summary>Sinopsis completa</summary>

Raymundo Betancourt es el ciudadano modelo: profesionista honesto y responsable, solidario y comprometido con el bienestar de su comunidad. Pero como la vida no sólo es trabajo, también se permite dos sencillos placeres cotidianos: los chicles de canela y las niñas que mantiene secuestradas en su sótano. El monstruo pentápodo nos enfrenta sin ambages ni eufemismos con la mente oscura del asesino, del psicópata adorable y manipulador ante cuyos encantos sucumbió Aimeé –otra “pequeña”, pero a su modo- hasta el punto de volverse cómplice a cambio de un poco de amor. Liliana Blum es tan hábil como despiadada. No se toca el corazón para empujar al lector al foso donde habita esa bestia con piel de ángel que se esconde a plena luz y que podría ser tu vecino, o el mío, o el de cualquiera…

</details>

### 75. El mundo de Sofía

**Jostein Gaarder** · *Histórico · Otros*

Poco antes de cumplir los quince años, la joven Sofía recibe una misteriosa carta anónima con las siguientes preguntas: «¿Quién eres?», «¿De dónde viene el mundo?». Éste es el punto de partida de una apasionada …

<details><summary>Sinopsis completa</summary>

Poco antes de cumplir los quince años, la joven Sofía recibe una misteriosa carta anónima con las siguientes preguntas: «¿Quién eres?», «¿De dónde viene el mundo?». Éste es el punto de partida de una apasionada expedición a través de la historia de la filosofía con un enigmático filósofo. A lo largo de la novela, Sofía irá desarrollando su identidad a medida que va ampliando su pensamiento a través de estas enseñanzas: porque la Verdad es mucho más interesante y más compleja de lo que podría haber imaginado en un principio. El mundo de Sofía no es sólo una novela de misterio, también es la primera novela hasta el momento que presenta una completa –y entretenida– historia de la filosofía desde sus inicios hasta nuestros días.

</details>

### 76. El niño con el pijama de rayas

**John Boyne** · *Drama*

Aunque el uso habitual de un texto como éste es describir las características de la obra, por una vez nos tomaremos la libertad de hacer una excepción a la norma establecida. No sólo porque el …

<details><summary>Sinopsis completa</summary>

Aunque el uso habitual de un texto como éste es describir las características de la obra, por una vez nos tomaremos la libertad de hacer una excepción a la norma establecida. No sólo porque el libro que tienes en tus manos es muy difícil de definir, sino porque estamos convencidos de que explicar su contenido estropearía la experiencia de la lectura. Creemos que es importante empezar esta novela sin saber de qué trata. No obstante, si decides embarcarte en la aventura, debes saber que acompañarás a Bruno, un niño de nueve años, cuando se muda con su familia a una casa junto a una cerca. Cercas como ésa existen en muchos sitios del mundo, sólo deseamos que no te encuentres nunca con una. Por último, cabe aclarar que este libro no es sólo para adultos; también lo pueden leer, y sería recomendable que lo hicieran, niños a partir de los trece años de edad.

</details>

### 77. El nombre de la rosa

**Umberto Eco** · *Histórico · Intriga · Policíaco*

Participando de características propias de la novela gótica, la crónica medieval, la novela policíaca, el relato ideológico en clave, y la alegoría narrativa, El nombre de la rosa ofrece distintos puntos de interés: primero, una …

<details><summary>Sinopsis completa</summary>

Participando de características propias de la novela gótica, la crónica medieval, la novela policíaca, el relato ideológico en clave, y la alegoría narrativa, El nombre de la rosa ofrece distintos puntos de interés: primero, una trama apasionante y constelada de golpes de efecto, que narra las actividades detectivescas de Guillermo de Baskerville para esclarecer los crímenes de una abadía benedictina; segundo, la reconstrucción portentosa de una época especialmente conflictiva, reconstrucción que no se para en lo exterior, sino que se centra en las formas de pensar y sentir del siglo XIV; y tercero, el modo en que Umberto Eco el teórico, Umberto Eco el ensayista, ha construido su primera novela, escrita —nos dice— por haber descubierto, en edad madura, «aquello» sobre lo cual no se puede teorizar, aquello que hay que narrar.

</details>

### 78. El nombre del viento

**Patrick Rothfuss** · *Aventuras · Fantástico* · Serie: La crónica del asesino de reyes, tomo 1

He robado princesas a reyes agónicos. Incendié la ciudad de Trebon. He pasado la noche con Felurian y he despertado vivo y cuerdo. Me expulsaron de la Universidad a una edad a la que a …

<details><summary>Sinopsis completa</summary>

He robado princesas a reyes agónicos. Incendié la ciudad de Trebon. He pasado la noche con Felurian y he despertado vivo y cuerdo. Me expulsaron de la Universidad a una edad a la que a la mayoría todavía no los dejan entrar. He recorrido de noche caminos de los que otros no se atreven a hablar ni siquiera de día. He hablado con dioses, he amado a mujeres y escrito canciones que hacen llorar a los bardos. "Me llamo Kvothe. Quizás hayas oído hablar de mi."

</details>

### 79. El perfume

**Patrick Süskind** · *Drama · Histórico · Terror*

Quizá los olores evoquen el privilegio de la invisibilidad. Antes del tacto, sucede el olor, como mensajero de una esencia que sabe desaparecer en el aire y ser agente de un gran poder. La seducción …

<details><summary>Sinopsis completa</summary>

Quizá los olores evoquen el privilegio de la invisibilidad. Antes del tacto, sucede el olor, como mensajero de una esencia que sabe desaparecer en el aire y ser agente de un gran poder. La seducción que despliega el olor es implacable: se instala en nosotros y sella su poderío en los tejidos de la memoria. Jean-Baptiste Grenouille tiene su marca de nacimiento: no despide ningún olor y por ello hace temer la presencia de algún demonio. Al mismo tiempo posee un don excepcional: un olfato prodigioso que le permite percibir todos los olores del mundo. Desde la miseria en que nace, abandonado al cuidado de unos monjes, Jean-Baptiste Grenouille lucha contra su condición y escala posiciones sociales convirtiéndose en un afamado perfumista. Crea perfumes capaces de hacerle pasar inadvertido o inspirar simpatía, amor, compasión... Para obtener estas fórmulas magistrales debe asesinar a jóvenes muchachas vírgenes, obtener sus fluidos corporales y licuar sus olores íntimos. Su arte se convierte en una suprema e inquietante prestidigitacion. Patrick Süskind, convertido en maestro del naturalismo irónico, nos transmite una visión ácida y desengañada del hombre en un libro repleto de sabiduría olfativa, imaginación y enorme amenidad. Su persuasión iguala la de su personaje y nos propone una inmersión literaria en el arco iris natural de los olores y en los turbadores abismos del espíritu humano.

</details>

### 80. El Pozo de la Ascensión. (Ed. revisada)

**Brandon Sanderson** · *Fantástico · Novela* · Serie: Nacidos de la bruma, tomo 2

Durante mil años, han caído las cenizas y nada florece. Durante mil años, los skaa han sido esclavizados y han vivido sumidos en un miedo inevitable. Durante mil años, el Lord Legislador ha reinado con …

<details><summary>Sinopsis completa</summary>

Durante mil años, han caído las cenizas y nada florece. Durante mil años, los skaa han sido esclavizados y han vivido sumidos en un miedo inevitable. Durante mil años, el Lord Legislador ha reinado con un poder absoluto gracias al terror y la divina invencibilidad que le otorga la poderosa magia de la alomancia. Pero vencer y matar al Lord Legislador fue la parte sencilla. El verdadero desafío será sobrevivir a las consecuencias de su caída. Tomar el poder tal vez resultó fácil, pero ¿qué ocurre después, cómo se usa? En ese mundo de aventura épica, la estrategia política y religiosa debe lidiar con los siempre misteriosos poderes de la alomancia.

</details>

### 81. El príncipe cruel

**Holly Black** · *Fantástico · Novela* · Serie: Los habitantes del aire, tomo 1

Jude tenía siete años cuando sus padres fueron asesinados y, junto con sus dos hermanas, fue trasladada a la traicionera Corte Suprema del Reino Feérico. Diez años más tarde, lo único que Jude desea, a …

<details><summary>Sinopsis completa</summary>

Jude tenía siete años cuando sus padres fueron asesinados y, junto con sus dos hermanas, fue trasladada a la traicionera Corte Suprema del Reino Feérico. Diez años más tarde, lo único que Jude desea, a pesar de ser una mera mortal, es sentir que pertenece a ese lugar. Pero muchos de los habitantes desprecian a los humanos. Especialmente el Príncipe Cardan, el hijo más joven y perverso del Alto Rey. Para hacerse un hueco en la Corte, Jude deberá enfrentarse a él. Y afrontar las consecuencias. Como resultado, se verá envuelta en las intrigas y engaños del palacio, ademas de descubrir su propia habilidad para el derramamiento de sangre. Al tiempo que la guerra civil amenaza con arrasar las Cortes Feéricas, Jude se verá obligada a poner en riesgo su propia vida con una peligrosa alianza para tratar de salvar a sus hermanas, y al propio reino.

</details>

### 82. El principito

**Antoine de Saint-Exupéry** · *Fantástico · Juvenil*

'El Principito' (en francés: 'Le Petit Prince'), publicado el 6 de abril de 1943, es el relato corto más conocido del escritor y aviador francés Antoine de Saint-Exupéry. Lo escribió mientras se hospedaba en un …

<details><summary>Sinopsis completa</summary>

'El Principito' (en francés: 'Le Petit Prince'), publicado el 6 de abril de 1943, es el relato corto más conocido del escritor y aviador francés Antoine de Saint-Exupéry. Lo escribió mientras se hospedaba en un hotel en Nueva York y fue publicado por primera vez en los Estados Unidos. Ha sido traducido a ciento ochenta lenguas y dialectos, convirtiéndose en una de las obras más reconocidas de la literatura universal. El principito habita un pequeñísimo asteroide, que comparte con una flor caprichosa y tres volcanes. Pero tiene «problemas» con la flor y empieza a experimentar la soledad; hasta que decide abandonar el planeta en busca de un amigo. Buscando esa amistad recorre varios planetas, habitados sucesivamente por un rey, un vanidoso, un borracho, un hombre de negocios, un farolero, un geógrafo… El concepto de «seriedad» que tienen estas «personas mayores» le deja perplejo y confuso. Prosiguiendo su búsqueda llega al planeta Tierra, pero en su enorme extensión siente más que nunca la soledad. Una serpiente le da su versión pesimista sobre los hombres y lo poco que se puede esperar de ellos. Tampoco el zorro contribuye a mejorar su opinión, pero en cambio le enseña el modo de hacerse amigos: hay que crear lazos, hay que dejarse «domesticar». Y al final le regala su secreto: «Sólo se ve bien con el corazón. Lo esencial es invisible a los ojos». De pronto, el principito se da cuenta de que su flor le ha «domesticado» y decide regresar a su planeta valiéndose de los medios expeditivos que le ofrece la serpiente. Y es entonces cuando entra en contacto con el aviador; también el hombre habrá encontrado un amigo…

</details>

### 83. El problema de los Tres Cuerpos

**Liu Cixin** · *Ciencia ficción · Novela* · Serie: Trilogía de los Tres Cuerpos, tomo 1

Este libro ofrece la posibilidad única de acercarse al fenómeno editorial chino que ha conquistado el mundo y ha ganado el premio Hugo 2015 a la mejor novela, siendo la primera vez que una obra …

<details><summary>Sinopsis completa</summary>

Este libro ofrece la posibilidad única de acercarse al fenómeno editorial chino que ha conquistado el mundo y ha ganado el premio Hugo 2015 a la mejor novela, siendo la primera vez que una obra no escrita originariamente en inglés merece tal reconocimiento. Su autor, Cixin Liu, es el escritor de ciencia ficción más relevante en China, capaz de vender más de un millón de ejemplares en su país y convencer a prescriptores de la talla de Barack Obama, quien seleccionó El problema de los Tres Cuerpos como una de sus lecturas navideñas de 2015, y Mark Zuckerberg, que lo convirtió en la primera novela de su club de lectura. Ahora el público y la crítica de los cinco continentes se rinden a esta obra maestra, enormemente visionaria, sobre el papel de la ciencia en nuestras sociedades, que nos ayuda a comprender el pasado y el futuro de China, pero también, leída en clave geopolítica, del mundo en que vivimos.

</details>

### 84. El psicoanalista

**John Katzenbach** · *Intriga* · Serie: El psicoanalista, tomo 1

-Feliz 53 cumpleaños, doctor. Bienvenido al primer día de su muerte. Pertenezco a algún momento de su pasado. Usted arruinó mi vida. Quizá no sepa cómo por qué o cuándo, pero lo hizo. Llenó todos …

<details><summary>Sinopsis completa</summary>

-Feliz 53 cumpleaños, doctor. Bienvenido al primer día de su muerte. Pertenezco a algún momento de su pasado. Usted arruinó mi vida. Quizá no sepa cómo por qué o cuándo, pero lo hizo. Llenó todos mis instantes de desastre y tristeza. Arruinó mi vida. Y ahora estoy decidido a arruinar la suya. Así comienza el anónimo que recibe Fredrerick Starks, psicoanalista con una larga experiencia y una tranquila vida cotidiana. Starks tendrá que emplear toda su astucia y rapidez para, en quince días, averiguar quién es el autor de esa amenazadora misiva que promete hacerle la existencia imposible.

</details>

### 85. El resplandor

**Stephen King** · *Terror* · Serie: El resplandor, tomo 1

Éste es uno de los relatos más celebres del gran maestro del terror Stephen King. Luego que otro gran maestro, Stanley Kubrick, llevara una adaptación de esta obra al cine, millones de copias de este …

<details><summary>Sinopsis completa</summary>

Éste es uno de los relatos más celebres del gran maestro del terror Stephen King. Luego que otro gran maestro, Stanley Kubrick, llevara una adaptación de esta obra al cine, millones de copias de este libro se han vendido en todo el mundo. El Resplandor es la tercera novela publicada por King y ésta marca su carrera dentro de género que le dará la fama. Jack es un hombre abrumado por un pasado que va más allá de lo que él puede recordar y, no estamos hablando de sólo un problema de alcohol. Luego de aceptar un trabajo que supondrá un cambio en su vida, la sombra de su pasado se cernirá sobre sus seres más queridos: Su esposa y su hijo Danny de 5 años, quien puede presentir el mal rumbo que tomaran las cosas cuando su padre decida vivir aislados del mundo en un hotel que es un universo en sí mismo... pero un universo perverso.

</details>

### 86. El secreto de la asistenta

**Freida McFadden** · *Intriga · Novela · Psicológico* · Serie: La asistenta, tomo 2

Es todo una cuestión de hasta dónde estoy dispuesta a llegar… Es difícil encontrar a alguien que te ofrezca trabajo sin preguntar demasiado sobre tu pasado. Así que le agradezco al universo que, milagrosamente, los …

<details><summary>Sinopsis completa</summary>

Es todo una cuestión de hasta dónde estoy dispuesta a llegar… Es difícil encontrar a alguien que te ofrezca trabajo sin preguntar demasiado sobre tu pasado. Así que le agradezco al universo que, milagrosamente, los Garrick me hayan dado empleo limpiando su impresionante ático con vistas a todo Manhattan y preparándoles comidas sofisticadas en su inmensa cocina. Puedo trabajar aquí durante un tiempo, ser discreta hasta conseguir lo que quiero. Es casi perfecto. Sin embargo, todavía no he conocido a la señora Garrick ni he podido ver lo que hay dentro de la habitación de invitados. Estoy segura de que la oigo llorar. Veo las pequeñas manchas de sangre en el cuello de sus camisones blancos cuando hago la colada. Y, un día, no puedo evitar llamar a su puerta. Cuando esta se abre lentamente, lo que veo lo cambia todo… Es entonces cuando hago una promesa. Douglas Garrick se ha equivocado. Y va a pagar.

</details>

### 87. El silencio de la ciudad blanca

**Eva García Sáenz** · *Novela · Policíaco* · Serie: Trilogía de la Ciudad Blanca, tomo 1

Tasio Ortiz de Zárate, el brillante arqueólogo condenado por los extraños asesinatos que aterrorizaron la tranquila ciudad de Vitoria hace dos décadas, está a punto de salir de prisión en su primer permiso cuando los …

<details><summary>Sinopsis completa</summary>

Tasio Ortiz de Zárate, el brillante arqueólogo condenado por los extraños asesinatos que aterrorizaron la tranquila ciudad de Vitoria hace dos décadas, está a punto de salir de prisión en su primer permiso cuando los crímenes se reanudan de nuevo: en la emblemática Catedral Vieja de Vitoria, una pareja de veinte años aparece desnuda y muerta por picaduras de abeja en la garganta. Poco después, otra pareja de veinticinco años es asesinada en la Casa del Cordón, un conocido edificio medieval. El joven inspector Unai López de Ayala ―alias Kraken―, experto en perfiles criminales, está obsesionado con prevenir los crímenes antes de que ocurran, una tragedia personal aún fresca no le permite encarar el caso como uno más. Sus métodos poco ortodoxos enervan a su jefa, Alba, la subcomisaria con la que mantiene una ambigua relación marcada por los crímenes… El tiempo corre en su contra y la amenaza acecha en cualquier rincón de la ciudad. ¿Quién será el siguiente? Una novela negra absorbente que se mueve entre la mitología y las leyendas de Álava, la arqueología, los secretos de familia y la psicología criminal. Un noir elegante y complejo que demuestra cómo los errores del pasado pueden influir en el presente.

</details>

### 88. El temor de un hombre sabio

**Patrick Rothfuss** · *Aventuras · Fantástico* · Serie: La crónica del asesino de reyes, tomo 2

Músico, mendigo, ladrón, estudiante, mago, héroe y asesino. Kvothe es un personaje legendario, el héroe o el villano de miles de historias que circulan entre la gente. Todos le dan por muerto, cuando en realidad …

<details><summary>Sinopsis completa</summary>

Músico, mendigo, ladrón, estudiante, mago, héroe y asesino. Kvothe es un personaje legendario, el héroe o el villano de miles de historias que circulan entre la gente. Todos le dan por muerto, cuando en realidad se ha ocultado con un nombre falso en una aldea perdida. Allí simplemente es el taciturno dueño de Roca de Guía, una posada en el camino. Hasta que hace un día un viajero llamado Cronista le reconoció y le suplicó que le revelase su historia, la auténtica, la que deshacía leyendas y rompía mitos, la que mostraba una verdad que sólo Kvothe conocía. A lo que finalmente Kvothe accedió, con una condición: había mucho que contar, y le llevaría tres días. Es la mañana del segundo día, y tres hombres se sientan a una mesa de Roca de Guía: un posadero de cabello rojo como una llama, su pupilo Bast y Cronista, que moja la pluma en el tintero y se prepara a transcribir... El temor de un hombre sabio empieza donde terminaba El nombre del viento: en la Universidad. De la que luego Kvothe se verá obligado a partir en pos del nombre del viento, en pos de la aventura, en pos de esas historias que aparecen en libros o se cuentan junto a una hoguera del camino o en una taberna, en pos de la antigua orden de los caballeros Amyr y, sobre todo, en pos de los Chandrian. Su viaje le lleva a la corte plagada de intrigas del maer Alveron en el reino de Vintas, al bosque de Eld en persecución de unos bandidos, a las colinas azotadas por las tormentas que rodean la ciudad de Ademre, a los confines crepusculares del reino de los Fata. Y cada vez parece que tiene algo más cerca la solución del misterio de los Chandrian, y su venganza.

</details>

### 89. El túnel

**Ernesto Sábato** · *Drama · Intriga · Otros* · Serie: Trilogía de Sábato, tomo 1

El túnel es una de las grandes novelas sudamericanas de este siglo, cuyos ecos recogieron pronto en Europa Graham Greene y Camus. El relato, montado en los recursos de la novela policial, desarrolla un personaje …

<details><summary>Sinopsis completa</summary>

El túnel es una de las grandes novelas sudamericanas de este siglo, cuyos ecos recogieron pronto en Europa Graham Greene y Camus. El relato, montado en los recursos de la novela policial, desarrolla un personaje que revela su psicología introspectiva e impone al lector un análisis de la desesperanza. El protagonista, Juan Pablo Castel, persigue inútilmente lo inalcanzable, que no es sino el regreso a la infancia, simbolizada en la ventana de un cuadro, motivo reiterado largamente en la narración.

</details>

### 90. El último deseo

**Andrzej Sapkowski** · *Fantástico* · Serie: Geralt de Rivia, tomo 1

Geralt de Rivia, brujo y mutante sobrehumano, se gana la vida como cazador de monstruos en una tierra de magia y maravilla: con sus dos espadas al hombro -la de acero para hombres, y la …

<details><summary>Sinopsis completa</summary>

Geralt de Rivia, brujo y mutante sobrehumano, se gana la vida como cazador de monstruos en una tierra de magia y maravilla: con sus dos espadas al hombro -la de acero para hombres, y la de plata para bestias- da cuenta de estriges, manticoras, grifos, vampiros, quimeras y lobisomes, pero sólo cuando amenazan la paz. Irónico, cínico, descreído y siempre errante, sus pasos le llevan de pueblo en pueblo ofreciendo sus servicios, hallando las más de las veces que los auténticos monstruos se esconden bajo rostros humanos. En su camino sorteará intrigas, elegirá el mal menor, debatirá cuestiones de precio, hollará el confín del mundo y realizará su último deseo: así comienzan las aventuras del brujo Geralt de Rivia.

</details>

### 91. El visitante

**Stephen King** · *Novela · Terror*

Un niño de once años ha sido brutalmente violado y asesinado. Todas las pruebas apuntan a uno de los ciudadanos más queridos de Flint City: Terry Maitland, entrenador en la liga infantil, profesor de literatura, …

<details><summary>Sinopsis completa</summary>

Un niño de once años ha sido brutalmente violado y asesinado. Todas las pruebas apuntan a uno de los ciudadanos más queridos de Flint City: Terry Maitland, entrenador en la liga infantil, profesor de literatura, marido ejemplar y padre de dos niñas. El detective Ralph Anderson ordena su detención. Maitland tiene una coartada firme que demuestra que estuvo en otra ciudad cuando se cometió el crimen, pero las pruebas de ADN encontradas en el lugar de los hechos confirman que es culpable. Ante la justicia y la opinión pública Terry Maitland es un asesino y el caso está resuelto. Pero el detective Anderson no está satisfecho. Maitland parece un buen tipo, un ciudadano ejemplar, ¿acaso tiene dos caras? Y ¿cómo es posible que estuviera en dos sitios a la vez?

</details>

### 92. Elantris. Edición X Aniversario y definitiva del autor

**Brandon Sanderson** · *Fantástico · Novela*

Brandon Sanderson debutó en 2006 ante los lectores en castellano con Elantris , una novela de fantasía épica que marcó un auténtico hito. Cuando se cumple el décimo aniversario de su publicación, se relanza en …

<details><summary>Sinopsis completa</summary>

Brandon Sanderson debutó en 2006 ante los lectores en castellano con Elantris , una novela de fantasía épica que marcó un auténtico hito. Cuando se cumple el décimo aniversario de su publicación, se relanza en esta edición especial, que permite rememorar y descubrir los inicios de un autor que, desde entonces, ha cosechado ocho millones de seguidores en todo el mundo, confirmando su condición de heredero al trono de todo un género. Esta nueva versión, convertida en la edición definitiva del autor, empieza con un prefacio de Dan Wells, la primera persona que leyó el manuscrito completo, y un nuevo prólogo de Miquel Barceló, su primer editor en castellano. Lo cierra un epílogo en que el propio Sanderson nos cuenta por qué escribió esta novela y su importancia en el Cosmere, el fascinante universo que comparte la mayoría de sus obras. Se incluye también una versión ampliada del apéndice «Ars Arcanum», con más detalles técnicos sobre la magia de un libro mítico para su legión de lectores. Bienvenidos a la ciudad de Elantris, la poderosa y bella capital de Arelon llamada la «ciudad de los dioses». Antaño famosa sede de inmortales, lugar repleto de poderosa magia, Elantris ha caído en desgracia. Ahora solo acoge a los nuevos «muertos en vida», postrados en una insufrible «no-vida» tras una misteriosa y terrible transformación. Un matrimonio de Estado destinado a unir los reinos de Arelon y Teod se frustra, ya que el novio, Raoden, el príncipe de Arelon, sufre inesperadamente la Transformación y se convierte en un «muerto en vida» obligado a refugiarse en Elantris. Su reciente esposa, la princesa Sarene de Teod, creyéndolo muerto, se ve obligada a incorporarse a la vida de Arelon y su nueva capital, Kae. Mientras, el embajador y alto sacerdote de otro reino vecino, Fjordell, usará su habilidad política para intentar dominar Arelod y Teod con el propósito de somerterlos a su emperador y su dios.

</details>

### 93. Eleanor & Park

**Rainbow Rowell** · *Juvenil · Novela · Romántico*

Una historia de amor entre dos outsiders lo bastante inteligentes como para saber que el primer amor nunca es para siempre, pero lo suficientemente valientes y desesperados como para intentarlo. «—Bono conoció a la que …

<details><summary>Sinopsis completa</summary>

Una historia de amor entre dos outsiders lo bastante inteligentes como para saber que el primer amor nunca es para siempre, pero lo suficientemente valientes y desesperados como para intentarlo. «—Bono conoció a la que sería su mujer en el instituto —dijo Park. —Sí, y también Jerry Lee Lewis —contestó Eleanor. —No estoy bromeando. —Pues deberías. Tenemos 16 años —dijo Eleanor. —¿Y qué pasa con Romeo y Julieta? —Superficiales, confundidos y, posteriormente, muertos. —Te quiero, y no estoy bromeando —le dijo Park. —Pues deberías».

</details>

### 94. En llamas

**Suzanne Collins** · *Ciencia ficción · Juvenil* · Serie: Distritos, tomo 2

Contra todo pronóstico, Katniss ha ganado Los Juegos del Hambre. Es un milagro que ella y su compañero del Distrito 12, Peeta Mellark, sigan vivos. Katniss debería sentirse aliviada, incluso contenta, ya que, al fin …

<details><summary>Sinopsis completa</summary>

Contra todo pronóstico, Katniss ha ganado Los Juegos del Hambre. Es un milagro que ella y su compañero del Distrito 12, Peeta Mellark, sigan vivos. Katniss debería sentirse aliviada, incluso contenta, ya que, al fin y al cabo, ha regresado con su familia y su amigo de toda la vida, Gale. Sin embargo, nada es como a ella le gustaría. Gale guarda las distancias y Peeta le ha dado la espalda por completo. Además se rumorea que existe una rebelión contra el Capitolio…

</details>

### 95. Ensayo sobre la ceguera

**José Saramago** · *Ensayo · Otros*

Un hombre parado ante un semáforo en rojo se queda ciego súbitamente. Es el primer caso de una «ceguera blanca» que se expande de manera fulminante. Internados en cuarentena o perdidos en la ciudad, los …

<details><summary>Sinopsis completa</summary>

Un hombre parado ante un semáforo en rojo se queda ciego súbitamente. Es el primer caso de una «ceguera blanca» que se expande de manera fulminante. Internados en cuarentena o perdidos en la ciudad, los ciegos tendrán que enfrentarse con lo que existe de más primitivo en la naturaleza humana: la voluntad de sobrevivir a cualquier precio. Ensayo sobre la ceguera es la ficción de un autor que nos alerta sobre «la responsabilidad de tener ojos cuando otros los perdieron». José Saramago traza en este libro una imagen aterradora y conmovedora de los tiempos que estamos viviendo. En un mundo así, ¿cabrá alguna esperanza? El lector conocerá una experiencia imaginativa única. En un punto donde se cruzan literatura y sabiduría, José Saramago nos obliga a parar, cerrar los ojos y ver. Recuperar la lucidez y rescatar el afecto son dos propuestas fundamentales de una novela que es, también, una reflexión sobre la ética del amor y la solidaridad.

</details>

### 96. Entrevista con el vampiro

**Anne Rice** · *Fantástico · Terror* · Serie: Crónicas Vampíricas, tomo 1

Entrevista con el vampiro es el primer titulo de la famosa e inquietante serie de Cronicas Vampiricas. En esta novela, Anne Rice narra la conversion de un joven de Nueva Orleans en eterno habitante de …

<details><summary>Sinopsis completa</summary>

Entrevista con el vampiro es el primer titulo de la famosa e inquietante serie de Cronicas Vampiricas. En esta novela, Anne Rice narra la conversion de un joven de Nueva Orleans en eterno habitante de la noche. El protagonista, llevado por el sentimiento de culpabilidad que le ha causado la muerte de su hermano menor, anhela transformarse en un ser maldito. Sin embargo, ya desde el inicio de su vida sobrenatural, se siente invadido por los sentimientos mas humanos, una pasión no exenta de dependencia sexual y psicológica.

</details>

### 97. Escuadrón

**Brandon Sanderson** · *Ciencia ficción · Novela* · Serie: Escuadrón, tomo 1

El mundo de Spensa lleva décadas bajo un ataque continuo. Los pilotos son los héroes de lo que queda de la raza humana, y pilotar un caza siempre ha sido el sueño de Spensa. Desde …

<details><summary>Sinopsis completa</summary>

El mundo de Spensa lleva décadas bajo un ataque continuo. Los pilotos son los héroes de lo que queda de la raza humana, y pilotar un caza siempre ha sido el sueño de Spensa. Desde niña se ha imaginado elevándose hacia el cielo y demostrando su valentía. Pero su destino está entremezclado con el de su padre, un piloto al que derribaron, anulando así cualquier posibilidad de que Spensa accediera a la escuela de vuelo. Nadie dejará que Spensa olvide lo que hizo su padre; sin embargo, el destino funciona de formas misteriosas. Tal vez la escuela de vuelo esté casi fuera de su alcance, pero ella está decidida a volar. Y un descubrimiento casual en una caverna perdida podría proporcionarle un modo de reclamar las estrellas.

</details>

### 98. Fahrenheit 451

**Ray Bradbury** · *Ciencia ficción · Otros*

Fahrenheit 451: la temperatura a la que el papel se enciende y arde. Guy Montag es un bombero y el trabajo de un bombero es quemar libros, que están prohibidos porque son causa de discordia …

<details><summary>Sinopsis completa</summary>

Fahrenheit 451: la temperatura a la que el papel se enciende y arde. Guy Montag es un bombero y el trabajo de un bombero es quemar libros, que están prohibidos porque son causa de discordia y sufrimiento. El Sabueso Mecánico del Departamento de Incendios, armado con una letal inyección hipodérmica, escoltado por helicópteros, está preparado para rastrear a los disidentes que aún conservan y leen libros. Como 1984, de George Orwell, como Un mundo feliz, de Aldous Huxley, Fahrenheit 451 describe una civilización occidental esclavizada por los medios, los tranquilizantes y el conformismo. La visión de Bradbury es asombrosamente profética: pantallas de televisión que ocupan paredes y exhiben folletines interactivos; avenidas donde los coches corren a 150 kilómetros por hora persiguiendo a peatones; una población que no escucha otra cosa que una insípida corriente de música y noticias transmitidas por unos diminutos auriculares insertados en las orejas.

</details>

### 99. Flores para Algernon

**Daniel Keyes** · *Ciencia ficción · Otros*

Este relato le proporcionó al autor varios premios Hugo y Nebula. Fue llevado a la televisión y posteriormente al cine, con el título Charly. Charlie Gordon es un chico con discapacidad mental, una buena persona …

<details><summary>Sinopsis completa</summary>

Este relato le proporcionó al autor varios premios Hugo y Nebula. Fue llevado a la televisión y posteriormente al cine, con el título Charly. Charlie Gordon es un chico con discapacidad mental, una buena persona que siente respeto por quienes le rodean. Charlie es escogido para una operación quirúrgica experimental, a la que también es sometido el ratón Algernon. A partir de entonces su inteligencia se irá ampliando, su visión del mundo se irá convirtiendo en algo más real y más decepcionante...., hasta llegar a la cúspide, donde se encuentra solo y adquiere la certeza de su terrible futuro.

</details>

### 100. Frankenstein

**Mary Shelley** · *Clásico · Terror*

Año: 1818 Sinopsis: La noche del 16 de junio de 1816, después de que Lord Byron y Percy B. Shelley discutieran largamente sobre la posibilidad de descubrir el principuo vital de la naturaleza y transferirlo …

<details><summary>Sinopsis completa</summary>

Año: 1818 Sinopsis: La noche del 16 de junio de 1816, después de que Lord Byron y Percy B. Shelley discutieran largamente sobre la posibilidad de descubrir el principuo vital de la naturaleza y transferirlo a un cuerpo inerte, Mary W. Shelley tuvo una memorable pesadilla sobre la visión de un monstruo creado por la ciencia humana. Éste sería el punto de partida de una de las obras más proféticas de la historia de la literatura: Frankenstein o el moderno Prometeo. Un drama romántico sobre la voluntad prometeica del ser humano, decidida a emular y planteando nuevos problemas morales de consecuencias desconocidas. Los recientes avances de la ciencias biológicas, en esta época de clones y transgénicos, nos invitan a recorrer, convirtiendo su obra en un clásico tan vivo y actual como hace casi 200 años.

</details>

### 101. Hábitos atómicos

**James Clear** · *Autoayuda · Ensayo*

Hábitos atómicos parte de una simple pero poderosa pregunta: ¿Cómo podemos vivir mejor? Sabemos que unos buenos hábitos nos permiten mejorar significativamente nuestra vida, pero con frecuencia nos desviamos del camino: dejamos de hacer ejercicio, …

<details><summary>Sinopsis completa</summary>

Hábitos atómicos parte de una simple pero poderosa pregunta: ¿Cómo podemos vivir mejor? Sabemos que unos buenos hábitos nos permiten mejorar significativamente nuestra vida, pero con frecuencia nos desviamos del camino: dejamos de hacer ejercicio, comemos mal, dormimos poco, despilfarramos. ¿Por qué es tan fácil caer en los malos hábitos y tan complicado seguir los buenos? James Clear nos brinda fantásticas ideas basadas en investigaciones científicas, que le permiten revelarnos cómo podemos transformar pequeños hábitos cotidianos para cambiar nuestra vida y mejorarla. Esta guía pone al descubierto las fuerzas ocultas que moldean nuestro comportamiento —desde nuestra mentalidad, pasando por el ambiente y hasta la genética— y nos demuestra cómo aplicar cada cambio a nuestra vida y a nuestro trabajo. Después de leer este libro, tendrás un método sencillo para desarrollar un sistema eficaz que te conducirá al éxito. Aprende cómo… 1. Darte tiempo para desarrollar nuevos hábitos. 2. Superar la falta de motivación y de fuerza de voluntad. 3. Diseñar un ambiente para que el éxito sea fácil de alcanzar. 4. Regresar al buen camino cuando te hayas desviado un poco.

</details>

### 102. Harry Potter y la cámara secreta

**J. K. Rowling** · *Aventuras · Fantástico · Infantil y juvenil · Intriga* · Serie: Harry Potter, tomo 2

Tras derrotar una vez más a lord Voldemort, su siniestro enemigo en Harry Potter y la piedra filosofal, Harry espera impaciente en casa de sus insoportables tíos el inicio del segundo curso del Colegio Hogwarts …

<details><summary>Sinopsis completa</summary>

Tras derrotar una vez más a lord Voldemort, su siniestro enemigo en Harry Potter y la piedra filosofal, Harry espera impaciente en casa de sus insoportables tíos el inicio del segundo curso del Colegio Hogwarts de Magia y hechicería. Sin embargo, la espera dura poco, pues un elfo aparece en su habitación y le advierte que una amenaza mortal se cierne sobre la escuela. Así pues, Harry no se lo piensa dos veces y, acompañado de Ron, su mejor amigo, se dirige a Hogwarts en un coche volador. Pero ¿puede un aprendiz de mago defender la escuela de los malvados que pretenden destruirla? Sin saber que alguien ha abierto la Cámara de los Secretos, dejando escapar una serie de monstruos peligrosos, Harry y sus amigos Ron y Hermione tendrán que enfrentarse con arañas gigantes, serpientes encantadas, fantasmas enfurecidos y, sobre todo, con la mismísima reencarnación de su más temible adversario.

</details>

### 103. Harry Potter y la orden del fénix

**J. K. Rowling** · *Aventuras · Fantástico · Infantil y juvenil · Intriga* · Serie: Harry Potter, tomo 5

Las tediosas vacaciones de verano en casa de sus tíos todavía no han acabado y Harry se encuentra más inquieto que nunca. Apenas ha tenido noticias de Ron y Hermione, y presiente que algo extraño …

<details><summary>Sinopsis completa</summary>

Las tediosas vacaciones de verano en casa de sus tíos todavía no han acabado y Harry se encuentra más inquieto que nunca. Apenas ha tenido noticias de Ron y Hermione, y presiente que algo extraño está sucediendo en Hogwarts. En efecto, cuando por fin comienza otro curso en el famoso colegio de magia y hechicería, sus temores se vuelven realidad. El Ministerio de Magia niega que Voldemort haya regresado y ha iniciado una campaña de desprestigio contra Harry y Dumbledore, para lo cual ha asignado a la horrible profesora Dolores Umbridge la tarea de vigilar todos sus movimientos. Así pues, además de sentirse solo e incomprendido, Harry sospecha que Voldemort puede adivinar sus pensamientos, e intuye que el temible mago trata de apoderarse de un objeto secreto que le permitiría recuperar su poder destructivo.

</details>

### 104. Harry Potter y la piedra filosofal

**J. K. Rowling** · *Aventuras · Fantástico · Infantil y juvenil · Intriga* · Serie: Harry Potter, tomo 1

Harry Potter se ha quedado huérfano y vive en casa de sus abominables tíos y del insoportable primo Dudley. Harry se siente muy triste y solo, hasta que un buen día recibe una carta que …

<details><summary>Sinopsis completa</summary>

Harry Potter se ha quedado huérfano y vive en casa de sus abominables tíos y del insoportable primo Dudley. Harry se siente muy triste y solo, hasta que un buen día recibe una carta que cambiará su vida para siempre. En ella le comunican que ha sido aceptado como alumno en el colegio interno Hogwarts de magia y hechicería. A partir de ese momento, la suerte de Harry da un vuelco espectacular. En esa escuela tan especial aprenderá encantamientos, trucos fabulosos y tácticas de defensa contra las malas artes. Se convertirá en el campeón escolar de quidditch, especie de fútbol aéreo que se juega montado sobre escobas, y se hará un puñado de buenos amigos... aunque también algunos temibles enemigos. Pero sobre todo, conocerá los secretos que le permitirán cumplir con su destino. Pues, aunque no lo parezca a primera vista, Harry no es un chico común y corriente. ¡Es un mago!

</details>

### 105. Harry Potter. La colección completa

**J. K. Rowling** · *Aventuras · Fantástico · Infantil y juvenil · Intriga · Recopilación* · Serie: Harry Potter, tomo 0

Harry Potter es una heptalogía de novelas fantásticas escrita por la autora británica J. K. Rowling, en la que se describen las aventuras del joven aprendiz de mago Harry Potter y sus amigos Hermione Granger …

<details><summary>Sinopsis completa</summary>

Harry Potter es una heptalogía de novelas fantásticas escrita por la autora británica J. K. Rowling, en la que se describen las aventuras del joven aprendiz de mago Harry Potter y sus amigos Hermione Granger y Ron Weasley, durante los siete años que pasan en el Colegio Hogwarts de Magia y Hechicería. El argumento se centra en la lucha entre Harry Potter y el malvado mago Lord Voldemort, quien mató a los padres de Harry en su afán de conquistar el mundo mágico. Desde el lanzamiento de la primera novela, Harry Potter y la piedra filosofal en 1997, la serie logró una inmensa popularidad, críticas favorables y éxito comercial alrededor del mundo. Para diciembre de 2007, se habían vendido más de 400 millones de copias de los siete libros, los cuales han sido traducidos a más de 65 idiomas, entre los que se incluyen el latín y el griego antiguo. El séptimo y último libro, Harry Potter y las Reliquias de la Muerte fue lanzado mundialmente en inglés el 21 de julio de 2007, mientras que en español se publicó el 21 de febrero de 2008.

</details>

### 106. Hush, Hush

**Becca Fitzpatrick** · *Fantástico · Infantil y juvenil · Romántico* · Serie: Hush, Hush, tomo 1

Un juramento sagrado, un ángel caído, un amor prohibido. Nora Grey es responsable y lista y nada inclinada a la temeridad. Su primer error fue enamorarse de Patch. Patch tiene un pasado que podría llamarse …

<details><summary>Sinopsis completa</summary>

Un juramento sagrado, un ángel caído, un amor prohibido. Nora Grey es responsable y lista y nada inclinada a la temeridad. Su primer error fue enamorarse de Patch. Patch tiene un pasado que podría llamarse cualquier cosa excepto inofensivo. Lo mejor que hizo nunca fue enamorarse de Nora. Después de ser emparejada con Patch en biología, todo lo que Nora quiere hacer es permanecer lejos de él, pero él siempre parece estar dos pasos por delante de ella. Puede sentir sus ojos sobre ella incluso cuando no está cerca. Lo siente cerca incluso cuando está sola en su habitación. Y cuando su atracción ya no puede ser negada, conoce el secreto de lo que es Patch y de lo que lo llevó hasta ella. A pesar de todas las preguntas que tiene sobre su pasado, tal vez haya una única pregunta que puedan hacerse: ¿hasta dónde estás dispuesto a caer?

</details>

### 107. Indigno de ser humano

**Osamu Dazai** · *Drama · Novela · Psicológico*

«Por lo general, las personas no muestran lo terribles que son. Pero son como una vaca pastando tranquila que, de repente, levanta la cola y descarga un latigazo sobre el tábano. Basta que se dé …

<details><summary>Sinopsis completa</summary>

«Por lo general, las personas no muestran lo terribles que son. Pero son como una vaca pastando tranquila que, de repente, levanta la cola y descarga un latigazo sobre el tábano. Basta que se dé la ocasión para que muestren su horrenda naturaleza. Recuerdo que se me llegaba a erizar el cabello de terror al pensar en que este carácter innato es una condición esencial para que el ser humano sobreviva. Al pensarlo, perdía cualquier esperanza sobre la humanidad». Publicada por primera vez en 1948, Indigno de ser humano es una de las novelas más célebres de la literatura japonesa contemporánea. Su polémico y brillante autor, Osamu Dazai, incorporó numerosos episodios de su turbulenta vida a los tres cuadernos que conforman esta novela y que narran, en primera persona y de forma descarnada, el progresivo declive como ser humano de Yozo, joven estudiante de provincias que lleva una vida disoluta en Tokio. Repudiado por su familia tras un intento de suicidio e incapaz de vivir en armonía con sus hipócritas semejantes, Yozo malvive como dibujante de historietas y subsiste gracias a la ayuda de mujeres que se enamoran de él pese a su alcoholismo y adicción a la morfina. Sin embargo, tras el despiadado retrato que Yozo hace de su vida, Dazai cambia repentinamente de punto de vista y nos muestra, mediante la voz de una de las mujeres con las que Yozo convivió, una semblanza muy distinta del trágico protagonista de esta perturbadora historia. Indigno de ser humano se ha convertido, con el paso de los años, en una de las obras más populares de la literatura japonesa, superando los diez millones de ejemplares vendidos desde su primera publicación en 1948.

</details>

### 108. It

**Stephen King** · *Terror*

¿Quién o qué mutila y mata a los niños de un pequeño pueblo norteamericano? ¿Por qué llega cíclicamente el horror a Derry en forma de un payaso siniestro que va sembrando la destrucción a su …

<details><summary>Sinopsis completa</summary>

¿Quién o qué mutila y mata a los niños de un pequeño pueblo norteamericano? ¿Por qué llega cíclicamente el horror a Derry en forma de un payaso siniestro que va sembrando la destrucción a su paso? Esto es lo que se proponen averiguar los protagonistas de esta novela. Tras veintisiete años de tranquilidad y lejanía una antigua promesa infantil les hace volver al lugar en el que vivieron su infancia y juventud como una terrible pesadilla. Regresan a Derry para enfrentarse con su pasado y enterrar definitivamente la amenaza que los amargó durante su niñez. Saben que pueden morir, pero son conscientes de que no conocerán la paz hasta que aquella cosa sea destruida para siempre. It es una de las novelas más ambiciosas de Stephen King, donde ha logrado perfeccionar de un modo muy personal las claves del género de terror.

</details>

### 109. Jerusalén

**J. J. Benítez** · *Aventuras · Ciencia ficción · Histórico* · Serie: Caballo de Troya, tomo 1

Un investigador español (Juán José Benítez) es contactado por un individuo autodenominado "el mayor", quien resulta ser un antiguo integrante de la USAF. Tras la muerte de tan misterioso personaje, Juan José Benítez es conducido …

<details><summary>Sinopsis completa</summary>

Un investigador español (Juán José Benítez) es contactado por un individuo autodenominado "el mayor", quien resulta ser un antiguo integrante de la USAF. Tras la muerte de tan misterioso personaje, Juan José Benítez es conducido a través de acertijos a un manuscrito, que resulta ser el testimonio del mayor como partícipe de un proyecto ultrasecreto denominado "Caballo de Troya". El proyecto consiste en la creación y puesta en marcha de una máquina del tiempo, destinada a viajar a los momentos de pasión y muerte de Jesús de Nazaret. El manuscrito describe someramente los detalles técnicos involucrados en tal empresa, pero sobre todo, las andanzas de los viajeros del tiempo al lado del maestro de Galilea. Describe al Hijo del Hombre como un individuo jovial y alegre, alejado de la ortodoxia tradicional, gustoso de ofrecer sus profundas enseñanzas espirituales a quien así lo desee. El mayor, conocido como "Jason" por los habitantes de la época, junto con su compañero nombrado "Eliseo", van dejando atrás su inicial escepticismo, convirtiéndose poco a poco al mensaje espiritual y religioso que Jesús va predicando.

</details>

### 110. Juego de tronos

**George R. R. Martin** · *Aventuras · Bélico · Fantástico* · Serie: Canción de hielo y fuego, tomo 1

Tras el largo verano, el invierno se acerca a los Siete Reinos. Lord Eddars Stark, señor de Invernalia, deja sus dominios para unirse a la corte del rey Robert Baratheon el Usurpador, hombre díscolo y …

<details><summary>Sinopsis completa</summary>

Tras el largo verano, el invierno se acerca a los Siete Reinos. Lord Eddars Stark, señor de Invernalia, deja sus dominios para unirse a la corte del rey Robert Baratheon el Usurpador, hombre díscolo y otrora guerrero audaz cuyas mayores aficiones son comer, beber y engendrar bastardos. Eddard Stark desempeñará el cargo de Mano del Rey e intentará desentrañar una maraña de intrigas que pondrá en peligro su vida... y la de los suyos. En un mundo cuyas estaciones duran décadas y en el que retazos de una magia inmemorial y olvidada surgen en los rincones más sombrios y maravillosos, la traición y la lealtad, la compasión y la sed de venganza, el amor y el poder hacen del juego de tronos una poderosa trampa que atrapa en sus fauces a los personajes... y al lector.

</details>

### 111. Jumper

**Steven Gould** · *Ficción · Infantil y juvenil* · Serie: Jumper, tomo 1

Imagina que pudieras ir a cualquier lugar del mundo con sólo cerrar los ojos. ¿Adónde irías? ¿Qué harías allí? David Rice es un “jumper”, un saltador, capaz de teletransportarse a sí mismo a cualquier lugar …

<details><summary>Sinopsis completa</summary>

Imagina que pudieras ir a cualquier lugar del mundo con sólo cerrar los ojos. ¿Adónde irías? ¿Qué harías allí? David Rice es un “jumper”, un saltador, capaz de teletransportarse a sí mismo a cualquier lugar del mundo. Puede ir a donde quiera, cuando quiera. Puede vivir una vida que otros sólo sueñan. Realizar todas sus fantasías. Sin fronteras, sin límites. Pero pronto descubre que usar sus poderes en un mundo que no está preparado para ellos sólo trae complicaciones. Algunas, incluso extremadamente peligrosas.

</details>

### 112. La asistenta

**Freida McFadden** · *Intriga · Novela · Psicológico* · Serie: La asistenta, tomo 1

Detrás de la puerta, ella lo ve todo . Todos los días friego la preciosa casa de los Winchester de arriba abajo. Recojo a su hija del colegio y preparo deliciosas comidas para toda la …

<details><summary>Sinopsis completa</summary>

Detrás de la puerta, ella lo ve todo . Todos los días friego la preciosa casa de los Winchester de arriba abajo. Recojo a su hija del colegio y preparo deliciosas comidas para toda la familia antes de subir a cenar sola en mi minúscula habitación del piso superior. Intento no prestar atención a Nina cuando lo ensucia todo simplemente para ver cómo lo limpio. A las extrañas mentiras que cuenta sobre su propia hija. A su marido, que cada día parece más abatido. Pero cuando miro a Andrew a los ojos, castaños, encantadores y llenos de dolor, no me resulta difícil imaginar cómo sería vivir en la piel de Nina. El gran vestidor, el coche de lujo, el esposo perfecto. Hasta que un día no me resisto a probarme uno de sus maravillosos vestidos blancos. Solo quiero saber qué se siente. Pero ella pronto lo descubre, y cuando me doy cuenta de que la puerta de mi habitación solo se cierra por fuera ya es demasiado tarde. Algo me reconforta: los Winchester no saben quién soy en realidad .

</details>

### 113. La Biblioteca de la Medianoche

**Matt Haig** · *Fantástico · Novela*

PREMIO GOODREADS 2020 A LA MEJOR OBRA DE FICCIÓN «Entre la vida y la muerte hay una biblioteca. Y los estantes de esa biblioteca son infinitos. Cada libro da la oportunidad de probar otra vida …

<details><summary>Sinopsis completa</summary>

PREMIO GOODREADS 2020 A LA MEJOR OBRA DE FICCIÓN «Entre la vida y la muerte hay una biblioteca. Y los estantes de esa biblioteca son infinitos. Cada libro da la oportunidad de probar otra vida que podrías haber vivido y de comprobar cómo habrían cambiado las cosas si hubieras tomado otras decisiones... ¿Habrías hecho algo de manera diferente si hubieras tenido la oportunidad?». Nora Seed aparece, sin saber cómo, en la Biblioteca de la Medianoche , donde se le ofrece una nueva oportunidad para hacer las cosas bien. Hasta ese momento, su vida ha estado marcada por la infelicidad y el arrepentimiento. Nora siente que ha defraudado a todos, y también a ella misma. Pero esto está a punto de cambiar. Los libros de la Biblioteca de la Medianoche permitirán a Nora vivir como si hubiera hecho las cosas de otra manera. Con la ayuda de una vieja amiga, tendrá la opción de esquivar todo aquello que se arrepiente de haber hecho (o no haber hecho), en pos de la vida perfecta. Pero las cosas no siempre serán como imaginó que serían, y pronto sus decisiones enfrentarán a la Biblioteca y a ella misma en un peligro extremo. Nora deberá responder una última pregunta antes de que el tiempo se agote: ¿cuál es la mejor manera de vivir?

</details>

### 114. La cabaña

**William Paul Young** · *Drama · Relato*

Una agradable excursión familiar se transforma en tragedia cuando Missy, la hija pequeña de Mack, desaparece. Ante la evidencia del asesinato de la niña, el padre reaccionará rebelándose frente a Dios, ante lo que considera …

<details><summary>Sinopsis completa</summary>

Una agradable excursión familiar se transforma en tragedia cuando Missy, la hija pequeña de Mack, desaparece. Ante la evidencia del asesinato de la niña, el padre reaccionará rebelándose frente a Dios, ante lo que considera una radical injusticia. Transcurridos tres años, Mack recibe una extraña carta, firmada por Dios, que le conmina a reunirse con él en la cabaña donde la niña murió. A pesar de lo aparentemente absurdo de la situación, acude a la cita y tiene un peculiar encuentro con un hombre y dos mujeres, personificaciones de Dios, Jesucristo y el Espíritu Santo. Tras permanecer un tiempo en su compañía y exponer su indignación y sus dudas, la reflexión de Mack acerca de lo ocurrido cambia por completo.En principio, el autor escribió esta historia para sus amigos y sus seis hijos, y autofinanció la edición. Gracias al boca a boca llegó a manos de una editorial canadiense, y hoy es ya un best seller.

</details>

### 115. La carretera

**Cormac McCarthy** · *Ciencia ficción · Drama*

La carretera, novela galardonada con el premio Pulitzer 2007 y best seller literario del año en Estados Unidos, transcurre en la inmensidad del territorio norteamericano, un paisaje literalmente quemado por lo que parece haber sido …

<details><summary>Sinopsis completa</summary>

La carretera, novela galardonada con el premio Pulitzer 2007 y best seller literario del año en Estados Unidos, transcurre en la inmensidad del territorio norteamericano, un paisaje literalmente quemado por lo que parece haber sido un reciente holocausto nuclear. Un padre trata de salvar a su hijo emprendiendo un viaje con él. Rodeados de un paisaje baldío, amenazados por bandas de caníbales, empujando un carrito de la compra donde guardan sus escasas pertenencias, recorren los lugares donde el padre pasó una infancia recordada a veces en forma de breves bocetos del paraíso perdido, y avanzan hacia el sur, hacia el mar, huyendo de un frío "capaz de romper las rocas".

</details>

### 116. La casa de los espíritus

**Isabel Allende** · *Drama · Histórico · Otros*

La novela recorre, con el paso de los años, la evolución de los cambios sociales e ideológicos del país (Chile), sin perder de vista las peripecias personales —a menudo misteriosas— de la saga familiar. Entrarán …

<details><summary>Sinopsis completa</summary>

La novela recorre, con el paso de los años, la evolución de los cambios sociales e ideológicos del país (Chile), sin perder de vista las peripecias personales —a menudo misteriosas— de la saga familiar. Entrarán en escena los avances tecnológicos, la mudanza en las costumbres, las «nuevas ideas» socialistas y de emancipación de la mujer, el espiritismo y los fantasmas comunistas, hasta desembocar en el triunfo socialista y el posterior golpe militar. Estas convulsiones afectarán a la familia de Esteban Trueba —cuyos miembros poseen siempre algún rasgo extravagante y desmedido— con distintos matices de dramatismo y violencia. EL viejo terrateniente envejece y, con él, una forma de ver el mundo basada en el dominio, el código de honor y la venganza.

</details>

### 117. La catedral del mar

**Ildefonso Falcones** · *Histórico* · Serie: La catedral del mar, tomo 1

Siglo XIV. La ciudad de Barcelona se encuentra en su momento de mayor prosperidad; ha crecido hacia la Ribera, el humilde barrio de los pescadores, cuyos habitantes deciden construir, con el dinero de unos y …

<details><summary>Sinopsis completa</summary>

Siglo XIV. La ciudad de Barcelona se encuentra en su momento de mayor prosperidad; ha crecido hacia la Ribera, el humilde barrio de los pescadores, cuyos habitantes deciden construir, con el dinero de unos y el esfuerzo de otros, el mayor templo mariano jamás conocido: Santa María de la Mar. Una construcción que es paralela a la azarosa historia de Arnau, un siervo de la tierra que huye de los abusos de su señor feudal y se refugia en Barcelona, donde se convierte en ciudadano y, con ello, en hombre libre. El joven Arnau trabaja como palafrenero, estibador, soldado y cambista. Una vida extenuante, siempre al amparo de la catedral de la Mar, que le iba a llevar de la miseria del fugitivo a la nobleza y la riqueza. Pero con esta posición privilegiada también le llega la envidia de sus pares, que urden una sórdida conjura que pone su vida en manos de la Inquisición... La catedral del mar es una trama en la que se entrecruzan lealtad y venganza, traición y amor, guerra y peste, en un mundo marcado por la intolerancia religiosa, la ambición material y la segregación social. Todo ello convierte a esta obra no solo en una novela absorbente, sino también en la más fascinante y ambiciosa recreación de las luces y sombras de la época feudal.

</details>

### 118. La chica del tren

**Paula Hawkins** · *Intriga · Novela · Policíaco*

¿Estabas en el tren de las 8.04? ¿Viste algo sospechoso? Rachel, sí. Rachel toma siempre el tren de las 8.04 h. Cada mañana lo mismo: el mismo paisaje, las mismas casas… y la misma parada …

<details><summary>Sinopsis completa</summary>

¿Estabas en el tren de las 8.04? ¿Viste algo sospechoso? Rachel, sí. Rachel toma siempre el tren de las 8.04 h. Cada mañana lo mismo: el mismo paisaje, las mismas casas… y la misma parada en la señal roja. Son solo unos segundos, pero le permiten observar a una pareja desayunando tranquilamente en su terraza. Siente que los conoce y se inventa unos nombres para ellos: Jess y Jason. Su vida es perfecta, no como la suya. Pero un día ve algo. Sucede muy deprisa, pero es suficiente. ¿Y si Jess y Jason no son tan felices como ella cree? ¿Y si nada es lo que parece? Tú no la conoces. Ella a ti, sí.

</details>

### 119. La ciudad de las bestias

**Isabel Allende** · *Aventuras · Infantil y juvenil* · Serie: Memorias del Águila y el Jaguar, tomo 1

Alexander Cold, un muchacho americano de 15 años aficionado a tocar la flauta y al montañismo, se ve obligado a acompañar a su abuela, la aventurera, escritora y periodista Kate Cold, a una expedición a …

<details><summary>Sinopsis completa</summary>

Alexander Cold, un muchacho americano de 15 años aficionado a tocar la flauta y al montañismo, se ve obligado a acompañar a su abuela, la aventurera, escritora y periodista Kate Cold, a una expedición a la selva amazónica organizada por la 'International Geographic' y cuyo objetivo es capturar a la Bestia. Allí conocerá a su nueva amiga y compañera de viaje Nadia Santos y junto con un chamán llamado Walimai intentarán salvar a la gente de la neblina. Se internarán en el corazón del Amazonas y el muchacho descubrirá un mundo sorprendente y fantástico. Alexander sufrirá una drástica metamorfosis de su personalidad durante el viaje, de ser una especie de «niño bien» al que le dan casi todo en bandeja pasa a convertirse en Jaguar, protector de la gente de la neblina, y es proclamado entre los indios como jefe para negociar con los 'nahab' (los extranjeros a la tribu).

</details>

### 120. La comunidad del anillo

**J. R. R. Tolkien** · *Fantástico* · Serie: El señor de los anillos, tomo 1

En la adormecida e idílica Comarca, un joven hobbit recibe un encargo: custodiar el Anillo Único y emprender el viaje para su destrucción en la Grieta del Destino. Acompañado por magos, hombres, elfos y enanos, …

<details><summary>Sinopsis completa</summary>

En la adormecida e idílica Comarca, un joven hobbit recibe un encargo: custodiar el Anillo Único y emprender el viaje para su destrucción en la Grieta del Destino. Acompañado por magos, hombres, elfos y enanos, atravesará la Tierra Media y se internará en las sombras de Mordor, perseguido siempre por las huestes de Sauron, el Señor Oscuro, dispuesto a recuperar su creación para establecer el dominio definitivo del Mal.

</details>

### 121. La divina comedia (Ilustrado)

**Dante Alighieri** · *Fantástico · Filosófico · Poesía*

La Divina Comedia es un poema donde se mezcla la vida real con la sobrenatural, muestra la lucha entre la nada y la inmortalidad, una lucha donde se superponen tres reinos, tres mundos, logrando una …

<details><summary>Sinopsis completa</summary>

La Divina Comedia es un poema donde se mezcla la vida real con la sobrenatural, muestra la lucha entre la nada y la inmortalidad, una lucha donde se superponen tres reinos, tres mundos, logrando una suma de múltiples visuales que nunca se contradicen o se anulan. Los tres mundos infierno, purgatorio y paraíso reflejan tres modos de ser de la humanidad, en ellos se reflejan el vicio, el pasaje del vicio a la virtud y la condición de los hombres perfectos. Es entonces a través de los viciosos, penitentes y buenos que se revela la vida en todas sus formas, sus miserias y hazañas, pero también se muestra la vida que no es, la muerte, que tiene su propia vida, todo como una mezcla agraciada planteada por Dante, que se vuelve arquitecto de lo universal y de lo sublime. IMPORTANTE: Recomendamos descargar los libros de poesía en formato EPUB dado que en PDF pueden tener problemas de visualización.

</details>

### 122. La hipótesis del amor

**Ali Hazelwood** · *Novela · Romántico*

Olive Smith es una doctoranda de tercer año que no cree en las relaciones amorosas duraderas, pero su mejor amiga, Ahn, sí, y por eso Olive se ha metido en un lío monumental. A Ahn …

<details><summary>Sinopsis completa</summary>

Olive Smith es una doctoranda de tercer año que no cree en las relaciones amorosas duraderas, pero su mejor amiga, Ahn, sí, y por eso Olive se ha metido en un lío monumental. A Ahn le gusta el exnovio de Olive, pero jamás daría el primer paso porque es una buena amiga. A Olive no le va a resultar nada fácil convencerla de que ha pasado página, puesto que los científicos necesitan pruebas. Por eso, como cualquier mujer con un mínimo de amor propio, se deja llevar por el pánico y besa al primer hombre con el que se encuentra para que Ahn la vea. Ese hombre es nada más y nada menos que Adam Carlsen, un joven profesor tan reputado por la calidad de su trabajo como por su imbecilidad. Así que Olive se queda de piedra cuando Carlsen accede a mantener su farsa en secreto y ser su novio falso.

</details>

### 123. La Historia Interminable – Color

**Michael Ende** · *Aventuras · Ciencia ficción · Infantil y juvenil*

Bastián Baltasar Bux, es un niño tímido al que le encanta leer y tiene una portentosa imaginación. Leyendo un extraño libro averigua que el reino de la Fantasía está en peligro. En este mismo libro …

<details><summary>Sinopsis completa</summary>

Bastián Baltasar Bux, es un niño tímido al que le encanta leer y tiene una portentosa imaginación. Leyendo un extraño libro averigua que el reino de la Fantasía está en peligro. En este mismo libro lee, asombrado, que Bastián Baltasar Bux debe unirse a Attreyu, un valiente guerrero, para salvar la Fantasía. Así comprende que ese libro es Fantasía y Fantasía es La historia interminable. Versión ilustrada por Roswitha Quadeflieg. Maquetación a dos tintas y diferentes tipografías para distinguir las dos historias narradas.

</details>

### 124. La jaula del rey

**Victoria Aveyard** · *Fantástico · Juvenil · Novela* · Serie: La Reina Roja, tomo 3

Ahora que la chispa de la «Niña Relámpago» ha sido anulada, ¿quién guiará el camino de la rebelión? Debilitada y prisionera, atormentada por sus errores, Mare Barrow se ha postrado a los pies de un …

<details><summary>Sinopsis completa</summary>

Ahora que la chispa de la «Niña Relámpago» ha sido anulada, ¿quién guiará el camino de la rebelión? Debilitada y prisionera, atormentada por sus errores, Mare Barrow se ha postrado a los pies de un traidor. El espurio rey de Norta continúa su malévola campaña de expansión y genocidio, y no se detendrá ante nada ni nadie. Pero más allá de las murallas palaciegas, la rebelión Roja crece y se multiplica; y el príncipe exiliado, legítimo heredero del trono, hará todo lo posible por rescatar a su amada. La lealtad será probada en ambos lados, y la sangre roja y plateada correrá como un río de fuego que hará que todo arda a su paso.

</details>

### 125. La ladrona de libros

**Markus Zusak** · *Drama · Infantil y juvenil*

Érase una vez un pueblo donde las noches eran largas y la muerte contaba su propia historia. En el pueblo vivía una niña que quería leer, un hombre que tocaba el acordeón y un joven …

<details><summary>Sinopsis completa</summary>

Érase una vez un pueblo donde las noches eran largas y la muerte contaba su propia historia. En el pueblo vivía una niña que quería leer, un hombre que tocaba el acordeón y un joven judío que escribía cuentos hermosos para escapar del horror de la guerra. Al cabo de un tiempo, la niña se convirtió en una ladrona que robaba libros y regalaba palabras. Con estas palabras se escribió una historia hermosa y cruel que ahora ya es una novela inolvidable.

</details>

### 126. La larga marcha

**Stephen King** · *Ciencia ficción · Terror*

Una inquietante novela futurista donde la realidad supera a la fantasía más terrorífica. El escenario: una sociedad ultraconservadora que ha llevado al paroxismo sus rasgos más perversos, dominada por un estado policial. El acontecimiento: la …

<details><summary>Sinopsis completa</summary>

Una inquietante novela futurista donde la realidad supera a la fantasía más terrorífica. El escenario: una sociedad ultraconservadora que ha llevado al paroxismo sus rasgos más perversos, dominada por un estado policial. El acontecimiento: la más extraordinaria competición deportiva, una agotadora marcha a pie donde un resbalón puede ser el último. Los competidores: cien adolescentes elegidos por sorteo y decididos a pasar sobre los cadáveres de sus compañeros para llegar a la meta. El premio: fama y fortuna para el ganador, es decir, para el único superviviente... Solo uno será el triunfador. Los 99 restantes morirán.

</details>

### 127. La lección de August

**R.J. Palacio** · *Infantil y juvenil*

Su cara lo hace distinto y él solo quiere ser uno más. Camina siempre mirando al suelo, la cabeza gacha y el flequillo tratando en vano de esconder su rostro, pero, aun así, es objeto …

<details><summary>Sinopsis completa</summary>

Su cara lo hace distinto y él solo quiere ser uno más. Camina siempre mirando al suelo, la cabeza gacha y el flequillo tratando en vano de esconder su rostro, pero, aun así, es objeto de miradas furtivas, susurros ahogados y codazos de asombro. August sale poco, su vida transcurre entre las acogedoras paredes de su casa, entre la compañía de su familia, su perra Daisy y las increíbles historias de La guerra de las Galaxias. Este año todo va a cambiar, porque este año va a ir, por primera vez, a la escuela. Allí aprenderá la lección más importante de su vida, la que no se enseña en las aulas ni en los libros de texto: crecer en la adversidad, aceptarse tal y como es, sonreír a los días grises y saber que, al final, siempre encontrará una mano amiga.

</details>

### 128. La llamada de Cthulhu

**H. P. Lovecraft** · *Terror*

Comienza con la explicación de la muerte de un prominente profesor de la Universidad de Miskatonic y un estudio de sus documentos. Estos incluyen un informe sobre un ataque en un culto satánico. Una investigación …

<details><summary>Sinopsis completa</summary>

Comienza con la explicación de la muerte de un prominente profesor de la Universidad de Miskatonic y un estudio de sus documentos. Estos incluyen un informe sobre un ataque en un culto satánico. Una investigación sobre los cultistas saca a la luz pistas sobre la horrorosa criatura que veneran, Cthulhu. Este ser, que supuestamente llegó con sus seguidores extraterrestres desde las estrellas millones de años antes de la aparición del Hombre, ahora descansa en un sueño profundo en su ciudad hundida R’lyeh.

</details>

### 129. La maldición de Hill House

**Shirley Jackson** · *Novela · Terror*

La escritora Shirley Jackson (1916-1965) publicó su primera novela The Road Through the Wall en 1948, a la que siguieron Hangsaman (1951), The Bird’s Nest (1954), The Sundial (1958) y We Have Always Lived in …

<details><summary>Sinopsis completa</summary>

La escritora Shirley Jackson (1916-1965) publicó su primera novela The Road Through the Wall en 1948, a la que siguieron Hangsaman (1951), The Bird’s Nest (1954), The Sundial (1958) y We Have Always Lived in the Castle , en 1962, que obtuvo una valiosa publicidad extraliteraria cuando al marido de Shirley Jackson se le ocurrió hacer público, en las páginas de un conocido rotativo, que su autora había practicado la brujería, cosa que ésta negó rápidamente. No obstante, después de su muerte se supo que semejante desmentido sólo trataba de evitar el rechazo de la opinión pública hacia su persona. Según explicó su hijo, Laurence Hyman, su madre poseía un tablero Ouija y cartas del Tarot y sabía perfectamente cómo utilizarlos, además de unos quinientos libros sobre ocultismo. La maldición de Hill House ( The Haunting of Hill House , 1959), considerada una de las principales novelas de horror del siglo XX, narra el inquietante experimento de John Montague, doctor en Filosofía y antropólogo, que lleva años entregado al estudio de «las perturbaciones psíquicas» que suelen manifestarse en las «casas encantadas». Infructuosamente ha buscado una casa idónea, cuando un día oye hablar de Hill House, una mansión solitaria y de siniestra reputación. Montague decide alquilarla y busca ayudantes dispuestos a pasar una temporada en ella: Eleanor, una mujer desdichada que, tras once años cuidando a su arisca madre inválida, se ha vuelto una persona solitaria; Theodora, joven alegre y curiosa, seleccionada por su increíble capacidad telepática; y Luke, vividor y mentiroso, incluido en el grupo por exigencia de la propietaria, su tía. El objetivo: tomar notas de cualquier fenómeno paranormal que se presente para documentar el libro sobre casas encantadas que prepara el doctor. Las alucinantes experiencias que vivirán en la casa será mejor que el lector las descubra por sí mismo.

</details>

### 130. La máquina de matar

**Nicolás Márquez** · *Divulgación · Historia*

En este revelador libro, el prolífico escritor Nicolás Márquez (probablemente el argentino que más y mejor sepa sobre la vida y obra del Che), con apasionante narrativa y escalofriante documentación cuenta la verdadera biografía que …

<details><summary>Sinopsis completa</summary>

En este revelador libro, el prolífico escritor Nicolás Márquez (probablemente el argentino que más y mejor sepa sobre la vida y obra del Che), con apasionante narrativa y escalofriante documentación cuenta la verdadera biografía que la dictadura de la corrección política pretende ocultar sobre Guevara. Aquí el lector va encontrar no el ficcionario relato del idealista simpático tan agasajado mediante camisetas, adornos y banderines (suerte de souvenir contestatario para consumo del buen progresista de manual), sino al verdadero Che Guevara en toda su intrincada y tenebrosa dimensión. La Máquina de Matar. Biografía definitiva del Che Guevara, constituye la más fiel y provocadora obra que se haya escrito sobre el personaje en cuestión, la cual la convierte en un texto de lectura indispensable para todo aquel que quiera escapar de la propaganda dominante.

</details>

### 131. La metamorfosis

**Franz Kafka** · *Clásico · Terror*

Durante el otoño de 1912, en Praga, escribió Franz Kafka (1883-1924) La metamorfosis, la peripecia subterránea y literal de Gregor Samsa, un viajante de comercio que al despertarse una mañana «de un sueño lleno de …

<details><summary>Sinopsis completa</summary>

Durante el otoño de 1912, en Praga, escribió Franz Kafka (1883-1924) La metamorfosis, la peripecia subterránea y literal de Gregor Samsa, un viajante de comercio que al despertarse una mañana «de un sueño lleno de pesadillas se encontró en su cama convertido en un bicho enorme». En pocos libros de Kafka queda tan explícito y tan nítido su mundo como en La metamorfosis, en la que el protagonista, convertido en bestia, sumido en la más absoluta incomunicación, se ve reducido cruelmente a la nada y arrastrado inexorablemente a la muerte. Otros escritos de Kafka desarrollan rigurosas variaciones paralelas, desmenuzan inexorables pesadillas, asignan obsesiones enigmáticas a personajes desorientados y vencidos, pero tal vez sea La metamorfosis la narración que mejor expresa al «hombre primordial kafkiano». De ahí que merezca la calificación unánime de obra perfecta y obra maestra, un texto decididamente superior en el panorama de la literatura universal del siglo XX.

</details>

### 132. La novia gitana

**Carmen Mola** · *Intriga · Novela · Policíaco* · Serie: Inspectora Elena Blanco, tomo 1

«En Madrid se mata poco», le decía al joven subinspector Ángel Zárate su mentor en la policía; «pero cuando se mata, no tiene nada que envidiarle a ninguna ciudad del mundo», podría añadir la inspectora …

<details><summary>Sinopsis completa</summary>

«En Madrid se mata poco», le decía al joven subinspector Ángel Zárate su mentor en la policía; «pero cuando se mata, no tiene nada que envidiarle a ninguna ciudad del mundo», podría añadir la inspectora Elena Blanco, jefa de la Brigada de Análisis de Casos, un departamento creado para resolver los crímenes más complicados y abyectos. Susana Macaya, de padre gitano pero educada como paya, desaparece tras su fiesta de despedida de soltera. El cadáver es encontrado dos días después en la Quinta de Vista Alegre del madrileño barrio de Carabanchel. Podría tratarse de un asesinato más, si no fuera por el hecho de que la víctima ha sido torturada siguiendo un ritual insólito y atroz, y de que su hermana Lara sufrió idéntica suerte siete años atrás, también en vísperas de su boda. El asesino de Lara cumple condena desde entonces, por lo que solo caben dos posibilidades: o alguien ha imitado sus métodos para matar a la hermana pequeña, o hay un inocente encarcelado. Por eso el comisario Rentero ha decidido apartar a Zárate del caso y encargárselo a la veterana Blanco, una mujer peculiar y solitaria, amante de la grappa , el karaoke, los coches de coleccionista y las relaciones sexuales en todoterrenos. Una policía vulnerable, que se mantiene en el cuerpo para no olvidar que en su vida existe un caso pendiente, que no ha podido cerrar. Investigar a una persona implica conocerla, descubrir sus secretos y contradicciones, su historia. En el caso de Lara y Susana, Elena Blanco debe asomarse a la vida de unos gitanos que han renunciado a sus costumbres para integrarse en la sociedad y a la de otros que no se lo perdonan, y levantar cada velo para descubrir quién pudo vengarse con tanta saña de ambas novias gitanas. «¿La Elena Ferrante española? Carmen Mola irrumpe con fuerza en el panorama de la novela negra con La novia gitana [...]. Una estructura sólida y un argumento llevado como un clásico policial pero que al tiempo rompe varios convencionalismos.» Juan Carlos Galindo, El País «Un estupendo y tremendo thriller ... No paré hasta la última página.» Manuel Rodríguez Rivero, Babelia «Intensa obra de una misteriosa Carmen Mola [...]. Una intriga bien pensada y ejecutada [...]. Los lectores fascinados por Dazieri y por las más crueles novelas de Pierre Lemaitre se interesarán también por este libro [...]. Un sorprendente final.» Lilian Neuman, Cultura/s de La Vanguardia «Prepárate para sufrir con la primera novela de Carmen Mola.» Elena Méndez, La Voz de Galicia «Un potente thriller [...] con una narración detallista en la que el tratamiento de la violencia recuerda por su crudeza y originalidad al estilo de Pierre Lemaitre o Víctor del Árbol.» Ana Belén García Flores, RTVE

</details>

### 133. La paciente silenciosa

**Alex Michaelides** · *Intriga · Novela*

Alicia Berenson, una pintora de éxito, dispara cinco tiros en la cabeza de su marido, y no vuelve a hablar nunca más. Su negativa a emitir palabra alguna convierte una tragedia doméstica en un misterio …

<details><summary>Sinopsis completa</summary>

Alicia Berenson, una pintora de éxito, dispara cinco tiros en la cabeza de su marido, y no vuelve a hablar nunca más. Su negativa a emitir palabra alguna convierte una tragedia doméstica en un misterio que atrapa la imaginación de toda Inglaterra. Theo Faber, un ambicioso psicoterapeuta forense obsesionado con el caso, está empeñado en desentrañar el misterio de lo que ocurrió aquella noche fatal y consigue una plaza en The Grove, la unidad de seguridad en el norte de Londres a la que Alicia fue enviada hace seis años y en la que sigue obstinada en su silencio. Pronto descubre que el mutismo de la paciente está mucho más enraizado de lo que pensaba. Pero, si al final hablara, ¿estaría dispuesto a escuchar la verdad?

</details>

### 134. La pareja de al lado

**Shari Lapena** · *Intriga · Novela*

Todo comenzó en una cena con los vecinos... Tu vecina te dijo que preferiría que no llevaras a tu bebé de seis meses a la cena. No es nada personal, simplemente no soporta sus llantos. …

<details><summary>Sinopsis completa</summary>

Todo comenzó en una cena con los vecinos... Tu vecina te dijo que preferiría que no llevaras a tu bebé de seis meses a la cena. No es nada personal, simplemente no soporta sus llantos. Tu marido estaba de acuerdo. Después de todo, vivís en la casa de al lado. Podíais llevaros el monitor infantil y turnaros para pasar a verla cada media hora. Tu hija dormía cuando fuiste a comprobar por última vez. Sin embargo, en este momento, mientras subes corriendo las escaleras hasta su habitación envuelta en un absoluto silencio, confirmas que tu peor pesadilla se ha hecho realidad: ha desaparecido. Nunca antes habías tenido que llamar a la policía. Ahora están en tu casa y quién sabe lo que pueden llegar a descubrir. ¿De qué serías capaz cuando has sobrepasado tus límites?

</details>

### 135. La Reina Roja

**Victoria Aveyard** · *Aventuras · Fantástico · Juvenil · Novela* · Serie: La Reina Roja, tomo 1

En una sociedad dividida por el color de la sangre, los Rojos luchan por sobrevivir bajo la sombra de los Plateados, «superhumanos» con poderes terribles que les permiten manejar el mundo a su antojo. Pero …

<details><summary>Sinopsis completa</summary>

En una sociedad dividida por el color de la sangre, los Rojos luchan por sobrevivir bajo la sombra de los Plateados, «superhumanos» con poderes terribles que les permiten manejar el mundo a su antojo. Pero cuando se revela que Mare Barrow —una joven ladronzuela Roja— tiene también esas habilidades, es llevada al mundo de los Plateados. Allí descubrirá que el poder es un juego peligroso y que la única certeza es la traición. «En la escuela aprendimos acerca del mundo anterior a este, el mundo de los ángeles y los dioses que vivían en el cielo y gobernaban la Tierra con amor y bondad. Algunos dicen que son solo leyendas, pero yo no lo creo. Los dioses aún nos dominan, han descendido de las estrellas y no les queda ni un ápice de bondad».

</details>

### 136. La selección

**Kiera Cass** · *Ciencia ficción · Infantil y juvenil · Romántico* · Serie: La Selección, tomo 1

Para treinta y cinco chicas, La Selección es una oportunidad que sólo se presenta una vez en la vida. La oportunidad de escapar de la vida que les ha tocado por nacer en una determinada …

<details><summary>Sinopsis completa</summary>

Para treinta y cinco chicas, La Selección es una oportunidad que sólo se presenta una vez en la vida. La oportunidad de escapar de la vida que les ha tocado por nacer en una determinada familia. La oportunidad de que las trasladen a un mundo de trajes preciosos y joyas que no tienen precio. La oportunidad de vivir en un palacio y de competir por el corazón del guapísimo príncipe Maxon. Sin embargo, para America Singer, ser seleccionada es una pesadilla porque significa alejarse de su amor secreto, Aspen, quien pertenece a una casta inferior a la de ella; y también abandonar su hogar para pelear por una corona que no desea y vivir en un palacio que está bajo la constante amenaza de ataques violentos por parte de los rebeldes.

</details>

### 137. La sombra del viento

**Carlos Ruiz Zafón** · *Intriga* · Serie: El cementerio de los libros olvidados, tomo 1

Año de publicación: 2002 Sinopsis: Un amanecer de 1945 un muchacho es conducido por su padre a un misterioso lugar oculto en el corazón de la ciudad vieja: El Cementerio de los Libros Olvidados. Allí, …

<details><summary>Sinopsis completa</summary>

Año de publicación: 2002 Sinopsis: Un amanecer de 1945 un muchacho es conducido por su padre a un misterioso lugar oculto en el corazón de la ciudad vieja: El Cementerio de los Libros Olvidados. Allí, Daniel Sempere encuentra un libro maldito que cambiará el rumbo de su vida y le arrastrará a un laberinto de intrigas y secretos enterrados en el alma oscura de la ciudad. La Sombra del Viento es un misterio literario ambientado en la Barcelona de la primera mitad del siglo XX, desde los últimos esplendores del Modernismo a las tinieblas de la posguerra. La Sombra del Viento mezcla técnicas de relato de intriga, de novela histórica y de comedia de costumbres pero es, sobre todo, una tragedia histórica de amor cuyo eco se proyecta a través del tiempo. Con gran fuerza narrativa, el autor entrelaza tramas y enigmas a modo de muñecas rusas en un inolvidable relato sobre los secretos del corazón y el embrujo de los libros ,manteniendo la intriga hasta la última página.

</details>

### 138. La vegetariana

**Kang Han** · *Novela · Otros · Realista*

Yeonghye es una mujer aparentemente normal, joven, sin mayores virtudes o defectos. Una noche, sin ninguna actitud previa que hiciera suponer un cambio en su carácter, su marido la encuentra en la cocina tirando a …

<details><summary>Sinopsis completa</summary>

Yeonghye es una mujer aparentemente normal, joven, sin mayores virtudes o defectos. Una noche, sin ninguna actitud previa que hiciera suponer un cambio en su carácter, su marido la encuentra en la cocina tirando a la basura toda la carne almacenada en el congelador. Cuando él la increpa por lo que está haciendo, ella le dice que ha tenido un sueño y que abandonará la ingesta de carnes. Su determinación es absolutamente radical e irrevocable, pero el marido y la familia no están preparados para esta decisión ni para la transformación que comienza a gestarse en Yeonghye a partir de ese momento. La vegetariana es una novela con un fuerte componente psicológico, que cuestiona los límites culturales de la cordura, la violencia y el valor del cuerpo como un bien privado y último refugio.

</details>

### 139. La verdad sobre el caso Harry Quebert

**Joël Dicker** · *Novela · Policíaco* · Serie: Marcus Goldman, tomo 1

Quién mató a Nola Kellergan es la gran incógnita a desvelar en este thriller incomparable cuya experiencia de lectura escapa a cualquier tentativa de descripción. Intentémoslo: una gran novela policiaca y romántica a tres tiempos …

<details><summary>Sinopsis completa</summary>

Quién mató a Nola Kellergan es la gran incógnita a desvelar en este thriller incomparable cuya experiencia de lectura escapa a cualquier tentativa de descripción. Intentémoslo: una gran novela policiaca y romántica a tres tiempos −1975, 1998 y 2008− acerca del asesinato de una joven de quince años en la pequeña ciudad de Aurora, en New Hampshire. En 2008, Marcus Goldman, un joven escritor, visita a su mentor −Harry Quebert, autor de una aclamada novela−, y descubre que éste tuvo una relación secreta con Nola Kellergan. Poco después, Harry es arrestado, acusado de asesinato, al encontrarse el cadáver de Nola enterrado en su jardín. Marcus comienza a investigar y a escribir un libro sobre el caso. Mientras intenta demostrar la inocencia de Harry, una trama de secretos sale a la luz. La verdad sólo llega al final de un largo, intrincado y apasionante recorrido.

</details>

### 140. Las dos muertes

**Jaime Alfonso Sandoval** · *Fantástico · Humor · Juvenil · Novela* · Serie: Mundo Umbrío, tomo 1

Hablemos de vampiros , pero no de los de mirada vidriosa que seducen a las doncellas con sus labios perfectos y sus colmillos impecables, sino de los de la vida real: los que usan pantuflas …

<details><summary>Sinopsis completa</summary>

Hablemos de vampiros , pero no de los de mirada vidriosa que seducen a las doncellas con sus labios perfectos y sus colmillos impecables, sino de los de la vida real: los que usan pantuflas con forma de pollo , tienen alergia al polen y su esposa les dice flaquito . A los trece años, Lina descubre que su padre, Benjamín Posada, es en realidad Benvolio Pozafria, un chupasangre . ¡Ya bastante tenía con ser una nerd impopular y fea! Titania Labios Sangrantes, la tía Tripa, el Doctor Peste, Guano, Gusanos y Gargajo son apenas una muestra de la numerosa parentela vampírica que la espera en el Mundo Umbrío .

</details>

### 141. Las ventajas de ser un marginado

**Stephen Chbosky** · *Infantil y juvenil*

Vivir al margen ofrece una perspectiva única. Pero siempre llega el momento de entrar en escena y ver el mundo desde dentro. Charlie tiene 15 años y se ha quedado solo tras el suicidio de …

<details><summary>Sinopsis completa</summary>

Vivir al margen ofrece una perspectiva única. Pero siempre llega el momento de entrar en escena y ver el mundo desde dentro. Charlie tiene 15 años y se ha quedado solo tras el suicidio de su mejor amigo. Vive con sus padres, su popular y guapa hermana y un hermano mayor que es una estrella del fútbol americano y que está a punto de comenzar la universidad. Su profesor de lengua está convencido de que Charlie posee una gran capacidad intelectual. Tras conocer a Sam y Patrick empieza a comprender lo que es ser un adolescente, y comienza un viaje hacia la madurez que le llevará a recorrer caminos nuevos e inesperados. Con ellos descubre nueva música, empieza a beber, fumar y coquetear con drogas, cambia de amigos… ¡Hasta que se convierte en un joven de verdad!

</details>

### 142. Llámame por tu nombre

**André Aciman** · *Drama · Filosófico · Novela · Otros*

En una localidad de la costa de Italia, durante la década de los ochenta, la familia de Elio instauró la tradición de recibir en el verano a estudiantes o creadores jóvenes que, a cambio de …

<details><summary>Sinopsis completa</summary>

En una localidad de la costa de Italia, durante la década de los ochenta, la familia de Elio instauró la tradición de recibir en el verano a estudiantes o creadores jóvenes que, a cambio de alojamiento, ayudaran al cabeza de familia, catedrático, en sus compromisos culturales. Oliver es el elegido este verano, un joven escritor norteamericano que pronto excita la imaginación de Elio. Durante las siguientes semanas, los impulsos ocultos de obsesión y miedo, fascinación y deseo intensificarán su pasión.

</details>

### 143. Los jardines de la Luna

**Steven Erikson** · *Fantástico* · Serie: Malaz: El libro de los caídos, tomo 1

El inicio de una de las mejores sagas de fantasía épica de la historia Tras interminables guerras, amargas luchas internas y sangrientas confrontaciones, incluso las tropas imperiales necesitan un descanso. Pero la obsesión expansionista de …

<details><summary>Sinopsis completa</summary>

El inicio de una de las mejores sagas de fantasía épica de la historia Tras interminables guerras, amargas luchas internas y sangrientas confrontaciones, incluso las tropas imperiales necesitan un descanso. Pero la obsesión expansionista de la emperatriz Lassen no tiene límites, y cuenta con el apoyo de sus sanguinarios agentes de la Garra. Tras el último asedio, el sargento Whiskeyjack y su pelotón de Arrasapuentes necesitan tiempo para descansar y enterrar a sus muertos, pero Darujhistan, la última de las Ciudades Libres de Genabackis, les espera. Es el objetivo último de la insaciable emperatriz. ... Y parece que el Imperio no es el único que codicia esa plaza: fuerzas siniestras conspiran dentro y fuera de las sendas mágicas, y todo indica que los propios dioses se preparan para la batalla...

</details>

### 144. Los juegos del hambre

**Suzanne Collins** · *Ciencia ficción · Juvenil* · Serie: Distritos, tomo 1

GANAR SIGNIFICA FAMA Y RIQUEZA. PERDER SIGNIFICA UNA MUERTE SEGURA. En una oscura versión del futuropróximo, doce chicos y doce chicas se ven obligados a participar en un reality show llamado Los juegos del hambre. …

<details><summary>Sinopsis completa</summary>

GANAR SIGNIFICA FAMA Y RIQUEZA. PERDER SIGNIFICA UNA MUERTE SEGURA. En una oscura versión del futuropróximo, doce chicos y doce chicas se ven obligados a participar en un reality show llamado Los juegos del hambre. Solo hay una regla: matar o morir. Cuando Katniss Everdeen, una joven de dieciséis años se presenta voluntaria para ocuparel lugar de su hermana en los juegos, lo entiende como una condena a muerte. Sin embargo Katniss ya ha visto la muertede cerca y la supervivencia forma parte de su naturaleza. ¡Que empiecen los septuagésimo cuartos juegos del hambre!

</details>

### 145. Los renglones torcidos de Dios

**Torcuato Luca de Tena** · *Drama · Intriga*

Alice Gould es ingresada en un sanatorio mental. En su delirio, cree ser una investigadora privada a cargo de un equipo de detectives dedicados a esclarecer complicados casos. Según una carta de su médico particular, …

<details><summary>Sinopsis completa</summary>

Alice Gould es ingresada en un sanatorio mental. En su delirio, cree ser una investigadora privada a cargo de un equipo de detectives dedicados a esclarecer complicados casos. Según una carta de su médico particular, la realidad es otra: su paranoica obsesión es atentar contra la vida de su marido. La extrema inteligencia de esta mujer y su actitud aparentemente normal confundirán a los médicos hasta el punto de no saber a ciencia cierta si Alice ha sido ingresada injustamente o padece realmente un grave y peligroso trastorno psicológico.

</details>

### 146. Los siete maridos de Evelyn Hugo

**Taylor Jenkins Reid** · *Drama · Novela*

Evelyn Hugo, el ícono de Hollywood que se ha recluido en su edad madura, decide al fin contar la verdad sobre su vida llena de glamour y de escándalos. Pero cuando elige para ello a …

<details><summary>Sinopsis completa</summary>

Evelyn Hugo, el ícono de Hollywood que se ha recluido en su edad madura, decide al fin contar la verdad sobre su vida llena de glamour y de escándalos. Pero cuando elige para ello a Monique Grant, una periodista desconocida, nadie se sorprende más que la misma Monique. ¿Por qué ella? ¿Por qué ahora? Monique no está precisamente en su mejor momento. Su marido la abandonó, y su vida profesional no avanza. Aun ignorando por qué Evelyn la ha elegido para escribir su biografía, Monique está decidida a aprovechar esa oportunidad para dar impulso a su carrera. Convocada al lujoso apartamento de Evelyn, Monique escucha fascinada mientras la actriz le cuenta su historia. Desde su llegada a Los Ángeles en los años 50 hasta su decisión de abandonar su carrera en el espectáculo en los 80 —y, desde luego, los siete maridos que tuvo en ese tiempo—. Evelyn narra una historia de ambición implacable, amistad inesperada y un gran amor prohibido. Monique empieza a sentir una conexión muy real con la actriz legendaria, pero cuando el relato de Evelyn se acerca a su fin, resulta evidente que su vida se cruza con la de Monique de un modo trágico e irreversible.

</details>

### 147. Maze Runner: Correr o morir

**James Dashner** · *Fantástico · Juvenil · Novela* · Serie: Maze Runner, tomo 1

Al despertar dentro de un oscuro elevador en movimiento, lo único que Thomas logra recordar es su nombre. No sabe quién es. Tampoco hacia dónde va. Pero no está solo: cuando la caja llega a …

<details><summary>Sinopsis completa</summary>

Al despertar dentro de un oscuro elevador en movimiento, lo único que Thomas logra recordar es su nombre. No sabe quién es. Tampoco hacia dónde va. Pero no está solo: cuando la caja llega a su destino, las puertas se abren y se ve rodeado por un grupo de jóvenes. «Bienvenido al Área, Novicio». El Área. Un espacio abierto cercado por muros gigantescos. Al igual que Thomas, ninguno de ellos sabe cómo ha llegado allí. Ni por qué. De lo que están seguros es de que cada mañana las puertas de piedra del laberinto que los rodea se abren y por la noche, se cierran. Y que cada treinta días alguien nuevo es entregado por el elevador. Un hecho altera de forma radical la rutina del lugar: llega una chica, la primera enviada al Área. Y más sorprendente todavía es el mensaje que trae. Thomas será más importante de lo que imagina. Pero para eso deberá descubrir los sombríos secretos guardados en su mente. Por alguna razón, sabe que para lograrlo debe correr. Correr será la clave. O morirá. James Dashner ha urdido un apasionante thriller psicológico y de acción. «Correr o morir» es el primer título de una trilogía que atrapará sin concesiones al lector. Porque cada salida puede convertirse en el pasaje a una verdadera pesadilla…

</details>

### 148. Memorias de una geisha

**Arthur Golden** · *Drama*

En esta maravillosa novela escuchamos las confesiones de Sayuri, una de las más hermosas geishas del Japón de entreguerras, un país en el que aún resonaban los ecos feudales y donde las tradiciones ancestrales empezaban …

<details><summary>Sinopsis completa</summary>

En esta maravillosa novela escuchamos las confesiones de Sayuri, una de las más hermosas geishas del Japón de entreguerras, un país en el que aún resonaban los ecos feudales y donde las tradiciones ancestrales empezaban a convivir con los modos occidentales. De la mano de Sayuri entraremos en un mundo secreto dominado por las pasiones y sostenido por las apariencias, donde sensualidad y belleza no pueden separarse de la degradación y el sometimiento: un mundo en el que las jóvenes aspirantes a geishas son duramente adiestradas en el arte de la seducción, en el que su virginidad se venderá al mejor postor y donde tendrán que convencerse de que, para ellas, el amor no es más que un espejismo.

</details>

### 149. Mi Lucha

**Adolf Hitler** · *Biografía · Histórico*

¿Qué sabe usted de Adolf Hitler y sus ideas? En realidad, cuando se habla de Hitler se hace siempre a partir de lo que sobre él se ha escrito tras la II Guerra Mundial. Prácticamente …

<details><summary>Sinopsis completa</summary>

¿Qué sabe usted de Adolf Hitler y sus ideas? En realidad, cuando se habla de Hitler se hace siempre a partir de lo que sobre él se ha escrito tras la II Guerra Mundial. Prácticamente nadie sabe lo que pensaba realmente el hombre más discutido de nuestra época. Al iniciarse el Siglo XXI ha llegado el momento de recurrir a los documentos originales y juzgar con información de primera mano el pensamiento político y social de este personaje histórico. Sus vencedores le siguen profesando un odio feroz. Y hoy, más de medio siglo después de su muerte, sigue siendo difícil encontrar publicaciones sobre Hitler y su época que no partan de la demonización sin matice. El libro perfila las ideas principales que el líder nacional-socialista alemán llevaría a término durante los seis años anteriores a la Segunda Guerra Mundial. Es de destacar su clara denuncia del lobby judío internacional. Hitler demostraba la tesis de una presunta conspiración judía para conquistar el liderazgo mundial. También explica muchos detalles autobiográficos de la niñez de Hitler, especialmente durante sus años en Viena. Otra parte importante del libro destaca la importancia de la identidad étnica y de cierta homogeneidad racial para que una sociedad se mantenga estable y conserve su energía creativa. El libro supone igualmente una crítica demoledora al sistema partitocrático parlamentario. Esta obra puede considerarse como uno de los libros más relevantes de la historia por haber sido totalmente ignorado. Introduzcámonos en su pensamiento mediante su propia autobiografía, escrita entre 1923 y 1924 cuando se encontraba en la prisión de Landsberg, y donde proponía reformas económicas, políticas y sociales que generarían el gran éxito del Nacional-Socialismo a partir de su llegada al poder en 1933.

</details>

### 150. Mi lucha. La historia del libro que marcó el siglo XX

**Sven Felix Kellerhoff** · *Ensayo · Historia*

Tras setenta años de prohibición, se publica en Alemania Mi lucha (Mein Kampf), en el que Hitler mezcló su autobiografía imaginaria y su programa. Sven Felix Kellerhoff, historiador y periodista, nos ofrece con este libro …

<details><summary>Sinopsis completa</summary>

Tras setenta años de prohibición, se publica en Alemania Mi lucha (Mein Kampf), en el que Hitler mezcló su autobiografía imaginaria y su programa. Sven Felix Kellerhoff, historiador y periodista, nos ofrece con este libro un estudio ampliamente documentado sobre una obra que ha marcado la historia del siglo XX. Kellerhoff nos cuenta que se escribió en la cárcel de Landsberg, nos descubre cómo Hitler falsificó en él su vida, analiza las ideas que expuso y desvela su procedencia. Sigue después el proceso por el que el libro, que fue un fracaso de ventas en los primeros años, se convirtió en un negocio (hasta 1945 se imprimieron unos doce millones de ejemplares) que hizo al Führer millonario, a costa de evadir los impuestos, y explica la forma en que sus ideas se aplicaron en la política del régimen nazi. Una referencia indispensable para el conocimiento de Hitler y del nazismo.

</details>

### 151. Misery

**Stephen King** · *Terror*

Paul Sheldon es un escritor que sufre un grave accidente y recobra el conocimiento en una apartada casa en la que vive una misteriosa mujer, corpulenta y de extraño carácter. Se trata de una antigua …

<details><summary>Sinopsis completa</summary>

Paul Sheldon es un escritor que sufre un grave accidente y recobra el conocimiento en una apartada casa en la que vive una misteriosa mujer, corpulenta y de extraño carácter. Se trata de una antigua enfermera, involucrada en varias muertes misteriosas ocurridas en diversos hospitales. Fanática de un personaje de una serie de libros que él ha decidido deja de escribir, está dispuesto a hacer todo lo necesario para "convencerlo" de que retome la escritura. Esta mujer es capaz de los mayores horrores, y Paul, con las piernas rotas y entre terribles dolores, tendrá que luchar por su vida. Un relato obsesivo y aterrador, que solo Stephen King podía ofrecernos.

</details>

### 152. Momo

**Michael Ende** · *Fantástico · Infantil y juvenil*

Momo es una niña con un don muy especial: sólo con escuchar consigue que todos se sientan mejor. Pero pronto la llegada de los hombres grises va a cambiar su vida. Prometen que ahorrar tiempo …

<details><summary>Sinopsis completa</summary>

Momo es una niña con un don muy especial: sólo con escuchar consigue que todos se sientan mejor. Pero pronto la llegada de los hombres grises va a cambiar su vida. Prometen que ahorrar tiempo es lo mejor que se puede hacer, y poco a poco nadie tiene tiempo ni para jugar con los niños. Momo es la única que no se deja engañar, y con la ayuda de la tortuga Casiopea y del maestro Hora emprenderá una aventura fantástica contra los ladrones de tiempo. Una novela única con la que redescubrir la importancia de la amistad, la bondad y el valor de las cosas sencillas. En definitiva, sobre lo que de verdad nos hace felices.

</details>

### 153. Muchas vidas, muchos maestros

**Brian Weiss** · *Autoayuda · Esoterismo*

El doctor Brian Weiss, jefe de psiquiatría del hospital Mount Sinai de Miami, relata en éste, su primer libro, una asombrosa experiencia que cambió por completo su propia vida y su visión de la psicoterapia. …

<details><summary>Sinopsis completa</summary>

El doctor Brian Weiss, jefe de psiquiatría del hospital Mount Sinai de Miami, relata en éste, su primer libro, una asombrosa experiencia que cambió por completo su propia vida y su visión de la psicoterapia. Una de sus pacientes, Catherine, recordó bajo hipnosis varias de sus vidas pasadas y pudo encontrar en ellas el origen de muchos, de los traumas que sufría: Catherine su curó, pero ocurrió algo todavía más importante: logró ponerse en contacto con los Maestros, espíritus superiores que habitan los estados entre dos vidas. Ellos le comunicaron importantes mensajes de sabiduría y de conocimiento. Este relato, profundamente conmovedor, punto de encuentro entre ciencia y metafísica, constituyó un extraordinario best-séller y sigue siendo de obligada lectura en un mundo convulsionado, en especial para los que buscan un nuevo sentido espiritual.

</details>

### 154. No culpes al karma de lo que te pasa por gilipollas

**Laura Norton** · *Humor · Novela* · Serie: Karma, tomo 1

Si estás leyendo estas líneas es que te ha llamado la atención el título. ¿Te gustaría decírselo a alguien?¿Serías capaz de decírtelo a ti mismo? Y lo más importante: ¿te gustaría mantener durante un buen …

<details><summary>Sinopsis completa</summary>

Si estás leyendo estas líneas es que te ha llamado la atención el título. ¿Te gustaría decírselo a alguien?¿Serías capaz de decírtelo a ti mismo? Y lo más importante: ¿te gustaría mantener durante un buen rato la sonrisa que se te ha quedado en la cara? Pues esta es tu novela. Te podríamos contar con más o menos gracia de qué va la cosa, para que te hicieras una idea: que si la protagonista, Sara, es muy maja, que si tiene un trabajo muy interesante (es plumista, ¿a que nunca lo habías oído?), que si es un pelín obsesiva y alérgica a los sobresaltos... Por supuesto, la vida se le complica y se encuentra con que su piso se convierte en una especie de camarote de los hermanos Marx cuando en la misma semana se meten a vivir con ella su padre deprimido, su hermana rebelde y su excéntrico prometido y, sobre todo, el novio al que lleva mucho tiempo sin ver... Pero mejor no te lo contamos porque te gustará leerlo. Lo único que necesitas saber es que, desde el título, te garantizamos unas cuantas horas de descacharrante diversión como hacía tiempo que no disfrutabas.

</details>

### 155. No soy un serial killer

**Dan Wells** · *Intriga · Terror* · Serie: John Wayne Cleaver, tomo 1

John Wayne Cleaver tiene 15 años y sabe que es diferente. Pero no porque sólo tenga un amigo ni porque ayude a su madre en el depósito de cadáveres. John es un sociópata que reconoce …

<details><summary>Sinopsis completa</summary>

John Wayne Cleaver tiene 15 años y sabe que es diferente. Pero no porque sólo tenga un amigo ni porque ayude a su madre en el depósito de cadáveres. John es un sociópata que reconoce en sí mismo los clásicos signos de ser un incipiente asesino en serie. Para no hacer daño a nadie, John se ha creado un conjunto rígido de reglas para controlar su naturaleza más oscura y tener una vida normal. Pero cuando empiezan a haber una cadena de horripilantes asesinatos en su ciudad, John utilizará sus conocimientos sobre los asesinos en serie para investigar quién tiene aterrorizado el vecindario. Sus pesquisas le llevarán a descubrir el asesino: su vecino. Éste no sigue el patrón de un asesino en serie porque es un ser sobrenatural que mata porque necesita órganos de otros seres para seguir viviendo. Entonces John decide que si quiere pararlo, tendrá que romper con sus propias reglas y convertirse en asesino también.

</details>

### 156. No tengo boca y debo gritar

**Harlan Ellison** · *Ciencia ficción · Relato*

Un ordenador militar (AM, tomado de I think, therefore I AM, en inglés pienso, luego existo) toma consciencia de sí mismo y decide acabar con la raza humana mediante un holocausto nuclear, rescatando únicamente a …

<details><summary>Sinopsis completa</summary>

Un ordenador militar (AM, tomado de I think, therefore I AM, en inglés pienso, luego existo) toma consciencia de sí mismo y decide acabar con la raza humana mediante un holocausto nuclear, rescatando únicamente a cinco personas.

</details>

### 157. Noches Blancas (Ilustrado)

**Fiódor Mijáilovich Dostoyevski** · *Realista · Relato*

San Petersburgo, su luz, sus casas y sus avenidas son el escenario de esta apasionada novela. En una de esas «noches blancas» que se dan en la ciudad rusa durante la época del solsticio de …

<details><summary>Sinopsis completa</summary>

San Petersburgo, su luz, sus casas y sus avenidas son el escenario de esta apasionada novela. En una de esas «noches blancas» que se dan en la ciudad rusa durante la época del solsticio de verano, un joven solitario e introvertido narra cómo conoce de forma accidental a una muchacha a la orilla del canal. Tras el primer encuentro, la pareja de desconocidos se citará las tres noches siguientes, noches en las que ella, de nombre Nástenka, relatará su triste historia y en las que harán acto de presencia, de forma sutil y envolvente, las grandes pasiones que mueven al ser humano: el amor, la ilusión, la esperanza, el desamor, el desengaño.

</details>

### 158. Nuestra parte de noche

**Mariana Enríquez** · *Novela · Terror*

Un padre y un hijo atraviesan Argentina por carretera, desde Buenos Aires hacia las cataratas de Iguazú, en la frontera norte con Brasil. Son los años de la junta militar, hay controles de soldados armados …

<details><summary>Sinopsis completa</summary>

Un padre y un hijo atraviesan Argentina por carretera, desde Buenos Aires hacia las cataratas de Iguazú, en la frontera norte con Brasil. Son los años de la junta militar, hay controles de soldados armados y tensión en el ambiente. El hijo se llama Gaspar y el padre trata de protegerlo del destino que le ha sido asignado. La madre murió en circunstancias poco claras, en un accidente que acaso no lo fue. Como su padre, Gaspar está llamado a ser un médium en una sociedad secreta, la Orden, que contacta con la Oscuridad en busca de la vida eterna mediante atroces rituales. En ellos es vital disponer de un médium, pero el destino de estos seres dotados de poderes especiales es cruel, porque su desgaste físico y mental es rápido e implacable. Los orígenes de la Orden, regida por la poderosa familia de la madre de Gaspar, se remontan a siglos atrás, cuando el conocimiento de la Oscuridad llegó desde el corazón de África a Inglaterra y desde allí se extendió hasta Argentina.

</details>

### 159. Origen

**Dan Brown** · *Aventuras · Intriga* · Serie: Robert Langdon, tomo 5

Robert Langdon, profesor de simbología e iconografía religiosa de la universidad de Harvard, acude al Museo Guggenheim Bilbao para asistir a un trascendental anuncio que «cambiará la faz de la ciencia para siempre». El anfitrión …

<details><summary>Sinopsis completa</summary>

Robert Langdon, profesor de simbología e iconografía religiosa de la universidad de Harvard, acude al Museo Guggenheim Bilbao para asistir a un trascendental anuncio que «cambiará la faz de la ciencia para siempre». El anfitrión de la velada es Edmond Kirsch, un joven multimillonario cuyos visionarios inventos tecnológicos y audaces predicciones lo han convertido en una figura de renombre mundial. Kirsch, uno de los alumnos más brillantes de Langdon años atrás, se dispone a revelar un extraordinario descubrimiento que dará respuesta a las dos preguntas que han obsesionado a la humanidad desde el principio de los tiempos. ¿DE DÓNDE VENIMOS? ¿ADÓNDE VAMOS? Al poco tiempo de comenzar la presentación, meticulosamente orquestada por Edmond Kirsch y la directora del museo Ambra Vidal, estalla el caos para asombro de cientos de invitados y millones de espectadores en todo el mundo. Ante la inminente amenaza de que el valioso hallazgo se pierda para siempre, Langdon y Ambra deben huir desesperadamente a Barcelona e iniciar una carrera contrarreloj para localizar la críptica contraseña que les dará acceso al revolucionario secreto de Kirsch. Perseguidos por un atormentado y peligroso enemigo, Langdon y Ambra descubrirán los episodios más oscuros de la Historia y del extremismo religioso. Siguiendo un rastro de pistas compuesto por obras de arte moderno y enigmáticos símbolos, tendrán pocas horas para intentar desvelar la fascinante investigación de Kirsch… y su sobrecogedora revelación sobre el origen y el destino de la Humanidad. ORIGEN se desarrolla íntegramente en España. Barcelona, Bilbao, Madrid y Sevilla son los escenarios principales en los que transcurre la nueva aventura de Robert Langdon. De la mano del autor de El código Da Vinci, el lector recorrerá escenarios como el Monasterio de Montserrat, la Casa Milà (La Pedrera), la Sagrada Familia, el Museo Guggenheim Bilbao, el Palacio Real o la Catedral de Sevilla. Como ya sucedió con París en El código Da Vinci, con Roma en Ángeles y demonios o con Florencia en Inferno, los escenarios de las novelas de Dan Brown siempre han sido un elemento clave en sus tramas.

</details>

### 160. Palabras radiantes

**Brandon Sanderson** · *Fantástico · Novela* · Serie: El archivo de las tormentas, tomo 2

Palabras radiantes es la continuación de El camino de los reyes, la aclamada primera parte de la serie en diez volúmenes The Stormlight Archive. En ella retrocedemos seis años en el tiempo, cuando un asesino, …

<details><summary>Sinopsis completa</summary>

Palabras radiantes es la continuación de El camino de los reyes, la aclamada primera parte de la serie en diez volúmenes The Stormlight Archive. En ella retrocedemos seis años en el tiempo, cuando un asesino, entre cuyos primeros objetivos se halla Dalinar, mata al rey alezi. Kaladin está al mando de los guardaespaldas reales, un puesto controvertido por su baja condición, y debe proteger al rey y a Dalinar, al tiempo que dominar, en secreto, los nuevos y extraordinarios poderes vinculados a sus honorspren. Shallan tiene la misión de impedir el fin de las Desolaciones. Las Llanuras Quebradas tienen la respuesta; en ellas los parshendi están convencidos, gracias a su líder, de arriesgarlo todo en una apuesta desesperada...

</details>

### 161. Palmeras en la nieve

**Luz Gabás** · *Relato*

Es 1953 y Kilian abandona la nieve de la montaña oscense para iniciar, junto a su hermano Jacobo, el viaje hacia una tierra desconocida, lejana y exótica, la isla de Fernando Poo. En las entrañas …

<details><summary>Sinopsis completa</summary>

Es 1953 y Kilian abandona la nieve de la montaña oscense para iniciar, junto a su hermano Jacobo, el viaje hacia una tierra desconocida, lejana y exótica, la isla de Fernando Poo. En las entrañas de esa isla exuberante y seductora, le espera su padre, un veterano de la finca Sampaka, el lugar donde se cultiva y tuesta uno de los mejores cacaos del mundo. En esa tierra eternamente verde, cálida y voluptuosa, los jóvenes hermanos descubren la ligereza de la vida social de la colonia en comparación con una España encorsetada y gris; comparten el duro trabajo necesario para conseguir el cacao perfecto de la finca Sampaka; aprenden las diferencias y similitudes culturales entre coloniales y nativos; y conocen el significado de la amistad, la pasión, el amor y el odio. Pero uno de ellos cruzará una línea prohibida e invisible y se enamorará perdidamente de una mujer. Su amor por ella, enmarcado en unas complejas circunstancias históricas, y el especial vínculo que se crea entre el colono y los nativos de la isla, transformará la relación de los hermanos, cambiará el curso de sus vidas y será el origen de un secreto cuyas consecuencias alcanzarán al presente. En el año 2003, Clarence, hija y sobrina de ese par de hermanos, llevada por la curiosidad de quien desea conocer sus orígenes, se zambulle en el ruinoso pasado que habitaron Kilian y Jacobo y descubre los hilos polvorientos de ese secreto que finalmente será desentrañado. Una excelente novela que recupera nuestras raíces coloniales y una extraordinaria y conmovedora historia de amor prohibido con resonancias a Memorias de África.

</details>

### 162. Parque Jurásico

**Michael Crichton** · *Aventuras · Ciencia ficción* · Serie: Parque jurásico, tomo 1

En esta espectacular novela, los dinosaurios vuelven a conquistar la Tierra. En una isla remota, un grupo de hombres y mujeres emprende una carrera contra el tiempo para evitar un desastre mundial provocado por la …

<details><summary>Sinopsis completa</summary>

En esta espectacular novela, los dinosaurios vuelven a conquistar la Tierra. En una isla remota, un grupo de hombres y mujeres emprende una carrera contra el tiempo para evitar un desastre mundial provocado por la desmedida ambición de comercializar la ingeniería genética. Pero todos los esfuerzos resultarán vanos cuando el inescrupuloso proyecto quede fuera de control y el mundo a merced de unas bestias monstruosas… 'Parque Jurásico', la novela más célebre de Michael Crichton y una de las más leídas en los últimos años, fue adaptada al cine por Steven Spielberg en una película que se convirtió en el gran acontecimiento cinematográfico de 1993 y en el origen del fenómeno de masas llamado «dinomanía».

</details>

### 163. Patria

**Fernando Aramburu** · *Drama · Novela · Realista*

El retablo definitivo sobre más de 30 años de la vida en Euskadi bajo el terrorismo. El día en que ETA anuncia el abandono de las armas, Bittori se dirige al cementerio para contarle a …

<details><summary>Sinopsis completa</summary>

El retablo definitivo sobre más de 30 años de la vida en Euskadi bajo el terrorismo. El día en que ETA anuncia el abandono de las armas, Bittori se dirige al cementerio para contarle a la tumba de su marido el Txato, asesinado por los terroristas, que ha decidido volver a la casa donde vivieron. ¿Podrá convivir con quienes la acosaron antes y después del atentado que trastocó su vida y la de su familia? ¿Podrá saber quién fue el encapuchado que un día lluvioso mató a su marido, cuando volvía de su empresa de transportes? Por más que llegue a escondidas, la presencia de Bittori alterará la falsa tranquilidad del pueblo, sobre todo de su vecina Miren, amiga íntima en otro tiempo, y madre de Joxe Mari, un terrorista encarcelado y sospechoso de los peores temores de Bittori. ¿Qué pasó entre esas dos mujeres? ¿Qué ha envenenado la vida de sus hijos y sus maridos tan unidos en el pasado? Con sus desgarros disimulados y sus convicciones inquebrantables, con sus heridas y sus valentías, la historia incandescente de sus vidas antes y después del cráter que fue la muerte del Txato, nos habla de la imposibilidad de olvidar y de la necesidad de perdón en una comunidad rota por el fanatismo político.

</details>

### 164. PD. Todavía te quiero

**Jenny Han** · *Juvenil · Novela · Romántico* · Serie: A todos los chicos de los que me enamoré, tomo 2

Lara Jean no esperaba enamorarse. Mucho menos enamorarse en serio de Peter. Al principio era una fantasía. Pero de pronto, ya no es sólo eso, y ahora Lara Jean está muy confundida. Otro chico del …

<details><summary>Sinopsis completa</summary>

Lara Jean no esperaba enamorarse. Mucho menos enamorarse en serio de Peter. Al principio era una fantasía. Pero de pronto, ya no es sólo eso, y ahora Lara Jean está muy confundida. Otro chico del pasado vuelve a su vida y lo que sentía por él también resurge. ¿Puede una chica estar enamorada de dos chicos a la vez?

</details>

### 165. Pinochet

**Mario Spataro** · *Ensayo · Historia · Memorias*

Así comentó el diario Corriere de Roma la aparición de este libro: «Por primera vez en Europa un escritor ha tenido el coraje de disociarse de la fábula del “Buen Allende” y el “Malvado Pinochet”». …

<details><summary>Sinopsis completa</summary>

Así comentó el diario Corriere de Roma la aparición de este libro: «Por primera vez en Europa un escritor ha tenido el coraje de disociarse de la fábula del “Buen Allende” y el “Malvado Pinochet”». Spataro fue un escritor prolífico pero enormemente sólido: la investigación que respalda sus afirmaciones es sencillamente abrumadora. Documentos, libros, periódicos, revistas, sitios de Internet, figuran entre sus fuentes, ordenadamente citadas al pie de página. Consciente de que sus temas eran polémicos, consultaba por igual las opiniones adictas o contrarias a la suya. A pesar de que lo polémico del tema exigía al escritor esta prolijidad, Pinochet: Las «incómodas» verdades es un libro muy ameno. Spataro tiene el profesionalismo de los grandes periodistas y la viveza de su relato lleva en vilo al lector.

</details>

### 166. Prohibido

**Tabitha Suzuma** · *Novela · Romántico*

No podemos. Si empezamos, ¿cómo vamos a pararlo? Lochan y Maya siempre se han sentido más amigos que hermanos. Ante la incapacidad de cuidarlos de su madre alcohólica y la ausencia de un padre que …

<details><summary>Sinopsis completa</summary>

No podemos. Si empezamos, ¿cómo vamos a pararlo? Lochan y Maya siempre se han sentido más amigos que hermanos. Ante la incapacidad de cuidarlos de su madre alcohólica y la ausencia de un padre que los abandonó, los dos jóvenes deben hacerse cargo de sus tres hermanos menores y esconder su situación a los servicios sociales, porque ninguno de los dos es mayor de edad. La responsabilidad que comparten y las dificultades a las que se enfrentan les unen, hasta empujarlos a enamorarse. Ambos saben que su relación está mal y que no debe continuar, pero al mismo tiempo no pueden controlar sus emociones y la atracción que los domina.

</details>

### 167. Ready Player One

**Ernest Cline** · *Ciencia ficción*

Estamos en el año 2044 y, como el resto de la humanidad, Wade Watts prefiere mil veces el videojuego de OASIS al cada vez más sombrío mundo real. Se afirma que esconde las piezas de …

<details><summary>Sinopsis completa</summary>

Estamos en el año 2044 y, como el resto de la humanidad, Wade Watts prefiere mil veces el videojuego de OASIS al cada vez más sombrío mundo real. Se afirma que esconde las piezas de un rompecabezas diabólico cuya resolución conduce a una fortuna incalculable. Durante años, millones de humanos han intentado dar con ellas, sin éxito. De repente, Wade logra resolver el primer rompecabezas del premio, y a partir de ese momento debe competir contra miles de jugadores para conseguir el trofeo. La única forma de sobrevivir es ganar. ‘Ready Player One’, el impresionante debut de Ernest Cline, está revolucionando la literatura de género en Estados Unidos. Antes incluso de su publicación, convenció a la Warner Bros., de convertirlo en su próxima gran producción, a agentes y editores de medio mundo de que compraran sus derechos, y cautivó a autores de la talla de Charlaine Harris y Patrick Rothfuss, a quien, según ha confesado, le pareció un libro escrito por él mismo. Desde entonces, esta novela ha seducido a la crítica y ha alcanzado las listas de más vendidos del New York Times y Amazon.

</details>

### 168. Rebelión en la granja

**George Orwell** · *Aventuras · Clásico · Drama*

Una condena de la sociedad totalitaria, brillantemente plasmada en una ingeniosa fábula de carácter alegórico. Los animales de la granja de los Jones se sublevan contra sus dueños humanos y les vencen. Pero la rebelión …

<details><summary>Sinopsis completa</summary>

Una condena de la sociedad totalitaria, brillantemente plasmada en una ingeniosa fábula de carácter alegórico. Los animales de la granja de los Jones se sublevan contra sus dueños humanos y les vencen. Pero la rebelión fracasará al surgir entre ellos rivalidades y envidias, y al aliarse algunos con los amos que derrocaron, traicionando su propia identidad y los intereses de su clase. Aunque Rebelión en la granja fue concebida como una despiadada sátira del estalinismo, el carácter universal de su mensaje hace de este libro un extraordinario análisis de la corrupción que engendra el poder, una furibunda diatriba contra el totalitarismo de cualquier especie y un lúcido examen de las manipulaciones que sufre la verdad histórica en los momentos de transformación política.

</details>

### 169. Rebelión en la granja (trad. Marcial Souto y Miguel Temprano García)

**George Orwell** · *Novela · Sátira*

Un rotundo alegato a favor de la libertad y en contra del totalitarismo que se ha convertido en un clásico de la literatura del siglo XX. Esta sátira de la Revolución rusa y el triunfo …

<details><summary>Sinopsis completa</summary>

Un rotundo alegato a favor de la libertad y en contra del totalitarismo que se ha convertido en un clásico de la literatura del siglo XX. Esta sátira de la Revolución rusa y el triunfo del estalinismo, escrita en 1945, se ha convertido por derecho propio en un hito de la cultura contemporánea y en uno de los libros más mordaces de todos los tiempos. Ante el auge de los animales de la Granja Solariega, pronto detectamos las semillas del totalitarismo en una organización aparentemente ideal; y en nuestros líderes más carismáticos, la sombra de los opresores más crueles. «Una obra literaria perfecta.» T.S. Eliot Epílogo de Christopher Hitchens.

</details>

### 170. Reina roja

**Juan Gómez-Jurado** · *Intriga · Novela · Policíaco* · Serie: Antonia Scott & Jon Gutiérrez, tomo 1

NO HAS CONOCIDO A NADIE COMO ELLA Antonia Scott es especial. Muy especial. No es policía ni criminalista. Nunca ha empuñado un arma ni llevado una placa, y, sin embargo, ha resuelto decenas de crímenes. …

<details><summary>Sinopsis completa</summary>

NO HAS CONOCIDO A NADIE COMO ELLA Antonia Scott es especial. Muy especial. No es policía ni criminalista. Nunca ha empuñado un arma ni llevado una placa, y, sin embargo, ha resuelto decenas de crímenes. Pero hace un tiempo que Antonia no sale de su ático de Lavapiés. Las cosas que ha perdido le importan mucho más que las que esperan ahí fuera. Tampoco recibe visitas. Por eso no le gusta nada, nada, cuando escucha unos pasos desconocidos subiendo las escaleras hasta el último piso. Sea quien sea, Antonia está segura de que viene a buscarla. Y eso le gusta aún menos.

</details>

### 171. Relatos

**Carlos Ruiz Zafón** · *Otros · Relato*

Recopilación de relatos de Carlos Ruiz Zafón. Todos estos relatos se pueden encontrar en la web del autor, salvo "Rosa de fuego" que salió publicado en la prensa española. - Rosa de fuego - Alicia, …

<details><summary>Sinopsis completa</summary>

Recopilación de relatos de Carlos Ruiz Zafón. Todos estos relatos se pueden encontrar en la web del autor, salvo "Rosa de fuego" que salió publicado en la prensa española. - Rosa de fuego - Alicia, al Alba - Gaudí en Manhatan - Inferno - La Mujer de Vapor

</details>

### 172. Romper el círculo

**Colleen Hoover** · *Novela · Realista* · Serie: Romper el círculo, tomo 1

A veces, quien más te quiere es quién más daño te hace. Lily no siempre lo ha tenido fácil. Por eso, su idílica relación con un magnífico neurocirujano llamado Ryle Kincaid, parece demasiado buena para …

<details><summary>Sinopsis completa</summary>

A veces, quien más te quiere es quién más daño te hace. Lily no siempre lo ha tenido fácil. Por eso, su idílica relación con un magnífico neurocirujano llamado Ryle Kincaid, parece demasiado buena para ser verdad. Cuando Atlas, su primer amor, reaparece repentinamente y Ryle comienza a mostrar su verdadera cara, todo lo que Lily ha construido con él se ve amenazado.

</details>

### 173. Sapiens

**Yuval Noah Harari** · *Ciencias naturales · Ensayo · Historia*

Hace 100.000 años al menos seis especies de humanos habitaban la Tierra. Hoy solo queda una, la nuestra: Homo sapiens. ¿Cómo logró nuestra especie imponerse en la lucha por la existencia? ¿Por qué nuestros ancestros …

<details><summary>Sinopsis completa</summary>

Hace 100.000 años al menos seis especies de humanos habitaban la Tierra. Hoy solo queda una, la nuestra: Homo sapiens. ¿Cómo logró nuestra especie imponerse en la lucha por la existencia? ¿Por qué nuestros ancestros recolectores se unieron para crear ciudades y reinos? ¿Cómo llegamos a creer en dioses, en naciones o en los derechos humanos; a confiar en el dinero, en los libros o en las leyes? ¿Cómo acabamos sometidos a la burocracia, a los horarios y al consumismo? ¿Y cómo será el mundo en los milenios venideros? En De animales a dioses Yuval Noah Harari traza una breve historia de la humanidad, desde los primeros humanos que caminaron sobre la Tierra hasta los radicales y a veces devastadores avances de las tres grandes revoluciones que nuestra especie ha protagonizado: la cognitiva, la agrícola y la científica. A partir de hallazgos de disciplinas tan diversas como la biología, la antropología, la paleontología o la economía, Harari explora cómo las grandes corrientes de la historia han modelado nuestra sociedad, los animales y las plantas que nos rodean e incluso nuestras personalidades. ¿Hemos ganado en felicidad a medida que ha avanzado la historia? ¿Seremos capaces de liberar alguna vez nuestra conducta de la herencia del pasado? ¿Podemos hacer algo para influir en los siglos futuros? Audaz, ambicioso y provocador, este libro cuestiona todo lo que creíamos saber sobre el ser humano: nuestros orígenes, nuestras ideas, nuestras acciones, nuestro poder... y nuestro futuro.

</details>

### 174. Sinceramente

**Cristina Fernández de Kirchner** · *Ciencias sociales · Ensayo · Memorias*

Del amanecer sin dolor el día después de dejar la Presidencia a la compleja toma de decisiones políticas, económicas y sociales durante doce años que cambiaron la vida de millones de argentinos. Del estado en …

<details><summary>Sinopsis completa</summary>

Del amanecer sin dolor el día después de dejar la Presidencia a la compleja toma de decisiones políticas, económicas y sociales durante doce años que cambiaron la vida de millones de argentinos. Del estado en que recibió la Casa Rosada a la estatización de las AFJP. De la muerte de Nisman al entramado que une a agentes, jueces y fiscales de la causa AMIA con los fondos buitre. Del malentendido que mantuvo alejados a su marido y a Jorge Bergoglio a los elocuentes detalles que revelan el origen de la hoy famosa carta de San Martín a O'Higgins confiscada por el juez Bonadio. De las decisiones consensuadas con Lula a cómo Chávez acortaba los discursos para no aburrir a Néstor. Del origen de su patrimonio a las conversaciones con Magnetto y las causas judiciales en su contra. De manera tan esperada como inesperada, Cristina Fernández de Kirchner presenta Sinceramente , un recorrido íntimo por circunstancias y momentos de su vida, de la del país y de los años del gobierno más discutido y celebrado de la reciente democracia argentina. «Hicieron y siguen haciendo todo lo posible para destruirme. Creyeron que terminarían abatiéndome. Es claro que no me conocen. Por eso les ofrezco una mirada y una reflexión retrospectivas para desentrañar algunos hechos y capítulos de la historia reciente. Hoy que el país está en completo retroceso político, económico, social y cultural espero que al leer estas páginas podamos pensar y discutir sin odio, sin mentiras y sin agravios. Estoy convencida de que es el único camino para volver a tener sueños, una vida mejor y un país que nos cobije a todos y todas.»

</details>

### 175. Sinsajo

**Suzanne Collins** · *Ciencia ficción · Juvenil* · Serie: Distritos, tomo 3

Katniss Everdeen, ha sobrevivido de nuevo a LOS JUEGOS, aunque no queda nada de su hogar. Gale ha escapado. Su familia está a salvo. El Capitolio ha capturado a Peeta. El Distrito 13 existe de …

<details><summary>Sinopsis completa</summary>

Katniss Everdeen, ha sobrevivido de nuevo a LOS JUEGOS, aunque no queda nada de su hogar. Gale ha escapado. Su familia está a salvo. El Capitolio ha capturado a Peeta. El Distrito 13 existe de verdad. Hay rebeldes. Hay nuevos líderes. Están en plena revolución. El plan de rescate para sacar a Katniss de la arena del cruel e inquietante Vasallaje de los Veinticinco no fue casual, como tampoco lo fue que llevara tiempo formando parte de la revolución sin saberlo. El Distrito 13 ha surgido de entre las sombras y quiere acabar con el Capitolio. Al parecer, todos han tenido algo que ver en el meticuloso plan..., todos menos Katniss.

</details>

### 176. Soy leyenda

**Richard Matheson** · *Ciencia ficción · Fantástico · Terror*

Robert Neville es el único superviviente de una guerra bacteriológica que ha asolado el planeta y convertido al resto de la humanidad en vampiros. Su vida se ha reducido a asesinar el máximo número posible …

<details><summary>Sinopsis completa</summary>

Robert Neville es el único superviviente de una guerra bacteriológica que ha asolado el planeta y convertido al resto de la humanidad en vampiros. Su vida se ha reducido a asesinar el máximo número posible de estos seres sanguinarios durante el día, y a soportar su asedio cada noche. Para ellos, el auténtico monstruo es este hombre que lucha por subsistir en un nuevo orden establecido. Todo un clásico en su género, éste es un perturbador relato sobre la soledad y el aislamiento y una reflexión sobre los binomios como normalidad y anormalidad, bien y mal, que se evidencian como una mera convención derivada del temor y el desconcierto ante lo diferente.

</details>

### 177. Sueños de piedra

**Iria G. Parente | Selene M. Pascual** · *Fantástico · Juvenil · Novela* · Serie: Marabilia, tomo 1

Érase una vez un reino muy muy lejano donde un príncipe premió a un mago por ayudar a rescatar a una joven en apuros. Encantador. Lástima que nada de esto sea verdad. En realidad, el …

<details><summary>Sinopsis completa</summary>

Érase una vez un reino muy muy lejano donde un príncipe premió a un mago por ayudar a rescatar a una joven en apuros. Encantador. Lástima que nada de esto sea verdad. En realidad, el príncipe sueña con gloria y venganza; el mago, con que sus hechizos no sean siempre un desastre y la joven en apuros, con huir de un pasado que la atormenta… y del recuerdo del hombre al que ha matado. Érase una vez…

</details>

### 178. Tal vez mañana

**Colleen Hoover** · *Juvenil · Novela* · Serie: Tal vez, tomo 1

A los veintidós años, Sydney lo tiene todo: el novio perfecto, un futuro brillante y un bonito apartamento que comparte con su mejor amiga. Pero todo cambia el día en que Ridge, su misterioso y …

<details><summary>Sinopsis completa</summary>

A los veintidós años, Sydney lo tiene todo: el novio perfecto, un futuro brillante y un bonito apartamento que comparte con su mejor amiga. Pero todo cambia el día en que Ridge, su misterioso y atractivo vecino músico, le advierte que su novio la engaña con su mejor amiga y Sydney debe decidir qué hacer con su vida. Sólo con lo puesto y sin recursos, Ridge la acoge en su casa y no deja de sorprenderla: es el líder y letrista de Sounds of Cedar , el grupo de moda, y es capaz de componer maravillosas melodías, a pesar de ser completamente sordo. Juntos empiezan a escribir letras para el grupo. Syd vibra cuando él toca sus hermosas melodías y, aunque el corazón de Ridge está ocupado, él no puede ignorar que ha encontrado a su musa. Cuando finalmente se den cuenta de que se necesitan, entenderán que los sentimientos no pueden traicionar al corazón.

</details>

### 179. Tan poca vida

**Hanya Yanagihara** · *Novela · Realista*

Para descubrir... Qué dicen y qué callan los hombres. De dónde viene y dónde va la culpa. Cuánto importa el sexo. A quien podemos llamar amigo. Y finalmente... Qué precio tiene la vida y cuándo …

<details><summary>Sinopsis completa</summary>

Para descubrir... Qué dicen y qué callan los hombres. De dónde viene y dónde va la culpa. Cuánto importa el sexo. A quien podemos llamar amigo. Y finalmente... Qué precio tiene la vida y cuándo deja de tener valor. Para descubrir eso y más, aquí está Tan poca vida , una historia que recorre más de tres décadas de amistad en la vida de cuatro hombres que crecen juntos en Manhattan. Cuatro hombres que tienen que sobrevivir al fracaso y al éxito y que, a lo largo de los años, aprenden a sobreponerse a las crisis económicas, sociales y emocionales. Cuatro hombres que comparten una idea muy peculiar de la intimidad, una manera de estar juntos hecha de pocas palabras y muchos gestos. Cuatro hombres cuya relación la autora utiliza para realizar una minuciosa indagación de los límites de la naturaleza humana.

</details>

### 180. Te doy mi corazón

**Julia Quinn** · *Histórico · Novela · Romántico* · Serie: Bridgerton, tomo 3

Como en el cuento de Cenicienta, Sophie ve una noche cumplirse su sueño. A espaldas de su madrastra, se viste como una reina y acude al baile de disfraces más importante de Londres. Lo que …

<details><summary>Sinopsis completa</summary>

Como en el cuento de Cenicienta, Sophie ve una noche cumplirse su sueño. A espaldas de su madrastra, se viste como una reina y acude al baile de disfraces más importante de Londres. Lo que es más, consigue captar la atención de Benedict Bridgerton, el soltero más atractivo y encantador de la reunión. Sin embargo, pronto vuelve a enfrentarse a su cruda realidad, la de una hija ilegítima, pobre y sin recursos. El destino quiere darle una segunda oportunidad cuando entra a servir en casa de Benedict, aunque él no reconoce en ella a la hermosa joven a la que lleva años buscando. Ella es ahora una simple criada, incapaz de revelarle la verdad. La magia de aquella noche parece perdida para siempre ¿o quizás no? De princesa radiante… Sophie vivió una infancia extraña. Todos sabían que era hija del conde de Penwood y, aunque este nunca la reconoció como tal, cuidó de que no le faltara nada. Todo cambió cuando su padre se casó de nuevo, y la madrastra y sus dos hijas hicieron de la vida de Sophie una pesadilla. Muerto el conde, su testamento las obligaba a cuidar de la niña, pero nunca la consideraron una igual. Y tampoco le permitirían nunca que se atreviera a competir con ellas por la atención de los muy cotizados solteros de la familia Bridgerton, tan atractivos como bien situados. Antes, la echarían a la calle donde, suponían, no tendría jamás una oportunidad de acercarse a ellos. … a criada en casa del príncipe. ¿Quién era esa mujer extraordinaria? Benedict no puede olvidar aquella belleza enmascarada que le hechizó en un instante, a la que solo conoce como la Dama Plateada por el color de su vestido y a quien, inconscientemente, le entregó su corazón. Pero ahora, años después, se siente poderosamente atraído por una sencilla criada a la que salva de un asaltante borracho. Ella es la única que le hace revivir la emoción que le produjo la misteriosa enmascarada. Pero también ella parece fuera de su alcance, a causa de las insalvables barreras de clase que los separan. Sin embargo, la familia Bridgerton tiene muchos recursos para ayudar a uno de los suyos cuando surgen problemas de amor…

</details>

### 181. Todas las hadas del reino

**Laura Gallego García** · *Fantástico · Juvenil · Novela* · Serie: Hadas Madrinas, tomo 1

Camelia es un hada madrina que lleva trescientos años ayudando con gran eficacia a jóvenes doncellas y aspirantes a héroe para que alcancen sus propios finales felices. Su magia y su ingenio nunca le han …

<details><summary>Sinopsis completa</summary>

Camelia es un hada madrina que lleva trescientos años ayudando con gran eficacia a jóvenes doncellas y aspirantes a héroe para que alcancen sus propios finales felices. Su magia y su ingenio nunca le han fallado, pero todo empieza a complicarse cuando le encomiendan a Simón, un mozo de cuadra que necesita su ayuda desesperadamente. Camelia ha solucionado casos más difíciles; pero, por algún motivo, con Simón las cosas comienzan a torcerse de forma inexplicable...

</details>

### 182. Todo esto te daré

**Dolores Redondo** · *Intriga · Novela*

En el escenario majestuoso de la Ribeira Sacra, Álvaro sufre un accidente que acabará con su vida. Cuando Manuel, su marido, llega a Galicia para reconocer el cadáver, descubre que la investigación sobre el caso …

<details><summary>Sinopsis completa</summary>

En el escenario majestuoso de la Ribeira Sacra, Álvaro sufre un accidente que acabará con su vida. Cuando Manuel, su marido, llega a Galicia para reconocer el cadáver, descubre que la investigación sobre el caso se ha cerrado con demasiada rapidez. El rechazo de su poderosa familia política, los Muñiz de Dávila, le impulsa a huir pero le retiene el alegato contra la impunidad que Nogueira, un guardia civil jubilado, esgrime contra la familia de Álvaro, nobles mecidos en sus privilegios, y la sospecha de que ésa no es la primera muerte de su entorno que se ha enmascarado como accidental. Lucas, un sacerdote amigo de la infancia de Álvaro, se une a Manuel y a Nogueira en la reconstrucción de la vida secreta de quien creían conocer bien. La inesperada amistad de estos tres hombres sin ninguna afinidad aparente ayuda a Manuel a navegar entre el amor por quien fue su marido y el tormento de haber vivido de espaldas a la realidad, blindado tras la quimera de su mundo de escritor. Empezará así la búsqueda de la verdad, en un lugar de fuertes creencias y arraigadas costumbres en el que la lógica nunca termina de atar todos los cabos.

</details>

### 183. Todo lo que nunca fuimos

**Alice Kellen** · *Novela · Romántico* · Serie: Deja que ocurra, tomo 1

Leah está rota. Leah ya no pinta. Leah es un espejismo desde el accidente que se llevó a sus padres. Axel es el mejor amigo de su hermano mayor y, cuando accede a acogerla en …

<details><summary>Sinopsis completa</summary>

Leah está rota. Leah ya no pinta. Leah es un espejismo desde el accidente que se llevó a sus padres. Axel es el mejor amigo de su hermano mayor y, cuando accede a acogerla en su casa durante unos meses, quiere ayudarla a encontrar y unir los pedazos de la chica llena de color que un día fue. Pero no sabe que ella siempre ha estado enamorada de él, a pesar de que sean casi familia, ni de que toda su vida está a punto de cambiar. Porque ella está prohibida, pero le despierta la piel. Porque es el mar, noches estrelladas y vinilos de los Beatles. Porque a veces basta un «deja que ocurra» para tenerlo todo.

</details>

### 184. Tokio Blues

**Haruki Murakami** · *Drama · Fantástico · Romántico*

Tôru Watanabe, un ejecutivo de 37 años, escucha casualmente mientras aterriza en un aeropuerto europeo una vieja canción de los Beatles, y la música le hace retroceder a su juventud, al turbulento Tokio de finales …

<details><summary>Sinopsis completa</summary>

Tôru Watanabe, un ejecutivo de 37 años, escucha casualmente mientras aterriza en un aeropuerto europeo una vieja canción de los Beatles, y la música le hace retroceder a su juventud, al turbulento Tokio de finales de los sesenta. Tôru recuerda, con una mezcla de melancolía y desasosiego, a la inestable y misteriosa Naoko, la novia de su mejor —y único— amigo de la adolescencia, Kizuki. El suicidio de éste les distancia durante un año hasta que se reencuentran en la universidad. Inician allí una relación íntima; sin embargo, la frágil salud mental de Naoko se resiente y la internan en un centro de reposo. Al poco, Tôru se enamora de Midori, una joven activa y resuelta. Indeciso, sumido en dudas y temores, experimenta el deslumbramiento y el desengaño allá donde todo parece cobrar sentido: el sexo, el amor y la muerte. La situación, para él, para los tres, se ha vuelto insostenible; ninguno parece capaz de alcanzar el delicado equilibrio entre las esperanzas juveniles y la necesidad de encontrar un lugar en el mundo.

</details>

### 185. Trenza del mar Esmeralda

**Brandon Sanderson** · *Aventuras · Fantástico · Novela* · Serie: Novela secreta, tomo 1

Vuelve al universo del Cosmere con una aventura divertida y cautivadora que encantará a los fans de La princesa prometida . En su isla natal sobre un océano verde esmeralda, la única vida que Trenza …

<details><summary>Sinopsis completa</summary>

Vuelve al universo del Cosmere con una aventura divertida y cautivadora que encantará a los fans de La princesa prometida . En su isla natal sobre un océano verde esmeralda, la única vida que Trenza conoce es sencilla, marcada por el placer de coleccionar las tazas que traen los marineros de tierras lejanas y escuchar las historias que le cuenta su amigo Charlie. Pero cuando el padre de Charlie se lo lleva en barco para buscarle esposa y sucede una catástrofe, Trenza deberá colarse como polizona en un barco y partir en busca de la hechicera que habita en el mortífero mar de Medianoche. Sobre unos océanos de esporas repletos de piratas, ¿podrá Trenza abandonar su tranquila vida y crearse un lugar en un océano donde una sola gota puede significar la muerte instantánea?

</details>

### 186. Trilogía Los juegos del hambre

**Suzanne Collins** · *Ciencia ficción · Juvenil* · Serie: Distritos, tomo 0

La trilogía Los juegos del hambre , se lleva a cabo en un período de tiempo futuro no identificado después de la destrucción de los países actuales de América del Norte, en un país conocido …

<details><summary>Sinopsis completa</summary>

La trilogía Los juegos del hambre , se lleva a cabo en un período de tiempo futuro no identificado después de la destrucción de los países actuales de América del Norte, en un país conocido como "Panem". Panem esta formado por un rico Capitolio, ubicado en lo que solía ser de las rocosas de América del Norte, y doce (antes trece) distritos que lo rodean, los distritos más pobres, que atienden a las necesidades del Capitolio. Como castigo por una rebelión en contra de este último, en el que Capitolio derroto a los doce primeros distritos y destruyó al decimotercero, cada año, un chico y una chica de cada uno de los doce distritos restantes, entre doce y dieciocho años, son seleccionados por sorteo y obligados a participar en los "Juegos del Hambre". Los juegos son un evento televisado donde los participantes, llamados "tributos", deben luchar hasta la muerte en un estadio al aire libre hasta que sólo queda uno. El tributo ganador y su distrito correspondiente, recibiran alimentos. La trilogía se compone de Los juegos del hambre , En llamas y Sinsajo . Los dos primeros libros fueron cada uno best-sellers de The New York Times, y el tercer libro, Sinsajo , encabezó todas las listas de libros más vendidos de Estados Unidos en su lanzamiento

</details>

### 187. Trono de cristal

**Sarah J. Maas** · *Aventuras · Fantástico · Infantil y juvenil* · Serie: Trono de cristal, tomo 1

Tras un año de trabajos forzados en las minas de sal, la joven asesina Celaena Sardothien ha sido convocada por el príncipe del Reino de Endovier. Celaena no ha acudido con la intención de acabar …

<details><summary>Sinopsis completa</summary>

Tras un año de trabajos forzados en las minas de sal, la joven asesina Celaena Sardothien ha sido convocada por el príncipe del Reino de Endovier. Celaena no ha acudido con la intención de acabar con la vida del príncipe, sino con el deseo de conquistar su libertad. Si vence a veintitrés asesinos, ladrones y guerreros en una competición a vida o muerte, será liberada de prisión para ejercer como campeona real. El príncipe la aconsejará. El capitán de la guardia la protegerá. Pero algo maligno se esconde en el palacio de cristal, y está allí para matar. Mientras sus competidores van muriendo uno a uno, la lucha de Celaena por conquistar su libertad se convierte en una lucha por sobrevivir y en una incesante búsqueda del origen del mal antes de que destruya el mundo.

</details>

### 188. Últimas noticias del nuevo idiota iberoamericano

**Álvaro Vargas Llosa | Carlos Alberto Montaner | Plinio Apuleyo Mendoza | Varios Autores** · *Ciencias sociales · Ensayo*

Muchas cosas han pasado desde que algunos críticos de izquierda apodaron a Plinio Apuleyo Mendoza, Carlos Alberto Montaner y Álvaro Vargas Llosa «Los tres chiflados del liberalismo», por publicar el Manual del perfecto Idiota Latinoamericano. …

<details><summary>Sinopsis completa</summary>

Muchas cosas han pasado desde que algunos críticos de izquierda apodaron a Plinio Apuleyo Mendoza, Carlos Alberto Montaner y Álvaro Vargas Llosa «Los tres chiflados del liberalismo», por publicar el Manual del perfecto Idiota Latinoamericano. Ahora, estos tres connotados escritores regresan con Últimas noticias del nuevo idiota iberoamericano, un apasionante viaje por la actual realidad política, social y económica de América Latina y también de España. La pluma de Mendoza, Montaner y Vargas Llosa desnuda lo que sucede por estos días en la Cuba de los Castro, la Venezuela de Maduro sin Chávez, la Argentina de los Kirchner, el Ecuador del duro Correa, la pujanza chilena, la contradicción colombiana, el sorprendente modelo peruano, la encrucijada mexicana y la hecatombe española. ¿Quiénes son los nuevos idiotas de Iberoamérica? Los autores responden: son los gobernantes de varios países que han utilizado el artificio populista para mantenerse en el poder, pero ahora luchan por sostenerse ante el empuje de una nueva clase media, más exigente y preparada.

</details>

### 189. Un monstruo viene a verme

**Patrick Ness** · *Fantástico · Juvenil · Novela · Terror*

El monstruo apareció justo después de la medianoche. Pero no era el que Conor había estado esperando, el de la pesadilla que ha estado soñando todas las noches desde que su madre comenzó con el …

<details><summary>Sinopsis completa</summary>

El monstruo apareció justo después de la medianoche. Pero no era el que Conor había estado esperando, el de la pesadilla que ha estado soñando todas las noches desde que su madre comenzó con el tratamiento. El de la oscuridad y el viento y el grito… Ese monstruo del jardín es diferente. Antiguo, salvaje. Y quiere de Conor algo terrible y peligroso. Quiere la verdad.

</details>

### 190. Una corte de alas y ruina

**Sarah J. Maas** · *Fantástico · Juvenil · Novela* · Serie: Una corte de rosas y espinas, tomo 3

Feyre ha vuelto a la Corte Primavera decidida a desvelar las artimañas de Tamlin y las razones del rey que amenaza Prythian. Pero para hacerlo, tendrá que jugar al mortal juego del engaño… un solo …

<details><summary>Sinopsis completa</summary>

Feyre ha vuelto a la Corte Primavera decidida a desvelar las artimañas de Tamlin y las razones del rey que amenaza Prythian. Pero para hacerlo, tendrá que jugar al mortal juego del engaño… un solo paso en falso podría condenarla, no solo a ella sino a todo su mundo. La guerra se cierne sobre todos, y Feyre tendrá que elegir muy bien en quién confiar.

</details>

### 191. Una corte de hielo y estrellas

**Sarah J. Maas** · *Fantástico · Juvenil · Novela* · Serie: Una corte de rosas y espinas, tomo 3

Feyre, Rhys y su círculo más íntimo de amigos están muy ocupados reconstruyendo la Corte de la Noche y el vasto mundo que la rodea. Pero el Solsticio del Invierno finalmente se acerca, y con …

<details><summary>Sinopsis completa</summary>

Feyre, Rhys y su círculo más íntimo de amigos están muy ocupados reconstruyendo la Corte de la Noche y el vasto mundo que la rodea. Pero el Solsticio del Invierno finalmente se acerca, y con él, cierto alivio ganado con mucho esfuerzo. No obstante, esta atmósfera festiva no conseguirá detener las sombras del pasado que acechan sin tregua. Mientras Feyre transita su primer solsticio de invierno como Alta Dama, descubre que sus seres queridos tienen más heridas de las que había imaginado: cicatrices que impactarán de manera irrefrenable en el futuro de su Corte.

</details>

### 192. Una corte de niebla y furia

**Sarah J. Maas** · *Fantástico · Juvenil · Novela* · Serie: Una corte de rosas y espinas, tomo 2

Por amor, venció la muerte. Para el mundo, se convertirá en un arma mortal. Tras rescatar a su amado Tamlin de la malvada reina Amarantha, Feyre regresa a la Corte Primavera con los poderes de …

<details><summary>Sinopsis completa</summary>

Por amor, venció la muerte. Para el mundo, se convertirá en un arma mortal. Tras rescatar a su amado Tamlin de la malvada reina Amarantha, Feyre regresa a la Corte Primavera con los poderes de una Alta Fae. Pero no consigue olvidar los crímenes que debió cometer para salvar al pueblo de Tamlin… ni el perverso pacto que cerró con Rhysand, el Alto Lord de la temible Corte Noche. Mientras Feyre es arrastrada hacia el interior de la oscura red política y pasional de Rhysand, una guerra inminente acecha y un mal mucho más peligroso que cualquier reina amenaza con destruir todo lo que Feyre alguna vez intentó proteger. Ella deberá entonces enfrentarse a su pasado, aceptar sus nuevos dones y decidir su futuro.

</details>

### 193. Una corte de rosas y espinas

**Sarah J. Maas** · *Fantástico · Juvenil · Novela* · Serie: Una corte de rosas y espinas, tomo 1

Feyre, una cazadora de diecinueve años, mata a un lobo en el bosque. Como consecuencia, una criatura monstruosa llega buscando venganza y la arrastra a una tierra encantada que solo conoce a través de las …

<details><summary>Sinopsis completa</summary>

Feyre, una cazadora de diecinueve años, mata a un lobo en el bosque. Como consecuencia, una criatura monstruosa llega buscando venganza y la arrastra a una tierra encantada que solo conoce a través de las leyendas. Allí descubre que su captor no es un animal, sino Tamlin, uno de los letales fae. En su cautiverio, se dará cuenta de que lo que siente por él pasa de la fría hostilidad a una pasión que arderá a pesar de las advertencias que ha recibido. Pero una antigua y siniestra sombra crece en esta tierra extraña, y Feyre deberá encontrar una forma de detenerla o Tamlin y su mundo estarán condenados para siempre.

</details>

### 194. Verity. La sombra de un engaño

**Colleen Hoover** · *Intriga · Novela*

Lowen Ashleigh, autora al borde de la bancarrota, recibe un encargo que le cambiará la vida: Jeremy, el flamante marido de Verity Crawford, una de las autoras más importantes del momento, la contrata para terminar …

<details><summary>Sinopsis completa</summary>

Lowen Ashleigh, autora al borde de la bancarrota, recibe un encargo que le cambiará la vida: Jeremy, el flamante marido de Verity Crawford, una de las autoras más importantes del momento, la contrata para terminar la serie de libros en la que trabajaba su mujer antes de sufrir un grave accidente que la ha dejado en coma. Lowen se instala en la mansión del matrimonio para poder trabajar en las notas en las que trabajaba Verity, con la esperanza de encontrar material suficiente para empezar con su encargo, pero lo que no esperaba descubrir en la caótica oficina es una autobiografía de la propia Verity, escondida para que nunca salga a la luz.

</details>

### 195. Veronika decide morir

**Paulo Coelho** · *Autoayuda*

Verónica es una joven que tiene los mismos sueños y deseos que cualquier persona de su edad. Es guapa, cuenta con un buen trabajo y no le faltan pretendientes. Su vida transcurre sin mayores sobresaltos, …

<details><summary>Sinopsis completa</summary>

Verónica es una joven que tiene los mismos sueños y deseos que cualquier persona de su edad. Es guapa, cuenta con un buen trabajo y no le faltan pretendientes. Su vida transcurre sin mayores sobresaltos, sin grandes alegrías ni grandes tristezas. Pero Verónica no es feliz. Por eso, la mañana del 11 de noviembre de 1997, Verónica decide morir. Sueños y fantasías. Deseo y muerte. locura y pasión. Verónica, en su camino hacia la muerte, descubre que cada segundo de la existencia es una opción que tomamos entre la alternativa de seguir adelante o de abandonar. Verónica experimenta placeres nuevos y halla un nuevo sentido a la vida, un sentido que le había permanecido oculto hasta ahora, cuando ya es demasiado tarde para echarse atrás.

</details>

### 196. Voces de Chernóbil

**Svetlana Alexievich** · *Crónica · Historia*

Chernóbil, 1986. «Cierra las ventanillas y acuéstate. Hay un incendio en la central. Vendré pronto». Esto fue lo último que un joven bombero dijo a su esposa antes de acudir al lugar de la explosión. …

<details><summary>Sinopsis completa</summary>

Chernóbil, 1986. «Cierra las ventanillas y acuéstate. Hay un incendio en la central. Vendré pronto». Esto fue lo último que un joven bombero dijo a su esposa antes de acudir al lugar de la explosión. No regresó. Y en cierto modo, ya no volvió a verle, pues en el hospital su marido dejó de ser su marido. Todavía hoy ella se pregunta si su historia trata sobre el amor o la muerte. Voces de Chernóbil está planteado como si fuera una tragedia griega, con coros y unos héroes marcados por un destino fatal, cuyas voces fueron silenciadas durante muchos años por una polis representada aquí por la antigua URSS. Pero, a diferencia de una tragedia griega, no hubo posibilidad de catarsis.

</details>

### 197. Yo antes de ti

**Jojo Moyes** · *Novela · Romántico* · Serie: Yo antes de ti, tomo 1

Louisa Clark sabe muchas cosas. Sabe cuántos pasos hay entre la parada del autobús y su casa. Sabe que le gusta trabajar en el café The Buttered Bun y sabe que quizá no quiera a …

<details><summary>Sinopsis completa</summary>

Louisa Clark sabe muchas cosas. Sabe cuántos pasos hay entre la parada del autobús y su casa. Sabe que le gusta trabajar en el café The Buttered Bun y sabe que quizá no quiera a su novio Patrick. Lo que Lou no sabe es que está a punto de perder su trabajo o que son sus pequeñas rutinas las que la mantienen en su sano juicio. Will Traynor sabe que un accidente de moto se llevó sus ganas de vivir. Sabe que ahora todo le parece insignificante y triste y sabe exactamente cómo va a ponerle fin. Lo que Will no sabe es que Lou está a punto de irrumpir en su mundo con una explosión de color. Y ninguno de los dos sabe que va a cambiar al otro para siempre. Yo antes de ti reúne a dos personas que no podrían tener menos en común en una novela conmovedoramente romántica con una pregunta: ¿qué decidirías cuando hacer feliz a la persona a la que amas significa también destrozarte el corazón?

</details>

### 198. Yo soy Eric Zimmerman. Volumen 1

**Megan Maxwell** · *Erótico · Novela · Romántico* · Serie: Eric Zimmerman, tomo 1

Me llamo Eric Zimmerman y soy un poderoso empresario alemán. Me caracterizo por ser un hombre frío e impersonal, que disfruta del sexo sin amor y sin compromiso. En uno de mis viajes a España …

<details><summary>Sinopsis completa</summary>

Me llamo Eric Zimmerman y soy un poderoso empresario alemán. Me caracterizo por ser un hombre frío e impersonal, que disfruta del sexo sin amor y sin compromiso. En uno de mis viajes a España para visitar una de mis delegaciones conocí a una joven llamada Judith Flores. Ella me hizo reír, me hizo cantar, me hizo incluso bailar, y yo no estaba acostumbrado a eso. Cuando me di cuenta de que sentía más de lo que debía, me alejé de ella, pero regresé, pues esa mujer me atraía como un imán. A partir de ese momento comenzamos una relación plagada de fantasía y erotismo, en la que disfruté enseñando a Judith a gozar del sexo de una manera que ella nunca había imaginado. Y tú, ¿te atreves a descubrir el lado sumiso, dominante y voyeur que todos llevamos dentro?

</details>

### 199. Yo, robot

**Isaac Asimov** · *Ciencia ficción · Policíaco* · Serie: Fundación - Serie de los Robots, tomo 1

Los robots de Isaac Asimov son máquinas capaces de llevar a cabo muy diversas tareas, y que a menudo se plantean a sí mismos problemas de 'conducta humana'. Pero estas cuestiones se resuelven en Yo, …

<details><summary>Sinopsis completa</summary>

Los robots de Isaac Asimov son máquinas capaces de llevar a cabo muy diversas tareas, y que a menudo se plantean a sí mismos problemas de 'conducta humana'. Pero estas cuestiones se resuelven en Yo, robot en el ámbito de las tres leyes fundamentales de la robótica, concebidas por Asimov, y que no dejan de proponer extraordinarias paradojas que a veces se explican por errores de funcionamiento y otras por la creciente complejidad de los 'programas'. Las paradojas que se plantean en estos relatos futuristas no son sólo ingeniosos ejercicios intelectuales sino sobre todo una indagación sobre la situación del hombre actual en relación con los avances tecnológicos y con la experiencia del tiempo.

</details>

### 200. Yo, Simon, Homo Sapiens

**Becky Albertalli** · *Juvenil · Novela · Romántico*

¿Qué serías capaz de hacer para proteger tu secreto mejor guardado? Simon ha hecho lo impensable: ceder al chantaje de Martin. O Simon se las ingenia para que su amiga Abby salga con Martin o …

<details><summary>Sinopsis completa</summary>

¿Qué serías capaz de hacer para proteger tu secreto mejor guardado? Simon ha hecho lo impensable: ceder al chantaje de Martin. O Simon se las ingenia para que su amiga Abby salga con Martin o este… le hablará a todo el mundo de los correos electrónicos. De los correos electrónicos que Simon, escondido tras un seudónimo, intercambia con un tal Bluegreen, que es el chico más divertido, desconcertante y adorable que Simon ha conocido nunca. Y es que Simon, pese a su afición al teatro, prefiere no exponer a los focos su identidad sexual… al menos de momento. Sin embargo, seguirle la corriente a Martin no será la solución a sus problemas, sino más bien el comienzo de un enorme embrollo. ¿Qué hará Martin si no consigue conquistar a Abby? ¿Cómo reaccionará Abby si se entera del chantaje? ¿Qué pensará Bluegreen de Simon si la intimidad de ambos queda comprometida? Y, la cuestión más importante: ¿Quién demonios es Bluegreen?

</details>
