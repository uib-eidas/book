#!/usr/bin/env python3
"""Generates content/eidas/11-summary/img/mapa-termes.svg: the trust triangle (emissors, usuari, part usuària)
with the wallet at the centre, the trust infrastructure as the base, and the trust services and protocols at the sides.
Edit the term lists or the arrows below and run: python3 tools/scripts/build-term-map.py"""
import os
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "content", "eidas", "11-summary", "img", "mapa-termes.svg")
W, H = 960, 760
FS, CH, GAP, PAD = 12, 22, 5, 10
BLUE, ORANGE = "#0065bd", "#b3541e"
svg = []

def width(s): return int(6.2 * len(s)) + PAD * 2

def chips_in(x, w, chips, start_y):
    cw = w - 20; rows = [[]]; cx = 0
    for text, hl in chips:
        cwid = min(width(text), cw)
        if cx + cwid > cw and rows[-1]: rows.append([]); cx = 0
        rows[-1].append((cx, text, hl, cwid)); cx += cwid + GAP
    for li, row in enumerate(rows):
        used = sum(ww for *_, ww in row) + GAP * (len(row) - 1); off = (cw - used) / 2
        cy = start_y + li * (CH + GAP)
        for cx, text, hl, ww in row:
            fill, stroke = ("#fff4e0", ORANGE) if hl else ("#e8f1fa", BLUE)
            svg.append(f'<rect x="{x+10+off+cx:.0f}" y="{cy}" width="{ww}" height="{CH}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
            svg.append(f'<text x="{x+10+off+cx+ww/2:.0f}" y="{cy+CH/2+4:.0f}" font-size="{FS}" fill="#1a1a1a">{text}</text>')
    return start_y + len(rows) * (CH + GAP)

def block(x, y, w, h, title, chips=(), hl=False, sub=None, note=None):
    fill, stroke = ("#fff8ec", ORANGE) if hl else ("#f6f9fc", BLUE)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>')
    svg.append(f'<text x="{x+w/2:.0f}" y="{y+22}" font-weight="bold" font-size="16" fill="{ORANGE if hl else BLUE}">{title}</text>')
    yy = y + 34
    if sub:
        for stitle, schips in sub:
            svg.append(f'<text x="{x+w/2:.0f}" y="{yy+12}" font-weight="bold" font-size="13" fill="{BLUE}">{stitle}</text>')
            yy = chips_in(x, w, schips, yy + 20) + 6
    elif chips:
        yy = chips_in(x, w, chips, yy)
    if note:
        svg.append(f'<text x="{x+w/2:.0f}" y="{yy+14}" font-size="12" fill="#444444">{note}</text>')

svg += [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" text-anchor="middle">',
        f'<defs><marker id="f" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{BLUE}"/></marker>'
        f'<marker id="fo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{ORANGE}"/></marker></defs>',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>']

# Geometry: side columns 20..250 and 710..940; centre column 320..640; base bar at the bottom.
SX, SW, CX, CW, RX = 20, 230, 320, 320, 710
TOP, TH = 96, 230          # side blocks, upper row
BOT, BH = 356, 200         # side blocks, lower row (the two base vertices of the triangle)
BAR_Y, BAR_H = 596, 140

# (svg element, label, (x, y), anchor, colour)
ARROWS = [
    (f'<line x1="480" y1="68" x2="480" y2="94" stroke="{ORANGE}" stroke-width="2.5" marker-end="url(#fo)"/>', "controla", (492, 86), "start", ORANGE),
    (f'<line x1="{SX+SW+2}" y1="{TOP+120}" x2="{CX-2}" y2="{TOP+120}" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#f)"/>', "QES", (285, TOP+108), "middle", ORANGE),
    (f'<line x1="{SX+SW+2}" y1="{BOT+100}" x2="{CX-2}" y2="{BOT+100}" stroke="{BLUE}" stroke-width="3" marker-end="url(#f)"/>', "emet", (285, BOT+88), "middle", ORANGE),
    (f'<line x1="{CX+CW+2}" y1="{TOP+120}" x2="{RX-2}" y2="{TOP+120}" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#f)"/>', "usa", (675, TOP+108), "middle", ORANGE),
    (f'<line x1="{CX+CW+2}" y1="{BOT+100}" x2="{RX-2}" y2="{BOT+100}" stroke="{BLUE}" stroke-width="3" marker-end="url(#f)"/>', "presenta", (675, BOT+88), "middle", ORANGE),
    (f'<line x1="135" y1="{BAR_Y-2}" x2="135" y2="{BOT+BH+2}" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#f)"/>', "registra", (145, BAR_Y-14), "start", ORANGE),
    (f'<line x1="480" y1="{BAR_Y-2}" x2="480" y2="{TOP+460+2}" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#f)"/>', "certifica", (490, BAR_Y-14), "start", ORANGE),
    (f'<line x1="825" y1="{BAR_Y-2}" x2="825" y2="{BOT+BH+2}" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#f)"/>', "registra", (835, BAR_Y-14), "start", ORANGE),
]
for el, *_ in ARROWS: svg.append(el)

block(380, 24, 200, 44, "Usuari (titular)", hl=True)
block(CX, TOP, CW, 460, "Cartera (EUDI Wallet)", sub=[
    ("Unitat de cartera", [("Proveïdor: estat o organització reconeguda", 0), ("Solució de cartera (certificada)", 0), ("Instància · WSCA · WSCD", 0), ("Magatzem de claus · QSCD", 0), ("WIA · KA (acreditacions)", 0), ("Estats: instal·lada · operativa · vàlida · revocada", 0)]),
    ("Credencials", [("PID", 1), ("EAA: QEAA · Pub-EAA · no qualificada", 1), ("Formats: mdoc · SD-JWT VC", 0), ("W3C VCDM (opcional)", 0), ("Divulgació selectiva", 0), ("Vinculació al dispositiu", 0), ("Revocació", 0), ("Llibre de regles · esquema", 0)]),
])
block(SX, TOP, SW, TH, "Serveis de confiança", [("Signatura (QES) · segell", 1), ("Segell de temps", 0), ("Entrega certificada", 0), ("QWAC", 0), ("Arxiu electrònic", 0), ("Llibres majors electrònics", 0), ("Signatura en remot (QESRC)", 0)])
block(SX, BOT, SW, BH, "Emissors", [("Proveïdor de PID", 1), ("Proveïdors d'EAA", 1), ("QTSP · públic · no qualificat", 0), ("Fonts autèntiques", 0), ("Catàleg d'esquemes i d'atributs", 0)], hl=True)
block(RX, TOP, SW, TH, "Protocols", [("OpenID4VCI (emissió)", 0), ("OpenID4VP (remot)", 0), ("ISO/IEC 18013-5 (presencial)", 0), ("ISO/IEC 18013-7", 0), ("HAIP · DCQL", 0), ("API de credencials digitals", 0), ("Dades transaccionals", 0)])
block(RX, BOT, SW, BH, "Part usuària", [("Verificador", 1), ("Banc · botiga · administració", 0), ("Intermediaris", 0), ("Certificat d'accés", 0), ("Certificat de registre", 0)], hl=True)
block(SX, BAR_Y, W - 2 * SX, BAR_H, "Infraestructura de confiança",
      [("Certificats X.509", 1), ("Àncora de confiança", 0), ("Llistes de confiança (ETSI TS 119 612)", 0), ("LoTE (ETSI TS 119 602)", 0), ("Registrador", 0), ("Autoritat de certificats d'accés", 0), ("CAB · NAB · Supervisió", 0), ("Certificació de carteres (CSA · ENISA)", 0)],
      note="La part usuària es fia d'un emissor que no coneix perquè és a les llistes de confiança")

for _, lab, (lx, ly), anc, col in ARROWS:
    svg.append(f'<text x="{lx}" y="{ly}" font-size="12" fill="{col}" font-weight="bold" text-anchor="{anc}">{lab}</text>')
svg.append("</svg>")
with open(OUT, "w", encoding="utf-8") as f: f.write("\n".join(svg) + "\n")
print("escrit", os.path.normpath(OUT))
