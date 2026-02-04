import os
import unicodedata
from fontTools.ttLib import TTFont

font_path = "AppleColorEmoji.ttf"
output_dir = "emojis_extracted"

if not os.path.exists(font_path):
    print(f"Error: {font_path} no encontrado.")
    exit(1)

os.makedirs(output_dir, exist_ok=True)

print("Abriendo fuente y cargando tablas...")
font = TTFont(font_path)

# La tabla 'sbix' contiene los bitmaps PNG
if 'sbix' not in font:
    print("Error: La fuente no contiene una tabla 'sbix'.")
    exit(1)

# Obtener el mapa de caracteres (CMap) para traducir nombres de glifos a Unicode
cmap = font.getBestCmap()
glyph_to_unicode = {v: k for k, v in cmap.items()}

# Buscar la resolución más alta disponible
strikes = font['sbix'].strikes
ppems = sorted(strikes.keys(), reverse=True)
best_ppem = ppems[0]
print(f"Extrayendo resolución: {best_ppem}x{best_ppem}")

strike = strikes[best_ppem]
count = 0

for glyph_name, glyph_data in strike.glyphs.items():
    if glyph_data.graphicType != 'png ':
        continue
    
    # Intentar obtener nombre descriptivo
    unicode_val = glyph_to_unicode.get(glyph_name)
    if unicode_val:
        try:
            name = unicodedata.name(chr(unicode_val)).replace(" ", "_").lower()
        except:
            name = f"u{unicode_val:04X}"
    else:
        name = glyph_name.replace(".", "_")

    filename = os.path.join(output_dir, f"{name}.png")
    
    with open(filename, "wb") as f:
        f.write(glyph_data.imageData)
    count += 1

print(f"Proceso finalizado. Se extrajeron {count} imágenes en '{output_dir}'.")
