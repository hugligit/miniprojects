***************
Forest Fire Sim
***************


.. tags:: short, bext, simulation



This simulation shows a forest whose trees are constantly growing and then
being burned down. On each step of the simulation, there is a 1 percent
chance that a blank space grows into a tree and a 1 percent chance that
a tree is struck by lightning and burns. Fires will spread to adjacent
trees, so a densely packed forest is more likely to suffer a larger fire
than a sparsely packed one. This simulation was inspired by Nicky Case’s
Emoji Sim at http://ncase.me/simulating/model/.


.. collapse:: forest_fire_sim.py

   .. literalinclude:: forest_fire_sim.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project29.html
