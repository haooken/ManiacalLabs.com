---
author: dan
date: 2014-03-04 23:26:27+00:00
draft: false
title: Polar Giraffe Control Board
type: post
url: /2014/03/04/polar-giraffe-control-board/
categories:
- Cool Stuff
---

_Gasp!_ An Update!

Yes, it's true. We're still here and after coming back from a nice and much-needed vacation, we're ready to start doing cool stuff again. First off, and update on a [previous post](/2014/01/21/enter-the-polar-giraffe/).

I recently put together a PCB to hold the important control elements of the Polar Giraffe. Many Thanks to [OSHPark](https://oshpark.com/) for another quality board!

{{< figure src="/wp-content/uploads/2014/03/PGControlBoard_APMon.jpg" caption="PGControlBoard with Arduino Pro Mini installed" >}}

The [Arduino Pro Mini](https://www.sparkfun.com/products/11113) and [Big Easy](https://www.sparkfun.com/products/11876) drivers from SparkFun have their spots. I was originally going to mount the drivers on headers so they could be removed. But I _might_ have forgotten to verify the correct drill size for the custom KiCAD footprint I made. Oops. Luckily, I was able to use some discarded resistor leads to fit the .0236" holes that should have been .04" holes. So while I can't easily remove the drivers, at least I don't have to spend another $40 to re-fab the board with the right sized hole. Since this is a personal project, I'm OK with it, but I went and updated the footprint as soon as I found out what was wrong.

{{< figure src="/wp-content/uploads/2014/03/PGControlBoard_APMoff.jpg" caption="PGControlBoard with Arduino Pro Mini removed" >}}

Under the Arduino Pro Mini are the resistors for the 4 status LEDs and the resistors and MOSFETs that make up the level converting circuitry that allows the Pi to talk to the APM. This was a great find, and credit to the folks over at [StackExchange](http://electronics.stackexchange.com/questions/18457/is-my-mosfet-based-bidirectional-level-shifter-insane) for providing the tips on how to make this work. Definitely check out that link. I was able to whip up a 2 channel, bi-directional level shifter for less than $2 in components.

{{< figure src="/wp-content/uploads/2014/03/PGControlBoard_7805CloseUp.jpg" caption="PGControlBoard 7805 Close-Up" >}}

So yeah, I also _might_ have forgotten to verify the pinout of the schematic footprint I was using for the 7805 regulator. Facepalm. As you can see, a crisis was averted by some careful pin bending, but I _Definitely_ wouldn't want to do this on a regular basis. Again, the footprint was fixed. The 9V supply is split off to the drivers to power the steppers, and through the regulator to provide the 5V for the servo (not pictured) and the APM.

{{< figure src="/wp-content/uploads/2014/03/PGControlBoard_TestSetupCloseUp.jpg" caption="PGControlBoard Test Setup" >}}

I certainly added to the "Lessons Learned" file on this build. Whenever you _THINK_ you may have everything 100% good-to-go on your PCB, take a step back for a bit, then come back and review EVERYTHING again. You can't be too careful. I'm happy to say that everything seems to be working. A quick test run yielded communication between the Pi and APM, as well as spinning steppers. Next, ah, step, is to figure out a more permanent mounting solution. Then, after dialing in the settings, I hope to be drawing soon!

{{< figure src="https:/wp-content/uploads/2014/03/PGControlBoard_TestSetup.jpg" caption="PGControlBoard Test Setup" >}}

