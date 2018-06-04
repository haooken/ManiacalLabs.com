---
author: dan
date: 2014-08-05 13:00:00+00:00
draft: false
title: NeoPixel Glass Skull Lighting Effect (A.K.A Mr. BlinkySkull)
type: post
url: /2014/08/05/blinkyskull/
categories:
- Cool Stuff
- Projects
---

Awesome skull-shaped vodka bottle plus Arduino Pro Mini plus NeoPixels equals:



{{< youtube zz2iUaCEhLY >}}



I've had this (empty) bottle of Crystal Head vodka for a while. Admittedly I mostly bought it because the bottle was really neat and I wanted to make it light up. Up until this point, I was using a small version of the RGB clock to illuminate it. It was a neat effect, but not very bright. It was time for an upgrade.

<!-- more -->

I have used before and really like the [Arduino Pro Mini](https://www.sparkfun.com/products/11113). All the Arduino power and flexibility in a cheap, tiny package. I picked up a [16 LED NeoPixel Ring](http://www.adafruit.com/products/1463) not too long ago, and I really like how neatly the APM fits inside of the ring (held in place with some solid-core wire. I can definitely see using this combination in other projects. For this project, the wiring is pretty basic. The ring power and ground are soldered to extra VCC and Ground pins respectively on the APM, and a barrel jack is soldered to the RAW (voltage regulator input) pin and another extra ground pin. Yet another nice thing about this configuration: the APM has enough extra pins to attach a peripheral and an extra power tap. The ring Data pin is connected to digital pin 7.

{{< gallery dir="/wp-content/galleries/2014-08-05-blinkyskull/0/" />}}

As you'll notice, the "enclosure" is a re-purposed SparkFun box. For quick enclosures where heat dissipation an looks aren't a top concern, these work pretty well. Note that I did end up cutting vent holes in this one since the LEDs can generate a bit of heat if the animation has the lights on all the time. The hardware is held in place by a piece of clear packing tape over the cutout and another piece across the back as a bit of insurance.

{{< gallery dir="/wp-content/galleries/2014-08-05-blinkyskull/1/" />}}

The animations are all done in code, with help from the Most Excellent [FastLED](http://fastled.io/) library. If you do anything with programmable LEDs on the Arduino, this library is worth a look. The code (such as it is) for this project can be found [here](https://github.com/ManiacalLabs/APMRingLight). This was a quick one-off thing, so please excuse the crudeness of the code. I didn't have time to build it to scale. Or paint it.

I guess the main take-away from this how well the Arduino Pro Mini and the NeoPixel ring work together. And glass vodka bottles are cool.

-Dan

{{< load-photoswipe >}}