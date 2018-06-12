---
author: dan
date: 2015-11-16 12:00:28+00:00
draft: false
title: Weekend Project - QuadWyoDisplay
type: post
url: /2015/11/16/weekend-project-quadwyodisplay/
categories:
- Weekend Project
- WyoLum
---

After a long week at the Day Job(tm), I sought the catharsis brought about by creativity and making something. To that end, I took stock of what parts I had lying around. I had been wanting to do something with a couple of [TinyTim LED boards](http://www.seeedstudio.com/depot/TinyTiM-LED-board-p-2392.html) I've had from previous projects. These displays were sent to us by our good friends at WyoLum. I decided I wanted to mount the 4 panels I had loose and make a nice-looking All-In-One 8x32 display. I grabbed a Raspberry Pi with wifi module, one of our [AllPixel LED controllers](/allpixel/), and got to work.

{{< figure src="/wp-content/uploads/2015/11/IMG_20151115_100654-Medium.jpg" caption="IMG_20151115_100654 (Medium)" >}}

<!-- more -->

I knew I wanted to mount the panels onto something. Wood seemed to be the logical choice since it would be easy to install standoffs, add cable management holes, and otherwise secure the various components. And it helped that I had a scrap piece of pine that was the exact width of 4 of these panels side by side.

{{< figure src="/wp-content/uploads/2015/11/IMG_20151114_115632-Medium.jpg" caption="IMG_20151114_115632 (Medium)" >}}

I used one of the panels to help determine the hole placement for the [M3x15mmx21mm PCB standoffs](http://www.amazon.com/gp/product/B00NPZCP2I). After measuring, marking, and drilling the holes, and installing the standoffs, a quick test fit of 4 panels confirmed that everything lined up well enough. With that done, I drilled a hole for the power/data/ground wires and got to work on the back.

{{< figure src="/wp-content/uploads/2015/11/IMG_20151114_134050-Medium.jpg" caption="IMG_20151114_134050 (Medium)" >}}

I wanted the option to mount this on a wall, but I needed to create spacers of some kind to allow for the Raspberry Pi and the AllPixel to be attached to the back. A few scrap pieces of the same pine and some wood glue did just the thing. The display can either sit on a desk top or, with some simple hardware, can mount on a wall like a picture frame.

{{< figure src="/wp-content/uploads/2015/11/IMG_20151115_082059-Medium.jpg" caption="IMG_20151115_082059 (Medium)" >}}

Once the glue was dry, I used a few small wood screws and a twist tie to secure the Raspberry Pi, the AllPixel, and the 5V power input jack. To save on the amount of USB cables needed, I cut up a prototyping wire with 0.1" female headers and was able to draw 5V from the power input jacks into one of the 5V pins on the GPIO header of the Pi.

{{< figure src="/wp-content/uploads/2015/11/IMG_20151115_091539-Medium.jpg" caption="IMG_20151115_091539 (Medium)" >}}

{{< figure src="/wp-content/uploads/2015/11/IMG_20151115_091600-Medium.jpg" caption="IMG_20151115_091600 (Medium)" >}}

With everything secured and wired up, I grabbed a 5V 4A wall wart and fired it up. Being able to utilize [PixelWeb](/2015/11/02/announcing-pixelweb-and-bibliopixel-2-0/), the web UI for our popular BiblioPixel LED library, makes it very easy to load and run animations on the display. Now to think up of some clever ways to utilize the display. First, a clock. Obviously :)

Questions? Comments? Drop a comment below or hit us up on [our forum](http://forum.maniacallabs.com/index.php).


