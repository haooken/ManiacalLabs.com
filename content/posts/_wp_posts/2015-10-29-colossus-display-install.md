---
author: adam
date: 2015-10-29 17:26:28+00:00
draft: false
title: Colossus Display Install
type: post
url: /2015/10/29/colossus-display-install/
---

{{< youtube wmQhT3Ot53E >}}

The [Colossus](/2015/09/22/building-the-colossus-led-display/) LED display wasn't just built to show off at things like SparkCon and MakerFaire. Honestly, that outing was a one-time-only deal. It was designed specifically for one patch of wall in my home office, so the intent was always to permanently install it there after its one weekend on the town.

There was just one slight problem... This guy:

[![EngineeringCat](/wp-content/uploads/2015/07/EngineeringCat-300x201.jpg)
](/wp-content/uploads/2015/07/EngineeringCat.jpg)

Meet Skeletor. The Maniacal Labs Engineering Cat. And he would have liked nothing more than to claw into that cloth diffuser. We had gone with white cloth instead of semi-opaque white plastic because of the cost, but the cloth would just not hold up to years of feline abuse. But we realized that clear acrylic would protect the display, be much cheaper, and fortunately available for cheap at a custom size from a local plastics supplier.

The install was rounded out with some right angle, white molding which was cut into a frame that holds the plastic onto the front of the display and nailed in from the side.

[![Colossus Framed](/wp-content/uploads/2015/10/1028151848-e1446072974325.jpg)
](/wp-content/uploads/2015/10/1028151848-e1446072974325.jpg)

As mentioned in the original [build details](/2015/09/22/building-the-colossus-led-display/) we wanted to use a Raspberry Pi 2 to drive the display but it just couldn't handle it. So for the final install, I picked up a [GIGABYTE GB-BXBT-1900](http://www.newegg.com/Product/Product.aspx?Item=N82E16856164024) for about $100. It's nothing special but contains a Celeron J1900 CPU with 4 cores running at 2.4GHz, quite a bit more oomph than the quad-900MHz Raspberry Pi 2. That's then running Ubuntu 15 and a soon-to-be-released web interface for BiblioPixel. I had an old Nexus 7 tablet that wasn't being used anymore, so it was put to use as a complete overkill touch interface for controlling the display:

[![Colossus Controller](/wp-content/uploads/2015/10/1028151847-e1446073508165.jpg)
](/wp-content/uploads/2015/10/1028151847-e1446073508165.jpg)

Check out the video at the top to see some of the games I programmed for the display :)
