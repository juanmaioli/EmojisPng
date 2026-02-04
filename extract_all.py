import os
import unicodedata
from fontTools.ttLib import TTFont

def get_name(unicode_val, glyph_name):
    if unicode_val:
        try:
            return unicodedata.name(chr(unicode_val)).replace(" ", "_").lower()
        except:
            return f"u{unicode_val:04X}"
    return glyph_name.replace(".", "_")

def extract_from_font(font_path):
    print(f"\n--- Procesando: {font_path} ---")
    if not os.path.exists(font_path):
        print(f"Error: {font_path} no encontrado.")
        return

    font_name = os.path.splitext(font_path)[0]
    output_base = f"{font_name}_extracted"
    os.makedirs(output_base, exist_ok=True)
    
    font = TTFont(font_path)
    cmap = font.getBestCmap()
    glyph_to_unicode = {v: k for k, v in cmap.items()}
    
    # 1. Intentar SBIX (Apple style bitmaps)
    if 'sbix' in font:
        print("Detectada tabla 'sbix' (bitmaps).")
        strikes = font['sbix'].strikes
        ppems = sorted(strikes.keys(), reverse=True)
        best_ppem = ppems[0]
        strike = strikes[best_ppem]
        
        out_dir = os.path.join(output_base, "png")
        os.makedirs(out_dir, exist_ok=True)
        
        count = 0
        for glyph_name, glyph_data in strike.glyphs.items():
            if glyph_data.graphicType != 'png ': continue
            name = get_name(glyph_to_unicode.get(glyph_name), glyph_name)
            with open(os.path.join(out_dir, f"{name}.png"), "wb") as f:
                f.write(glyph_data.imageData)
            count += 1
        print(f"Extraídos {count} PNGs (sbix) en {out_dir}")

    # 2. Intentar CBDT/CBLC (Google style bitmaps)
    if 'CBDT' in font:
        print("Detectada tabla 'CBDT' (bitmaps).")
        out_dir = os.path.join(output_base, "png")
        os.makedirs(out_dir, exist_ok=True)
        
        count = 0
        for strike in font['CBDT'].strikeData:
            for glyph_name, glyph_data in strike.items():
                data = glyph_data.data
                png_start = data.find(b'\x89PNG')
                if png_start != -1:
                    name = get_name(glyph_to_unicode.get(glyph_name), glyph_name)
                    with open(os.path.join(out_dir, f"{name}.png"), "wb") as f:
                        f.write(data[png_start:])
                    count += 1
        print(f"Extraídos {count} PNGs (CBDT) en {out_dir}")

    # 3. Intentar SVG (SVG vectors)
    if 'SVG ' in font:
        print("Detectada tabla 'SVG ' (vectores).")
        out_dir = os.path.join(output_base, "svg")
        os.makedirs(out_dir, exist_ok=True)
        
        count = 0
        for doc in font['SVG '].docList:
            # doc.data contains the SVG content
            # We need to map glyph IDs to names
            for start, end in zip(range(doc.startGlyphID, doc.endGlyphID + 1), range(doc.startGlyphID, doc.endGlyphID + 1)):
                glyph_name = font.getGlyphName(start)
                name = get_name(glyph_to_unicode.get(glyph_name), glyph_name)
                with open(os.path.join(out_dir, f"{name}.svg"), "wb") as f:
                    f.write(doc.data.encode('utf-8') if isinstance(doc.data, str) else doc.data)
                count += 1
                break # Usually one doc per glyph or range, but doc.data might contain multiple. 
                # Actually fontTools SVG table is a bit tricky with ranges.
        # Re-doing SVG extraction more carefully
        count = 0
        for doc in font['SVG '].docList:
            # Simplification: just save each doc
            glyph_name = font.getGlyphName(doc.startGlyphID)
            name = get_name(glyph_to_unicode.get(glyph_name), glyph_name)
            with open(os.path.join(out_dir, f"{name}.svg"), "wb") as f:
                 f.write(doc.data.encode('utf-8') if isinstance(doc.data, str) else doc.data)
            count += 1
        print(f"Extraídos {count} SVGs en {out_dir}")

    # 4. COLR/CPAL (Microsoft/Twitter style layered vectors)
    if 'COLR' in font and 'CPAL' in font:
        print(f"Detectada tabla 'COLR' (v{font['COLR'].version}) y 'CPAL'.")
        out_dir = os.path.join(output_base, "svg_layers")
        os.makedirs(out_dir, exist_ok=True)
        
        palette = font['CPAL'].palettes[0] # Use the first palette
        # Convert palette to hex colors
        colors = []
        for c in palette:
            colors.append(f"#{c.red:02x}{c.green:02x}{c.blue:02x}")

        count = 0
        if font['COLR'].version == 0:
            from fontTools.pens.svgPathPen import SVGPathPen
            from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
            
            for glyph_name, layers in font['COLR'].ColorLayers.items():
                svg_content = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048">']
                # Font coordinates are usually upside down compared to SVG
                svg_content.append('<g transform="matrix(1 0 0 -1 0 2048)">')
                
                for layer in layers:
                    layer_glyph = layer.name
                    color_index = layer.colorID
                    if color_index == 0xFFFF: # Foreground color
                        color = "black"
                    else:
                        color = colors[color_index] if color_index < len(colors) else "black"
                    
                    pen = SVGPathPen(font.getGlyphSet())
                    font.getGlyphSet()[layer_glyph].draw(pen)
                    path = pen.getCommands()
                    if path:
                        svg_content.append(f'<path d="{path}" fill="{color}" />')
                
                svg_content.append('</g></svg>')
                
                name = get_name(glyph_to_unicode.get(glyph_name), glyph_name)
                with open(os.path.join(out_dir, f"{name}.svg"), "wb") as f:
                    f.write("\n".join(svg_content).encode('utf-8'))
                count += 1
            print(f"Extraídos {count} SVGs (COLR v0) en {out_dir}")
        else:
            print("La versión COLR v1 es compleja (gradientes/transiciones) y no se puede extraer fácilmente a SVG simple.")

fonts = ['AppleColorEmoji.ttf', 'NotoColorEmoji.ttf', 'twemoji.ttf', 'SegoeUIColorEmoji.ttf', 'openmojicolor.ttf']
for f in fonts:
    if os.path.exists(f):
        extract_from_font(f)
