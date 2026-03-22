********
HEX Grid
********


.. tags:: tiny, artistic, beginner



This short program produces a tessellated image of a hexagonal grid, similar
to chicken wire. It shows that you don’t need a lot of code to make something
interesting. A slightly more complicated variation of this program is Project
65, “Shining Carpet.”

After entering the source code and running it a few times, try making
experimental changes to it. The comments marked with (!) have suggestions for
small changes you can make. On your own, you can also try to figure out how to
do the following:

Create tiled hexagons of a larger size.
Create tiled rectangular bricks instead of hexagons.
For practice, try re-creating this program with larger hexagon grids, such as
the following patterns:

::


    /   \     /   \     /   \     /   \     /   \     /   \     /   \
   /     \___/     \___/     \___/     \___/     \___/     \___/     \
   \     /   \     /   \     /   \     /   \     /   \     /   \     /
    \___/     \___/     \___/     \___/     \___/     \___/     \___/
    /   \     /   \     /   \     /   \     /   \     /   \     /   \
   /     \___/     \___/     \___/     \___/     \___/     \___/     \
   
     /     \         /     \         /     \         /     \
    /       \       /       \       /       \       /       \
   /         \_____/         \_____/         \_____/         \_____
   \         /     \         /     \         /     \         /
    \       /       \       /       \       /       \       /
     \_____/         \_____/         \_____/         \_____/
     /     \         /     \         /     \         /     \
    /       \       /       \       /       \       /       \
   /         \_____/         \_____/         \_____/         \_____



.. collapse:: hex_grid.py

   .. literalinclude:: hex_grid.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project35.html
