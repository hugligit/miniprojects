***************
Vigenere Cipher
***************


.. tags:: short, cryptography, math


The Vigenère cipher, misattributed to 19th-century cryptographer Blaise de
Vigenère (others had independently invented it earlier), was impossible to
crack for hundreds of years. It is essentially the Caesar cipher, except it
makes use of a multipart key. The so-called Vigenère key is a word, or even a
random series of letters. Each letter represents a number by which to shift the
letter in the message: A represents shifting a letter in the message by 0, B
represents 1, C represents 2, and so on.

For example, if a Vigenère key is the word “CAT,” the C represents a shift of
2, the A represents 0, and the T represents 19. The first letter of the message
gets shifted by 2, the second letter by 0, and the third letter by 19. For the
fourth letter, we repeat the key of 2.

This use of multiple Caesar cipher keys is what gives the Vigenère cipher its
strength. The possible number of combinations is too big to brute force. At the
same time, the Vigenère cipher doesn’t suffer from the frequency analysis
weakness that can crack the simple substitution cipher. For centuries, the
Vigenère cipher represented the state of the art in cryptography.

You’ll notice many similarities between the code for the Vigenère and Caesar
cipher programs. More info about the Vigenère cipher can be found at
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher. If you’d like to learn more
about ciphers and code breaking, you can read my book Cracking Codes with
Python (No Starch Press, 2018; https://nostarch.com/crackingcodes/).


.. collapse:: vigenere_cipher.py

   .. literalinclude:: vigenere_cipher.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project80.html
