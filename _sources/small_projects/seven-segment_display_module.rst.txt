****************************
Seven Segment Display Module
****************************


.. tags:: short, module



A seven-segment display is a type of LCD component used to display numbers in
pocket calculators, microwave ovens, and other small electronic devices.
Through different combinations of seven line-shaped segments in an LCD, a
seven-segment display can represent the digits 0 through 9. They look like
this:

::

   __         __    __          __    __   __    __    __
  |  |    |   __|   __|  |__|  |__   |__     |  |__|  |__|
  |__|    |  |__    __|     |   __|  |__|    |  |__|   __|

The benefit of this program is that other programs can import it as a module.
Project 14, “Countdown,” and Project 19, “Digital Clock,” import the sevseg.py
file so they can use its getSevSegStr() function. You can find more information
about seven-segment displays and other variations at
https://en.wikipedia.org/wiki/Seven-segment_display.


.. collapse:: sevseg.py

   .. literalinclude:: sevseg.py
      :language: python
      :linenos:


https://inventwithpython.com/bigbookpython/project64.html
