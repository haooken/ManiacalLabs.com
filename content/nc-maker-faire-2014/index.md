---
author: maniacal labs
date: 2014-06-08 02:01:58+00:00
draft: false
title: NC Maker Faire 2014
type: page
url: /nc-maker-faire-2014/
---

Maniacal Labs attended the 2014 North Carolina Maker Faire with a few of Adam and Dan's personal projects. This page is here to provide those curious with more information on those projects and will be kept update to date with any new information or tutorial links as they are created.



## "PolarGRaph"



{{< figure src="/wp-content/uploads/2014/06/ML_PolarGRaph_small.jpg" caption="PolarGRaph" >}}

Dan's take on a Plotterbot.  The PolarGRaph was seen on it's mobile mounting platform. Several small and large drawings were on display, including our table banners. The Raspberry Pi controller and the motor control board full of Sparkfun components were sources of good conversation. The fishing line was a surprise to some as it was hard to see, and gave the effect that the gondola was floating across the paper un-assisted. See original blog post [here](http://maniacallabs.com/2014/01/21/enter-the-polar-giraffe/). For info on how the control files are generated from grey-scale images, check out [this](http://www.makerbot.com/blog/2012/03/12/single-line-art-traveling-salesman-problem-tutorial/) blog post on stippling and the Traveling Salesman Problem.



## Fancy Pants MkI and MkII (LED Matrix Pants)



Adam is a long time fan of geek musician [Jonathan Coulton](http://jonathancoulton.com), who is probably best known for writing the theme songs to Valve's Portal and Portal 2. But he also headlines a yearly cruise (since 2010), JoCo Cruise Crazy, that is basically a week-long, floating, geek convention. He also wrote this song (which he's not very proud of):

{{< youtube vjfJxiDzRgU >}}

Long story short, it became a yearly cruise tradition to have a "Fancy Pants Parade" (as described in the song) and competition for who has the fanciest of pants. After the winner on JCCC2 (JoCo Cruise Crazy 2) was little more than some white pants with Christmas lights shoved down one leg, Adam thought he could build better fancy pants. Having procrastinated all year, and only have 3 weeks before the cruise, Fancy Pants MkI were rushed into production. Sparks flew, code was written, things were sewn, LED pants were born.

{{< youtube  NSlhehoKGFQ >}}

Note: these were constructed for Adam's wife. He is not that small.

Sadly, in the bright spotlights of the stage, the competition was lost, the lights did not have enough power.

For JCCC3, the building started much earlier. More than 6 months were spent designing and building Fancy Pants MkII. Now, instead of 132 LEDs and a maximum draw of 1A, they would have 504 LEDs and a maximum draw of 30A. This, clearly, clearly required bigger pants and they were now built for Adam. Everything is custom, the pants themselves are hand made, the LED matrix built from strips of WS2812 ("NeoPixel") LEDs, a custom controller board was fabricated via [OSHPark](http://oshpark.com), even the case for the controller was custom designed and 3D printed on our MakerBot Replicator 2. All that work led to this:

{{< youtube  hM7A822UeIg >}}

As always, all this work is open source. The code and design files for [MkI](https://github.com/adammhaile/FancyPants-MkI) and [MkII](https://github.com/adammhaile/FancyPantsMkII) are available on GitHub.



## Arduino Sous Vide



{{< figure src="/wp-content/uploads/2014/06/ML_SousVide_Small.jpg" >}}

For Sous Vide/Immersion cooking, precise temperature control is a must. Commercial products are expensive, and what fun is that when you can make one? Adafruit has a [great tutorial](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino) on how to make your own temperature controller for an immersion cooker, or any other application where exact temperature control is required. On display was a slight variant of that tutorial using a wireless remote control outlet to control the crock pot heating element. At some point in the near future, a more complete walk-through of the materials used and how the code was modified will be posted.



## Raspbery Pi Controlled LED Matrix



Another of Adam's projects, this 24 x 24 pixel matrix is completely hand built out of [LPD8806 LED Strips](http://www.adafruit.com/product/306) mounted on acrylic and controlled with a custom Python library running on a Raspberry Pi that handles all of the the animation rendering and driving the strips. The library is still in development but is the next generation of Adam's ever popular library for these strips, available on [GitHub](https://github.com/adammhaile/RPi-LPD8806). This display was built both to be an eventual art piece to hang (with a nicer case) but also as a test-bed for this new version of the library able to handle a wider array of configurations and animations as well as _nearly any_ LED display technology, not just the LPD8806.

{{< youtube  yE_N2OHX2uU >}}
