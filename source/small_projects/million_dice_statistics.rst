***********************
Million Dice Statistics
***********************


.. tags:: tiny, beginner, math, simulation



When you roll two six-sided dice, there’s a 17 percent chance you’ll roll a 7.
That’s much better than the odds of rolling a 2: just 3 percent. That’s because
there’s only one combination of dice rolls that gives you 2 (the one that
occurs when both dice roll a 1), but many combinations add up to seven: 1 and
6, 2 and 5, 3 and 4, and so on.

But what about when you roll three dice? Or four? Or 1,000? You could
mathematically calculate the theoretical probabilities, or you can have the
computer roll a number of dice one million times to empirically figure them
out. This program takes that latter approach. In this program, you tell the
computer to roll N dice one million times and remember the results. It then
displays the percentage chance of each sum.

This program does a massive amount of computation, but the computation itself
isn’t hard to understand.


.. collapse:: million_dice_statistics.py

   .. literalinclude:: million_dice_statistics.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project46.html
