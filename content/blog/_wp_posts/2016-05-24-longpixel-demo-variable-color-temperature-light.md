---
author: adam
date: 2016-05-24 22:45:05+00:00
draft: false
title: 'LongPixel Demo: Variable Color Temperature Light'
type: post
url: /2016/05/24/longpixel-demo-variable-color-temperature-light/
categories:
- Kickstarter
- LongPixel
---

The [LongPixel](/LongPixel) was designed to make using analog LED strips super easy and, typically, that means RGB LEDs as they are the most common. But the beauty of the way in which the LongPixel drives these LED strips is that it really doesn't matter what color the LEDs are. Sure, the 4 wire, 3 color RGB strips are the most convenient in most cases. But you could, for example, connect 3 single color, 2 wire, strips, of whatever color you desired. Hook up all of the strips' power input to the V+ on the LongPixel and then each strips' ground to a separate channel on the LongPixel and you are ready to go.

But another great use-case for choosing something other than RGB strips is if what you really need is white light above all else. Sure, you can get white light out of an RGB strip, but it's not _real_ white light. It's got peaks at each of the primary wavelengths of each sub-color which looks fine to our easily tricked eyes, but is not ideal for photography or video as a lighting source. This is where the simpler white LED strips come in. But then there's a conundrum... what [color temperature](https://en.wikipedia.org/wiki/Color_temperature) do you want? Why choose?

In this demo, I've taken two different white LED strips, 3000K (warm white) and 6000K (cool white), and used a little math to blend the two together to maintain roughly the same total light output while fading between 3000K and 6000K. The brightness and color temperature values are stored internally as unsigned bytes (0-255) and then the following calculation is used to determine the output to send to the LongPixel:

[code]
red = ((255 - _temp) * _brightness) >> 8
blue = (_temp * _brightness) >> 8
color = (red, 0, blue)
[/code]

In this case, the 3000K strip is connected to the red output and 6000K is connected to blue. The above allows fading between the two temperatures while generally maintaining the same overall brightness. For those confused by the ">> 8" code, this is just a fancy way of scaling two 8-bit values by each other. Multiply together and then right bit shift 8 places. This is _much_ faster on a microcontroller than using larger values.

Regarding the controller, it was re-purposed from a previous project, the [Fancy Pants MkII](/nc-maker-faire-2014/) for which I built the controller as a wrist mounted device. Because of the memory demands of the controller and the pants, between having 500 pixels and a 128x64 pixel OLED display, it uses a super beefy ATMega1284p chip which is _complete_ overkill for this project. But it certainly beat building a new board from scratch and it already came with a nice case :)

Enough babble... check out the demo for all the juicy details and a time-lapse build.

{{< youtube hIPvXKeT28U >}}

You can find the code, PCB, and case design on [GitHub](https://github.com/ManiacalLabs/VariableColorTempLight/)
