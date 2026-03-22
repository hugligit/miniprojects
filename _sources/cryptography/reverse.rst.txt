**************
Reverse Cipher
**************

The reverse cipher encrypts by printing the characters in reverse order.
For example "*my howercraft is full of eels*" becomes "*slle fo lluf si
tfarcrewoh ym* To decrypt the message we simply reverse again. This is
a weak cipher.

.. admonition:: Implementation

   .. .. code-block:: python
   ..    :linenos:
   ..    :caption: hugli

   ..    for i in range(4):
   ..        print(i)

   .. collapse:: reverse.py

      .. literalinclude:: reverse.py
         :language: python
         :linenos:
