---
author: youshallnotpass
date: 2014-11-13 04:37:00+00:00
draft: false
title: AllPixel Update - Staff Pick!
type: post
url: /2014/11/13/allpixel-update-staff-pick/
categories:
- Announcements
- Kickstarter
- New Product
- Products
---

First of all, the [AllPixel Kickstarter](https://www.kickstarter.com/projects/1101128588/allpixel-usb-interface-for-all-your-led-needs) has been going great! Fully funded in less than 48 hours, chosen as a Kickstarter Staff Pick on the third day, and currently at over 130% funded and 150 backers... with 26 days left!

We didn't want to bog down the main page with really technical details about how the AllPixel works, but we thought we should give some more background.



# The Hardware



At the core, the AllPixel is not much different from devices like the Arduino Leonardo, Arduino Pro Micro, or Teensy 2. In fact, our original prototype used a Pro Micro.

[![IMG_0528-16x9](/wp-content/uploads/2014/11/IMG_0528-16x9-300x168.jpg)
](/wp-content/uploads/2014/11/IMG_0528-16x9.jpg)

[![IMG_0537-Edit-16x9](/wp-content/uploads/2014/11/IMG_0537-Edit-16x9-300x168.jpg)
](/wp-content/uploads/2014/11/IMG_0537-Edit-16x9.jpg)

The heart of the AllPixel is an ATMega32u4 which is what allowed us to provide such amazing frame rates, since it is capable of full 12Mbps throughput on the USB Serial connection. It also provides 2.5KB of SRAM, 2K of which is used to buffer the pixel data. Not needing to waste SRAM on the serial buffer was also a huge advantage of using this chip over the venerable FTDI and something without built-in USB support.

All of this is supplemented by the optional hardware which makes hooking up your LED strips a breeze.




  * 2.1mm barrel jack - makes providing up to 5A of power at 5V super easy.
  * 4-pin screw terminal - no more need to solder your strip connections directly. The AllPixel was designed with using any kind of strip in mind, so making it hard to swap them out wouldn't have made much sense!
  * 1000uF capacitor - Power requirements can fluctuate wildly, depending on the state of an animation. This ensures nice even power when your power supply needs a few fractions of a second to catch up.
  * 300 ohm resistors - These can be placed in R6 and R7 to drop the logic level slightly. This can help prevent damage to some strips, like the WS2812.
  * 1N5817 Schottky diode - Installing this allows for the AllPixel and a small number of attached LEDs to be powered directly from USB. It also protects against accidental external power connections damaging the board and your computer when operating in USB mode.


Last thing of hardware note is that, in order to make the AllPixel work as seamlessly as possible, we provided a super simple method in hardware for the board to reboot itself. This is necessary to allow the firmware to reconfigure and allocate all the necessary resources and provide the best speed when driving all the different chipsets. This is achieved by connecting an NPN transistor and pull-up resistor to the IC's reset pin. To reboot the board, we just drive the transistor input high, which brings the output and the reset low, resetting the chip. Since the digital IO pins all default to input and low on reboot, that logic is immediately flipped upon successful reboot and the firmware restarts.



# The Firmware



All the above alone was not enough to achieve the speeds we wanted. The base Arduino core libraries for the ATMega32u4 max out around 60KB/s. When you need 2KB for each frame, that would've meant at most 30fps, not counting other overhead. This just wasn't good enough.

But then we found the amazing [Teensy Arduino](https://github.com/PaulStoffregen/cores) cores which could handle full USB 1.1 speed! So we got to work adapting those core libraries to what we needed and came up with our own [variant core](https://github.com/ManiacalLabs/ATUSB_Core). These modified core libraries allow us to run full USB speed on anything with a 32u4, even our original Arduino Pro Micro mock-up, and have a few changes such as the ability to change the USB VID and PID from the boards.txt file.

One thing of note, however, is that the current Arduino bootloaders for the Leonardo and Pro Micro do not work with our modified core libraries. This is mainly due to some significant differences in the way the Teensy USB code handles the automatic reboot that puts the device in bootloader mode. In the end, we decided that it was best since we wanted the AllPixel to be able to reboot as fast as possible and having to wait for the bootloader was not an option. The board can still, however, be reprogrammed with any compatible ICSP programmer like the AVR ISP MkII or even another arduino with the "Arduino as ICSP" sketch.

Finally, the real party piece of the whole setup is the great [FastLED](http://fastled.io/) library. This is the "universal translator" of the whole operation. FastLED is an amazing library that not only knows how to talk to all the different LED strips, but is super fast doing it.

We hope that answers some of the questions that people have had about what makes the AllPixel tick.
We'll have more details and some fun little projects for you soon. So, stay tuned and keep spreading the word!
