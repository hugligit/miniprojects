**********************
Mondrian Art Generator
**********************


.. tags:: large, artistic, bext


Piet Mondrian was a 20th-century Dutch painter and one of the founders of
neoplasticism, an abstract art movement. His most iconic paintings relied on
blocks of primary colors (blue, yellow, red), black, and white. Using a
minimalist approach, he separated these colors with horizontal and vertical
elements.

This program generates random paintings that follow Mondrian’s style. You can
find out more about Piet Mondrian at
https://en.wikipedia.org/wiki/Piet_Mondrian.

The algorithm works by creating a data structure (the canvas dictionary) with
randomly spaced vertical and horizontal lines.

Next, it removes some of the line segments to create larger rectangles.

Finally, the algorithm randomly fills some rectangles with yellow, red, blue,
or black.

You can find another version of this Mondrian art generator at
https://github.com/asweigart/mondrian_art_generator/ along with several sample
images.

.. collapse:: mondrian_art_generator.py

   .. literalinclude:: mondrian_art_generator.py
      :language: python
      :linenos:


After entering the source code and running it a few times, try making
experimental changes to it. On your own, you can also try to figure out how to
do the following:

* Create programs with different color palettes.
* Use the Pillow module to produce image files of Mondrian art. You can learn
  about this module from Chapter 19 of Automate the Boring Stuff with Python at
  https://automatetheboringstuff.com/2e/chapter19/.

https://inventwithpython.com/bigbookpython/project46.html
