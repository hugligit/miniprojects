**********************
Hangman and Guillotine
**********************


.. tags:: large, game, puzzle, word



This classic word game has the player guess the letters to a secret word.
For each incorrect letter, another part of the hangman is drawn. Try to
guess the complete word before the hangman completes. The secret words in
this version are all animals like RABBIT and PIGEON, but you can replace
these with your own set of words.

The HANGMAN_PICS variable contains ASCII-art strings of each step of the hangman’s noose:

::


  +--+     +--+     +--+     +--+     +--+     +--+     +--+
  |  |     |  |     |  |     |  |     |  |     |  |     |  |
     |     O  |     O  |     O  |     O  |     O  |     O  |
     |        |     |  |    /|  |    /|\ |    /|\ |    /|\ |
     |        |        |        |        |    /   |    / \ |
     |        |        |        |        |        |        |
 =====    =====    =====    =====    =====    =====    =====

For a French twist on the game, you can replace the strings in the HANGMAN_PICS variable with the following strings depicting a guillotine:

::


|        |   |    |===|    |===|    |===|    |===|    |===|
|        |   |    |   |    |   |    |   |    || /|    || /|
|        |   |    |   |    |   |    |   |    ||/ |    ||/ |
|        |   |    |   |    |   |    |   |    |   |    |   |
|        |   |    |   |    |   |    |   |    |   |    |   |
|        |   |    |   |    |   |    |/-\|    |/-\|    |/-\|
|        |   |    |   |    |\ /|    |\ /|    |\ /|    |\O/|
|===     |===|    |===|    |===|    |===|    |===|    |===|


.. collapse:: hangman_and_guillotine.py

   .. literalinclude:: hangman_and_guillotine.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project34.html
