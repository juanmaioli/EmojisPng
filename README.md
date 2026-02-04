# 🎨 Proyecto de Recursos de Emojis

Este repositorio contiene una colección completa de activos de emojis extraídos de la fuente **AppleColorEmoji.ttf** y organizados jerárquicamente.

## 🚀 Proceso de Extracción y Mejora
Se han procesado las tablas de la fuente original para obtener una biblioteca de activos lista para usar:
1.  **Extracción de Bitmaps**: Recuperación de **4229 archivos PNG** desde la tabla `CBDC`.
2.  **Mapeo Unicode**: Los archivos han sido nombrados descriptivamente (ej. `grinning_face.png`) utilizando la base de datos de Unicode.
3.  **Análisis de Ligaduras**: Se procesó la tabla `GSUB` para identificar y nombrar correctamente secuencias complejas (parejas, familias, variaciones).
4.  **Clasificación Inteligente**: Organización automática en 10 categorías temáticas.

## 📂 Estructura del Repositorio
- 📁 **emojis_extracted/**: Biblioteca de imágenes PNG.
    - `activities/`: Deportes, juegos y música.
    - `animals_nature/`: Fauna, flora y clima.
    - `flags/`: Banderas nacionales y regionales.
    - `food_drink/`: Alimentos y bebidas.
    - `objects/`: Tecnología y herramientas.
    - `people_body/`: Personajes, gestos y anatomía.
    - `smileys_emotions/`: Expresiones y sentimientos.
    - `symbols/`: Iconos, signos y formas.
    - `travel_places/`: Transporte y lugares.
    - `others/`: Otros símbolos.
- 📄 **AppleColorEmoji.ttf**: Archivo de fuente original.
- 📄 **emoji.svg / emoji.xml**: Hojas de sprites de referencia.

## 👤 Autor
Gestionado y procesado por **Juan Gabriel Maioli**.

---
*Documentación actualizada automáticamente por Gemini CLI.*