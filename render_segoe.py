import os
import unicodedata
from fontTools.ttLib import TTFont
from blackrenderer.render import renderText

font_path = "SeguiEmj.ttf"
output_dir = "SeguiEmj_extracted/png"
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

print(f"Iniciando renderizado de {len(cmap)} emojis (COLR v1)...")
count = 0
errors = 0

for unicode_val, glyph_name in cmap.items():
    try:
        char = chr(unicode_val)
        name = get_name(unicode_val, glyph_name)
        output_path = os.path.join(output_dir, f"{name}.png")
        
        # Renderizado a 256px usando Cairo
        renderText(font_path, char, output_path, fontSize=256, margin=20, backendName="cairo")
        count += 1
        
        if count % 100 == 0:
            print(f"Progreso: {count} emojis procesados...")
            
    except Exception as e:
        errors += 1
        if errors < 10:
            print(f"Error en {glyph_name}: {e}")

print(f"\nFinalizado. Extraídos: {count}, Errores: {errors}")
print(f"Archivos guardados en: {output_dir}")
