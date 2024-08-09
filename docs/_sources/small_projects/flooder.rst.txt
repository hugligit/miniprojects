*******
Flooder
*******


.. tags:: large, bext, game



Flooder is a colorful game where a player tries to fill the board with
a single color by changing the color of the tile in the upper-left corner.
This new color spreads to all neighboring tiles that matched the original
color. It’s similar to the Flood It mobile game. This program also has
a colorblind mode, which uses shapes instead of flat colored tiles. It
relies on the recursive flood fill algorithm to paint the board and works
similarly to the “paint bucket” or “fill” tool in many painting
applications.


How It Works
------------

Accessibility is a large issue in video games, and addressing it can take many
forms. For example, deuteranopia, or red-green colorblindness, causes shades of
red and green to appear the same, making it hard to distinguish between red
objects and green objects on the screen. We can make Flooder more accessible
with a mode that uses distinct shapes instead of distinct colors. Note that
even the colorblind mode still uses color. This means you can eliminate the
“standard” mode, if you wish, and have even color-sighted users play in the
colorblind mode. The best accessibility designs are those that incorporate
accessibility considerations from the start rather than add them as a separate
mode. This reduces the amount of code we have to write and makes any future bug
fixes easier.

Other accessibility issues include making sure that text is large enough to be
read without perfect vision, that sound effects have visual cues and spoken
language has subtitles for those hard of hearing, and that controls can be
remapped to other keyboard keys so people can play the game with one hand. The
YouTube channel Game Maker’s Toolkit has a video series called “Designing for
Disability” that covers many aspects of designing your games with accessibility
in mind.

.. collapse:: flooder.py

   .. literalinclude:: flooder.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project28.html
