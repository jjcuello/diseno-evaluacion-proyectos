"""Genera los diagramas de la propuesta 1 como SVG.

Modo "estatico": colores fijos y fondo blanco (README en GitHub y PDF).
Modo "variables": colores como variables CSS (--d-*) para la página publicada,
de modo que los diagramas sigan el tema claro u oscuro del lector.
"""
import html
import math
from pathlib import Path

ESTATICO = dict(
    fg='#1f2a30', muted='#56646b', line='#7d8b91', surface='#eef3f4',
    bg='#ffffff', accent='#0b6e7f', accentbg='#dcf0f2', onaccent='#ffffff',
    ok='#2f7d4f', bad='#b3362c', oe1='#9a6412', oe2='#0b6e7f', oe3='#6b4fa8',
    font="'DejaVu Sans', sans-serif",
)
TOKENS = [k for k in ESTATICO if k != 'font']
VARIABLES = {k: f'var(--d-{k})' for k in TOKENS}
VARIABLES['font'] = 'var(--font-body)'


class Diagrama:
    def __init__(self, w, h, etiqueta, pal, fondo):
        self.w, self.h, self.etiqueta, self.p = w, h, etiqueta, pal
        self.partes = []
        if fondo:
            self.partes.append(f'<rect x="0" y="0" width="{w}" height="{h}" style="fill:{pal["bg"]}"/>')

    def rect(self, x, y, w, h, fill='surface', stroke='line', dash=False, rx=6, sw=1.2):
        d = ';stroke-dasharray:5 4' if dash else ''
        f = 'none' if fill is None else self.p[fill]
        self.partes.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'style="fill:{f};stroke:{self.p[stroke]};stroke-width:{sw}{d}"/>')

    def poligono(self, pts, fill, stroke=None, sw=1.2):
        s = f';stroke:{self.p[stroke]};stroke-width:{sw}' if stroke else ''
        pp = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        self.partes.append(f'<polygon points="{pp}" style="fill:{self.p[fill]}{s}"/>')

    def linea(self, pts, color='line', dash=False, sw=1.5):
        d = ';stroke-dasharray:6 4' if dash else ''
        pp = ' '.join(f'{x},{y}' for x, y in pts)
        self.partes.append(
            f'<polyline points="{pp}" style="fill:none;stroke:{self.p[color]};stroke-width:{sw}{d}"/>')

    def flecha(self, pts, color='line', dash=False, sw=1.5):
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        largo = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / largo, (y2 - y1) / largo
        nx, ny = -uy, ux
        cuerpo = pts[:-1] + [(x2 - 8 * ux, y2 - 8 * uy)]
        self.linea(cuerpo, color, dash, sw)
        self.poligono([(x2, y2), (x2 - 10 * ux + 4.5 * nx, y2 - 10 * uy + 4.5 * ny),
                       (x2 - 10 * ux - 4.5 * nx, y2 - 10 * uy - 4.5 * ny)], color)

    def texto(self, x, y, t, size=12, color='fg', anchor='start', bold=False):
        w = ';font-weight:700' if bold else ''
        self.partes.append(
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
            f'style="fill:{self.p[color]};font-size:{size}px{w}">{html.escape(t)}</text>')

    def caja(self, x, y, w, h, lineas, fill='surface', stroke='line', centro=True, color='fg'):
        """Caja con un título en negrita y líneas secundarias, centradas vertical y horizontalmente."""
        self.rect(x, y, w, h, fill, stroke)
        n = len(lineas)
        y0 = y + h / 2 - (n - 1) * 9 + 4
        for i, t in enumerate(lineas):
            cx = x + w / 2 if centro else x + 14
            self.texto(cx, y0 + i * 18, t, 12 if i == 0 else 11,
                       color if i == 0 else ('muted' if color == 'fg' else color),
                       'middle' if centro else 'start', bold=(i == 0))

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'role="img" aria-label="{html.escape(self.etiqueta)}" '
                f'style="max-width:100%;height:auto;font-family:{self.p["font"]}">'
                + ''.join(self.partes) + '</svg>')


def embudo(pal, fondo):
    d = Diagrama(760, 266, 'Del problema al título: el estudio macro, meso y micro converge en el título, '
                 'y el título en infinitivo es el objetivo general.', pal, fondo)
    cx = 380
    bandas = [
        (10, 740, 660, 'MACRO', 'PaaS comerciales extranjeros: cobro en divisas, condiciones cambiantes'),
        (62, 650, 570, 'MESO', 'Venezuela: barreras de pago y universidades sin infraestructura'),
        (114, 560, 480, 'MICRO', 'Politécnico: proyectos perdidos y despliegues manuales'),
        (166, 470, 410, 'TÍTULO', 'Plataforma web institucional (PaaS) del Politécnico'),
    ]
    for i, (y, tw, bw, etq, txt) in enumerate(bandas):
        titulo = i == 3
        d.poligono([(cx - tw / 2, y), (cx + tw / 2, y), (cx + bw / 2, y + 44), (cx - bw / 2, y + 44)],
                   'accentbg' if titulo else 'surface', 'accent' if titulo else 'line')
        d.texto(cx, y + 17, etq, 11, 'accent' if titulo else 'muted', 'middle', bold=True)
        d.texto(cx, y + 35, txt, 12, 'fg', 'middle', bold=titulo)
    d.rect(cx - 190, 218, 380, 44, 'accent', 'accent')
    d.texto(cx, 235, 'OBJETIVO GENERAL', 11, 'onaccent', 'middle', bold=True)
    d.texto(cx, 253, 'Desarrollar + el título (un solo verbo)', 12, 'onaccent', 'middle')
    return d.svg()


def topologia(pal, fondo):
    d = Diagrama(900, 440, 'Topología física: tres nodos k3s en un segmento aislado de la red del Politécnico; '
                 'el tráfico HTTPS entra por el borde de red hacia Traefik en el nodo 1.', pal, fondo)
    d.rect(246, 8, 646, 424, None, 'line', dash=True, rx=10)
    d.texto(262, 28, 'POLITÉCNICO SANTIAGO MARIÑO', 11, 'muted', bold=True)
    d.rect(478, 36, 404, 384, None, 'accent', dash=True, rx=10)
    d.texto(494, 54, 'Segmento de red aislado', 11, 'accent', bold=True)

    d.caja(16, 64, 150, 50, ['Estudiantes', 'y docentes'])
    d.caja(16, 150, 150, 50, ['GitHub / GitLab', 'repositorios'])
    d.caja(262, 64, 200, 64, ['Borde de red', '*.paas.psm.edu.ve → :80/:443', 'IP pública o Cloudflare Tunnel'])
    d.caja(262, 204, 200, 56, ['Administración (DTI)', 'SSH con llave, sin contraseña'])

    d.rect(496, 64, 370, 110)
    d.texto(512, 86, 'Nodo 1 · servidor k3s (plano de control)', 13, bold=True)
    d.texto(512, 110, 'Traefik (entrada HTTPS) · API del PaaS · panel web', 11, 'muted')
    d.texto(512, 130, 'PostgreSQL · Redis (cola) · registro de imágenes', 11, 'muted')
    d.texto(512, 156, 'Punto único de falla', 11, 'bad', bold=True)

    d.caja(496, 204, 370, 36, ['Switch Gigabit · cable Cat6 · IPs estáticas'])
    for x, n in ((496, 2), (691, 3)):
        d.rect(x, 268, 175, 84)
        d.texto(x + 16, 290, f'Nodo {n} · agente k3s', 12, bold=True)
        d.texto(x + 16, 314, 'Apps de estudiantes', 11, 'muted')
        d.texto(x + 16, 334, 'Jobs de compilación', 11, 'muted')
    d.caja(496, 374, 370, 34, ['UPS · respaldo eléctrico (no es alta disponibilidad)'])

    d.linea([(681, 174), (681, 204)])
    d.linea([(583, 240), (583, 268)])
    d.linea([(778, 240), (778, 268)])
    d.flecha([(166, 89), (262, 89)], 'accent', sw=2)
    d.texto(214, 81, 'HTTPS', 11, 'accent', 'middle', bold=True)
    d.flecha([(462, 96), (496, 96)], 'accent', sw=2)
    d.flecha([(166, 175), (362, 175), (362, 128)])
    d.texto(214, 167, 'webhook', 11, 'muted', 'middle')
    d.flecha([(462, 222), (496, 222)])
    return d.svg()


def flujo(pal, fondo):
    d = Diagrama(970, 300, 'Flujo de despliegue: el código llega por webhook o zip, la API lo encola, '
                 'un Job compila con BuildKit o Buildpacks según haya Dockerfile, la imagen va al registro '
                 'y la API crea los recursos en k3s.', pal, fondo)
    d.caja(10, 60, 160, 44, ['git push', 'webhook GitHub/GitLab'])
    d.caja(10, 120, 160, 44, ['Archivo zip', 'carga desde el panel'])
    d.flecha([(170, 82), (200, 82), (200, 110), (230, 110)])
    d.flecha([(170, 142), (200, 142), (200, 110), (230, 110)])
    d.caja(230, 82, 140, 56, ['API del PaaS', 'valida sesión y cuota'])
    d.flecha([(370, 110), (430, 110)])
    d.texto(400, 102, 'encola', 11, 'muted', 'middle')
    d.caja(430, 82, 120, 56, ['Cola', 'Redis'])
    d.flecha([(550, 110), (590, 110)])
    d.poligono([(650, 70), (710, 110), (650, 150), (590, 110)], 'accentbg', 'accent')
    d.texto(650, 114, '¿Dockerfile?', 12, 'fg', 'middle', bold=True)

    d.rect(780, 38, 180, 142, None, 'line', dash=True, rx=10)
    d.texto(870, 30, 'Job efímero · máx. 15 min', 11, 'muted', 'middle')
    d.linea([(710, 110), (750, 110)])
    d.flecha([(750, 110), (750, 75), (790, 75)])
    d.flecha([(750, 110), (750, 145), (790, 145)])
    d.texto(742, 90, 'sí', 11, 'fg', 'end', bold=True)
    d.texto(742, 138, 'no', 11, 'fg', 'end', bold=True)
    d.caja(790, 50, 160, 50, ['BuildKit rootless', 'usa el Dockerfile'])
    d.caja(790, 120, 160, 50, ['Paketo Buildpacks', 'detecta el lenguaje'])

    d.flecha([(870, 180), (870, 235)])
    d.texto(878, 212, 'push', 11, 'muted')
    d.caja(790, 235, 160, 50, ['Registro privado', 'TLS + autenticación'])
    d.flecha([(790, 260), (730, 260)])
    d.texto(760, 252, 'imagen', 11, 'muted', 'middle')
    d.caja(470, 232, 260, 56, ['La API crea en k3s', 'Deployment · Service · IngressRoute'])
    d.flecha([(470, 260), (410, 260)], 'accent', sw=2)
    d.caja(150, 232, 260, 56, ['app.paas.psm.edu.ve', 'HTTPS vía Traefik'], 'accentbg', 'accent')
    return d.svg()


def aislamiento(pal, fondo):
    d = Diagrama(900, 380, 'Aislamiento: cada estudiante tiene su namespace; solo se permite la entrada por Traefik '
                 'y la salida a internet; el tráfico hacia otros estudiantes, la API de Kubernetes y la red '
                 'interna del Politécnico está bloqueado.', pal, fondo)
    d.caja(20, 30, 150, 50, ['Internet'])
    d.caja(20, 165, 150, 50, ['Traefik', 'entrada HTTPS'])
    d.caja(640, 20, 240, 50, ['API de Kubernetes', 'plano de control'])
    d.caja(240, 315, 300, 50, ['Red interna del Politécnico'])
    for x, w, letra in ((240, 300, 'a'), (640, 240, 'b')):
        d.rect(x, 110, w, 160, None, 'accent', dash=True, rx=10)
        d.texto(x + 16, 130, f'namespace: estudiante-{letra}', 11, 'accent', bold=True)
        d.texto(x + 16, 146, 'ResourceQuota · LimitRange', 11, 'muted')
    d.caja(270, 160, 240, 80, ['App del estudiante A', 'sin root · sin privilegios', '256 MiB · ½ CPU'], 'bg')
    d.caja(660, 160, 200, 80, ['App del estudiante B', 'sin root · sin privilegios', '256 MiB · ½ CPU'], 'bg')

    d.flecha([(95, 80), (95, 165)], 'ok', sw=2)
    d.texto(103, 126, 'HTTPS', 11, 'ok', bold=True)
    d.flecha([(170, 190), (270, 190)], 'ok', sw=2)
    d.texto(205, 182, 'Ingress', 11, 'ok', 'middle', bold=True)
    d.flecha([(480, 160), (480, 55), (170, 55)], 'ok', sw=2)
    d.texto(325, 47, 'salida a internet (80/443)', 11, 'ok', 'middle', bold=True)

    d.flecha([(510, 205), (660, 205)], 'bad', dash=True, sw=2)
    d.texto(585, 197, '✕ bloqueado', 11, 'bad', 'middle', bold=True)
    d.flecha([(510, 175), (590, 175), (590, 45), (640, 45)], 'bad', dash=True, sw=2)
    d.texto(598, 100, '✕ sin token', 11, 'bad', bold=True)
    d.flecha([(390, 240), (390, 315)], 'bad', dash=True, sw=2)
    d.texto(398, 290, '✕ bloqueado', 11, 'bad', bold=True)
    return d.svg()


def cronograma(pal, fondo):
    d = Diagrama(900, 284, 'Cronograma de 18 semanas: diagnóstico en las semanas 1 a 4, diseño 5 a 6, '
                 'construcción 7 a 13, pruebas técnicas 14, piloto 15 a 17 y análisis 18.', pal, fondo)
    x0, sw, y0, rh = 210, 37, 36, 34
    d.texto(16, 24, 'Semana', 11, 'muted', bold=True)
    for s in range(1, 19):
        d.texto(x0 + (s - 0.5) * sw, 24, str(s), 11, 'muted', 'middle')
    filas = [
        ('Diagnóstico', 1, 4, 'oe1', 'instrumentos + campo'),
        ('Diseño', 5, 6, 'oe2', ''),
        ('Construcción', 7, 13, 'oe2', 'clúster → compilación → API → panel'),
        ('Pruebas técnicas', 14, 14, 'oe3', ''),
        ('Piloto (2–3 asignaturas)', 15, 17, 'oe3', ''),
        ('Análisis e informe', 18, 18, 'oe3', ''),
    ]
    fin = y0 + len(filas) * rh
    for s in range(19):
        d.linea([(x0 + s * sw, 32), (x0 + s * sw, fin)], 'surface', sw=1)
    for i, (nombre, a, b, oe, txt) in enumerate(filas):
        y = y0 + i * rh
        d.texto(16, y + 21, nombre, 12)
        d.rect(x0 + (a - 1) * sw + 2, y + 7, (b - a + 1) * sw - 4, 20, oe, oe, rx=4)
        if txt:
            d.texto(x0 + (a - 1 + (b - a + 1) / 2) * sw, y + 21, txt, 11, 'onaccent', 'middle', bold=True)
    ly = fin + 26
    for j, (oe, txt) in enumerate((('oe1', 'OE1 · Diagnosticar'), ('oe2', 'OE2 · Diseñar'),
                                   ('oe3', 'OE3 · Evaluar'))):
        x = x0 + j * 180
        d.rect(x, ly - 11, 14, 14, oe, oe, rx=3)
        d.texto(x + 22, ly, txt, 12)
    return d.svg()


DIAGRAMAS = {
    'embudo-problema': embudo,
    'topologia': topologia,
    'flujo-despliegue': flujo,
    'aislamiento': aislamiento,
    'cronograma': cronograma,
}


def generar(modo='estatico'):
    pal = ESTATICO if modo == 'estatico' else VARIABLES
    return {n: f(pal, modo == 'estatico') for n, f in DIAGRAMAS.items()}


if __name__ == '__main__':
    carpeta = Path(__file__).parent
    for nombre, svg in generar().items():
        (carpeta / f'{nombre}.svg').write_text(svg, encoding='utf-8')
        print('escrito', nombre)
