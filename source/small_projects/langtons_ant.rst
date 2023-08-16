************
Langtons Ant
************


.. tags:: large, artistic, bext, simulation



Langton’s Ant is a cellular automata simulation on a two-dimensional grid,
similar to Project 13, “Conway’s Game of Life.” In the simulation, an “ant”
begins on a square that is one of two colors. If the space is the first color,
the ant switches it to the second color, turns 90 degrees to the right, and
moves forward one space. If the space is the second color, the ant switches it
to the first color, turns 90 degrees to the left, and moves forward one space.
Despite the very simple set of rules, the simulation displays complex emergent
behavior. Simulations can feature multiple ants in the same space, causing
interesting interactions when they cross paths with each other. Langton’s Ant
was invented by computer scientist Chris Langton in 1986. More information
about Langton’s Ant can be found at
https://en.wikipedia.org/wiki/Langton%27s_ant.

This program uses two senses of “direction.” On the one hand, the dictionaries
that represent each ant store cardinal directions: north, south, east, and
west. However, turning left or right (or counterclockwise and clockwise, since
we are viewing the ants from above) is a rotational direction. Ants are
supposed to turn left or right in response to the tile they’re standing on, so
lines 78 to 100 set a new cardinal direction based on the ant’s current
cardinal direction and the direction they are turning.


.. collapse:: langtons_ant.py

   .. literalinclude:: langtons_ant.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project39.html
