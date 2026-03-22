***********
Sound Mimic
***********


.. tags:: short, beginner, game


Similar to the Simon electronic toy, this memorization game uses the
third-party playsound module to play four different sounds, which correspond to
the A, S, D, and F keys on the keyboard. As you successfully repeat the pattern
the game gives you, the patterns get longer and longer. How many sounds can you
hold in your short-term memory?

If you look at the code, you’ll see that the playsound.playsound() function is
passed the filename of the sound to play. You can download the sound files from
these URLs:

https://inventwithpython.com/soundA.wav

https://inventwithpython.com/soundS.wav

https://inventwithpython.com/soundD.wav

https://inventwithpython.com/soundF.wav

Place these files in the same folder as soundmimic.py before running the
program. More information about the playsound module can be found at
https://pypi.org/project/playsound/. Users on macOS must also install the
pyobjc module from https://pypi.org/project/pyobjc/ for playsound to work.


.. collapse:: sound_mimic.py

   .. literalinclude:: sound_mimic.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project71.html
