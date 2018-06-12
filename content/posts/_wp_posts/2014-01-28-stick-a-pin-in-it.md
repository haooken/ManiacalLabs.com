---
author: adam
date: 2014-01-28 21:42:34+00:00
draft: false
title: Stick A Pin In It
type: post
url: /2014/01/28/stick-a-pin-in-it/
categories:
- Fail
- Tools
- Tutorial
---

{{< figure src="/wp-content/uploads/2014/01/IMG_20140128_1554221.jpg" caption="Stick a Pin in It" >}}

I've been working on a side project that uses some of the WS2812 based LED strips, just like the "NeoPixel" strips from [Adafruit](http://www.adafruit.com/products/1461). Unfortunately, I began having problems with the strips in that they suddenly stopped responding to any control signals being sent to them. My suspicion was either a broken solder point or a dead pixel. Since they function by buffering the data and then sending it along to the next pixel in the line they have that old style Christmas lights problem of all lights after a broken light will not function.

As they were already installed in what was to be their final setup, this brought about the issue of getting access to the control signal at various points without tearing it all apart and removing the waterproof epoxy coating that covers the strip. I had set the problem aside for a while but then happened to walk by some sewing supplies in my house and noted a pin cushion... but I wasn't seeing pins. I was seeing logic probes.

It seemed too simple to work, but I grabbed a pin and some alligator clip wires, and tried using the pin to inject control signals at various points along the strips... and it worked! Not only did it work through the waterproofing epoxy but in the wires between segments of LED strips as well. I could easily press the pin through the wire insulator, make a connection, and never really risk creating an exposed wire.

In the end, it turned out that the very first LED in the run at somehow fried its control chip. The was easily confirmed by using the pin to connect the data pad just after that pixel to the control signal and, sure enough, the rest of the strip lit up. So, quickly swapping that segment of LEDs fixed the problem and I was up and running again.

While the original idea was somewhat specific to these type of LED strips, I was quite impressed with how well it worked on regular hookup wires. I will definitely be using this trick for troubleshooting in the future. Sometimes you don't need expensive tools, just some sewing supplies :)

