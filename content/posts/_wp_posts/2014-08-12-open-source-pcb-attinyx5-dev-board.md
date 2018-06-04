---
author: adam
date: 2014-08-12 13:00:32+00:00
draft: false
title: 'Open Source PCB: ATTinyX5 Dev Board'
type: post
url: /2014/08/12/open-source-pcb-attinyx5-dev-board/
categories:
- Arduino
- Projects
- Tools
---

While the standard Arduino (especially variants like the [Pro Mini](http://arduino.cc/en/Main/ArduinoBoardProMini)) truly is a lilliputian computing device, even it sometimes seems like trying to swat a fly with a sledgehammer. Sometimes you just need a few I/O pins for a status light, timer, tiny sensor, etc. Enter the [ATTinyX5 series](http://www.atmel.com/devices/attiny85.aspx) of chips.

The ATTiny25, ATTiny45, and ATTiny85 have 8 pins, 6 I/O and 2048/128, 4096/256 and 8192/512 bytes of flash/RAM respectively. The '85 can be had for just over $1 from sites like [Mouser](http://www.mouser.com/ProductDetail/Atmel/ATtiny85-20PU/?qs=sGAEpiMZZMtkfMPOFRTOl5CRAVRAdtfp). There's even an [Arduino core available](https://code.google.com/p/arduino-tiny/) for them so you can use most* of the code and libraries you already know and love. The only problem is that, without a complicated setup and boot-loader, they require an ICSP device like the AVR ISP MkII to upload your code.

<!-- more -->

After getting sick of having to wire up the 6-pin ICSP header of a breadboard every time I wanted to use one I finally decided to create this:

{{< gallery dir="/wp-content/galleries/2014-08-12-open-source-pcb-attinyx5-dev-board/0/" />}}

This tiny PCB takes some of the pain out of all the hookup needed for prototyping with the ATTinyX5. It only requires 2 components, the IC and a 0.1uF decoupling capacitor. On the underside of the board, there is an ICSP header that uses offset pin holes so that the 2x3 header doesn't actually need to be soldered on. Simple press fit the header into the holes and then connect the ICSP cable. When you are done programming you can remove the header and the cable. The headers on the side are spaced to fit nicely on a breadboard and are also offset so that they can be press fit and work without permanently soldering them on.

By placing the board onto your breadboard up-side-down, you have easy access to the ICSP header for programming. Once the code is good, you can then easily remove the press fit headers and solder everything on permanently.

{{< gallery dir="/wp-content/galleries/2014-08-12-open-source-pcb-attinyx5-dev-board/1/" />}}

Best of all, you can have 3 of these made by [OSHPark](http://oshpark.com) for only $1.65, shipped. They can be easily ordered directly from their project page [here](https://oshpark.com/shared_projects/zauik82y).

Also, you can grab the KiCad design files from our [GitHub repository](https://github.com/ManiacalLabs/ATTinyX5_Breakout).

*Many libraries require features the ATTiny series simply is missing or more RAM/Flash than available on the chip. However, there are also many libraries written specifically for these chips.

**Note: The silkscreen labels has been tweaked since what you see in the picture (see the OSH Park renders) as they were not very visible. They have been increased in size and re-oriented for better visibility.

{{< load-photoswipe >}}