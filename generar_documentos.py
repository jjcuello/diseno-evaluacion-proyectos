"""Genera los diagramas, el PDF imprimible y la página HTML publicable a partir del README.

Uso:
    python3 generar_documentos.py                 # diagramas SVG + PDF
    python3 generar_documentos.py pagina.html     # además, la página HTML en esa ruta
"""
import re
import sys
from pathlib import Path

import markdown
import weasyprint

sys.path.insert(0, str(Path(__file__).parent / 'diagramas'))
import generar as diagramas  # noqa: E402

RAIZ = Path(__file__).parent
EXTENSIONES = ['tables', 'fenced_code', 'sane_lists', 'toc']

CSS_PDF = """@page{size:Letter;margin:2cm}
body{font-family:'DejaVu Sans',sans-serif;font-size:10pt;line-height:1.45;color:#222}
h1{font-size:18pt;border-bottom:2px solid #333;padding-bottom:4px}
h2{font-size:14pt;margin-top:1.4em;border-bottom:1px solid #aaa}
h3{font-size:12pt;margin-top:1.2em}
h4{font-size:11pt;margin-top:1.1em;color:#333}
blockquote{border-left:3px solid #888;margin:0.6em 0;padding:0.2em 0.8em;background:#f4f4f4}
table{border-collapse:collapse;width:100%;font-size:8.5pt;margin:0.6em 0}
th,td{border:1px solid #999;padding:4px 6px;text-align:left;vertical-align:top}
th{background:#e8e8e8}
tr{page-break-inside:avoid}
code{font-family:'DejaVu Sans Mono',monospace;font-size:8.5pt}
hr{border:none;border-top:1px solid #ccc}
li{margin:0.15em 0}
p:has(> img){margin:0.8em 0 0.2em;page-break-inside:avoid}
img{width:100%}
p:has(> em:only-child){font-size:8.5pt;color:#555;margin-top:0}"""

DARK = dict(fg='#dde6e8', muted='#9aabb1', line='#7f9299', surface='#1d282b', bg='#141c1f',
            accent='#4fb3c2', accentbg='#17363b', onaccent='#0e1618', ok='#5cc28a', bad='#f07a6e',
            oe1='#e0a948', oe2='#4fb3c2', oe3='#a58ce6')


def generar_pdf(md):
    cuerpo = markdown.markdown(md, extensions=EXTENSIONES)
    html = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS_PDF}</style>'
            f'</head><body>{cuerpo}</body></html>')
    weasyprint.HTML(string=html, base_url=str(RAIZ)).write_pdf(RAIZ / 'Propuestas-Proyecto-de-Grado.pdf')


def generar_pagina(md, destino):
    svgs = diagramas.generar('variables')
    cuerpo = markdown.markdown(md, extensions=EXTENSIONES)
    cuerpo = re.sub(r'<h1[^>]*>.*?</h1>\s*', '', cuerpo, count=1)

    def figura(m):
        return (f'<figure><div class="lienzo">{svgs[m.group(1)]}</div>'
                f'<figcaption>{m.group(2)}</figcaption></figure>')
    cuerpo = re.sub(r'<p><img alt="[^"]*" src="diagramas/([\w-]+)\.svg" ?/?></p>\s*<p><em>(.*?)</em></p>',
                    figura, cuerpo, flags=re.S)
    cuerpo = re.sub(r'(<table>.*?</table>)', r'<div class="tabla">\1</div>', cuerpo, flags=re.S)
    cuerpo = cuerpo.replace('<li>[ ] ', '<li class="tarea">').replace('<li>\n<p>[ ] ', '<li class="tarea">\n<p>')

    indice = ''.join(
        f'<li class="n{nivel}"><a href="#{ident}">{re.sub("<[^>]+>", "", texto)}</a></li>'
        for nivel, ident, texto in re.findall(r'<h([23]) id="([^"]+)">(.*?)</h\1>', cuerpo))

    claro = ''.join(f'--d-{k}:{v};' for k, v in diagramas.ESTATICO.items() if k != 'font')
    oscuro = ''.join(f'--d-{k}:{v};' for k, v in DARK.items())
    plantilla = (RAIZ / 'diagramas' / 'plantilla.html').read_text(encoding='utf-8')
    pagina = (plantilla.replace('/*D-CLARO*/', claro).replace('/*D-OSCURO*/', oscuro)
              .replace('<!--INDICE-->', indice).replace('<!--CUERPO-->', cuerpo))
    Path(destino).write_text(pagina, encoding='utf-8')


if __name__ == '__main__':
    for nombre, svg in diagramas.generar().items():
        (RAIZ / 'diagramas' / f'{nombre}.svg').write_text(svg, encoding='utf-8')
    md = (RAIZ / 'README.md').read_text(encoding='utf-8')
    generar_pdf(md)
    if len(sys.argv) > 1:
        generar_pagina(md, sys.argv[1])
