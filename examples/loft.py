"""

name: loft.py
by:   Gumyr
date: July 15th 2022

desc:

    This example demonstrates lofting a set of sketches, selecting
    the top and bottom by type, and shelling.

license:

    Copyright 2022 Gumyr

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
from build123d.build123d_common import *
from build123d.build_sketch import *
from build123d.build_part import *

with BuildPart() as art:
    slice_count = 10
    for i in range(slice_count + 1):
        Workplanes(Plane(origin=(0, 0, i * 3), normal=(0, 0, 1)))
        with BuildSketch() as slice:
            Circle(10 * sin(i * pi / slice_count) + 5)
    Loft()
    top_bottom = art.faces().filter_by_type(Type.PLANE)
    Shell(*top_bottom, thickness=0.5)

if "show_object" in locals():
    show_object(art.part, name="art")
