---
author: dan
date: 2013-10-29 21:46:12+00:00
draft: false
title: 'CreepinEyes: Last-Minute Halloween Decorations'
type: post
url: /2013/10/29/creepineyes/
categories:
- Cool Stuff
---

Realizing that Halloween was only a few days away, I thought to myself "Self, your house has no Halloween decorations, and thus, is Lame." Being the crafty (and cheap) electrical engineer that I am, I took stock of my...stock...of electronic widgets and bits. After some thought, I decided on a couple of beady little red eyes peeking out of various windows would be appropriately festive, somewhat creepy, and very easy to through together.

{{< youtube RK16OR_Ojok >}}

Each pair of eyes uses an ATTiny85 chip and two 10mm red LEDs. Since Halloween decorations displayed year-round are frowned upon by my homeowner's association, I also wanted these to be temporary. Luckily, I had a few protoboards that I could tie up for a few days.

[![CreepinEyes_3boards](/wp-content/uploads/2013/10/CreepinEyes_3boards-300x225.png)
](/wp-content/uploads/2013/10/CreepinEyes_3boards.png)

Since this is a simple, temporary project, I made use of the awesome [Arduino-Tiny](https://code.google.com/p/arduino-tiny/) set of "cores" for the Arduino IDE. Arduino-Tiny allows for a variety of ATTiny chips to be programmed directly form the Arduino IDE. There may not be 100% functionality, but it's darn close. But of course the ability to blink lights is there, hehe. All I had to do was throw together the code and upload using my [USBTinyISP](http://www.adafruit.com/products/46).

[![CreepinEyes_prototyping](/wp-content/uploads/2013/10/CreepinEyes_prototyping-300x225.png)
](/wp-content/uploads/2013/10/CreepinEyes_prototyping.png)

Speaking of the code, here it is:




    int led = 2;
    int led2 = 3;

    int randblink = 0;

    void setup() {
      pinMode(led, OUTPUT);
      pinMode(led2, OUTPUT);
    }

    void loop() {
      digitalWrite(led, HIGH);
      digitalWrite(led2, HIGH);
      randblink=random(5000,30000);
      delay(randblink);
      digitalWrite(led, LOW);
      digitalWrite(led2, LOW);
      delay(400);
    }




Note: In the Arduino IDE, under 'Board', I selected 'ATTiny85 @ 1MHz (internal oscillator; BOD disabled)'

Using a little bit of 'random' allowed for a little bit of variety in the "blinking." The effect is simple, but pretty neat. And now my house is less Lame.

