*************
Caesar Cipher
*************

The cipher is named after Julius Caesar who used it 2000 year ago. It
works by substituting each letter of a message with a different one after
shifting the alphabeth order by a key. For example with the key of three
every "A" becomes "D" because it is shifted by three positions forward,
and "*my howercraft is full of eels*" becomes "QQQQ" To decrypt the
message the encryption must be performed with the negative of the original
key.

.. admonition:: Implementation

   .. .. code-block:: python
   ..    :linenos:
   ..    :caption: hugli

   ..    for i in range(4):
   ..        print(i)

   .. collapse:: caesar.py

      .. literalinclude:: caesar.py
         :language: python
         :linenos:
