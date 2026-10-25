"""Génère le motif jacquard du pull de Pauk (bande horizontale répétable) en SVG.

Usage : python pull.py ../assets/pull.svg          (motif complet)
        python pull.py ../assets/pull-lisere.svg lisere  (bande fine)
"""
import sys

W = 16  # largeur d'une répétition, en mailles
S = 6   # taille d'une maille, en px

colors = {  # couleur, ombre (fond entre les mailles)
    "D": ("#1B1F3B", "#10132A"),
    "R": ("#C8372D", "#962820"),
    "C": ("#F3E7D3", "#D6C7AE"),
    "O": ("#D9A441", "#A97C2C"),
}

rows = []
rows += ["D" * W]
rows += ["DDDCDDDDDDDCDDDD", "DDCCCDDDDDCCCDDD", "DDDCDDDDDDDCDDDD"]
rows += ["D" * W, "R" * W]

# grand losange concentrique centré colonne 7, croix ocre entre les losanges
band = []
for y in range(6, 19):
    row = []
    for x in range(W):
        d = abs(x - 7) + abs(y - 12)
        c = "C"
        if d <= 5:
            c = {5: "R", 4: "C", 3: "R", 2: "D", 1: "C", 0: "D"}[d]
        dx = min(abs(x - 15), abs(x + 1))  # distance horizontale à la colonne 15 (avec bouclage)
        if (dx == 0 and abs(y - 12) <= 2) or (y == 12 and dx <= 2):
            c = "O"
        row.append(c)
    band.append("".join(row))
rows += band

rows += ["R" * W, "D" * W]
rows += ["RCCC" * 4, "RRCR" * 4, "R" * W, "D" * W]

if len(sys.argv) > 2 and sys.argv[2] == "lisere":  # bande fine : dents de scie du bas
    rows = rows[19:]

H = len(rows)
out = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W*S}" height="{H*S}" viewBox="0 0 {W*S} {H*S}" shape-rendering="geometricPrecision">',
       "<defs>"]
for k, (fill, _) in colors.items():
    out.append(f'<g id="{k}" fill="{fill}"><ellipse cx="1.75" cy="3" rx="1.55" ry="2.9" transform="rotate(-28 1.75 3)"/>'
               f'<ellipse cx="4.25" cy="3" rx="1.55" ry="2.9" transform="rotate(28 4.25 3)"/></g>')
out.append("</defs>")
for y, row in enumerate(rows):
    x = 0
    while x < W:  # fond : une bande par suite de même couleur
        k = row[x]
        x2 = x
        while x2 < W and row[x2] == k:
            x2 += 1
        out.append(f'<rect x="{x*S}" y="{y*S}" width="{(x2-x)*S}" height="{S}" fill="{colors[k][1]}"/>')
        x = x2
for y, row in enumerate(rows):
    for x, k in enumerate(row):
        out.append(f'<use href="#{k}" xlink:href="#{k}" x="{x*S}" y="{y*S}"/>')
out.append("</svg>")
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(out))
print(f"{W*S}x{H*S}px, {H} rangs")
for r in rows:
    print(r)
