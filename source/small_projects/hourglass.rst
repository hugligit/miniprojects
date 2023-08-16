*********
Hourglass
*********


.. tags:: large, artistic, bext, simulation



This visualization program has a rough physics engine that simulates sand
falling through the small aperture of an hourglass. The sand piles up in
the bottom half of the hourglass; then the hourglass is turned over so the
process repeats.

The hourglass program implements a rudimentary physics engine.  A physics
engine is software that simulates physical objects falling under gravity,
colliding with each other, and moving according to the laws of physics.
You’ll find physics engines used in video games, computer animation, and
scientific simulations. On lines 91 to 102, each “grain” of sand checks if
the space beneath it is empty and moves down if it is. Otherwise, it
checks if it can move down and to the left (lines 104 to 112) or down and
to the right (lines 114 to 122). Of course, there is much more to
kinematics, the branch of classical physics that deals with the motion of
macroscopic objects, than this.  However, you don’t need a degree in
physics to make a primitive simulation of sand in an hourglass that is
enjoyable to look at.


.. collapse:: hourglass.py

   .. literalinclude:: hourglass.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project36.html
