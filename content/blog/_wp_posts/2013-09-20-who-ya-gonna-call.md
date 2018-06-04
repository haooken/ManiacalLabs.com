---
author: adam
date: 2013-09-20 03:49:59+00:00
draft: false
title: Who Ya Gonna Call?
type: post
url: /2013/09/19/who-ya-gonna-call/
categories:
- Cool Stuff
---

Friend of Maniacal Labs, Josh, is a _huge_ Ghostbusters fan. How much, you ask? This much:

[![Ecto Mini](/wp-content/uploads/2013/09/ecto-mini-1024x768.jpg)
](/wp-content/uploads/2013/09/ecto-mini.jpg)

Why yes, that is a Mini Cooper Ecto-1.

A couple weeks ago, Josh emailed me asking if it was possible to get en Epoch Clock Kit with blue LEDs. Obviously, I was intrigued and asked him why. To which his answer was this video:

{{< youtube EpZrzPRPNCs >}}

Yup, that's a Proton Pack, the only problem with it being that it didn't belong to Josh. He has one, but without the awesome, pulsing LED bar. His initial thought was that he could just install the blue LEDs in the clock in place of the red ones (while also changing out the 330 ohm resistors for 150 ohm). Unfortunately, after some measuring we realized that the 6.5" long clock was a bit _too_ long for the slot in his Proton Pack. But after a little brainstorming, we realized that if we reconfigured the LEDs to two columns of 32 an spaced them slightly farther apart it should fit perfectly. The original idea was to wire it all up on some perf-board but then he wouldn't be able to get the desired spacing and, well, it would be somewhat of a pain to build. So I decided to see what I could come up with in terms of a custom printed board and this was the result:

[![ecto adapter front](/wp-content/uploads/2013/09/ecto-front-1024x184.png)
](/wp-content/uploads/2013/09/ecto-front.png)

So, now the plan was simply to solder female headers to the clock board, solder some more to the above adapter board, onto which all the LEDs go, connect the two with some ribbon cable, and reprogram the firmware a little to get the desired animation.  The adapter was pretty cheap for three copies from the wonderful [OSH Park](http://oshpark.com) so Josh ordered some and I got a kit to him with some blue LEDs that I picked up in a recent [Mouser](http://mouser.com) order. Then, today, Josh sent me this:

{{< youtube Etvvc61Toa8 >}}

_Wow_ I'd say that's pretty spot on for the animation shown in the first video! Now I want a Proton Pack just so I have something to put one of these in!

Here's some more close up pictures of the final build:

[gallery ids="601,602,603,604,605"]

Once this goes in the actual pack, I'm sure it's going to look awesome and will really add to the authenticity.

Want to make your own? As is our way, all the source code and board designs are completely open source and can be downloaded from the [GitHub Repository](https://github.com/ManiacalLabs/EctoEpochMod). Just grab a kit from us, send off the adapter to OSH Park and load up the custom firmware!

It's projects like this what really make us here at Maniacal Labs love what we do. When we designed the Epoch Clock we had a few ideas for alternate uses but it's the projects that we _didn't_ think of that really astound us. We wouldn't even be here without such a great community.

