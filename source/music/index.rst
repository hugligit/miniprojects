*****
Music
*****



Supercollider
=============


Intro
*****


.. code-block:: supercollider


   // Harmonics adjusted
   (
   {
   (
   SinOsc.ar(400, mul: 1) + SinOsc.ar(800, mul: 1/2) +
   SinOsc.ar(1200, mul: 1/3) + SinOsc.ar(1600, mul: 1/4) +
   SinOsc.ar(2000, mul: 1/5) + SinOsc.ar(2400, mul: 1/6) +
   SinOsc.ar(2800, mul: 1/7) + SinOsc.ar(3200, mul: 1/8) +
   SinOsc.ar(3600, mul: 1/9) + SinOsc.ar(4000, mul: 1/10) +
   SinOsc.ar(4400, mul: 1/11) + SinOsc.ar(4800, mul: 1/12)
   )*0.1
   }.scope)
   
   
   (
   {
   f = 100;
   [
   SinOsc.ar(f*1, mul: 1), SinOsc.ar(f*2, mul: 1/2),
   SinOsc.ar(f*3, mul: 1/3), SinOsc.ar(f*4, mul: 1/4),
   SinOsc.ar(f*5, mul: 1/5), SinOsc.ar(f*6, mul: 1/6),
   SinOsc.ar(f*7, mul: 1/7), SinOsc.ar(f*8, mul: 1/8),
   SinOsc.ar(f*9, mul: 1/9), SinOsc.ar(f*10, mul: 1/10),
   SinOsc.ar(f*11, mul: 1/11), SinOsc.ar(f*12, mul: 1/12)
   ]
   }.scope(12)
   )
   
   
   (
   {
   	var speed = MouseY.kr(1, 50);
   	f = MouseX.kr(50, 880, 'exponential');
   t = Impulse.kr(1/3);
   Mix.ar([
   SinOsc.ar(f*1, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/1),
   SinOsc.ar(f*2, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/2),
   SinOsc.ar(f*3, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/3),
   SinOsc.ar(f*4, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/4),
   SinOsc.ar(f*5, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/5),
   SinOsc.ar(f*6, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/6),
   SinOsc.ar(f*7, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/7),
   SinOsc.ar(f*8, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/8),
   SinOsc.ar(f*9, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/9),
   SinOsc.ar(f*10, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/10),
   SinOsc.ar(f*11, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/11),
   SinOsc.ar(f*12, mul: LFNoise1.kr(rrand(speed, speed*2), 0.5, 0.5)/12)
   ])*0.5
   	}.scope(1)
   )
   
   
   
   
   (
   {
   f = 220;
   t = Impulse.kr(1/6);
   Mix.ar([
   SinOsc.ar(f*1, mul: EnvGen.kr(Env.perc(0, 6.4), t)/1),
   SinOsc.ar(f*2, mul: EnvGen.kr(Env.perc(0, 4.1), t)/2),
   SinOsc.ar(f*3, mul: EnvGen.kr(Env.perc(0, 2), t)/3),
   SinOsc.ar(f*4, mul: EnvGen.kr(Env.perc(0, 1), t)/4),
   SinOsc.ar(f*5, mul: EnvGen.kr(Env.perc(0, 1.8), t)/5),
   SinOsc.ar(f*6, mul: EnvGen.kr(Env.perc(0, 2.9), t)/6),
   SinOsc.ar(f*7, mul: EnvGen.kr(Env.perc(0, 4), t)/7),
   SinOsc.ar(f*8, mul: EnvGen.kr(Env.perc(0, 0.3), t)/8),
   SinOsc.ar(f*9, mul: EnvGen.kr(Env.perc(0, 1), t)/9),
   SinOsc.ar(f*10, mul: EnvGen.kr(Env.perc(0, 3.6), t)/10),
   SinOsc.ar(f*11, mul: EnvGen.kr(Env.perc(0, 2.3), t)/11),
   SinOsc.ar(f*12, mul: EnvGen.kr(Env.perc(0, 1.1), t)/12)
   ])*0.5
   }.scope(1)
   )
   
   
   
   ({
   	f = 110;
   	// f =  [60, 64, 67, 71, 74, 78].midicps + 12;
   	t = Impulse.kr(1/3);
   	Mix.ar(
   		SinOsc.ar(
   			f*(1..12),
   			// f,
   			mul: EnvGen.kr(
   				Env.perc(0, 1),
   				t,
   				levelScale: 1/(1..12),
   				timeScale: [6.4, 4.1, 2, 1, 1.8, 2.9, 4, 0.3, 1, 3.6, 2.3, 1.1]/(1+(f*0.002))
   			)
   		)
   	)*0.5
   }.scope(1))
   
   
   
   ({
   	t = Impulse.kr(1/3);
   	Mix.ar(
   		SinOsc.ar(
   			[60, 64, 67, 71, 74, 78].midicps,
   			mul: EnvGen.kr(
   				Env.perc(0, 1),
   				t,
   				levelScale: 1/(1..6),
   				timeScale: rrand(1.0, 3.0).dup
   
   			)
   		)
   	)*[0.3, 0.3]
   }.scope(1))
   
   
   ({
   	Mix.ar(
   		Pan2.ar(
   			SinOsc.ar(
   				[60, 62, 63, 65, 67, 68, 71, 72].midicps,
   				mul: LFNoise1.kr(rrand(0.1, 0.5).dup(8), 0.5, 0.5)
   			),
   			1.0.rand2.dup(8)
   		)
   	)*0.2
   }.scope(1))
   
   
   // Additive saw wave, separate decays
   ({
   	var gate, fund;
   	gate = Impulse.kr(1/3);
   	fund = MouseX.kr(50, 1000);
   	Mix.ar(
   		Array.fill(16,
   			{arg counter;
   				var partial;
   				partial = counter + 1;
   				SinOsc.ar(fund*partial) *
   				EnvGen.kr(Env.adsr(0, 0, 1.0, TRand.kr(0.2, 2.0, gate)),
   					gate, 1/partial)
   		})
   	)*0.2 //overall volume
   }.scope(1))
   
   
   
   // Additive saw wave, same decays
   ({
   	var gate, fund, env;
   	gate = MouseButton.kr(0, 1, 0);
   	fund = MouseX.kr(50, 1000);
   	env = Env.adsr(0, 0, 1.0, 2.0);
   	Mix.ar(
   		Array.fill(16,
   			{arg counter;
   				var partial;
   				partial = counter + 1;
   				SinOsc.ar(fund*partial) *
   				EnvGen.kr(env, gate, 1/partial)
   		})
   	)*0.2 //overall volume
   }.scope(1))
   
   {SinOsc.ar(400, mul: SinOsc.ar(1/3, mul: 0.5, add: 0.5))}.scope
   
   
   ({
   	var harmonics = 16, fund = 50;
   	Mix.fill(harmonics,
   		{ arg count;
   			Pan2.ar(
   				FSinOsc.ar(
   					fund * (count + 1), // calculates each harmonic
   					mul: FSinOsc.kr(rrand(1/3, 1/6), mul: 0.5, add: 0.5 )),
   				1.0.rand2)
   		}
   	) / (2*harmonics)
   }.play;)
   
   
   
   // Inharmonic spectrum
   
   ({Mix.ar(
   	SinOsc.ar(
   		[72, 135, 173, 239, 267, 306, 355, 473, 512, 572, 626],
   		0, //phase
   		[0.25, 0.11, 0.12, 0.04, 0.1, 0.15, 0.05, 0.01, 0.03, 0.02, 0.12]
   ))}.scope(1))
   
   
   (
   thisThread.randSeed = 3;
   {100.rand}.dup(3)
   )
   
   
   
   
   // different every time
   {SinOsc.ar(LFNoise0.kr(7, 12, 72).midicps, mul: 0.5)}.play
   
   // same every time
   ({
   	RandSeed.kr(1, 1956);
   	SinOsc.ar(LFNoise0.kr(7, 12, 72).midicps, mul: 0.5)
   }.play)
   
   // resets every 5 seconds
   ({
   	RandSeed.kr(Impulse.kr(1/2), 1956);
   	SinOsc.ar(LFNoise0.kr(4, 12, 72).midicps, mul: 0.5)
   }.play)
   
    // Let it run for a while, the strikes are random
   ({
   	var trigger, partials = 12;
   	trigger = Dust.kr(3/7);
   	// thisThread.randSeed = 2534563;
   	Pan2.ar(
   		Mix.ar(
   			{
   				SinOsc.ar(rrand(50.0, 4000)) *
   				EnvGen.kr(
   					Env.perc(0, rrand(0.2, 3.0)),
   					trigger,
   					1.0.rand
   				)
   			}.dup(partials)
   		)/partials,
   		1.0.rand2
   	)
   }.play)
   
   // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! //
   
   ({
   	var trigger, fund;
   	trigger = Dust.kr(3/7);
   	fund = rrand(100, 400);
   	Mix.ar(
   		Array.fill(16,
   			{arg counter;
   				var partial;
   				partial = counter + 1;
   				Pan2.ar(
   					SinOsc.ar(fund*partial) *
   					EnvGen.kr(Env.adsr(0, 0, 1.0, 5.0),
   						trigger, 1/partial
   				) * max(0, LFNoise1.kr(rrand(5.0, 12.0))), 1.0.rand2)
   		})
   	)*0.5 //overall volume
   }.play)
   
   
   
   //Several of the above mixed down
   ({
   	var trigger, fund, flashInst;
   	flashInst = Array.fill(5,
   		{
   			trigger = Dust.kr(3/7);
   			fund = rrand(100, 400);
   			Pan2.ar(
   				Mix.ar(
   					Array.fill(16,
   						{arg counter;
   							var partial;
   							partial = counter + 1;
   							SinOsc.ar(fund*partial) *
   							EnvGen.kr(Env.adsr(0, 0, 1.0, 5.0),
   								trigger, 1/partial
   							) * max(0, LFNoise1.kr(rrand(5.0, 12.0)))
   					})
   				)*0.2,
   				1.0.rand2)
   	});
   	Mix.ar(flashInst)*0.6
   }.play)
   
   
   
   // Gaggle of sines varations
   ({
   	var harmonics = 16, fund = 50, speeds;
   	speeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]/5;
   	Mix.fill(harmonics,
   		{ arg count;
   			Pan2.ar(
   				FSinOsc.ar(
   					fund * (count + 1),
   					mul: max(0, FSinOsc.kr(speeds.wrapAt(count)))),
   				1.0.rand2)
   		}
   	) / (2*harmonics)
   }.play;)
   
   
   ({
   	var harmonics = 16, fund, speeds;
   	speeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]/20;
   	fund = (MouseX.kr(0, 36).round(7) + 24).midicps;
   	Mix.fill(harmonics,
   		{ arg count;
   			Pan2.ar(
   				FSinOsc.ar(
   					fund * (count + 1),
   					mul: max(0, FSinOsc.kr(speeds.choose))),
   				1.0.rand2)
   		}
   	) / (2*harmonics)
   }.play;)
   
   ({
   	var harmonics = 16, fund;
   	fund = (MouseX.kr(0, 36).round(7) + 24).midicps;
   	Mix.fill(harmonics,
   		{ arg count;
   			Pan2.ar(
   				FSinOsc.ar(
   					fund * (count + 1),
   					mul: max(0, FSinOsc.kr(rrand(1, 1/3), mul: 20).softclip)),
   				1.0.rand2)
   		}
   	) / (2*harmonics)
   }.play;)
   
   
   ({
   	var harmonics = 16;
   	Mix.fill(harmonics,
   		{ arg count;
   			Pan2.ar(
   				FSinOsc.ar(
   					exprand(100, 2000),
   					mul: max(0, FSinOsc.kr(rrand(1/3, 1/6))*rrand(0.1, 0.9))),
   				1.0.rand2)
   		}
   	) / (2*harmonics)
   }.play;)
   
   
   // Dissipating and converging gongs illustrates how a patch can be built
   // from duplicating one idea; classic additive synthesis. It also illustrates
   // how additive synthesis can be used to control each harmonic independently.
   // Listen in stereo to hear the harmonics diverge.
   ({
   	var dur = 6, base, aenv, fenv, out, trig;
   	base = Rand(40, 100);
   	trig = SinOsc.ar(1/10);
   	out = Mix.fill(15,{
   		var thisDur;
   		thisDur = dur * rrand(0.5, 1.0);
   		aenv = EnvGen.kr(Env.perc(0, thisDur), trig);
   		fenv = EnvGen.kr(Env.new([0, 0, 1, 0], [0.25*thisDur, 0.75*thisDur, 0]), trig);
   		Pan2.ar(SinOsc.ar( Rand(base, base * 12) *
   			LFNoise1.kr(10, mul: 0.02 * fenv, add: 1), // freq
   			mul: aenv // amp
   		), ([1, -1].choose) * fenv)
   	}) * 0.05;
   	out
   
   }.play(s);)
   
   
   ({
   	var dur = 6, base, aenv, fenv, out, trig, detune;
   	base = Rand(40, 60);
   	detune = 0.1; // increase this number to detune the second bell
   	trig = SinOsc.ar(1/10, pi);
   	out = Mix.fill(15,
   		{ arg count;
   			var thisDur;
   			thisDur = dur * rrand(0.5, 1.0);
   			aenv = EnvGen.kr(Env.perc(0, thisDur), trig);
   			fenv = EnvGen.kr(Env.new([1, 1, 0, 1], [0.05*thisDur, 0.95*thisDur, 0]), trig);
   			Pan2.ar(SinOsc.ar( base*(count+1+ detune.rand) *
   				LFNoise1.kr(10, mul: 0.02 * fenv, add: 1), // freq
   				mul: aenv // amp
   			), ([1, -1].choose) * fenv)
   	}) * 0.05;
   	out
   }.play(s);)
   
   // Decaying bell
   ({
   	var aenv, fenv, out, trig, dur, base;
   	dur = rrand(1.0, 6.0);
   	base = exprand(100, 1000);
   	out = Mix.ar(
   		Array.fill(15,{
   			arg count;
   			var thisDur;
   			thisDur = dur * rrand(0.5, 1.0);
   			aenv = EnvGen.kr(Env.new([0, 1, 0.4, 1, 0], [0, 0.5, 0.5, 0]), 1,
   				timeScale: thisDur);
   			fenv = EnvGen.kr(Env.new([0, 0, 0.5, 0.5, 0], [0.25, 0.5, 0.25, 0]),
   				1, timeScale: thisDur);
   			Pan2.ar(SinOsc.ar( Rand(base, base * 12) *
   				LFNoise1.kr(10, mul: 0.1 * fenv, add: 1), // freq
   				mul: aenv // amp
   			), ([1, -1].choose) * fenv)
   		})
   	) * EnvGen.kr(Env.linen(0, dur, 0), timeScale: dur,
   		levelScale: 0.05, doneAction: 2);
   	out;
   }.play;)








.. toctree::
   :maxdepth: 2
   :caption: Contents:

   leadsheets.rst
   patchsheet.rst
