*************
Sudoku Puzzle
*************


.. tags:: large, game, oop, puzzle



Sudoku is a popular puzzle game in newspapers and mobile apps. The Sudoku board
is a 9 × 9 grid in which the player must place the digits 1 to 9 once, and only
once, in each row, column, and 3 × 3 subgrid. The game begins with a few spaces
already filled in with digits, called givens. A well-formed Sudoku puzzle will
have only one possible valid solution.

Objects of the SudokuGrid class are the data structures that represent the
Sudoku grid. You can call their methods to make modifications to, or retrieve
information about, the grid. For example, the makeMove() method places a number
on the grid, the resetGrid() method restores the grid to its original state,
and isSolved() returns True if all the solution’s numbers have been placed on
the grid.

The main part of the program, starting on line 141, uses a SudokuGrid object
and its methods for this game, but you could also copy and paste this class
into other Sudoku programs you create to reuse its functionality.


.. collapse:: sudoku_puzzle.py

   .. literalinclude:: sudoku_puzzle.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project73.html
