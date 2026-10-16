import sys
out = sys.argv[1]

def piece(s):
    # ponytail: tailles calées sur la photo du modèle pour une assiette de 23 cm, mises à l'échelle pour les autres
    win_frame = '''<circle r="30" fill="none" stroke="#000" stroke-width="1.2"/>
      <line x1="-30" y1="0" x2="30" y2="0" stroke="#000" stroke-width="1.6"/>
      <line x1="0" y1="-30" x2="0" y2="30" stroke="#000" stroke-width="1.6"/>'''
    ghost = f'''<g transform="translate(35,35)">
      <circle r="30" fill="#fff"/>
      <g clip-path="url(#c{s})"><g transform="translate(-3,-9) scale(0.85)">
        <path d="M-20,32 L-20,-6 A13,13 0 0 1 6,-6 L6,4 Q14,-2 21,2 Q15,10 6,11 L6,32 Z" fill="#fff" stroke="#000" stroke-width="0.6"/>
        <ellipse cx="-12" cy="-8" rx="1.7" ry="2.6"/><ellipse cx="-2" cy="-8" rx="1.7" ry="2.6"/>
        <path d="M-14,-2 Q-7,8 0,-2 Z"/>
        <path d="M-11,1.5 Q-7,5 -3,1.5" fill="#e8636b"/>
      </g></g>{win_frame}</g>'''
    pumpkin = f'''<g transform="translate(115,35)">
      <circle r="30" fill="#fff"/>
      <g clip-path="url(#c{s})"><g transform="translate(14,10) scale(0.62)">
        <path d="M-1,-13 Q-2,-20 2,-22 L4,-20 Q1,-18 2,-13 Z" fill="#3f8a3a" stroke="#1f4d1c" stroke-width="0.4"/>
        <ellipse cy="4" rx="19" ry="17" fill="#f39231" stroke="#c4621a" stroke-width="0.5"/>
        <ellipse cy="4" rx="8" ry="17" fill="none" stroke="#c4621a" stroke-width="0.5"/>
        <path d="M-12,-2 L-5,-2 L-8.5,-8 Z M5,-2 L12,-2 L8.5,-8 Z M-2,4 L2,4 L0,0 Z"/>
        <path d="M-13,8 L-9,11 L-6,8 L-3,12 L0,8 L3,12 L6,8 L9,11 L13,8 Q8,17 0,17 Q-8,17 -13,8 Z"/>
      </g></g>{win_frame}</g>'''
    door = '''<g transform="translate(0,85)">
      <path d="M0,75 L0,35 A45,35 0 0 1 90,35 L90,75 Z" fill="#fff" stroke="#000" stroke-width="1.2"/>
      <circle cx="13" cy="52" r="3" fill="none" stroke="#000" stroke-width="0.7"/>
      <g>
        <path d="M78,70 Q90,66 86,56 Q84,52 87,50" fill="none" stroke="#111" stroke-width="2.4" stroke-linecap="round"/>
        <ellipse cx="68" cy="62" rx="12" ry="11.5" fill="#111"/>
        <path d="M58,47 L58,33 L64,40 Z M78,47 L78,33 L72,40 Z" fill="#111"/>
        <circle cx="68" cy="45" r="10" fill="#111"/>
        <ellipse cx="64" cy="45" rx="2.4" ry="2.8" fill="#fff"/><ellipse cx="72" cy="45" rx="2.4" ry="2.8" fill="#fff"/>
        <circle cx="64.4" cy="45.4" r="1.4"/><circle cx="72.4" cy="45.4" r="1.4"/>
        <path d="M67,49 L69,49 L68,50.2 Z" fill="#f2a0a8"/>
        <path d="M60,54 Q68,57.5 76,54" fill="none" stroke="#f08a24" stroke-width="1.8" stroke-linecap="round"/>
        <ellipse cx="68" cy="36" rx="15" ry="3" fill="#2a2a2a" stroke="#555" stroke-width="0.4"/>
        <path d="M60,36 Q63,24 68,20 Q72,15 80,15 Q74,19 75,27 L76,36 Z" fill="#2a2a2a" stroke="#555" stroke-width="0.4"/>
        <path d="M61,33 L75.4,33" stroke="#8a4fc4" stroke-width="2"/>
      </g></g>'''
    leaf_pts = "48,96 52,96 51,74 72,78 70,70 90,58 84,54 88,40 76,42 74,34 64,46 66,22 58,26 50,8 42,26 34,22 36,46 26,34 24,42 12,40 16,54 10,58 30,70 28,78 49,74"
    leaf = f'''<g transform="translate(92,80) scale(0.68)">
      <polygon points="{leaf_pts}" fill="#a6dc8e" stroke="#2f6b2a" stroke-width="1.4" stroke-linejoin="round"/>
      <path d="M50,74 L50,16 M50,64 L82,47 M50,64 L18,47 M50,46 L64,30 M50,46 L36,30 M50,70 L68,72 M50,70 L32,72" fill="none" stroke="#2f6b2a" stroke-width="0.9"/></g>'''
    stem = '''<g transform="translate(112,155)">
      <path d="M0,50 L0,4 Q11,-2 22,4 L22,50 Z" fill="#8b5a3c" stroke="#000" stroke-width="0.8"/>
      <line x1="0" y1="25" x2="22" y2="25" stroke="#fff" stroke-width="0.5" stroke-dasharray="1.5 1.5"/>
      <text x="11" y="35" font-size="3.6" fill="#fff" text-anchor="middle" font-family="sans-serif">coller</text>
      <text x="11" y="40" font-size="3.6" fill="#fff" text-anchor="middle" font-family="sans-serif">derrière</text></g>'''
    return ghost + pumpkin + door + leaf + stem

pages = []
for d in (18, 23, 26):
    k = d / 23
    w, h = 157 * k, 205 * k
    ox, oy = (210 - w) / 2, 32 + (250 - 32 - h) / 2 if h < 218 else 32
    s = str(d)
    pages.append(f'''<section><svg viewBox="0 0 210 297" width="210mm" height="297mm">
  <defs><clipPath id="c{s}"><circle r="29.4"/></clipPath></defs>
  <text x="105" y="18" font-size="7" text-anchor="middle" font-family="sans-serif" font-weight="bold">Maison citrouille - assiette de {d} cm</text>
  <text x="105" y="25" font-size="3.8" text-anchor="middle" font-family="sans-serif" fill="#555">Imprimer en taille réelle (100 %), puis découper le long des traits.</text>
  <g transform="translate({ox:.1f},{oy:.1f}) scale({k:.4f})">{piece(s)}</g>
</svg></section>''')

html = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Maison citrouille</title>
<style>@page{{size:A4;margin:0}}body{{margin:0}}section{{width:210mm;height:297mm;page-break-after:always;overflow:hidden}}svg{{display:block}}</style>
</head><body>{"".join(pages)}</body></html>'''
open(out, "w").write(html)
