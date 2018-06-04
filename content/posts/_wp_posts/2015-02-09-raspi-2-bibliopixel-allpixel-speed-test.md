---
author: adam
date: 2015-02-09 13:38:51+00:00
draft: false
title: RasPi 2 BiblioPixel / AllPixel Speed Test
type: post
url: /2015/02/09/raspi-2-bibliopixel-allpixel-speed-test/
---

Since the [Raspberry Pi 2](http://www.raspberrypi.org/raspberry-pi-2-on-sale/) was such an InstaBuy™, we of course bought a couple immediately and they showed up this weekend! So of course, the first thing to test out was how much of a speed improvement we could get with BiblioPixel and the AllPixel. Especially with the new [multi-driver support](/2015/01/21/multi-driver-demo-with-bibliopixel/) :)

The tests were broken down into 3 stages; Easy animation with increasing pixel count, Hard animation with increasing pixel count, and constant pixel count with increasing driver count. In all cases the Bloom animation, which is quite CPU intensive, was used; for which there are two code versions. The easy one is designed for speed at the sacrifice of brightness or matrix rotation support. The hard version handles brightness and rotation but is much more computationally expensive. Each test ran an increasing number of AllPixel drivers, from one to four, each of which always drove a 26x26 matrix of 676 total pixels. So, not only does the driver count increase with each level but so does the pixel count.

The constant pixel test used the easy Bloom version and maintained a constant 600 pixels total, which was divided among each of the four AllPixel drivers so that the more drivers, the fewer pixels each had to control.

The test hardware used consisted of four final revision AllPixel driver boards, a Raspberry Pi 2 Model B and a Raspberry Pi Model B+. To ensure there was no difference due to software version, the same SD card was simply swapped between the Pis.

[![Pi2SpeedTestEasy](/wp-content/uploads/2015/02/Easy.png)
](/wp-content/uploads/2015/02/Easy.png)

In the Easy animation test, you can see that the Pi 2 provides as much as a 300% speed improvement with threading and 200% without.

[![Pi2SpeedTestHard](/wp-content/uploads/2015/02/Hard.png)
](/wp-content/uploads/2015/02/Hard.png)

In the Hard animation test, you can see that the Pi 2 provides nearly a 400% speed improvement for threaded _and_ non-threaded tests. You might have noticed for both the easy and hard tests that the single driver non-threaded was faster than the threaded on the Pi 2, for one driver. We're not 100% sure what's going on in that case... this will require more investigation. But it's likely that the overhead of running the serial communication on another thread isn't overcome by the speed gains of using multiple drivers. As you'll notice, the more drivers used, the greater the difference between multi and single threaded.

[![Pi2SpeedTestConstant](/wp-content/uploads/2015/02/Constant.png)
](/wp-content/uploads/2015/02/Constant.png)

The constant pixel count test was really interesting. The single threaded version on the Pi 2 was consistently faster than the multiple threaded version, but almost the same once you get to four drivers. Each driver is running less pixels as the driver count increases, but there's a minimum overhead incurred which only becomes negated as the driver count increases.

However, it still maintained a 300% speed improvement over the Pi B+, similar to the rest of the tests.

While it's not the 600% performance boost touted by the Raspberry Pi team, it's hard to complain about the speed improvement we are getting. Note that the difference comes from the fact that we only gain a speed boost on the frame generation but almost none from actually sending the data to the AllPixels. Each was setup with an LPD8806 strip, clocked at 16Mhz, so the time to output to each AllPixel was basically a fixed constant, regardless of which Pi was used.

That's all for now. We're super happy to see such a capable single board computer be available and still for only $35!

Happy Making!
