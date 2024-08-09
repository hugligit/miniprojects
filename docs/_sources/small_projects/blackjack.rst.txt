*********
Blackjack
*********

.. tags:: large, game, cardgame



Blackjack, also known as 21, is a card game where players try to get as close
to 21 points as possible without going over. This program uses images drawn
with text characters, called ASCII art. American Standard Code for Information
Interchange (ASCII) is a mapping of text characters to numeric codes that
computers used before Unicode replaced it. The playing cards in this program
are an example of ASCII art:

::

    ___   ___
   |A  | |10 |
   | ♣ | | ♦ |
   |__A| |_10|




How It Works

The card suit symbols don’t exist on your keyboard, which is why we call the
chr() function to create them. The integer passed to chr() is called a Unicode
code point, a unique number that identifies a character according to the
Unicode standard. Unicode is often misunderstood. However, Ned Batchelder’s
2012 PyCon US talk “Pragmatic Unicode, or How Do I Stop the Pain?” is an
excellent introduction to Unicode, and you can find it at
https://youtu.be/sgHbC6udIqc/. Appendix B gives a full list of Unicode
characters you can use in your Python programs.


You can find other rules and the history of this card game at
https://en.wikipedia.org/wiki/Blackjack.

.. collapse:: blackjack.py

   .. literalinclude:: blackjack.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project4.html
