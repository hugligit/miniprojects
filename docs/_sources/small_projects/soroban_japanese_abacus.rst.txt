***********************
Soroban Japanese Abacus
***********************


.. tags:: large, artistic, math, simulation


An abacus, also called a counting frame, is a calculating tool used in many
cultures long before electronic calculators were invented. Figure 70-1 shows
the Japanese form of the abacus, called a soroban. Each wire represents a place
in a positional numeral system, and the beads on the wire represent the digit
at that place. For example, a soroban with two beads moved over on the
rightmost wire and three beads moved over on the second-to-rightmost wire would
represent the number 32. This program simulates a soroban. (The irony of using
a computer to simulate a pre-computer computing tool is not lost on me.)

Each column in the soroban represents a different digit. The rightmost column
is the ones place, the column to its left is the tens place, the column to the
left of that is the hundreds place, and so on. The Q, W, E, R, T, Y, U, I, O,
and P keys along the top of your keyboard can increase the digit at their
respective positions, while the A, S, D, F, G, H, J, K, L, and ; keys will
decrease them. The beads on the virtual soroban will slide to reflect the
current number. You can also enter numbers directly.

The four beads below the horizontal divider are “earth” beads, and lifting them
up against the divider counts as 1 for that digit. The bead above the
horizontal divider is a “heaven” bead, and pulling it down against the divider
counts as 5 for that digit, so pulling down one heaven bead and pulling up
three earth beads in the tens column represents the number 80. More information
about abacuses and how to use them can be found at
https://en.wikipedia.org/wiki/Abacus.


.. collapse:: soroban_japanese_abacus.py

   .. literalinclude:: soroban_japanese_abacus.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project70.html
