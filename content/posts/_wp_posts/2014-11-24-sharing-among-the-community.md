---
author: maniacal labs
date: 2014-11-24 13:00:43+00:00
draft: false
title: Sharing Among the Community
type: post
url: /2014/11/24/sharing-among-the-community/
categories:
- Cool Stuff
- Kickstarter
---

{{< youtube x4qb5ww9QDM >}}

We already knew that the open source and open hardware community was full of awesome people, but launching the [AllPixel Kickstarter](https://www.kickstarter.com/projects/1101128588/allpixel-usb-interface-for-all-your-led-needs/) has just confirmed that even more. There has been an outpouring of support and advice that will certainly be helpful as we move through the final manufacturing steps.

What has been really cool is that some other open hardware makers like us have been super excited to see how their hardware works with the AllPixel. Two in particular are [RGB-123](http://rgb-123.com/shop) and [WyoLum](http://shop.wyolum.com/) who were kind enough to send us some of their awesome LED displays, for which we've traded some pre-production AllPixel boards.

{{< gallery dir="/wp-content/galleries/2014-11-24-sharing-among-the-community/0/" />}}

Ryan from [RGB-123](http://rgb-123.com) sent us one of his awesome 16x16 WS2812 displays - or in this case, two of his 16x8 displays that haven't been depaneled. It's a standard single data input setup with a serpentine pixel layout and a really nice size and pixel density. What's really cool about these displays is how they are designed for maximum power. Just look at those power connectors! 12 gauge wrapped in silicone insulation.

{{< gallery dir="/wp-content/galleries/2014-11-24-sharing-among-the-community/1/" />}}

This panel will draw over 15A at full power, made possible by using huge 5V and Ground planes instead of single power traces. And it is _bright_! At 256 total pixels it doesn't even break half of what the AllPixel is capable of.

The fine people at WyoLum sent us a prototype version of their [TiM](http://wyolum.com/the-intelligent-matrix-tim/) and their yet to be announced TinyTiM... yup, that's right. We're breaking the news here... TinyTiM is coming soon!

TiM is a 16x8 matrix of WS2812 LEDs with a little twist. Instead of the usual serpentine layout of the LEDs the TiM can be used in parallel mode where you control each of the 8 rows individually. This can allow slightly faster update speed with the WS2812 if you were using a bunch of these displays together. This is not supported on the AllPixel, but that's OK, because you can _also_ configure the board to run in that usual serial mode where there's a single data input and output.

[![WyoLum TiM](/wp-content/uploads/2014/11/IMG_0571-16x9.jpg)
](/wp-content/uploads/2014/11/IMG_0571-16x9.jpg)

The new TinyTiM is the same great setup as the TiM but in an 8x8 configuration and with updated connection options including chainable IDC connectors.

{{< gallery dir="/wp-content/galleries/2014-11-24-sharing-among-the-community/2/" />}}

We've used a ton of different LED displays and strips, but it's always great to see the AllPixel working with another. If you want great and super easy to use matrices for use with your AllPixel, you can't go wrong with any of these. It's a lot easier than [building your own](/2014/08/19/24x24-led-matrix-build/)! Thanks so much to both RGB-123 and WyoLum!

{{< load-photoswipe >}}