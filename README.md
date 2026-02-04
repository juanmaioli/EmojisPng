# 🎨 Proyecto de Recursos de Emojis

Este repositorio es una central de recursos de emojis, gestionando activos extraídos de las principales fuentes del mercado (**Apple, Google, Microsoft, Twitter y OpenMoji**).

## 🚀 Capacidades de Extracción
El proyecto ha evolucionado para soportar múltiples formatos y tecnologías de fuentes de emojis:

1.  **Bitmaps (PNG)**: Extracción de activos de alta resolución desde tablas `CBDT/CBLC` y `sbix`.
2.  **Vectores Nativos (SVG)**: Recuperación de documentos SVG integrados en las fuentes.
3.  **Vectores por Capas (COLR/CPAL)**: Reconstrucción de emojis vectoriales a partir de capas de colores (Soporte para COLR v0).
4.  **Mapeo Inteligente**: Nombramiento automático basado en el estándar Unicode.

## 📁 Biblioteca de Activos
Los emojis se organizan por la fuente de origen y su formato:

| Directorio | Origen | Formato | Cantidad |
| :--- | :--- | :--- | :--- |
| `AppleColorEmoji_extracted/` | **Apple / iOS** | PNG | 4229 activos |
| `TwEmoji_extracted/` | **Twitter / X** | SVG | 3852 activos |
| `OpenmojiColor_extracted/` | **OpenMoji** | SVG | 4147 activos |
| `NotoColorEmoji_extracted/` | **Google / Android** | SVG/PNG | 684+ activos |
| `SegoeUIColorEmoji_extracted/` | **Microsoft / Windows** | - | *En desarrollo (v1)* |

## 🛠️ Herramientas
- `extract_all.py`: Script principal que detecta automáticamente las tablas de la fuente (CBDT, sbix, SVG, COLR) y extrae los activos en el mejor formato posible.
- `extract_emoji.py`: Script original para extracción básica de bitmaps.

## 👤 Autor
Gestionado y procesado por **Juan Gabriel Maioli**.

---
*Documentación actualizada automáticamente por Gemini CLI.*
