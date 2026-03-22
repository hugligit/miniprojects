**************************
Simple Substitution Cipher
**************************


.. tags:: short, cryptography, math


The Simple Substitution Cipher substitutes one letter for another. Since there
are 26 possible substitutions for the letter A, 25 possible substitutions for
B, 24 for C, and so on, the total number of possible keys is 26 × 25 × 24 × 23
× . . . × 1, or 403,291,461,126,605,635,584,000,000 keys! That’s far too many
keys for even a supercomputer to brute force, so the code-breaking method used
in Project 7, “Caesar Hacker,” can’t be used against the simple cipher.
Unfortunately, devious attackers can take advantage of known weakness to break
the code. If you’d like to learn more about ciphers and code breaking, you can
read my book Cracking Codes with Python (No Starch Press, 2018;
https://nostarch.com/crackingcodes/).


.. collapse:: simple_substitution_cipher.py

   .. literalinclude:: simple_substitution_cipher.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project66.html
