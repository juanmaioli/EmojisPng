# 🎨 Proyecto de Recursos de Emojis

Este repositorio contiene una colección completa de activos de emojis extraídos de la fuente **AppleColorEmoji.ttf** y organizados jerárquicamente para su uso en aplicaciones y diseño.

## 🚀 Proceso de Extracción
Se han procesado las tablas de la fuente utilizando herramientas de ingeniería de fuentes para extraer **4229 archivos PNG** de alta calidad. El proceso incluyó:
1.  **Extracción de Bitmaps**: Recuperación de los datos PNG desde la tabla `CBDT`.
2.  **Renombrado Inteligente**: Análisis de la tabla `GSUB` para nombrar correctamente incluso las secuencias de ligaduras complejas según el estándar Unicode.
3.  **Organización Temática**: Clasificación automática en subcarpetas basadas en categorías oficiales.

## 📂 Estructura del Repositorio
- 📁 **emojis_extracted/**: Carpeta raíz con los activos organizados.
    - `activities/`: Deportes, juegos y música.
    - `animals_nature/`: Fauna, flora y clima.
    - `flags/`: Banderas nacionales y regionales.
    - `food_drink/`: Alimentos y bebidas.
    - `objects/`: Tecnología y objetos cotidianos.
    - `people_body/`: Personajes, gestos y anatomía.
    - `smileys_emotions/`: Expresiones y sentimientos.
    - `symbols/`: Iconos, signos y formas.
    - `travel_places/`: Transporte y lugares.
- 📄 **AppleColorEmoji.ttf**: Fuente fuente original.
- 📄 **emoji.svg / emoji.xml**: Hojas de referencia en formato vectorial.

## 👤 Autor
Proyecto gestionado y procesado por **Juan Gabriel Maioli**.

---
*Generado automáticamente con la asistencia de Gemini CLI.*
