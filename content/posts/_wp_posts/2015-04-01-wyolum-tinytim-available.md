---
author: adam
date: 2015-04-01 23:30:15+00:00
draft: false
title: WyoLum TinyTiM Available
type: post
url: /2015/04/01/wyolum-tinytim-available/
categories:
- AllPixel
- BiblioPixel
- Cool Stuff
- WyoLum
---

We've shown off pre-production versions before, but our friends at [WyoLum](http://wyolum.com) have just made the awesome TinyTiM [available](http://www.seeedstudio.com/depot/TinyTiM-LED-board-p-2392.html)!

The TinyTiM, much like their larger [TiM](http://www.seeedstudio.com/depot/TiM-p-1516.html), is an awesome, well-made (by the same manufacturer as the AllPixel!), and versatile 8x8 LED matrix based on the WS2812 LED. And it's 100% compatible with the [AllPixel](/AllPixel)!

As usual, Justin from WyoLum is super awesome and sent us some early production boards...

{{< figure src="/wp-content/uploads/2015/04/IMG_20150228_193754-1.jpg" caption="WyoCube" >}}

{{< figure src="/wp-content/uploads/2015/04/IMG_20150228_194004-2.jpg" caption="WyoCube" >}}

Nope... it wasn't just one TinyTiM... it was six!

<!-- more -->

{{< figure src="/wp-content/uploads/2015/04/IMG_20150228_194328-3.jpg" caption="WyoCube" >}}

{{< figure src="/wp-content/uploads/2015/04/IMG_20150228_195203-4.jpg" caption="WyoCube" >}}

Six TinyTiMs to make one _seriously_ cool LED cube :)

As I mentioned, they are fully compatible with the AllPixel but there's a slight setup step that needs to be done first. The TiM and TinyTiM can be used in both parallel and serial mode. Parallel is for driving each of the 8 columns separately with something like the FadeCandy. Serial means that the entire matrix is setup as one continuous strip, which exactly what the AllPixel needs. There are solder pads on the back of the matrix and if you jump them with a small solder blob, it will connect all the columns into a serial configuration.

{{< figure src="/wp-content/uploads/2015/04/IMG_20150228_195401-6.jpg" caption="WyoCube" >}}

{{< figure src="/wp-content/uploads/2015/04/IMG_20150228_195409-7.jpg" caption="WyoCube" >}}

I then installed male and female JST leads onto each of the input and output pads (since you can't use the black IDC connectors in serial mode). Be sure that the input and output connector genders remains consistent!

{{< figure src="/wp-content/uploads/2015/04/IMG_20150228_220607-8.jpg" caption="WyoCube" >}}

Next, to assemble the panels into a cube. This is achieved with some awesome, [3D printed corner brackets](https://github.com/wyolum/Lada/blob/master/fabricate/TinyTiMCube.stl) that are held on with some M3 screws. I've been told that WyoLum doesn't have current plans to sell these brackets, but they are quick to print if you have access to a printer. And there are plenty of online service options if you don't.

{{< figure src="/wp-content/uploads/2015/04/IMG_20150228_232344-9.jpg" caption="WyoCube" >}}

{{< figure src="/wp-content/uploads/2015/04/IMG_20150228_235909-10.jpg" caption="WyoCube" >}}

{{< figure src="/wp-content/uploads/2015/04/IMG_20150301_141451-11.jpg" caption="WyoCube" >}}

{{< figure src="/wp-content/uploads/2015/04/IMG_20150301_143305-12.jpg" caption="WyoCube" >}}

{{< figure src="/wp-content/uploads/2015/04/IMG_20150301_143335-13.jpg" caption="WyoCube" >}}

{{< figure src="/wp-content/uploads/2015/04/IMG_20150301_144049-14.jpg" caption="WyoCube" >}}

There's a bunch of ways you could layout the panels and it all depends on how you are going to program the cube. But for the sake of consistency, the panels in this cube are setup as follows and this layout is assume in the below example code.

{{< figure src="/wp-content/uploads/2015/04/cube_diagram-e1427930117868.png" caption="cube_diagram" >}}

{{< figure src="/wp-content/uploads/2015/04/TimCubeLayout-e1427930137181.png" caption="TimCubeLayout" >}}

I'm still working on the best and least confusing way to handle 3D animations, but for now it's a bit on the manual side, using LEDMatrix and some custom coordinate mapping:

[gist https://gist.github.com/adammhaile/9544a512efe8f848783b]

Run the above and you'll get this totally hypnotic awesomeness:

{{< youtube WtDjheOwY7s >}}

That's all for now, but I'm still working on improving 3D animations to work with this. **Many** thanks to WyoLum for sending us this awesome piece of kit! Be sure to head on over to their [Seeed Studio store](http://www.seeedstudio.com/depot/TinyTiM-LED-board-p-2392.html) and pick one, or six, up!

Happy making!
