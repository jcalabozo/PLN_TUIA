# Instrucciones para Claude Code

Repo del grupo con los trabajos prácticos de Procesamiento de Lenguaje Natural (TUIA, UNR). Cada TP vive en su carpeta `P<n>/`, con su propio README, entorno y notebook.

## Cómo trabajar

- Responder en **español rioplatense, con voseo**.
- **La consigna manda.** Resolver lo que pide el enunciado (`P<n>/enunciado/`), sin análisis, gráficos ni secciones que no pida. El notebook se organiza con los mismos pasos y títulos del enunciado. Si algo es ambiguo, elegir la interpretación más simple y dejarla escrita en el notebook.
- **Herramientas de la cátedra:** solo las librerías y técnicas de las unidades que cubre el TP (el TP3, por ejemplo, usa las Unidades 1 a 3) y las que menciona o sugiere el enunciado. Cuando el enunciado ofrece opciones (por ejemplo, spaCy o GLiNER), usar una sola, la que ya se use en otra parte del TP. Si hace falta otra, consultar antes.
- **Código para quien empieza en NLP:** simple y claro, con comentarios que explican el porqué y funciones cortas con un docstring de una línea. Nada de trucos de una línea.
- **Datos que solo puede dar una persona** (como las valoraciones del lector del TP3): no se inventan. Se deja listo el código y la planilla para completarlos, y en el notebook y el informe se marca lo pendiente.
- **Pedidos grandes:** presentar hallazgos y una propuesta, con preguntas numeradas y una opción recomendada, y esperar el OK. Si se pide avanzar sin consultar, resolver hasta el final con criterio propio y, al terminar, resumir las decisiones tomadas y lo que quedó pendiente.
- Los archivos de la cátedra (enunciados y datos) no se modifican.

## Criterio común de los TP

Los TP siguen el mismo formato (ver P3; el TP2, ya entregado, conserva su estructura con `data/` y `docs/`):

- **Notebook** con el nombre que pide la consigna (en el TP3, `TP3_grupo02.ipynb`: somos el grupo 2) o, si no pide ninguno, `TP<n>_calabozo_giuntoli_darruiz_dicarlo.ipynb`, ejecutado y con las salidas guardadas. Se ejecuta con `P<n>/` como carpeta de trabajo, porque lee y escribe con rutas relativas; para guardar las salidas sin abrirlo, con `nbclient`.
- **Una celda de preparación** con los imports, `SEMILLA = 42` y las rutas.
- **Después de cada resultado, una celda «Qué muestra»** que lo interpreta con los números reales de la corrida.
- **Embeddings que tardan en calcularse:** se guardan en `embeddings/`, que no se versiona.
- **Carpetas:** `enunciado/` (enunciado y archivos de ejemplo de la cátedra), `data/` (los datos que lee y escribe el notebook), `entregables/` (lo que pide entregar la consigna, salvo el notebook, que queda en la raíz de `P<n>/`), `informe/` (archivos auxiliares del informe: `informe.md` y la carátula) y `embeddings/`.
- **Entorno propio por TP:** README con instalación y ejecución, `requirements.txt`, `.gitignore`, un `.venv` creado con `py -3.12 -m venv .venv` (Python 3.12 de python.org, sin uv) y el kernel `pln-tp<n>`.
- **Uso de IA:** el informe lo declara en dos o tres líneas, como pide la cátedra.

## Git

- Mensajes en español y en tercera persona: "Agrega …", "Corrige …", "Reorganiza …".
- **Sin atribución a Claude:** ni `Co-Authored-By` en commits, ni "Generated with Claude Code" en PRs, issues u otros archivos. Los autores son los integrantes del grupo.
- **No commitear ni pushear sin pedido explícito:** el repo es compartido con el grupo y los docentes.
