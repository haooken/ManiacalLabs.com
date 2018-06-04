---
author: youshallnotpass
date: 2013-10-06 19:28:26+00:00
draft: false
title: Challenge Accepted! Binary Epoch Clock 1D Pong Mode
type: post
url: /2013/10/06/challenge-accepted-binary-epoch-clock-1d-pong-mode/
categories:
- Announcements
- Clocks
- Cool Stuff
---

Last night I got to show off our [Binary Epoch Clock kit](/product/becv1/) on Adafruit's excellent Show-And-Tell weekly Hangout.
There was a great turnout with tons of cool projects and I'd like to thank Adafruit again for letting me join in.

Check out the whole show. There were a ton of great projects (I'm at [2:26](http://www.youtube.com/watch?v=C51y6V6NJGs&feature=share&t=2m26s)):

{{< youtube C51y6V6NJGs >}}

Towards the end of my time, Limor Fried noted that the only thing it needs now is a 1D pong mode and I am rarely one to pass up such a challenge...
So this morning I came up with this:

{{< youtube 0s55wwXbCHY >}}

It's not actually playable, but just plays through a random game of (very linear) Pong.
Since there's no where for the "paddles" to actually move to I decided to pretend that in this world of 1D pong the paddles simply have a binary state. They are either there or they are not.
Internally, those states are randomly chosen on each ball bounce or reset.

After either side scores, the current score is shown for one second by filling either side with the current count. Being that there are only 16 LEDs per side, the first one to 16 points wins! (And then the game resets).

Since I wanted to keep this as a functional clock, I didn't involve the two buttons and make this playable but it would be very doable. Just make it so the button on either side has to be pressed with in a certain window of time that the ball is near either end.

I took this opportunity to also release to the published firmware a new clock face created by our good old friend, Josh, of the [Proton Pack display](/2013/09/19/who-ya-gonna-call/) fame. He thought it would be cool to have a clock face that breaks the 32 LEDs into subsections that show the binary value for seconds, minutes, hours, day, month and year. Amazingly, 32 was the exact number needed. This makes reading the time a little easier to begin with and even easier when coupled with this printable guide he created.

![/misc/Binary_Clock_Key.png]

Just print it off, and adhere it to the back of the clock.

To facilitate all of these clock faces, I've made a tap of button A cycle through each of the faces in the order: 32 bit Epoch Binary > Normal Binary > 1D Pong

You can grab this new firmware from [GitHub](https://github.com/ManiacalLabs/BinaryEpochClock) and load it up on your clock today!

Don't have one yet? Grab yours [from the store](/product/becv1/) now!*

*Note: Our current shipping kits have the older v1.0 firmware pre-programmed. You will need an FTDI cable and the Arduino IDE to load this v1.1 firmware.

-Adam

