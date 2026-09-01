# **Extracción de metadatos y sinopsis con Playwright y BeautifulSoup**

### **Presentación**

El objetivo del trabajo es construir un corpus de libros a partir de la información pública disponible en [Lectulandia](https://ww3.lectulandia.co/).

Cada grupo seleccionará una categoría y extraerá los metadatos y las sinopsis de entre 100 y 200 libros. El dataset obtenido será utilizado posteriormente en actividades de procesamiento de texto y en la construcción de un recomendador de libros.

### **Modalidad**

* Trabajo en grupos de aproximadamente cuatro integrantes.  
* Una categoría por grupo.  
* Entre 100 y 200 libros.  
* Cada integrante deberá incorporar el trabajo a su repositorio personal.

### **Herramientas**

Se utilizarán:

* **Playwright:** para abrir el navegador, recorrer las páginas de la categoría y visitar las fichas de los libros.  
* **BeautifulSoup:** para analizar el HTML obtenido y extraer los datos.  
* **pandas:** para organizar y guardar el dataset.  
* **Git:** para registrar el trabajo en el repositorio personal.

Playwright se encargará de la navegación, mientras que BeautifulSoup se utilizará para interpretar el contenido HTML.

## 

## 

## 

## **Parte 1 — Diseño de la extracción**

Antes de comenzar a programar, cada grupo deberá presentar un documento breve que contenga:

### **1\. Categoría seleccionada**

* Nombre de la categoría.  
* URL de la categoría.  
* Cantidad de libros que se propone extraer.  
* Criterio utilizado para seleccionar las páginas.

### **2\. Datos que se extraerán**

El dataset deberá contener, como mínimo:

| Campo | Descripción |
| :---- | ----- |
| `titulo` | Título del libro |
| `autores` | Autor o autores |
| `generos` | Género o géneros |
| `serie` | Serie a la que pertenece, si corresponde |
| `sinopsis` | Texto completo de la sinopsis |
| `url_libro` | Dirección de la ficha |
| `categoria_origen` | Categoría seleccionada por el grupo |
| `fecha_extraccion` | Fecha en que se obtuvo el registro |

La dirección de la portada podrá incorporarse como campo opcional.

### 

### **3\. Localización de los datos**

Para cada campo deberán indicar dónde se encuentra y cómo planean extraerlo.

| Dato | Tipo de página | Etiqueta HTML | Selector propuesto |
| :---- | :---- | :---- | :---- |
| Título | Ficha individual | A determinar | A determinar |
| Autores | Ficha individual | A determinar | A determinar |
| Géneros | Ficha individual | A determinar | A determinar |
| Sinopsis | Ficha individual | A determinar | A determinar |

Los selectores deberán obtenerse inspeccionando el HTML del sitio desde las herramientas de desarrollo del navegador.

### 

### **4\. Estrategia de extracción**

El grupo deberá describir brevemente el procedimiento que implementará:

1. Abrir la página de la categoría con Playwright.  
2. Recorrer las páginas necesarias.  
3. Obtener el HTML mediante Playwright.  
4. Analizar ese HTML con BeautifulSoup.  
5. Extraer las URL de las fichas de los libros.  
6. Visitar cada ficha con Playwright.  
7. Extraer los metadatos y la sinopsis con BeautifulSoup.  
8. Limpiar y validar los datos.  
9. Eliminar libros duplicados.  
10. Guardar el resultado en un archivo CSV.

## **Parte 2 — Implementación**

Una vez aprobado el diseño, el grupo deberá desarrollar un programa en Python que:

* Inicie un navegador Chromium mediante Playwright.  
* Puede ejecutarse sin mostrar la ventana del navegador.  
* Recorra la categoría seleccionada.  
* Obtenga entre 100 y 200 fichas de libros.  
* Utilice BeautifulSoup para extraer los datos.  
* Incorpore una pausa entre las páginas visitadas.  
* Controlar errores sin detener completamente la ejecución.  
* Evite registros duplicados.  
* Guarde los resultados incrementalmente.  
* Genere el archivo final `libros.csv`.

No se deberán descargar libros, archivos EPUB, PDF ni otros contenidos. El trabajo se limita a los metadatos y las sinopsis públicas.

### **Controles mínimos**

Antes de finalizar, el grupo deberá comprobar:

* Que no existan registros duplicados por `url_libro`.  
* Que todos los registros tengan título.  
* Que todos los registros tengan una URL válida.  
* Que la mayoría de los registros tenga sinopsis.  
* Que se hayan eliminado espacios y saltos de línea innecesarios.  
* Que los campos ausentes se representen de manera consistente.  
* Que la cantidad obtenida se encuentre entre 50 y 100 libros.

## 

## 

## 

## 

## **Entrega:**

Cada repositorio deberá contener:

*README.md*

*src/*

  *scraper.py*

*data/*

  *libros.csv*

*docs/*

  *diseno\_extraccion.md*

El archivo `README.md` deberá indicar:

* Integrantes del grupo.  
* Categoría seleccionada.  
* Cantidad de libros extraídos.  
* Instrucciones de instalación.  
* Instrucciones para ejecutar el programa.  
* Principales dificultades encontradas.

El archivo `docs/diseno_extraccion.md` contendrá el análisis previo solicitado en la Parte 1\.

