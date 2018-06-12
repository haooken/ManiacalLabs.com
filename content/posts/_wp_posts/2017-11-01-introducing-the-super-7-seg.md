---
author: adam
date: 2017-11-01 16:47:53+00:00
draft: false
title: Introducing the Super 7 Seg!
type: post
url: /2017/11/01/introducing-the-super-7-seg/
---

We are pleased to announce availability of our latest kit, the Super 7 Seg display!
{{< figure src="https://github.com/ManiacalLabs/Super7Seg/raw/master/doc/img/Super7Test.gif" caption="" >}}


The **Super 7 Seg** kit takes using a 7 Segment display to the extreme! It started as an exercise in "how many 7 segment displays can I drive with a single ATMega328p" and we are quite proud of the result.

Twelve beautiful, bright, 0.8" tall digits powered and driven by only 3 pins. The simple serial connection (literally just sending text) means you can have a simple to use 7 segment display controlled by anything able to output a serial signal, including but not limited to Arduino, Raspberry Pi, and any normal computer (with a USB to serial cable). If required, there are also basic, easy to use, commands that can be sent allowing direct control over each segment of each digit of the display.

But wait, is twelve digits not enough for you? Fear not! You can chain up to 10 Super 7 Seg displays together and still control all of them from just the same 3 pins! Every bit of text that won't fit on the first display is automatically sent down the line to the next and the next after that.

{{< youtube SQ2GdSKWSIE >}}

For more details check out the [Super 7 Seg product page](/Super7).
