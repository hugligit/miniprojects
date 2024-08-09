**************
Maze Runner 2D
**************


.. tags:: large, game, maze



This two-dimensional maze runner shows the player a top-down, bird’s-eye view
of a maze file you create in a text editor, such as the IDE you use to write
your .py files. Using the WASD keys, the player can move up, left, down, and
right, respectively, to navigate the @ symbol toward the exit marked by the X
character.

To make a maze file, open a text editor and create the following pattern. Don’t
type the numbers along the top and left side; they are only there for
reference:

::

    123456789
  1 #########
  2 #S# # # #
  3 #########
  4 # # # # #
  5 #########
  6 # # # # #
  7 #########
  8 # # # #E#
  9 #########

The # characters represent walls, the S marks the start, and the E marks the
exit. The # characters in bold represent walls that you can remove to form
your maze. Don’t remove the walls at odd-numbered columns and odd-numbered
rows, and don’t remove the borders of the maze. When you’re done, save the
maze as a .txt (text) file. It could look something like this:

::

    #########
    #S    # #
    # ### # #
    # #   # #
    # ##### #
    #   #   #
    ### # # #
    #     #E#
    #########

Of course, this is a simple maze. You can make maze files of any size as long
as they have an odd number of rows and columns. Be sure it’ll still fit on the
screen, though! You can also download maze files from
https://invpy.com/mazes/.


.. collapse:: maze_runner_2d.py

   .. literalinclude:: maze_runner_2d.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project44.html
