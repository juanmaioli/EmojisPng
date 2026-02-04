import os
import unicodedata
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

font_path = "SegoeIcons.ttf"
output_dir = "SegoeIcons_extracted/svg"
os.makedirs(output_dir, exist_ok=True)

def get_name(unicode_val, glyph_name):
    if unicode_val:
        try:
            return unicodedata.name(chr(unicode_val)).replace(" ", "_").lower()
        except:
            return f"u{unicode_val:04X}"
    return glyph_name.replace(".", "_")

print(f"Abriendo {font_path}...")
font = TTFont(font_path)
cmap = font.getBestCmap()
glyph_set = font.getGlyphSet()

print(f"Extrayendo {len(cmap)} iconos a SVG...")
count = 0

for unicode_val, glyph_name in cmap.items():
    try:
        name = get_name(unicode_val, glyph_name)
        output_path = os.path.join(output_dir, f"{name}.svg")
        
        pen = SVGPathPen(glyph_set)
        glyph_set[glyph_name].draw(pen)
        path_data = pen.getCommands()
        
        if not path_data:
            continue

        # Font coordinates are usually upside down compared to SVG
        # We wrap it in a group with a flip transform
        svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048">
  <g transform="matrix(1 0 0 -1 0 2048)">
    <path d="{path_data}" fill="black" />
  </g>
</svg>"""
        
        with open(output_path, "w") as f:
            f.write(svg_content)
        
        count += 1
        if count % 200 == 0:
            print(f"Progreso: {count} iconos extraídos...")
            
    except Exception as e:
        print(f"Error en {glyph_name}: {e}")

print(f"\nFinalizado. Extraídos: {count} archivos SVG.")
print(f"Archivos guardados en: {output_dir}")
