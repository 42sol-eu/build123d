##########################
Readme: @folder `examples`
##########################


TODO: check more examples / information how to use line types ("assets/line_types.svg")

TODO: add python files from ./docs/


+---------------------------------------+---------------------------------------------------------------------+
| `../docs/center.py`                   | Helper script to center create a svg with centered image.           |
|                                       | (configuration file for the Sphinx documentation builder)           |
+---------------------------------------+---------------------------------------------------------------------+
| `../docs/general_examples.py`         | General example for builder-mode (by jdegenstein 2022-12-29)        |
|                                       | collection of examples from the documentaiton (tagged to be used in |
|                                       | the different places), generating the SVG for the documentation.    |
+---------------------------------------+---------------------------------------------------------------------+
| `../docs/general_examples_algebra.py` | General example for algebra-mode                                    |
|                                       | (by Bernhard Walter/jdegenstein 2023-03) collection of examples     |
|                                       | from the documentation (tagged to be used in the different places), |
|                                       | not generating the SVG.                                             |
+---------------------------------------+---------------------------------------------------------------------+
| `../docs/line_types.py`               | This script generates sample of all the available line types        | 
|                                       | resulting in "./assets/line_types.svg". (by Gumyr 2023)             |
+---------------------------------------+---------------------------------------------------------------------+
| `../docs/objects_1d.py`               | This script generates sample of all the available 1d-objects        |
|                                       | resulting in "./assets/buildline_example_{d}.svg"[d=1..8]           |
+---------------------------------------+---------------------------------------------------------------------+
| `../docs/objects_2d.py`               | This script generates sample of all the available 2d-objects        |
|                                       | resulting in "./assets/{2d_name}_example.svg" with 2d_name=circle,  |
|                                       | ellipse,polygon,rectangle,rectangle_rounded,regular_poligon,        |
|                                       | slots, text, trapezoid ... and the align overview.                  |
+---------------------------------------+---------------------------------------------------------------------+
| `../docs/objects_3d.py`               | This script generates sample of all the available 3d-objects        |
|                                       | resulting in "./assets/{3d_name}_example.svg" with 3d_name=(box,    |
|                                       | cone,cylinder,sphere,torus,wedge,*hole*)                            |
| `../docs/rigid_joints_pipe.py`        | This script shows the usage of `bd_warehouse` objects with joints   |
|                                       | to connect them.                                                    |
+---------------------------------------+---------------------------------------------------------------------+
| `../docs/rod_end.py`                  | This script shows the usage of `bd_warehouse` objects with a thread |
|                                       | line placed on a rod.                                               |
+---------------------------------------+---------------------------------------------------------------------+
| `../docs/selector_example.py`         | This illustrates the selector usage (Gumyr, 2022-09-28)             |
+---------------------------------------+---------------------------------------------------------------------+
| `../docs/slide_latch.py`              | Create a latch and joints (Gumyr, 2022-??-??)                       |
+---------------------------------------+---------------------------------------------------------------------+
| `../docs/tutorial_joints.py`          | Creates a box with a lid attached with a hinge.(Gumyr, 2022-12-27)  |
+---------------------------------------+---------------------------------------------------------------------+


########
Examples
########

Benchy (`bench_low_poly.py`)
############################

+-------+-------------+
| by:   | Gumyr       |
+-------+-------------+
| date: | 2023-07-09  |
+-------+-------------+


This example imports a STL model as a solid object and changes it.
The [low-poly-benchy](./assets/bench_low_poly.stl) used in this example is designed by [reddaugherty](https://www.printables.com/model/151134-low-poly-benchy).

Makes uses of special workplane placements for the `chimney` on the `roof_plane` at `smoke_stack_center`. 

..
    TODO: (felix) this concepts could be added in a Advanced topic rst 



Boxes On A Face (`./boxes_on_faces.py` and `./boxes_on_faces_algebra.py`)
#########################################################################

- Example from documentation-chapter [Worklpanes](https://build123d.readthedocs.io/en/latest/key_concepts.html#Workplanes).
- TODO: note that the example still uses `import build123d as bd`.


build123d-customizable-logo (`./build123d_customizable_logo.py` and `./build123d_customizable_logo_algebra.py`)
###############################################################################################################

- [Text](https://build123d.readthedocs.io/en/latest/objects.html#objects_sketch.Text)
- [Builders](https://build123d.readthedocs.io/en/latest/builders.html)
- [Compound](https://build123d.readthedocs.io/en/latest/assemblies.html)
- [Export SVG](https://build123d.readthedocs.io/en/latest/import_export.html#svg)

The build123d Logo (`./build123d_logo.py` and `./build123d_logo_algebra.py`)
############################################################################

- [Text](https://build123d.readthedocs.io/en/latest/objects.html#objects_sketch.Text)
- [Builders](https://build123d.readthedocs.io/en/latest/builders.html)
- [Compound](https://build123d.readthedocs.io/en/latest/assemblies.html)
- [Export SVG](https://build123d.readthedocs.io/en/latest/import_export.html#svg)


The Canadian Flag (`./canadian_flag.py` and `./canadian_flag_algebra.py`)
#########################################################################

Circuit Board (`./circuit_board.py` and `./circuit_board_algebra.py`)
#####################################################################

A Clock (`./clock.py` and `./clock_algebra.py`)
###############################################

Custom Sketch Objects (`./custom_sketch_objects.py` and `./custom_sketch_objects_algebra.py`)
#############################################################################################

DIN Rail  (`./din_rail.py` and `./din_rail_algebra.py`)
#######################################################

Dual Color Export (`./dual_color_3mf.py`)
#########################################

Extrude (`./extrude.py` and `./extrude_algebra.py`)
###################################################

Handle (`./handle.py` and `./handle_algebra.py`)
################################################

Heat Exchanger (`./heat_exchanger.py` and `./heat_exchanger_algebra.py`)
########################################################################

Holes (`./holes.py` and `./holes_algebra.py`)
#############################################

Intersecting Chamfers (`./intersecting_chamfers.py` and `./intersecting_chamfers_algebra.py`)
#############################################################################################

Intersecting Joints (`./intersecting_pipes.py` and `./intersecting_pipes_algebra.py`)
#####################################################################################

Joints (`./joints.py` and `./joints_algebra.py`)
################################################

Key Caps (`./key_cap.py` and `./key_cap_algebra.py`)
####################################################

A Brick (Lego-Brick) (`./lego.py` and `./lego_algebra.py`)
##########################################################

Loft (`./loft.py` and `./loft_algebra.py`)
###############################################################################################################

This example demonstrates lofting a set of sketches, selecting the top and bottom by type, and shelling.

>> Loft (docs example)


Mixed Algebra Context (`./mixed_algebra_context.py`)
####################################################

multiple workplanes (`./multiple_workplanes.py` and `./multiple_workplanes_algebra.py`)
#######################################################################################

Pegboard J Hook (`./pegboard_j_hook.py` and `./pegboard_j_hook_algebra.py`)
###########################################################################

Pillow Block (`./pillow_block.py` and `./pillow_block_algebra.py`)
##################################################################

Playing Cards (`./playing_cards.py` and `./playing_cards_algebra.py`)
#####################################################################

Projection (`./projection.py` and `./projection_algebra.py`)
############################################################

Roller Coaster (`./roller_coaster.py` and `./roller_coaster_algebra.py`)
########################################################################

Shamrock (`./shamrock.py`)
##########################

Adds a four leaf clover implemented as a `BaseSketchObject`.

![[shamrock.png]]


Tea Cup (`./tea_cup.py` and `./tea_cup_algebra.py`)
###################################################

>> tea cup from docs 

https://build123d.readthedocs.io/en/latest chapter overview


TTT SM Hanger (`./ttt_sm_hanger.py`)
####################################

Vase (`./vase.py` and `./vase_algebra.py`)
##########################################

