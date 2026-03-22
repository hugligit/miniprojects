********
J'accuse
********


.. tags:: huge, game, humour, puzzle


You are the world-famous detective Mathilde Camus. Zophie the cat has gone
missing, and you must sift through the clues. Suspects either always tell lies
or always tell the truth. Will you find Zophie the cat in time and accuse the
guilty party?

In this game, you take a taxi to different locations around the city. At each
location is a suspect and an item. You can ask suspects about other suspects
and items, compare their answers with your own exploration notes, and determine
if they are lying or telling the truth. Some will know who has catnapped Zophie
(or where she is, or what item is found at the location of the kidnapper), but
you must determine if you can believe them. You have five minutes to find the
criminal but will lose if you make three wrong accusations. This game is
inspired by Homestar Runner’s “Where’s an Egg?” game.

To fully understand this program, you should pay close attention to the clues
dictionary, which is set up on lines 51 to 109. You can uncomment lines 151 to
154 to display it on the screen. This dictionary has strings from the SUSPECTS
list for the keys and “clue dictionaries” for the values. Each of these clue
dictionaries contains strings from SUSPECTS and ITEMS. The original suspect
will answer with these strings when asked about another suspect or item. For
example, if clues['DUKE HAUTDOG']['CANDLESTICK'] is set to 'DUCK POND', then
when the player asks Duke Hautdog about the Candlestick, they’ll say it is at
the Duck Pond. The suspects, items, locations, and culprit get shuffled each
time the game is played.

The code for this program revolves around this data structure, so understanding
it is necessary to unlocking your understanding of the rest of the program.


.. collapse:: jaccuse.py

   .. literalinclude:: jaccuse.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project38.html
