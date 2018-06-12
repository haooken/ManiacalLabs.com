---
author: dan
date: 2015-08-12 15:19:26+00:00
draft: false
title: Arduino-Based "Analog" Slow Cooker Controller
type: post
url: /2015/08/12/slow-cooker-controller/
categories:
- Projects
---

{{< figure src="/wp-content/uploads/2015/08/IMG_0884_SM.jpg" caption="IMG_0884_SM" >}}

I had two options: One required me to spend money. The other cost me nothing and gave me an opportunity to make something useful.

<!-- more -->

To make a short story longer, I have an "analog" slow cooker (just a dial on the front) and I wanted the ability to set the cooking time and temperature. Now I could have just gone out and bought an appliance timer, which certainly would have done the job. But that wouldn't have given me temperature control. I had a few bits lying around from other projects, so I decided to smash them together and see what happened.

Since I would actually be using the slow cooker for its intended purpose, I really wasn't concerned with being able to set the temperature to the exact tenth of a degree. Being able to select Warm/Low/Medium/High would be fine. Instead of modifying the slow cooker, I would just set the dial to High and control the AC power connection. Having played around with [Adafruit's SousViduino project](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino/sous-vide) a while back, I would use that as a starting point. There, I modified a [wireless outlet](http://www.amazon.com/Woods-32555-Outdoor-Control-Converter/dp/B001Q9EFUK/ref=sr_1_3?&ie=UTF8&qid=1439140906&sr=8-3&keywords=wireless+outlet) remote control such that I could control it with two GPIO pins. This allowed for the actual mains power switching hardware to be completely isolated from the controller. I've used this trick several times to great effect. This time would be no different.

With the AC power control figured out, I considered the User Interface. I opted for something simple. The [Adafruit RGB LCD Shield](https://www.adafruit.com/products/716) would work well as it had both a display and buttons built in. Sure, I could have beat this project about the head and neck with "IoT"-this and "ESP8266"-that, but I was feeling lazy and just wanted a simple timer control. Of course, there's nothing that says I _won't_ add some kind of wireless connectivity, but for now, local control is fine.

{{< figure src="/wp-content/uploads/2015/08/IMG_0882_SM.jpg" caption="IMG_0882_SM" >}}

Having figured out the hardware, the Software was the next part. I'll spare you the gory details and just provide a summary here, but if you want to check out the code, it is up on our [github repo](https://github.com/ManiacalLabs/AnalogSlowCookerController).  The SousViduino project was referenced a number of times for this part as well. There's three main parts to the code: a state machine, a 1-second interrupt, and the AC power control logic. The state machine governs the operation of the controller in its various states (Off, setting time/temp, running, etc.). The code in the repo mentioned above has a detailed description of the state machine functionality, for those interested. The 1-second interrupt ensures accurate timekeeping regardless of what state the state machine is in. When time is up, the temperature is set to the 'Warm' setting to keep the food warm until ready to eat.

The AC power control logic may look familiar to those who have worked with PID control before. In short, the different temperature settings change the duty cycle of the control logic. For example, consider a 60-second window. At the 'High' setting, AC power is on for 100% of that time. For 'Low', it may be on for only 50% of that time (30 seconds). Of course, the trick with this project will be to "dial in" the duty cycle for the different temperature settings. Once I have an accurate power meter (thanks broken Kill-A-Watt...), I can give that a go. This also means that if others wanted to use this code, they could adjust the duty cycle settings for their individual cookers. Of course, this isn't as accurate as a real controller with a temperature probe and active feedback, but like I said, it's a slow cooker acting as a slow cooker. I'm not worried about extremely precise temperature control.

{{< figure src="/wp-content/uploads/2015/08/IMG_20150809_131048_SM.jpg" caption="IMG_20150809_131048_SM" >}}

So I have the controller up and running now. In a few hours, I'll have some tasty pork for burritos. Mmm, burritos. I mentioned that I haven't yet dialed in the temperature control duty cycles for the different settings. I'm hoping to get a new power meter tomorrow, but in the meantime, the slow cooker dial is set to Low and the controller is set to 'High.' This way, AC power is always on, but the dial setting on the slow cooker actually controls the temperature. That's the theory, at least. We'll see in a few hours. If not, I'm ordering a pizza :)

-Dan
