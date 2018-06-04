---
author: dan
date: 2014-04-08 04:01:13+00:00
draft: false
title: Wireless Outlet Remote Control...Control
type: post
url: /2014/04/08/wireless-outlet-control/
categories:
- Projects
---

In the near future, Scott and myself will be taking a crack at Adafruit's [Arduino-powered immersion cooker](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino/sous-vide). I've looked at this tutorial a few times, and I have now amassed enough of the parts as a result of other projects to make this a not-very-expensive build.

There was one wrinkle, though. This project requires the control of a 120V outlet with an Arduino. The recommended [Power Switch Tail](http://www.adafruit.com/products/268) is, at this time, difficult to come by. I'm not sure if it has been discontinued or not, but lead times and cost are significant on the sites that I've visited. I feel that I have the skill to throw together a relay and some cut-up extension cord, but if I burn my house down, it would kind of be a hard sell to the insurance company. So another solution to switch on and off an 'analog' crock pot was needed.

Some time ago, I picked up a set of three outlets that can be toggled on and off with a small RF remote. I thinks to myself, if I can toggle a button on the remote with a simple circuit, I have the answer to the 120V control wrinkle. Here's what I came up with:



**[![RemoteBuild_ClosedSideView](/wp-content/uploads/2014/04/RemoteBuild_ClosedSideView-300x225.jpg)
](/wp-content/uploads/2014/04/RemoteBuild_ClosedSideView.jpg)**





[![RemoteBuild_TestSetup](/wp-content/uploads/2014/04/RemoteBuild_TestSetup-300x225.jpg)
](/wp-content/uploads/2014/04/RemoteBuild_TestSetup.jpg)





By soldering on two wires to either side of the button for outlet 3, I was able to bring those two points out to accessible female headers:





[![RemoteBuild_Prebuild](/wp-content/uploads/2014/04/RemoteBuild_Prebuild-300x225.jpg)
](/wp-content/uploads/2014/04/RemoteBuild_Prebuild.jpg)





[![RemoteBuild_PCBunderside](/wp-content/uploads/2014/04/RemoteBuild_PCBunderside-300x225.jpg)
](/wp-content/uploads/2014/04/RemoteBuild_PCBunderside.jpg)





[![RemoteBuild_OpenSideView](/wp-content/uploads/2014/04/RemoteBuild_OpenSideView-300x225.jpg)
](/wp-content/uploads/2014/04/RemoteBuild_OpenSideView.jpg)



So now, if I were to short those two headers together, the circuit completes and the button is "pushed." That's the first step. Now I need a way to "short" that connection that can be controlled by a digital output pin. A small transistor works pretty well for this. I had a [2N3904](http://www.fairchildsemi.com/ds/2N/2N3904.pdf) lying around. A 10K resistor and some prototype wire later, I had this circuit implemented:



[![Circuit](/wp-content/uploads/2014/04/Circuit.png)
](/wp-content/uploads/2014/04/Circuit.png)





[![RemoteBuild_TestCircuit](/wp-content/uploads/2014/04/RemoteBuild_TestCircuit-300x225.jpg)
](/wp-content/uploads/2014/04/RemoteBuild_TestCircuit.jpg)





I was really happy with this solution. The remote is still completely usable. When we decide to give the Adafruit project a go, all we need to do is plug in the remote. And for future projects, modifying the remote to allow control of the other two outlets wouldn't be too difficult. 





I suspect there will be some slight code modification required for the final project, however. In the test circuit, the button was toggled by raising D13 high for a 300ms pulse. So there's not a direct 1-to-1 relation between the control pin being high and the heat being on. I don't think it will be too big a problem, just something to remember to do.





From a safety standpoint, this is probably the best option for the immersion cooker build. The mains power control is about as isolated from the control circuit as you can get. All the same, when this thing is running, it won't be left unattended. After all, something that I built will be controlling something with a heating element. Common Sense is advised.





-Dan
