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

This is a very long kick drum that is well suited to a low tempo rhytms in
which the kick has time to fade away before it is triggered again. For
example, it could be used as little as once in a 16-step pattern, or
perhaps twice. Try it on step 1 and step 14c oa 88bpm.

This is identical to the original A1 Kick except for the Layer 1 RELEASE
time, which is now at the maximum 255 setting. This causes the main
low-frequency wave to remain audible for much longer.

Try reducing the RELEASE time if the sound is too long. Also try
increasing the FLD and DRV settings to make the REL phase more audible on
smaller speaker systems.

.. drumkitpart::

   sin 255 A1
   rmp 39 144
   exp 0 255

   sin 47 A1
   smp 60 130
   exp 0 96

   0 78 24
   0 0 0


.. }}}
.. {{{ Chip Kick 

Chip Kick 
----------

This uses a single layer to create a harsh, digital sounding kick drum
that is reminiscent of the 8-bit computing era. A sawtooth wave creates
the body of the sound (tuned to A1 in this example). The BIT, FLD and DRV
effects add harmonics in the upper mid-range. Pitch modulation using
a Rise/Fall shape generates an ATTACK section with higer frequencies. The
exponential Attack/Release wave creates a rapid ATTACK and medium RELEASE
phase. The LEVEL of Layer 2 is set to 0, so the remaining Layer 2 settings
have no effect.

.. drumkitpart::

   saw 255 A1
   rmp 28 128
   exp 0 133

   - 0 -
   - - -
   - - -

   255 76 255
   0 0 0


.. }}}
.. {{{ Tight Kick Short 

Tight Kick Short 
-----------------

Layer 1 and Layer 2 both use a sine wave (tuned to A1 in this case). The
AMOUNT, RATE, ATTACK and RELEASE settings are slightly different for each
layer, which helps to create a distinct attack section with higher
frequencies and longer, deeper and to the sound. This works well for high
tempo rhytms. Try a lower RELEASE setting for Layer 2 to create a shorter
sound, or a higher setting for a much longer sound as detailed in Tight
Kick Long.

.. drumkitpart::

   sin 255 A1
   rmp 30 77
   exp 0 120

   sin 47 A1
   rmp 60 130
   exp 0 154

   0 78 24
   0 30 0


.. }}}
.. {{{ Tight Kick Long 

Tight Kick Long 
----------------

This is very effective in lower-tempo music, whenit might be used only
once or twice in a 16-step pattern. It is exactly the same as Tight Short
Kick version except for the Layer 2 RELEASE value, which has been
increased to the maximum value of 255. This generates a long, deep bass
tone after the initial attack section.

Tune the PITCH of both layers to a different note to suit the key of
a your music. Try duplicating this sound into another part of the kit
(select the sound, hold FUNC, press key 7, press another part key) and
tune it to a different note to enable a 2-note bassline.

.. drumkitpart::

   sin 255 A1
   rmp 30 77
   exp 0 120

   sin 47 A1
   rmp 60 130
   exp 0 154

   0 78 24
   0 30 0


.. }}}
.. {{{ Techno Double Kick 

Techno Double Kick 
-------------------

This is an incredibly powerful sound for fast techno (try 150bpm). The
long ATTACK setting of Layer 2 creates a secondary bass throb. The timing
of the throb can be adjusted to fit the tempo with very fine adjustments
to the Layer 2 ATTACK setting.  The amount of throb can be adjusted
withthe Layer 2 RELEASE setting. As with other kicks here, this is tuned
to A1, but you can tune both Layers to a different note according to the
key of your music. If this is too loud, reduce the Gain (GAN) amount.

.. drumkitpart::

   sin 255 A1
   rmp 27 87
   exp 0 145

   sin 255 A1
   rmp 38 169
   exp 147 70

   0 0 150
   0 50 0


.. }}}
.. {{{ Retro Rhytm Kick 

Retro Rhytm Kick 
-----------------

This is a short, fairly light bass drum, based on the sounds of early
rhythm machines such as the Korg Minipops series. You will notice that
Layer 1 and Layer 2 are identical. You could program this sound with one
layer only, setting the Level of the other layer to 0, perhaps increasing
the Gain (GAN) setting to increase the volume. Alternatively, start with
these settings for each layer, then make changes to Layer 2 to explore
variations of the basic sound.

.. drumkitpart::

   sin 255 24
   rmp 42 179
   lin 0 112

   sin 255 24
   rmp 42 179
   lin 0 112

   0 0 0
   0 0 -

.. }}}
.. {{{ Urban Underground Kick 

Urban Underground Kick 
-----------------------

This is a long, hard kick that would be effective at low tempos (below
100bpm) or much higher tempos (above 160bpm). Layer 1 creates a long, deep
sine wave a which is distorted by the Fold and Drive effects. Layer
2 generates a short metallic click to add high frequency detail at the
start of the sound. Here, the GAN (gain) setting is at -9 to offset the
increase in the loudness created by the Fold and Drive effects. You can
adjust this to balance it with the rest of the kit. The sound could be
tuned to specific notes by turning QPI On and changing the Layer 1 PITCH
setting

.. drumkitpart::

   sin 255 16
   rmp 32 126
   lin 0 255

   sin 74 70
   sin 69 184
   lin 0 66

   0 54 154
   0 -9 -


.. }}}
.. {{{ Soft Deep Kick 

Soft Deep Kick 
---------------

Unlike most kick drums, this has a fairly long Attack phase, so it sounds
softer. It still has a lot of low-frequency rumble. Layer 1 and Layer
2 have different pitches and different ATTACK and RELEASE settings, so the
two waves overlap within the same sound. This was inspired by the bass
drumin the Jam & Spoon mix of “Age of Love” by Age of Love. The longer
Attack settings are an integral part of the warmth in this sound, but if
you want more definition at the start of the sound, try increasing the
Layer 1 AMOUNT setting. Increase the BIT setting to add higher frequency
harmonics.

.. drumkitpart::

   sin 255 G1
   rmp 46 145
   exp 70 140

   sin 255 D1
   rmp 0 0
   exp 156 114

   0 78 85
   0 0 -

.. }}}
.. {{{ Heartbeat 

Heartbeat 
----------

This is similar to the “Soft, deep kick” on the previous page, using
a sine wave a for each layer, offset with different ATTACK settings. Here,
both layers have the same PITCH, with longer ATTACK times to create more
distinction between the two pulses. As with all of these kick or bass
drums, the Pitch setting can be adjusted to suit the key of your music,
and the QPI setting can be turned on or off to set the frequency to
a specific note or a more precise frequency.

.. drumkitpart::

   sin 255 G1
   rmp 46 145
   exp 110 150

   sin 255 G1
   rmp 0 0
   exp 156 114

   0 153 85
   0 0 -


.. }}}
.. {{{ Hardcore Warehouse Kick 

Hardcore Warehouse Kick 
------------------------

This is a hard kick drum with a simulated reverb effect created by
low-pass filtered noise d from Layer 2. This secondary “whoosh” fades up
after the initial ATTACK phase of Layer 1. Layer 1 could be tuned to
another frequency to match your music.  Layer 2 uses a higher ATTACK
setting to delay the low-pass filtered noise d, moving it to towards the
end of the sound. Try changing the Layer 2 ATTACK to fit the tempo. The
Drive and Gain effects add loudness and distortion. Adjust the Layer
2 LEVEL for more or less of the “whoosh”. Also try adjusting Layer
1 RELEASE time.

.. drumkitpart::

   sin 255 A1
   rmp 40 108
   exp 0 145

   lp 150 F0
   sin 40 255
   exp 150 157

   0 0 255
   0 100 -

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
