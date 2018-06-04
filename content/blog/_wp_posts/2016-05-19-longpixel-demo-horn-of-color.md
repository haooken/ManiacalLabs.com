---
author: dan
date: 2016-05-19 12:13:52+00:00
draft: false
title: 'LongPixel Demo: Horn of Color'
type: post
url: /2016/05/19/longpixel-demo-horn-of-color/
---

During initial testing of the [LongPixel](/LongPixel) we were brainstorming new ways of stress testing it, since it's actually really hard to get a long enough run of 12V LED strips that draw near the 10A current limit of the board. This little project was an attempt to approach that limit and didn't nearly get there, but it was certainly fun trying.

24 3W RGB LEDs were wired in 8 parallel sets of 3 LEDs in series along with some beefy power resistors to get the voltage on each series chain channel just right. Each channel is then controlled by the corresponding R/G/B channel on the LongPixel.

The structure is a quick foam board job because it's easy to work with and was what we had on hand. Since this was really more of a one-time demo kind of thing, there's no heat sinking on the LEDs or resistors. They do warm up a bit after a few minutes, but as long as they're not being driven full bright white, the heat was manageable for a few quick pictures/videos.

There are other better ways of generating huge amounts of light with these kind of LEDs, but this was a fun side project. And now we have a thing to throw gobs of color all over the place :)



{{< youtube sAi2p-SuOtU >}}
