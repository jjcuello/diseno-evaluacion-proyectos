"""Genera los diagramas, los PDF de trabajo, la entrega con formato del Manual y la página HTML publicable.

Uso:
    python generar_documentos.py                 # diagramas SVG, PDF de trabajo y entrega (PDF + DOCX)
    python generar_documentos.py pagina.html     # además, la página HTML del documento técnico en esa ruta

Requisitos: markdown y weasyprint (pip), Pandoc para el .docx y, en Windows, Pango de MSYS2
(C:\\msys64\\mingw64\\bin), que el script detecta solo.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).parent
MSYS2_BIN = Path(r'C:\msys64\mingw64\bin')
if os.name == 'nt' and MSYS2_BIN.exists():
    os.environ.setdefault('WEASYPRINT_DLL_DIRECTORIES', str(MSYS2_BIN))

import markdown  # noqa: E402
import weasyprint  # noqa: E402

sys.path.insert(0, str(RAIZ / 'diagramas'))
import generar as diagramas  # noqa: E402

EXTENSIONES = ['tables', 'fenced_code', 'sane_lists', 'toc']
DOCUMENTOS = ['Documento-Tecnico', 'Documento-Metodologico']
ENTREGAS = RAIZ / 'entregas'
REFERENCIA_DOCX = RAIZ / 'plantillas' / 'referencia-manual.docx'

# Datos de la portada (Manual, anexo C-1). Lo que aún no se conoce queda marcado como pendiente.
PORTADA = {
    'encabezado': ['REPÚBLICA BOLIVARIANA DE VENEZUELA',
                   'MINISTERIO DEL PODER POPULAR PARA LA', 'EDUCACIÓN UNIVERSITARIA,', 'CIENCIA Y TECNOLOGÍA',
                   'INSTITUTO UNIVERSITARIO POLITÉCNICO', '"SANTIAGO MARIÑO"', 'EXTENSIÓN CARACAS'],
    'titulo': ['Plataforma web institucional de alojamiento y despliegue continuo',
               '(PaaS) para el Politécnico Santiago Mariño'],
    'leyenda': ['Propuesta de Trabajo de Grado como requisito parcial para optar al Título de',
                'Ingeniero de Sistemas'],
    'version': 'Avance para revisión: Capítulo I',
    'datos': [('Autor', 'José Javier Cuello Camargo'),
              ('Tutor(a)', '[PENDIENTE]'),
              ('Docente de la asignatura', 'Carmen Díaz')],
    'lugar_fecha': 'Caracas, octubre de 2026',
}
ARCHIVO_ENTREGA = 'Propuesta-Trabajo-de-Grado'

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

# Formato del Manual del IUPSM, cap. V: carta; márgenes 4/3/3/3 cm; Arial 12; interlineado 1,5; sangría de
# 5 espacios; capítulos en página nueva a 5 cm; preliminares en romanos y cuerpo en arábigos, centrados abajo.
CSS_MANUAL = """
@page{size:Letter;margin:3cm 3cm 3cm 4cm;
  @bottom-center{content:counter(page);font:10pt Arial,'Liberation Sans',sans-serif;
    vertical-align:bottom;padding-bottom:1.5cm}}
@page portada{@bottom-center{content:none}}
@page preliminar{@bottom-center{content:counter(page,lower-roman)}}
body{font-family:Arial,'Liberation Sans',sans-serif;font-size:12pt;line-height:1.5;color:#000}
.portada{page:portada;break-after:page;height:21.9cm;display:flex;flex-direction:column;
  text-align:center;line-height:1.15}
.portada .encabezado{font-weight:bold;font-size:11pt}
.portada .titulo{margin-top:5.5cm;font-weight:bold}
.portada .leyenda{font-size:11pt;margin-top:0.2cm}
.portada .version{font-size:11pt;font-style:italic;margin-top:0.6cm}
.portada .datos{margin-top:auto;text-align:right;font-size:11pt}
.portada .lugar{margin-top:1.5cm;font-size:11pt}
.preliminar{page:preliminar;break-after:page}
.preliminar h2,h2.referencias{text-align:center;font-size:12pt;font-weight:bold;margin:0 0 24pt}
.indice ol{list-style:none;padding:0;margin:0}
.indice li{margin:0}
.indice li.n2{font-weight:bold;margin-top:10pt}
.indice li.n3{padding-left:1.27cm}
.indice a{color:#000;text-decoration:none}
.indice li{display:flex}
.indice .txt{flex:1;min-width:0;overflow:hidden;white-space:nowrap}
.indice .txt::after{content:" ........................................................................................................................................"}
.indice .num{padding-left:4pt}
p{margin:0;text-indent:1.27cm;text-align:justify;orphans:2;widows:2}
h2.capitulo{break-before:page;padding-top:2cm;margin:0 0 24pt;text-align:center;font-size:12pt}
h2.capitulo span{display:block}
h2.capitulo span+span{margin-top:12pt}
h2.referencias{break-before:page}
h3{text-align:center;font-size:12pt;font-weight:bold;margin:24pt 0 12pt;break-after:avoid}
h4{text-align:center;font-size:12pt;font-weight:bold;font-style:italic;margin:24pt 0 12pt;break-after:avoid}
h5{text-align:left;font-size:12pt;font-weight:normal;font-style:italic;margin:18pt 0 6pt;break-after:avoid}
ul,ol{margin:0 0 0 1.27cm;padding-left:0.6cm}
li{text-align:justify}
p.ref{text-indent:-1.27cm;padding-left:1.27cm;line-height:1.15;margin-bottom:6pt;text-align:left}
mark{background:#fff0a0;font-size:10.5pt}
"""

DARK = dict(fg='#dde6e8', muted='#9aabb1', line='#7f9299', surface='#1d282b', bg='#141c1f',
            accent='#4fb3c2', accentbg='#17363b', onaccent='#0e1618', ok='#5cc28a', bad='#f07a6e',
            oe1='#e0a948', oe2='#4fb3c2', oe3='#a58ce6')

CAPITULO = re.compile(r'^## (CAPÍTULO [IVXL]+)\. (.+)$', re.M)


def generar_pdf(md, nombre):
    cuerpo = markdown.markdown(md, extensions=EXTENSIONES)
    html = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS_PDF}</style>'
            f'</head><body>{cuerpo}</body></html>')
    weasyprint.HTML(string=html, base_url=str(RAIZ)).write_pdf(RAIZ / f'{nombre}.pdf')


def extraer_entrega(md):
    """Toma desde el capítulo I hasta el final, sin capítulos pendientes, separadores ni notas internas."""
    md = md[md.index('## CAPÍTULO I'):]
    md = re.sub(r'(?m)^---\s*$', '', md)
    secciones = re.split(r'(?m)^(?=## )', md)
    secciones = [s for s in secciones if not re.fullmatch(r'## [^\n]+\n+\*Pendiente\.\*\s*', s)]
    md = ''.join(secciones)
    md = re.sub(r'(?m)^\*Provisional[^\n]*\n', '', md)
    return md


def portada_html():
    p = PORTADA
    datos = ''.join(f'<div><b>{k}:</b> {v}</div>' for k, v in p['datos'])
    return ('<section class="portada">'
            f'<div class="encabezado">{"<br>".join(p["encabezado"])}</div>'
            f'<div class="titulo">{"<br>".join(p["titulo"])}</div>'
            f'<div class="leyenda">{"<br>".join(p["leyenda"])}</div>'
            f'<div class="version">{p["version"]}</div>'
            f'<div class="datos">{datos}</div>'
            f'<div class="lugar">{p["lugar_fecha"]}</div></section>')


def generar_entrega_pdf(md):
    cuerpo = markdown.markdown(extraer_entrega(md), extensions=EXTENSIONES)
    cuerpo = re.sub(r'<h2 id="([^"]+)">(CAPÍTULO [IVXL]+)\. (.*?)</h2>',
                    r'<h2 class="capitulo" id="\1"><span>\2</span><span>\3</span></h2>', cuerpo)
    i = cuerpo.find('<h2 id="referencias">')
    if i >= 0:
        cola = cuerpo[i:].replace('<h2 id="referencias">Referencias</h2>',
                                  '<h2 class="referencias" id="referencias">REFERENCIAS</h2>')
        cuerpo = cuerpo[:i] + cola.replace('<p>', '<p class="ref">')
    cuerpo = re.sub(r'<code>(\[[^<]*\])</code>', r'<mark>\1</mark>', cuerpo)

    def documento(contenido):
        html = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS_MANUAL}</style>'
                f'</head><body>{contenido}</body></html>')
        return weasyprint.HTML(string=html, base_url=str(RAIZ)).render()

    # El cuerpo se pagina aparte para que empiece en 1; con sus anclas se arma el índice de las preliminares.
    doc_cuerpo = documento(cuerpo)
    pagina_de = {ancla: n for n, pag in enumerate(doc_cuerpo.pages, 1) for ancla in pag.anchors}
    entradas = []
    for nivel, ident, texto in re.findall(r'<h([23])[^>]*id="([^"]+)"[^>]*>(.*?)</h\1>', cuerpo):
        texto = re.sub(r'<[^>]+>', '', re.sub(r'</span><span>', '. ', texto))
        entradas.append(f'<li class="n{nivel}"><span class="txt">{texto}</span>'
                        f'<span class="num">{pagina_de.get(ident, "")}</span></li>')
    indice = ('<section class="preliminar indice"><h2>ÍNDICE GENERAL</h2>'
              f'<ol>{"".join(entradas)}</ol></section>')
    doc_prelim = documento(portada_html() + indice)

    ENTREGAS.mkdir(exist_ok=True)
    destino = ENTREGAS / f'{ARCHIVO_ENTREGA}.pdf'
    doc_prelim.copy(doc_prelim.pages + doc_cuerpo.pages).write_pdf(destino)
    return destino


def generar_entrega_docx(md):
    p = PORTADA

    def bloque(estilo, lineas):
        return f'::: {{custom-style="{estilo}"}}\n' + '\\\n'.join(lineas) + '\n:::\n\n'

    datos = [f'**{k}:** {v}' for k, v in p['datos']]
    salto = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'
    portada = (bloque('Portada Encabezado', p['encabezado'])
               + '&nbsp;\n\n' * 6 + bloque('Portada Titulo', p['titulo'])
               + bloque('Portada Leyenda', p['leyenda']) + bloque('Portada Leyenda', [f'*{p["version"]}*'])
               + '&nbsp;\n\n' * 6 + bloque('Portada Datos', datos)
               + '&nbsp;\n\n' * 2 + bloque('Portada Lugar', [p['lugar_fecha']]))

    cuerpo = extraer_entrega(md)
    cuerpo = CAPITULO.sub(lambda m: f'## {m[1]}\n\n::: {{custom-style="Nombre de Capítulo"}}\n{m[2]}\n:::', cuerpo)
    i = cuerpo.find('## Referencias')
    if i >= 0:
        refs = [r.strip() for r in cuerpo[i + len('## Referencias'):].split('\n\n') if r.strip()]
        cuerpo = cuerpo[:i] + '## REFERENCIAS\n\n' + ''.join(bloque('Referencia', [r]) for r in refs)

    ENTREGAS.mkdir(exist_ok=True)
    destino = ENTREGAS / f'{ARCHIVO_ENTREGA}.docx'
    subprocess.run(['pandoc', '-f', 'markdown', '-t', 'docx', '--reference-doc', str(REFERENCIA_DOCX),
                    '-o', str(destino)], input=portada + salto + cuerpo, text=True, encoding='utf-8',
                   check=True)
    return destino


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
    for nombre in DOCUMENTOS:
        generar_pdf((RAIZ / f'{nombre}.md').read_text(encoding='utf-8'), nombre)
    metodologico = (RAIZ / 'Documento-Metodologico.md').read_text(encoding='utf-8')
    print('Entrega:', generar_entrega_pdf(metodologico))
    print('Entrega:', generar_entrega_docx(metodologico))
    if len(sys.argv) > 1:
        generar_pagina((RAIZ / 'Documento-Tecnico.md').read_text(encoding='utf-8'), sys.argv[1])
