---
title: Billiard Ball Arcade Trackball Mouse
date: 2019-01-22T16:59:19-05:00
draft: false
tags: []
categories: []
weight: 20
# slug:
# description:
author: Adam Haile
---


{{< figure src="!header.jpg" >}}

I have a confession... it's hard to admit...

I... I use a trackball mouse.

There. I said it. Glad that's finally out.

I used to be a regular mouse user like everyone else, but between repetitive stress injury, frequently working on my laptop while watching TV on the couch, and absolutely *hating* trackpads; a trackball was the way to go. But, if I'm honest, I've gained a bit of an obsession with them. Currently I rock out with the Logitech [M570](https://www.logitech.com/en-us/product/wireless-trackball-m570 ) and [MX Ergo](https://www.logitech.com/en-us/product/mx-ergo-wireless-trackball-mouse).

So, a few months ago, when my wife and I were watching *Ocean's 8*, my jaw dropped a bit when I saw this:

{{< figure src="movie_mouse.jpg" >}}

Did I mention I also love billiards? I'm no good, but I play whenever I get a chance.

But anyways, what you see there is the trackball mouse used by the character "9-Ball", the con-woman team's quirky hacker, played by Rihanna.  There's only a couple brief shots of the actual mouse in the film and it at least appears to work (more on this in a second). Ridiculous as it is, I had to have one.

Fortunately, the internet is vast these days and it took mere seconds to find out that the mouse in question was the popular [Kensington Expert](https://www.trackballmouse.org/kensington-expert-trackball-in-the-movie-oceans-8/) but that it also wouldn't work.. at least not well.

You see, the Kensington Expert uses a 55mm (2.16 inch) ball but a standard American billiard ball is 57.3 (2.25 inch). So, at best, the billiard ball is slightly oversized and doesn't perfectly interact with the sensors. At worst, the sensors won't see it at all and, *gasp*, what you see in the film is pure movie magic.

But really, that was no matter because, as a trackball aficionado, I have opinions about these things and trackballs with a center ball instead of under the thumb are terrible and should be avoided. And besides, I didn't want the mouse from the movie... I wanted a mouse with a billiard ball. So in my true fashion, I started with a single specification, the 2 1/4 inch billiard ball and tried to find something that would work.

Now, sure, I'm entirely capable of rolling my own solution, but my time is precious. And while research showed that there were no regular computer mice that used a ball of that size (the Kensington was the largest), it turned out that arcade trackballs use both 2 1/4 and 3 inch. I ended up finding a not cheap, but not outrageous arcade trackball unit that is 80's Atari compatible and still manufactured by Happ over on [ArcadeShop.com](http://www.arcadeshop.com/i/19/2-trackball-unit-white-ball-atari-happ.htm)

{{< figure src="happ.jpg" >}}

Even better, since this is tech from the 80s, the interface is really simple; just 2 rotary encoders (of the optical slit-disc variety), one for each movement axis, connected to rollers that the ball sits on. With an Arduino they are exceptionally easy to read, especially using the [Encoder library](https://github.com/PaulStoffregen/Encoder) from Paul Stoggregen of Teensy fame. The library simply outputs a -1, 0, or 1 on each poll, indicating if it moved since last check and which direction. Combine two of those and you can move a mouse pointer in X and Y directions.

So now I had the trackball and at this point I was down the hole of an Arcade / Billiard themed mouse, so I decided it was best to just go all in and use 24mm arcade buttons as well. I found these great buttons over on [Adafruit](https://www.adafruit.com/product/3432) so I picked up a few of each color.

<video preload="auto" muted loop autoplay src="3432-03.mp4"></video>

They've each got a built in LED with resistor, so only power need be applied. Though as I'll mention later, not all were created equal.

So now all that was left was the interface between the trackball, buttons, and a computer. There's lots of options out there but, in my personal opinion, if you need to do a lot of fast IO interaction and/or anything USB HID related, you grab a [Teensy](https://www.pjrc.com/store/teensy32.html). Lucky for me I pretty much always throw one onto my [OSHPark](https://oshpark.com) orders so I have plenty on hand :)

Now, I could have easily just wired all the buttons and trackball directly to the Teensy as this literally requires no other passive or active hardware. But, I know how to use KiCAD, so...

{{< figure src="pcb.jpg" >}}

This also, of course, acts as mounting for the Teensy inside the mouse itself which is a lot better that hot glue :P

At this point the big hurdle was designing the mouse itself, which of course fell to Fusion 360. The main issues were getting everything to fit and to be as ergonomic as possible. With Fusion it was relatively easy to get the basics by taking a top-down picture of my own hand over the trackball assembly. That image was than overlaid in the CAD model as a canvas and calibrated to the correct size via the CAD model I had already made of the trackball. This allowed finding the correct placement of the 3 main mouse buttons under each finger. Note to those who may want to make their own: Small hands need not apply. This is very much designed for me.

{{< figure src="ergo.png" >}}

With that part figured out it was just a lot of sketching, extruding, pushing, and pulling until I had a general shape that fit all the components and some amount of ergonomics. I set the top face at a 10&deg; angle with the intent that it would be used with my elbow resting on my desk and that seemed like a comfortable angle. This made for what was... well, quite large. In my mind all good projects start with a single base concept and everything is built out from there, whatever that means. And while this is a mouse in functionality, it's certainly a mouse like none ever seen:

{{< figure src="arcademouse.gif" >}}

Remember, those are 24mm buttons and a 2.25" trackball! I would have preferred to make it smaller of course, but there was just no room for the hardware involved. And at that point I needed to have a built-in wrist rest to make it comfortable. Fortunately, I have a massive 3D printer which made short work of the case in only 2 pieces :)

{{< gallery >}}
    {{< figure link="/images/arcademouse/print1.jpg" >}}
    {{< figure link="/images/arcademouse/print2.jpg" >}}
    {{< figure link="/images/arcademouse/print3.jpg" >}}
    {{< figure link="/images/arcademouse/print4.jpg" >}}
{{< /gallery >}}

Originally my plan was just to leave it as is, straight off the printer. But my friend [Sam](https://www.instagram.com/munillagorilla/) convinced me to finally, after all these years of 3D printing, try my hand at finishing and painting it. After a much advice from Sam, a coat of XTC-3D, two coats of sandable primer, two coats of automotive paint, and three coats of clear enamel (one gloss, and two satin), I had something not perfect, but *way* better than the bare print. Much, smoother and nicer to use :)

{{< gallery >}}
    {{< figure link="/images/arcademouse/fin1.jpg" >}}
    {{< figure link="/images/arcademouse/fin2.jpg" >}}
    {{< figure link="/images/arcademouse/fin3.jpg" >}}
    {{< figure link="/images/arcademouse/fin4.jpg" >}}
{{< /gallery >}}

Maybe sometime I'll get Sam to share is 3D print painting secrets with the world ;)

In my typical fashion I left most of the code for this project until the hardware was done. Of course I had proof-of-concept code to be decently sure it would work but I left the bulk of the fine details until now. The one thing I wish I had tried more was all the different buttons and their LEDs. As noted before I had a bit of an issue with the buttons other than blue and clear. For some reason, the red and yellow buttons barely lit up at all when using the 3.3V available on the Teensy, while blue and clear did. Honestly I was surprised they worked at all but I was just happy that two colors worked and fortunately had ordered extras so I just stuck with those two colors, as you can see in the video below:

<video preload="auto" muted loop autoplay src="ArcadeMouse.mp4"></video>

Other than that little snag, the code was pretty trivial. All it really does is read the two encoder outputs and all five buttons, then sends the appropriate signals over USB using the `Mouse` class that comes with the Teensy software.

The two non-standard buttons that you may be wondering about are the two clear ones. The one at the top is the the sensitivity toggle. Because this is an arcade trackball the ball has to move farther than is really desirable for each pulse sent from the encoder. So to make the mouse more usable, I simply multiply the output of the encoder so that one pulse actually moves the mouse four pixels in the given direction. But this can make the mouse less precise. So toggling that button drops the multiplier down to two instead of four, making for slower movement but much more precise tracking.

The second button, the one below the trackball, is the scroll button. Holding this button will cause the trackball to send scroll wheel signals instead of mouse movements.

The three blue buttons are, of course, just your standard left, middle, and right click.

There is a link at the end to the code so be sure to check that out if you are curious.

After using the mouse for over a week at the day job I've got to say I like it. It definitely took some getting used to compared to my Logitech mice, but within a day it was no issue at all. It's quite comfortable to use even. It of course helps that it was modeled to my hands personally and that bump I added under the palm allows my hand to rest in a nice, comfortable position.

Were I to do it again, however, there are a few things I would change.

The scroll button position made sense at the time of design, with the thought that I would just move my hand so that my thumb was over the button and fingers over the ball. But in actual usage that immediately seems silly, because I have to move my hand! What was I thinking?! What I should've done was place that button under my pinky finger so that my hand never had to move at all. Fortunately I got pretty used to only barely moving my hand to scroll, but I may still think about redesigning the case a bit to change the layout in the future.

Second, I would like to attempt implementing some sort of mouse movement acceleration in the firmware. Something to the effect of the more cycles that go by with continuous mouse movement, the higher the movement multiplier. This would make fast and far movements easy, but allow precise tracking without needing that toggle button. Fortunately that's a software change that I can still do in the future.

And, honestly, that's it. It's fun to use and a major conversation starter. Amazingly the reaction has always been along the lines of **"what's with that crazy mouse?!"** and not **"what on earth is that?!"**. So I'm proud to have still made it obvious what it is, despite the crazy and huge design :)

So, you've made it this far and that probably means you're interested in the minute details of the project :)
Have no fear, everything you could ever want - PCB designs, Firmware, and CAD files - are all available over on GitHub: https://github.com/ManiacalLabs/ArcadeTrackballMouse

That's all for now. Thanks for following along with my journey of creating something that should likely not exist :)

