# file: gelcoat-nomogram.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2018-11-14T19:32:44+0100
# Last modified: 2018-11-18T16:08:20+0100
"""Create a nomogram for gelcoat/peroxide ratio"""

import math
from geom2 import line, intersect

print("% Generated by gelcoat-nomogram.py")
print("(align.inc) runlibfile")
print("(units.inc) runlibfile")
print("/Alegreya-Regular findfont 12 scalefont setfont")
print("2 setlinecap")

# Axis locations
xgel = 20  # mm
xper = 80  # mm


def ygel(g):
    """Calculates the y position for a given amount of gelcoat."""
    return 10 + (g - 600) * 1


def yper(p):
    """Calculates the y position for a given amount of peroxide."""
    return 100 + (p - 12) * -10  # mm


# Gelcoat axis with markings.
print(f"{xgel} mm {ygel(600)} mm moveto {xgel} mm {ygel(700)} mm lineto stroke")
for k in range(600, 701):
    if k % 10 == 0:
        print(f"{xgel} mm {ygel(k)} mm moveto -5 mm 0 rlineto stroke")
        print(f"{xgel-10} mm {ygel(k)} mm moveto ({k}) align_center")
    elif k % 5 == 0:
        print(f"{xgel} mm {ygel(k)} mm moveto -2.5 mm 0 rlineto stroke")
    else:
        print("gsave")
        print("0.1 setlinewidth")
        print(f"{xgel} mm {ygel(k)} mm moveto -2 mm 0 rlineto stroke")
        print("grestore")

# Peroxide axis with markings
print(f"{xper} mm {yper(12)} mm moveto {xper} mm {yper(21)} mm lineto stroke")
for k in range(120, 211):
    kk = k / 10
    if k % 10 == 0:
        print(f"{xper} mm {yper(kk)} mm moveto 5 mm 0 rlineto stroke")
        print(f"{xper+10} mm {yper(kk)} mm moveto ({kk}) align_center")
    elif k % 5 == 0:
        print(f"{xper} mm {yper(kk)} mm moveto 2.5 mm 0 rlineto stroke")
    else:
        print("gsave")
        print("0.1 setlinewidth")
        print(f"{xper} mm {yper(kk)} mm moveto 2 mm 0 rlineto stroke")
        print("grestore")

# Calculate the angle for the ratio labels
p1 = (xgel, ygel(600))
p3 = (xgel, ygel(700))
p2 = (xper, yper(12))
p4 = (xper, yper(14))
# 2%
ln1 = line(p1, p2)
ln2 = line(p3, p4)
intersect2 = intersect(ln1, ln2)
# 3%
p5 = (xper, yper(18))
p6 = (xper, yper(21))
ln3 = line(p1, p5)
ln4 = line(p3, p6)
intersect3 = intersect(ln3, ln4)
print(
    f"{intersect2[0]} mm {intersect2[1]} mm moveto "
    f"{intersect3[0]} mm {intersect3[1]} mm lineto stroke"
)
dx = intersect2[0] - intersect3[0]
dy = intersect2[1] - intersect3[1]
dist = math.sqrt(dx * dx + dy * dy)
angle = math.degrees(math.atan2(dy, dx)) - 90

# ratio axis markings
for p in range(200, 301):
    pp = p / 100
    A, B = (xgel, ygel(600)), (xper, yper(pp / 100 * 600))
    C, D = (xgel, ygel(700)), (xper, yper(pp / 100 * 700))
    l1 = line(A, B)
    l2 = line(C, D)
    ip = intersect(l1, l2)
    print("gsave")
    print(f"{ip[0]} mm {ip[1]} mm translate")
    print(f"{angle} rotate")
    if p % 10 == 0:
        print("0 0 moveto -5 mm 0 lineto stroke")
        print(f"-10 mm 0 moveto ({pp:.1f} %) align_center")
    elif p % 5 == 0:
        print("0 0 moveto -2.5 mm 0 lineto stroke")
    else:
        print("gsave")
        print("0.1 setlinewidth")
        print("0 0 moveto -2 mm 0 lineto stroke")
        print("grestore")
    print("grestore")

# Example reading
print("gsave")
print("1 0 0 setrgbcolor")
print(".5 setlinewidth")
print(f"{xgel} mm {ygel(640)} mm moveto {xper} mm {yper(15.36)} mm lineto stroke")
print("/Alegreya-Regular findfont 10 scalefont setfont")
print(f"{xgel+1} mm {ygel(638)} mm moveto (640 g) show")
print(f"{xper-1} mm {yper(15.30)} mm moveto (15,36 g) align_right")
print("grestore")

# Header for gelcoat
print(f"{xgel} mm {ygel(710)} mm moveto (gelcoat) align_middle")
print(f"{xgel} mm {ygel(705)} mm moveto ([g/30s]) align_middle")
# Header for peroxide
print(f"{xper} mm {yper(11)} mm moveto (peroxide) align_middle")
print(f"{xper} mm {yper(11.5)} mm moveto ([g/30s]) align_middle")
# Header for ratio
print("65 mm 90 mm moveto (ratio) align_middle")

print("showpage")
