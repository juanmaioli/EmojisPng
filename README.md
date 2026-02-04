# 🎨 Proyecto de Recursos de Emojis

Este repositorio es una central de recursos de emojis, gestionando activos extraídos de las principales fuentes del mercado (**Apple, Google, Microsoft, Twitter y OpenMoji**).

## 🚀 Capacidades de Extracción
El proyecto ha evolucionado para soportar múltiples formatos y tecnologías de fuentes de emojis:

1.  **Bitmaps (PNG)**: Extracción de activos de alta resolución desde tablas `CBDT/CBLC` y `sbix`.
2.  **Vectores Nativos (SVG)**: Recuperación de documentos SVG integrados en las fuentes.
3.  **Vectores por Capas (COLR v0)**: Reconstrucción de emojis vectoriales a partir de capas de colores (Twemoji, OpenMoji).
4.  **Renderizado Avanzado (COLR v1)**: Nuevo soporte experimental para renderizar fuentes modernas con gradientes (Noto Color Emoji) utilizando `blackrenderer` y `Cairo`.

## 📁 Biblioteca de Activos
Los emojis se organizan por la fuente de origen y su formato:

| Directorio | Origen | Formato | Notas |
| :--- | :--- | :--- | :--- |
| `AppleColorEmoji_extracted/` | **Apple / iOS** | PNG | 4229 bitmaps (137px). |
| `TwEmoji_extracted/` | **Twitter / X** | SVG | 3852 vectores reconstruidos. |
| `OpenmojiColor_extracted/` | **OpenMoji** | SVG | 4649 vectores (nativos + capas). |
| `NotoColorEmoji-Regular_extracted/` | **Google / Android** | SVG/PNG | 711 vectores nativos + soporte de renderizado v1. |
| `rendered_colrv1/` | **Renderizados** | PNG | Ejemplos de alta calidad (256px) generados desde COLR v1. |

## 🛠️ Herramientas
- `extract_all.py`: Script principal de extracción. Detecta automáticamente tablas `CBDT`, `sbix`, `SVG` y `COLR v0`.
- `render_colrv1.py`: **Nueva herramienta** para renderizar emojis COLR v1 (requiere entorno virtual con `blackrenderer`).
- `extract_emoji.py`: Script original para extracción básica.

## 👤 Autor
Gestionado y procesado por **Juan Gabriel Maioli**.

---
*Documentación actualizada automáticamente por Gemini CLI.*