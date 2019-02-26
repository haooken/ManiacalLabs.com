---
title: Custom CNC Wasteboard
date: 2019-03-05T00:00:00
draft: false
tags: []
categories: []
weight: 20
# slug:
# description:
author: Adam Haile
---

{{< figure src="!header.jpg" >}}

[Previously]({{< ref "/posts/2019/2/CNC_Dust_Boot_for_Dewalt_Router" >}}) on *The New Maniacal Labs Workshop*, we built a dust boot for the [Probotix Comet CNC](https://www.probotix.com/CNC-ROUTERS/CNC-ROUTER-GX2525-COMET). Today, it's time to upgrade the wasteboard that came with the machine. First, a little background information:

This particular CNC was barely used when acquired and had sat in a basement for a number of years before being brought back to life. This particular CNC ships with a wasteboard that covers the entire frame of the machine with the frame itself being mostly just four 60x30mm aluminum extrusions in a rectangle. This caused a few of issues as far as I was concerned.

First, it was visually noticeable that the wasteboard was not flat in relation to the router gantry. After fabricating a simple holder to attach a dial indicator to the dust boot mount, I found that the deviation from the origin point covered a 0.045" (1.2mm) spread. This may not sound like much, but for a CNC router it is pretty extreme. The most egregious point on the wasteboard was in the middle and that was very clearly because there was no central support, causing the board to sag. Normally this could be mostly fixed by resurfacing the board, however...

The second issue was that, because the wasteboard extended well beyond the reach of the router, it was impossible to resurface it in place without causing a sunken area in the board, which would make it hard to mount any stock that was larger than that resurfaced area.

Finally, I'd eventually have to replace the board completely and Probotix wanted nearly $130 for a new one! Yes, I could fabricate one out of a larger sheet of 0.75" MDF and drill all the mounting holes myself (since the board is larger than the work area of the CNC), but then the first two issues still remain. There had to be a better way.

After some research on the Probotix Wiki I found some listings for the exact [aluminum extrusions used](https://www.probotix.com/wiki/index.php/Aluminum_Extrusions) on the Comet and immediately noticed that, while no supplier was given, the part numbers listed were clearly from Misumi (why I know this is another story). So I hatched a new plan... Build out a central support frame from the same extrusions and mount to that an $8 24"x24" MDF board bought from the local orange hardware store. The actual work area is just over 25"x25" but this was actually perfect because it meant that I would be able to completely resurface the entire board and pieces larger than a 24" dimension would be fine hanging over a little bit.

So, after determining the exact length of extrusion needed, again from the [Wiki](https://www.probotix.com/wiki/index.php/Physical_Dimensions), as well as the required mounting hardware, it was off to Fusion 360. And because Misumi knows what's what, I could of course download CAD models of every single extrusion, bracket, and bolt I needed. Only thing I had to model was some MDF :)

{{< figure src="!header.jpg" >}}

The astute among you will of course notice that the modeled MDF has a grid of holes in it. This is, of course, so that I can use all manner of clamping solutions to hold down material. I was inspired by the [work of Winston Moy](http://www.winstonmoy.com/2016/11/shapeoko-3-xl-threaded-insert-installation/) and decided to use these [1/4-20 threaded inserts](https://amzn.to/2XrglAX). They would be secured in from the underside for maximum strength as well as leaving the option of resurfacing up to 10mm of the board away before having to replace it entirely again. But more on those again in a minute.

So, with design in hand and all the parts having arrived, Dan and I got to work with the modifications. First part was, easy... just removing the old wasteboard which came out with a couple dozen bolts. Next we assembled the brackets onto each of the three extrusions, using bolts and "post-install" t-nuts:

{{< figure src="1.jpg" >}}

Next, those were bolted into the CNC frame using the same bolts and nuts. This was probably the trickiest part because they needed to be at a specific spacing. This was not only so that each lined up with the mounting holes on the wasteboard, but so that the bottom left corner of the wasteboard was at the actual CNC **0,0** origin. This meant the first rail's right face needed to be 3.9" from the inner face of the left frame rail. And the other two rails needed to be spaced 10" and 20" further right, respectively.

Also, they needed to be mounted flush with the frame itself, as to not add any extra skew in the wasteboard once mounted. While the mounting hardware got everything close, this took some patience to get everything right.

{{< figure src="2.jpg" >}}

The wasteboard itself was, of course, cut out on the CNC itself, prior to removing the original board. Check out the links at the end for the Fusion 360 file which includes the CAM toolpaths used.

The previously mentioned grid of threaded insert holes were drilled as well as 18 holes for bolts to attach to the three new support rails. These were counter-bored so that the [chosen bolts](https://www.mcmaster.com/92235a238) would sit well below the surface, allowing for several resurfacing passes to occur over the board's life. This just left installing the threaded inserts. I purchased a 6mm hex driver ahead of time that would fit in my drill, which made installing the inserts a snap.

{{< figure src="3.jpg" >}}

After that all that was left was mounting the board to the new frame. At the suggestion of one of the wonderful Misumi support people, I ordered the [HNTP6-6](https://us.misumi-ec.com/vona2/detail/110302252720/?HissuCode=HNTP6-6) "Post-Assembly Insertion Spring Nuts" which worked great, since the spring loaded ball bearing keeps them from moving around. To ease installation even further, I first made marks on each of the rails with the spacing for each mount hole, allowing me to line up the nut accurately. From there it was just a matter of dropping the board on and bolting it down.

{{< figure src="4.jpg" >}}

The final step of this process was to make sure that the board was completely flat relative to the CNC machine itself. And the easiest way to do this is to just use the CNC to run a facing operation on the wasteboard making it completely flat. Some CNC control software have this built in, but LinuxCNC does not. Fortunately, I already had everything for this modeled in Fusion 360 so it was a simple matter of using that to generate the CAM toolpath for a facing operation. This was a *little* tricky since the 25"x25" was working area was barely big enough to run the toolpath with a [1" surfacing bit](https://amzn.to/2EwhIqe), but I was able to make it work.

{{< figure src="5.jpg" >}}

In the image above you can see the dial indicator that I mounted to the dust shoe. After running another pass with that I found that I only had about 0.004" (0.1mm) of deviation across the board! While that would be unacceptable for a precision metal machinist, it's right about at the accuracy tolerance for this machine, so I'll call it perfect :)

The only issue I ran into was that there was a very slight striation pattern after the facing operation. Further research yielded that the router spindle was likely not perfectly square to the gantry. But I did some measurements and math... the dial indicator showed up to a 0.0015" height deviation from one striation to another and given that the bit is 1" wide, that gives an angle deviation of 0.086&deg;. I'll just go ahead and call that square. Also, that means that with a 1/4" width it would only show a height deviation of 0.000375" (0.0095mm). Which is insignificant. Though I'm not about to resurface the whole board with a 1/4" bit! It's good enough.

Finally, because I enjoy time-lapses and soothing music, checkout the video of drilling all the holes and resurfacing the board below:

{{< youtube dI3JoD3KE0U >}}

&nbsp;

In case you want to make your own, we've of course got you covered.

- [CAD Files](https://github.com/ManiacalLabs/ProbotixComet/tree/master/Wasteboard) (includes CAM setup)
- [HFS6-3060-778 Extrusion](https://us.misumi-ec.com/vona2/detail/110302686970/?HissuCode=HFS6-3060-778)
- [HBLFTD6-SEP Bracket with bolts/nuts](https://us.misumi-ec.com/vona2/detail/110300442610/?HissuCode=HBLFTD6-SEP)
- [HNTP6-6 extrusion nuts](https://us.misumi-ec.com/vona2/detail/110302252720/?HissuCode=HNTP6-6)
- [Board M6 mount bolt](https://www.mcmaster.com/92235a238)