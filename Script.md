# Script 

## Introduction Slide (0:00 - 0:30)

Hello, I'm Matt Clarke, I'm a first year PhD student working with Saiful Islam, and I use atomistic modelling to help understand and develop battery materials.

> Overview slide - 10

Now, as we only have five minutes, I'm going to give you a quick whistlestop tour of batteries as a whole

> Materials

...I'll go over the materials that we use in batteries, the sustainability issues associated with these, and what's coming through the works...

> Modelling 

… And finally, I'll try and show how using modelling techniques to study these materials can help identify and understand new materials for next generation batteries.



## Context

Ok, so why are we interested in batteries?

Well, batteries are a really interesting area to work in, in that a coming up with a small improvement in the fundamental chemistry can impact a wide range of other fields.

Renewable energy sources are often intermittent, so widespread adoption will need an energy vector which is cheap and reliable to provide power when needed.

Vehicle electrification is another interesting case, as each new battery technology has the potential to both disrupt a multibillion dollar industry and provide huge environmental benefits.

And consumer demand for thinner and longer lasting portable electronics is pushing the current battery chemistries to their limits.

## Plot slide

…and the challenge is bigger than you might think.

One of the factors we are interested in is energy density, namely how much energy can we pack into a given volume or weight

Lead acid batteries are very large putting them at the bottom of this graph, and heavy, putting them to the left. Li-ion batteries outperformed it's predecessors, and the gap between NiMh and Li-ion here arguably corresponds to the leap that caused portable electronics revolution.

With that in mind, the fact that we need to be here for widespread adoption of vehicle electrification, should highlight the scale of the problem we're up against.

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

Now cobalt has  a whole range of sustainability issues. It has limited reserves, and these reserves are focused in geopolitically unstable regions, causing price fluctuations and ethical concerns to surround its procurement.

As such, cathode chemistries which minimise the use of cobalt are preferred.

Different applications require different chemistries. In the BMW i3, NMC is used, substituting nickel and manganese in for a portion of the cobalt. In the Tesla, Nickel and Aluminium are substituted in.



Both of these chemistries are more inherently safe and longer lasting than LCO, but this comes at the cost of energy density.

The exact compositions aren't set in stone either.

NMC 111, meaning a 1:1:1 ratio of the transition metals, is currently used commercially, but ratios like 8:11 are of significant research interest

Changing the metal ratio can only get us so far. If we want a big jump in performance, we need more than incremental changes.

This is where Li-rich cathodes come in. 

We substitute some of the TM sites for further Li ions, dramatically increasing the overall capacity of the battery.

### Modelling + ack (1:15)

Finally, what do I actually do here?

So firstly, starting with some experimental data, my job is to find a simple set of rules that can recreate the important aspects of this structure.

A good starting point is to look at pairs of atom types, using a buckingham potential for the short range , and coulombic term for the long range interactions. 

For each pair of atom types we make some educated guesses as to how these atoms will behave around one another.

We then look at the forces on the atoms and tweak the rules until our we can the same structure falls out.

Once we've done this, computational techniques really start to shine. 

We can use these same rules to probe other systems, which are less easy to synthesise.

And of course, we can probe atom scale features or phenomenon which cannot be measured experimentally such as looking at isolated defects.

Now more complex systems require more complex potentials. While I can't explain these in 5 minutes, I'm hoping I'll be able to do it in three years.

So with that, thanks to all of these people and thanks for listening.





 



