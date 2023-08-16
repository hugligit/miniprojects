************
ROT13 Cipher
************


.. tags:: tiny, cryptography


The ROT13 cipher, one of the simplest encryption algorithms, stands for “rotate
13 spaces.” The cypher represents the letters A to Z as the numbers 0 to 25 in
such a way that the encrypted letter is 13 spaces from the plaintext letter: A
becomes N, B becomes O, and so on. The encryption process is identical to the
decryption process, making it trivial to program. However, the encryption is
also trivial to break. Because of this, you’ll most often find ROT13 used to
conceal non-sensitive information, such as spoilers or trivia answers, so it’s
not read unintentionally. More information about the ROT13 cipher can be found
at https://en.wikipedia.org/wiki/ROT13. If you’d like to learn about ciphers
and code breaking more generally, you can read my book Cracking Codes with
Python (No Starch Press, 2018; https://nostarch.com/crackingcodes/).


.. collapse:: rot13_cipher.py

   .. literalinclude:: rot13_cipher.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project61.html
