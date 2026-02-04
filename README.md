# 🎨 Proyecto de Recursos de Emojis e Iconos

Este repositorio es una central de recursos gráficos, gestionando activos extraídos de las principales fuentes del mercado (**Apple, Google, Microsoft, Twitter y OpenMoji**).

## 🚀 Capacidades de Extracción
El proyecto soporta múltiples formatos y tecnologías de fuentes modernas:

1.  **Bitmaps (PNG)**: Extracción de activos de alta resolución desde tablas `CBDT/CBLC` y `sbix`.
2.  **Vectores Nativos (SVG)**: Recuperación de documentos SVG integrados en las fuentes (OpenMoji, Noto).
3.  **Vectores por Capas (COLR v0)**: Reconstrucción de emojis vectoriales a partir de capas de colores (Twemoji).
4.  **Renderizado de Alta Fidelidad (COLR v1)**: Pipeline avanzado para renderizar fuentes con gradientes complejos (Segoe UI Emoji, Noto Color Emoji) utilizando `blackrenderer` y `Cairo`.
5.  **Iconografía (SVG)**: Extracción de glifos monocromáticos desde fuentes de iconos (Segoe Icons).

## 📁 Biblioteca de Activos
Los recursos se organizan por la fuente de origen y su formato:

| Directorio | Origen | Formato | Cantidad | Notas |
| :--- | :--- | :--- | :--- | :--- |
| `AppleColorEmoji_extracted/` | **Apple / iOS** | PNG | 4229 activos | Bitmaps clásicos (137px). |
| `SeguiEmj_extracted/` | **Windows 11** | PNG | 2010 activos | **Renderizado v1** con gradientes (256px). |
| `SegoeIcons_extracted/` | **Windows Icons** | SVG | 1985 activos | Iconos vectoriales monocromáticos. |
| `TwEmoji_extracted/` | **Twitter / X** | SVG | 3852 activos | Vectores reconstruidos por capas. |
| `OpenmojiColor_extracted/` | **OpenMoji** | SVG | 4649 activos | Vectores (nativos + capas). |
| `NotoColorEmoji-Regular_extracted/` | **Google** | SVG | 711 activos | Vectores nativos (v1 disponible para render). |

## 🛠️ Herramientas
- `extract_all.py`: Motor principal de detección y extracción multiformato.
- `render_segoe.py`: Script de renderizado masivo para fuentes COLR v1 (Windows/Google).
- `extract_icons.py`: Herramienta para convertir fuentes de iconos monocromáticos a archivos SVG.
- `render_colrv1.py`: Utilidad de prueba para renderizado individual de alta fidelidad.

## 👤 Autor
Gestionado y procesado por **Juan Gabriel Maioli**.

---
*Documentación actualizada automáticamente por Gemini CLI.*
