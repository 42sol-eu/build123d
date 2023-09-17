"""
url: https://build123d.readthedocs.io/en/latest/introductory_examples.html#id25

creates a pylon like object.
"""

from build123d import *


length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex24:
    Box(length, length, thickness)
    with BuildSketch(ex24.faces().group_by(Axis.Z)[0][0]) as ex24_sk:
        Circle(length / 3)
    with BuildSketch(ex24_sk.faces()[0].offset(length / 2)) as ex24_sk2:
        Rectangle(length / 6, width / 6)
    loft() # consumes ex24_sk1 and ex24_sk2
    
    
if "show_object" in locals():
    show_object(ex24, name="example 2.4")
