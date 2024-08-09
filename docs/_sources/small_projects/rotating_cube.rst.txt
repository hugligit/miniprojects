*************
Rotating Cube
*************


.. tags:: large, artistic, math



This project features an animation of a 3D cube rotating using trigonometric
functions. You can adapt the 3D point rotation math and the line() function in
your own animation programs.


.. collapse:: rotating_cube.py

   .. literalinclude:: rotating_cube.py
      :language: python
      :linenos:

This algorithm has two main parts: the line() function and the rotatePoint()
function. The cube has eight points, one for each corner. The program stores
these corners as (x, y, z) tuples in the CUBE_CORNERS list. These points also
define the connections for the cube’s edge lines. When all the points rotate in
the same direction by the same amount, they give the illusion of a cube
rotating.

After entering the source code and running it a few times, try making
experimental changes to it. The comments marked with (!) have suggestions for
small changes you can make. On your own, you can also try to figure out how to
do the following:

* Modify CUBE_CORNERS and the tuple on line 184 to create different wireframe
  models such as a pyramid and a flat hexagon.

* Increase the coordinates of CUBE_CORNERS by 1.5 so that the cube revolves
  around the center of the screen, rather than rotating around its own center.

https://inventwithpython.com/bigbookpython/project62.html
