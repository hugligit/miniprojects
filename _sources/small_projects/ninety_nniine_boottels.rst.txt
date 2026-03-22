**********************
Ninety Nniine Boottels
**********************


.. tags:: short, scrolling, word



In this version of the song “Ninety-Nine Bottles,” the program introduces small
imperfections in each stanza by either removing a letter, swapping the casing
of a letter, transposing two letters, or doubling a letter.

As the song continues to play, these mutations add up, resulting in a very
silly song. It’s a good idea to try Project 50, “Ninety-Nine Bottles,” before
attempting this one.

String values in Python are immutable, meaning they cannot be changed. If the
string 'Hello' is stored in a variable called greeting, the code greeting =
greeting + ' world!' doesn’t actually change the 'Hello' string. Rather, it
creates a new string, 'Hello world!', to replace the 'Hello' string in
greeting. The technical reasons for this are beyond the scope of this book, but
it’s important to understand the distinction, because it means code like
greeting[0] = 'h' isn’t allowed, since strings are immutable. However, since
lists are mutable, we can create a list of single-character strings (as line 62
does), change the characters in the list, and then create a string from the
list (line 85). This is how our program seemingly changes, or mutates, the
strings containing the song lyrics.


.. collapse:: ninety_nniine_boottels.py

   .. literalinclude:: ninety_nniine_boottels.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project51.html
