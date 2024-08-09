******
Bagels
******

.. tags:: short, game, puzzle


A deductive logic game. You must guess a secret three-digit number based
on clues. You have ten guesses. The game offers following hints based on
your guesses.

Pico
   Correct digit in the wrong place

Fermi
   Correct digit in the correct place

Bagels
   No correct digits


.. Bagels, a deductive logic game.
.. By Al Sweigart al@inventwithpython.com
.. I am thinking of a 3-digit number. Try to guess what it is.
.. Here are some clues:
.. When I say: That means:
.. Pico One digit is correct but in the wrong position.
.. Fermi One digit is correct and in the right position.
.. Bagels No digit is correct.
.. I have thought up a number.
.. You have 10 guesses to get it.
.. Guess #1:

>>> 123
Pico
Guess #2:
>>> 456
Bagels
Guess #3:
>>> 178
Pico Pico
--snip--
Guess #7:
>>> 791
Fermi Fermi
Guess #8:
>>> 701
You got it!
Do you want to play again? (yes or no)
>>> no
Thanks for playing!

.. collapse:: bagels.py

   .. literalinclude:: bagels.py
      :language: python
      :linenos:
      :emphasize-lines: 12, 15-18
