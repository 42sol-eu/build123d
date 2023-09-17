"""
url: https://build123d.readthedocs.io/en/latest/introductory_examples.html#id25

creates a pylon like object.
"""

from build123d import *


length, width, thickness = 80.0, 60.0, 10.0

ex24 = Box(length, length, thickness)
plane = Plane(ex24.faces().sort_by().last)

faces = Sketch() + [
    plane * Circle(length / 3),
    plane.offset(length / 2) * Rectangle(length / 6, width / 6),
]

ex24 += loft(faces)

if "show_object" in locals():
    show_object(ex24, name="example 2.4")
