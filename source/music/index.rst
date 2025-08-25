*****
Music
*****

Crave
*****

Volca Drum
**********

.. {{{ Kicks

Kicks 
=====

.. {{{ Acoustic Kick Drum Emulation

Acoustic Kick Drum Emulation
----------------------------

Layer 1 generates the main low frequency element. A brief rise and
fall in pitch is created with the amount and rating settings. The
amplitude envelope has a fast attack and medium release .

Layer 2 has a low level settings and creates a shorter, softer
section of a band pass filtered noise to emulate the sound of the
beater hitting the drum, This is tuned to a pitch of 78 to get
a reasonably realistic sound. The drive setting is at 71 to add
some distortion and gain is boosted to 100 to ensure that the sound
is loud enough.

.. drumkitpart::

   sin 255 20
   rmp 42 188
   lin 0 115

   bp 18 78
   ran 39 158
   exp 59 99

   0 0 71
   0 100 0

.. }}}
.. {{{ A1 Kick 

A1 Kick 
--------

This is a deep kick drum designed for high-tempo dance music or pop, which
is effective on a range of speakers, from big club systems to mobile
phones.

QPI is turned on, an both layers are tuned to the note A1, You could tune
this to a different note to match the key of your music, Layer 1 is based
on a sine wave which uses the exponential pitch modulation envelope to
create a pitch slide, generaating a higher frequency attack section and
a lower frequency main body. The pitch slides up rapidly at the start of
the sound and the nfalls to the PITCH that been specified (the note A1).
Layer 2 has a medium EG REL setting using the exponential EG wave to
create a kick sound that is long enough to make an impact but short enough
to leave space for a bassline in a high-tempo track.

Layer 2 adds another level of high frequency detail to help it stand out
on smaller systems, with a faster pitch slide createdby the pitch
modulation settings to generate a subtle "zap". Layer 2 is turned down to
a volume LVL of 47 to balance it with the main kick sound of Layer 1, The
FLD and DRV effects are also used to create more character and high
frequency detail.

Try reduxing the FLD setting to 0 transform this into a very soft, smooth
kick. A lower REL value will create a shorter kick to give more space for
a bassline in a faster track (so that the kick and following bassline
notes do not overlap too much).

.. drumkitpart::

   sin 255 A1
   rmp 39 144
   exp 0 147

   sin 47 A1
   rmp 60 130
   exp 0 95

   0 78 24
   0 0 0

.. }}}
.. {{{ A1 Kick Long 

A1 Kick Long 
-------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -


.. }}}
.. {{{ Chip Kick 

Chip Kick 
----------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -


.. }}}
.. {{{ Tight Kick Short 

Tight Kick Short 
-----------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -


.. }}}
.. {{{ Tight Kick Long 

Tight Kick Long 
----------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -


.. }}}
.. {{{ Techno Double Kick 

Techno Double Kick 
-------------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -


.. }}}
.. {{{ Retro Rhytm Kick 

Retro Rhytm Kick 
-----------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Urban Underground Kick 

Urban Underground Kick 
-----------------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -


.. }}}
.. {{{ Soft Deep Kick 

Soft Deep Kick 
---------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Heartbeat 

Heartbeat 
----------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -


.. }}}
.. {{{ Hardcore Warehouse Kick 

Hardcore Warehouse Kick 
------------------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
 
.. }}}
.. {{{ Snares

Snares
======

.. {{{ A1 Snare 

A1 Snare 
--------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ A1 Snare Short 

A1 Snare Short 
--------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Metallic Snare 

Metallic Snare 
--------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Broken Snare 

Broken Snare 
------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}

.. }}} 
.. {{{ Claps

Claps
=====

.. {{{ Easy Clap

Easy Clap
---------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ A1 Clap

A1 Clap
-------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Reversed Clap

Reversed Clap
-------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Filtered Noise Clap

Filtered Noise Clap
-------------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Scratch Clap

Scratch Clap
------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Smash Clap

Smash Clap
----------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Minimal Clap

Minimal Clap
------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. }}}
.. {{{ Cymbals

Cymbals
=======

.. {{{ Metallic Closed High Hat

Metallic Closed High Hat
------------------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Metallic Open High Hat

Metallic Open High Hat
----------------------

description

.. drumkitpart::
   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Razor Hat Closed

Razor Hat Closed
----------------

description

.. drumkitpart::
   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Razor Hat Open

Razor Hat Open
--------------

description

.. drumkitpart::
   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Synth Crash Cymbal

Synth Crash Cymbal
------------------

description

.. drumkitpart::
   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}

.. }}}
.. {{{ Shakers

Shakers
=======

.. {{{ Basic Shaker

Basic Shaker
------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Shorter Shaker

Shorter Shaker
--------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Double Shaker

Double Shaker
-------------

description

.. drumkitpart::

   _ _ _
   _ _ _
   _ _ _

   _ _ _
   _ _ _
   _ _ _


   _ _ _
   _ _ _

.. }}}
.. }}}
.. {{{ Congas

Congas
======

.. {{{ High Conga

High Conga
----------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Middle Conga

Middle Conga
------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Low Conga

Low Conga
---------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. }}}
.. {{{ Toms

Toms
====

.. {{{ Floor Tom

Floor Tom
---------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Middle Tom

Middle Tom
----------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ High Tom

High Tom
--------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Disco Tom

Disco Tom
---------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. }}}
.. {{{ Percussions

Percussions
===========

.. {{{ Cowbell

Cowbell
-------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Rimshot

Rimshot
-------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Claves

Claves
------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Triangle

Triangle
--------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Glass Chime

Glass Chime
-----------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. }}}
.. {{{ Effects

Effects
=======

.. {{{ Metronome

Metronome
---------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ System Error

System Error
------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Space Trail

Space Trail
-----------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Random

Random
------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. }}}
.. {{{ Melodic Sounds

Melodic Sounds
==============
.. {{{ Sawtooth

Sawtooth
--------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Sine

Sine
----

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Basic Bass

Basic Bass
----------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. {{{ Perfect Fifth

Perfect Fifth
-------------

description

.. drumkitpart::

   - - -
   - - -
   - - -

   - - -
   - - -
   - - -

   - - -
   - - -

.. }}}
.. }}}

Ambient ø
*********
