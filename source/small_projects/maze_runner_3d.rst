**************
Maze Runner 3D
**************


.. tags:: huge, artistic, game, maze


This three-dimensional maze runner provides the player with a first-person view
from inside a maze. Try to find your way out! You can generate maze files by
following the instructions in Project 44, “Maze Runner 2D,” or by downloading
maze files from https://invpy.com/mazes/.

This 3D-perspective ASCII art starts with the multiline string stored in
ALL_OPEN. This string depicts a position in which no paths are closed off by
walls. The program then draws the walls, stored in the CLOSED dictionary, on
top of the ALL_OPEN string to generate the ASCII art for any possible
combination of closed-off paths. For example, here’s how the program generates
the view in which the wall is to the left of the player:

::

								\               \
	____         ____            \_              \_        ____
	   |\       /|                |               |       /|
	   ||       ||                |               |       ||
	   ||__   __||                |               |__   __||
	   || |\ /| ||                |               | |\ /| ||
	   || | X | ||        +       |       =       | | X | ||
	   || |/ \| ||                |               | |/ \| ||
	   ||_/   \_||                |               |_/   \_||
	   ||       ||                |               |       ||
	___|/       \|___             |               |       \|___
								 /               /
								/               /


The periods in the ASCII art in the source code get removed before the strings
are displayed; they only exist to make entering the code easier, so you don’t
insert or leave out blank spaces.



.. collapse:: maze_runner_3d.py

   .. literalinclude:: maze_runner_3d.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project45.html
