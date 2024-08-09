**************
Shining Carpet
**************


.. tags:: tiny, artistic, beginner


The Shining, a 1980 psychological horror film directed by Stanley Kubrick,
takes place at the haunted Overlook Hotel. The hotel carpet’s hexagonal design
became an iconic part of this famous movie. The carpet features alternating and
interlocking hexagons whose mesmerizing effect is well-suited for such an
unnerving film. The short program in this project, similar to Project 35, “Hex
Grid,” prints this repetitive pattern on the screen.

Note that this program uses raw strings, which prefix the opening quote with a
lowercase r, so that the backslashes in the string aren’t interpreted as escape
characters.

When you run shiningcarpet.py, the output will look like this:

::

 _ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ __
  \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _
 \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/
 / / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_
 _/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \__
 __/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \___
 _ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ __
  \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _
 \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/
 / / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_
 _/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \__
 __/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \___
 _ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ ___ \ \ \_/ __
  \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _ \ \ \___/ _
 \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/ \ \ \_____/
 / / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_/ / / ___ \_
 _/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \___/ / / _ \__
 __/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \_____/ / / \___

The creation of a program like this (or the similar Project 35) doesn’t begin
with coding but rather just drawing tessellating shapes in a text editor. Once
you’ve written out the pattern, you can cut it down to the smallest unit to be
tiled:

::

 _ \ \ \_/ __
  \ \ \___/ _
 \ \ \_____/
 / / / ___ \_
 _/ / / _ \__
 __/ / / \___

After you’ve copied and pasted this text into the source code, you can write
the rest of the program around it. Software is not just a matter of sitting
down and writing code from beginning to end. Every professional software
developer goes through several iterations of tinkering, experimentation, and
debugging. The end result may be just nine lines of code, but a small program
doesn’t necessarily imply that a small amount of effort went into making it.


.. collapse:: shining_carpet.py

   .. literalinclude:: shining_carpet.py
      :language: python
      :linenos:

For practice, try creating patterns such as the following:

::

	___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
	_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
	___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
	_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
	___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
	_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__

	((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )
	 ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(
	((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )
	 ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(
	((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )((  )
	 ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(  ))(

	 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/
	/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____
	\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __
	 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \
	 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/
	/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____
	\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __
	 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \

	  \__   \__   \__   \__   \__   \__   \__   \__   \__   \__
	__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \
	  \     \     \     \     \     \     \     \     \     \
	__/   __/   __/   __/   __/   __/   __/   __/   __/   __/
	  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/
	__/     /     /     /     /     /     /     /     /     /
	  \__   \__   \__   \__   \__   \__   \__   \__   \__   \__
	__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \

	/ ___ \ ^ / ___ \ ^ / ___ \ ^ / ___ \ ^ / ___ \ ^ / ___ \ ^
	 /   \ VVV /   \ VVV /   \ VVV /   \ VVV /   \ VVV /   \ VVV
	|() ()|   |() ()|   |() ()|   |() ()|   |() ()|   |() ()|
	 \ ^ / ___ \ ^ / ___ \ ^ / ___ \ ^ / ___ \ ^ / ___ \ ^ / ___
	\ VVV /   \ VVV /   \ VVV /   \ VVV /   \ VVV /   \ VVV /
	)|   |() ()|   |() ()|   |() ()|   |() ()|   |() ()|   |() (

https://inventwithpython.com/bigbookpython/project65.html
