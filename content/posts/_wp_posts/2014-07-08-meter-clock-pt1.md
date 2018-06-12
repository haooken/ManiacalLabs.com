---
author: dan
date: 2014-07-08 13:00:17+00:00
draft: false
title: 'Meter Clock: Keeping "Current" Time'
type: post
url: /2014/07/08/meter-clock-pt1/
categories:
- Clocks
- Projects
---

{{< figure src="/wp-content/uploads/2014/07/MeterClock_1.jpg" caption="MeterClock_LitUp" >}}

I've seen a few meter clocks in my travels of the web, and I love the idea. A few days ago, I decided that I must have one of my own. Such began the "How to do it" pondering cycle. I had seen builds where the face plate of the meter is replaced. This works, but I wanted to try and find a way to do it without modifying the meter, if possible. After some more ponderation, I came up with what I think is a serviceable idea.

<!-- more -->

{{< figure src="/wp-content/uploads/2014/07/IMG_0235-Medium.jpg" caption="MeterClock_MeterTest" >}}

I came across this style of [milliamp meter](http://www.ebay.com/itm/New-Analog-AMP-Panel-Meter-Gauge-DC-0-100mA-85C1-/250770439889?pt=LH_DefaultDomain_0&hash=item3a63153ed1) on <del>Amazon</del> Ebay (the original Amazon one appears to no longer exist). They're not quite 0-60 mA, but the 0-100 mA (a 0-20mA meter for the hours) is close enough. And they were cheap. So yay.

Part of my requirements were that the clock run off of an [Arduino Pro Mini](http://arduino.cc/en/Main/ArduinoBoardProMini) I had lying around, and with minimal additional parts. In order to drive the meters with some degree of precision, I would use the PWM pins to vary the effective voltage across a resistor in series with the meter. This would, by the grace of Ohm's Law, induce a current that, based on the PWM duty cycle, would be scaled in such a way as to move the needle on the meter to the corresponding hour, minute, or second.

One minor issue came up in the form of the max current the GPIO pins on the ATMega328 chip can source/sink. The pins can source/sink a maximum of 40mA, a bit far from the 60mA needed for the minutes and seconds meters. Enter the transistor.

Using a simple NPN transistor switch circuit, I was able to provide the current for the minute and second meters from the 5V supply. The PWM signals switch the respective transistors on and off, effectively varying the voltage across the resistors in series with the meters.

The resistor between 5V and the meter is actually **2 1/4 watt 100 Ohm resistors in parallel** for an effective resistance of 50 Ohms. The two in parallel was necessary as 5V x 0.06A = 0.3W (more than 0.25 that a single 1/4W resistor can handle safely).

{{< figure src="/wp-content/uploads/2014/07/MeterClock_MeterSchematic.jpg" caption="MeterClock_MeterSchematic" >}}



After the basic hardware was breadboarded and verified working, I set about throwing together a small board with the Arduino Pro Mini and a [ChronoDot](http://macetech.com/store/index.php?main_page=product_info&products_id=8) I also happened to have lying around.

{{< figure src="/wp-content/uploads/2014/07/IMG_0253-Medium.jpg" caption="MeterClock_assembled" >}}

The APM and the ChronoDot sit in female headers. This allows for smaller components to fit beneath the larger parts. I've used this trick in the past to maximize board space and to allow for core parts of the board to be removed and used elsewhere if needed. The two wires coming up from the ChronoDot to the top of the APM are the SDA and SCL lines (the ChronoDot uses the I2C interface). The remaining discrete components and wires are crammed in underneath:

{{< figure src="/wp-content/uploads/2014/07/IMG_0259-Medium.jpg" caption="MeterClock_Internal" >}}

In the picture above, only the meter connections are soldered on. As you might have guessed from the image at the start of this post, the meters light up. Ahh, well the LPD8806 RGB LED strip beneath the meters lights up. At present, the meters will change color based on the value they display. For example, as the seconds meter moves through 0-59, the color will change according to ROYGBIV (red, orange, yellow, green, blue, indigo, and violet).

The next steps will be to add a few buttons to change color mode/brightness, and to allow the clock to be set without needing to be re-programmed. I also want to either print or build from wood a case of some kind. More updates to follow as work progresses.

Github: [https://github.com/ManiacalLabs/MeterClock](https://github.com/ManiacalLabs/MeterClock)

Any comments/questions, please leave comments below. Thanks!

-Dan




