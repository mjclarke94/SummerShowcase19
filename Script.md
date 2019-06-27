# Script 

Timings

| Slide        | Time | Σ    | Potential time save | Σ    |
| ------------ | ---- | ---- | ------------------- | ---- |
| Introduction | 0:25 | 0:25 | 0:00                | 0:00 |
| Context      | 0:45 | 1:10 | 0:00                | 0:00 |
| Plot         | 0:40 | 1:50 | 0:00                | 0:00 |
| Inside       | 0:35 | 2:25 | 0:00                | 0:20 |
| Composition  | 1:32 | 3:57 | 0:00                | 0:20 |
| Interatomic  | 1:16 | 5:18 | 0:06                |      |

In the scripts, key events are noted alongside the time at which they occur and the interval.

The presentation should be okay as long as I remain within ± 10% of a given interval. 

Running short looks awkward, but overrunning is more flustering. As such, aim to be slighly ahead if in doubt.

## Introduction Slide (0:00 - 0:30)

Hello, I'm Matt Clarke, I'm a first year PhD student working with Saiful Islam on modelling battery materials.

> Overview slide - 10

As we only have five minutes, I'm going to give you a quick whistlestop tour of batteries as a whole

> Materials

...I'll go over the materials used in batteries, both commercially those coming through the works...

> Modelling 

… And finally, I'll try and show how modelling techniques can be used to help give valuable insights into the properties and performance of batteries.



## Context

Ok, so why are we interested in batteries?

Well, batteries are a really interesting area to work in, in that a small improvement in the fundamental chemistry can impact a wide range of other fields.

Renewable energy sources are often intermittent, so widespread adoption will need an energy vector which is cheap and reliable to provide power when needed.

Vehicle electrification is another interesting case, as each new battery technology has the potential to both disrupt a multibillion dollar industry and provide huge environmental benefits.

And portable electronics are getting more powerful, so it's a struggle to keep up with the shift towards thinner and longer lasting phones, let alone improve...

## Plot slide

…and the challenge is bigger than you might think.

One of the factors we are interested in is energy density, namely how much energy can we pack into a given volume or weight

Lead acid batteries, being both heavy and large for their stored energy end upin the bottom corner

Now on this graph, the gap between NiMH and Li-ion was enough to trigger the portable electronics revolution, but we're hitting the limits of what conventional Li-ion can do.

As a ballpark figure, for widespread vehicle electrification, we need batteries that are around *here*.

> Energy density. More energy, with less battery (lighter, smaller, both

### Inside a battery

So what's going on inside a battery?

You start with two electrodes, both of which can reversibly have Li ions extracted and inserted into their stuctures.

We combine these with an electrolyte to allow ion transport between the electrodes, and a seperator to force electrons to an alternate path.

We then charge the battery by applying a potential across the terminals, forcing Li ions to move into the anode structure.

In order to get useful work back out, we provide an electronic path back between the terminals via the thing you want to power.

## Composition slide (1:30)

Ok, now lets look a bit more at the cathode materials, as they're the limiting factor in batteries.

As the positively charged Li-ions leave or enter the cathode, something has to charge compensate that event. 

In your phone, we use cobalt for this. Specifically, LCO.

Now cobalt has  a whole range of sustainability issues including limited reserves, a ethically dubious supply chain, and it's expensive. 



> Cars

Different applications require different chemistries, all of which their own issues

NMC is found in the BMW i3, and NCA in the Tesla

There is a general push to try and maximise the Nickel content, both to increase power and decouple battery production from cobalt supplies

These compositions aren't set in stone either.

NMC 111 is currently produced commercially, but 811 is of interest

So how do these materials translate into batteries?

Intercalation cathodes have a structure, for NMC a layered structure, which allows the repeated extraction and insertion of some of the Li ions.

Changing the composition or broader structure of this material can provide different properties 

We still here find ourself at a limiting point, we can change the metal ratios to improve performance, but this will lead to diminishing returns.

This is where Li-rich cathodes come in. 

We substitute some of the TM sites for further Li ions, dramatically increasing the overall capacity of the battery.

### Modelling + ack (1:15)

Finally, what do I actually do here?

I've gone for salt here because it's easier to draw, but same idea.

So firstly, starting with some experimental data, my job is to find a simple set of rules that can recreate the important aspects of this structure.

A good starting point is to look at pairs of atom types, using a buckingham potential for the short range , and coulombic term for the long range interactions. 

For each pair of atom types we make some educated guesses as to how these atoms will behave around one another.

We then look at the forces on the atoms and tweak the rules until our we can the same structure falls out.

Once we've done this, computational techniques really start to shine. 

We can use these same rules to probe other systems, which are less easy to synthesise.

And of course, we can probe atom scale features or phenomenon which cannot be measured experimentally such as looking at isolated defects.

Now I should of course clarify, this is a simplification. There are layers on layers of complexity you can add to these models, but none I can explain in 5 minutes!

So with that, thanks to all of these people and thanks for listening.





 



