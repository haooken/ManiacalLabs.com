---
author: dan
date: 2014-10-07 13:00:51+00:00
draft: false
title: Random Photos
type: post
url: /2014/10/07/random-photos/
categories:
- Clocks
- Projects
---

I had a 24-led NeoPixel ring lying around being useless, so I decided to make it do something less useless. As is typical, it became a clock. Not an original idea, sure. But these rings are well-suited for clockification. The blue 'seconds' lights will fade around the ring once per minute. There's some mapping logic to determine where the green 'minutes' light should go. Hours is straightforward enough if the clock is showing 24hr time.

[![NeoPixelRingClock](/wp-content/uploads/2014/10/NeoPixelRingClock-300x200.jpg)
](/wp-content/uploads/2014/10/NeoPixelRingClock.jpg)



I found [this low-power ATTiny85 example circuit](http://arduinoelectronics.wordpress.com/2014/01/06/ultra-low-power-led-flasher-with-attiny/) in my travels and since I have a few ideas for low-power digital circuits, I decided to throw this together. It just blinks the LED once every 4 seconds. Nothing fancy, but the goodness is in the code in how the chip is put into deep sleep and only woken up when it's time to blink. Also, those ideas I mentioned involve dead-bug construction. With that 500 mAh battery, it should run for ... a really long time.

[![LowPowerATTiny85Test](/wp-content/uploads/2014/10/LowPowerATTiny85Test-e1412637628835-200x300.jpg)
](/wp-content/uploads/2014/10/LowPowerATTiny85Test-e1412637628835.jpg)



So when you have access to a 3D printer, making tabletop siege weaponry is part of the natural progression of things. These parts are part of a game called [Seej](http://zheng3.com/seej/). There's a whole bunch of obstacles, fortifications, and siege weapons that can be printed. Good fun. We found that printing on a higher detail level than "lowest of the low" might be a good idea since some of the tolerances are tight.

[![PlayinSeej](/wp-content/uploads/2014/10/PlayinSeej-300x225.jpg)
](/wp-content/uploads/2014/10/PlayinSeej.jpg)



That's all for today. Thanks for visiting!


