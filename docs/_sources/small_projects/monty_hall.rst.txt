**********
Monty Hall
**********


.. tags:: large, game, math, simulation



The Monty Hall Problem illustrates a surprising fact of probability. The
problem is loosely based on the old game show Let’s Make a Deal and its host,
Monty Hall. In the Monty Hall Problem, you can pick one of three doors. Behind
one door is a prize: a new car. Each of the other two doors opens onto a
worthless goat. Say you pick Door #1. Before the door you choose is opened, the
host opens another door (either #2 or #3), which leads to a goat. You can
choose to either open the door you originally picked or switch to the other
unopened door.

It may seem like it doesn’t matter if you switch or not, but your odds do
improve if you switch doors! This program demonstrates the Monty Hall problem
by letting you do repeated experiments.

To understand why your odds improve, consider a version of the Monty Hall
Problem with one thousand doors instead of three. You pick one door, and then
the host opens 998 doors, which all reveal goats. The only two doors that are
unopened are the one you selected and one other door. If you correctly picked
the car door to begin with (a 1 in a 1,000 chance), then the host left a random
goat door closed. If you picked a goat door (a 999 in a 1,000 chance), the host
specifically chose the car door to leave closed. The choice of which doors to
open isn’t random; the host knows to leave the car door closed. It’s almost
certain that you didn’t pick the car door to begin with, so you should switch
to the other door.

Another way to think of it is that you have 1,000 boxes and one box contains a
prize. You guess which box the prize is in and the host puts it in your hands.
Do you think the prize is in your box or one of the 999 other boxes? You don’t
need the host to open 998 of the 999 boxes that don’t contain a prize; the
amount of choice is the same as with the 1,000 doors. The odds that you guessed
correctly in the beginning are 1 in 1,000, while the odds that you did not (and
that the prize is in one of the other boxes) is a near certain 999 in 1,000.

More information about the Monty Hall Problem can be found at
https://en.wikipedia.org/wiki/Monty_Hall_problem.


.. collapse:: monty_hall.py

   .. literalinclude:: monty_hall.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project47.html
