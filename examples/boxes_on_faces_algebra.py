"""

name: boxes_on_faces_algebra.py
by:   Gumyr
date: March 6th 2023

desc: Demo adding features to multiple faces in one operation.
ref:  
  [Workplanes](https://build123d.readthedocs.io/en/latest/key_concepts.html#Workplanes)

license:

    Copyright 2023 Gumyr

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
from build123d import *
from ocp_vscode import *

b = Box(3, 3, 3)
b2 = Rot(0, 0, 45) * extrude(Rectangle(1, 2), 0.1)
for plane in [Plane(f) for f in b.faces()]:
    b += plane * b2

if "show_object" in locals():
    show_object(b, name="box on faces")
