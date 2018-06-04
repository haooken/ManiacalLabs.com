---
author: adam
date: 2013-11-12 14:50:29+00:00
draft: false
title: 'Building the PrismaChron: Diffusers'
type: post
url: /2013/11/12/building-the-prismachron-diffusers/
categories:
- Clocks
- Making Of
---

The [PrismaChron](/2013/11/11/announcing-the-prismachron/) (not its first name, more on that in another post) has been in the works for quite a long time. Longer even than the [Binary Epoch Clock](/products/becv1/). We've spent that time truly fine-tuning every little aspect of it in an effort to make it a fantastic little kit that we can be proud of. Being a clock that displays its time as color, getting it just right was very important to us and that meant getting the LED diffusion perfect.

Now, some might ask why we didn't just use diffused LEDs. This was an option, but RGB LEDs are strangely difficult to source at a reasonable cost, especially of the diffused variety. Also, we wanted to give our customers to option of displaying the clock with the light from the LEDs reflecting off another surface, like a wall. This would require non-diffused LEDs, for maximum brightness.

But with clear LEDs, the colors don't really mix together and they are far, far too bright to look at. I was seeing spots for days before finally making diffusers for the LEDs. So, to solve this problem of having a removable diffuser, we turned to some fun tech that we've been experimenting with... our [3D printer](/2013/04/26/no-good-can-come-of-this/).

Our [Replicator 2](http://store.makerbot.com/replicator2.html) made prototyping new diffusers from the comfort of Maniacal Labs HQ amazingly easy. But that doesn't mean it did not take many, many tries to get it just right. The image below shows just _some_ of the diffusers I tried before settling on the current version (shown installed on the PrismaChron on the left).

[![PrismaChron Diffusers](/wp-content/uploads/2013/11/diffusers_resized.jpg)
](/wp-content/uploads/2013/11/diffusers_resized.jpg)

We started with clear, or "Natural", [PLA](http://en.wikipedia.org/wiki/Polylactic_acid) filament and tried a variety of shapes, thicknesses and infills1. Our initial thought was to go with a nice domed shape so it would look like a really large LED, but because 3D printers lay down the material in thin layers (around 0.1-0.3mm) the areas where these layers met caused more of a refracting effecting than a diffusing one. It looked better for sure, but you could still see the individual colors. We then moved to a completely flat surface in varying thickness, only to find that even up to as much as 3mm thick, the clear2 PLA was still far too translucent to properly diffuse the colors together.

This led us to realize we would need to go with a plastic that was _much_ more opaque and simply rely on the fact that the LEDs are extremely bright to shine through. So we ordered some pure white PLA and printed off some of the designs we had tried with the clear. The domes were absolutely too thick to let a reasonable amount of light through, so we went back to the flat design.

Finally, we found that about 1mm thick, with 100% infill and a slight bevel around the top edge worked great. Also, by printing them upside-down, the top surface (which now contacts the build plate) is completely smooth instead of slightly textured, like the last layer to print always is. This design also worked out great because, despite the 100% infill, it uses a minimum of material and can be printed at 0.3mm layer thickness (the lowest on our printer) for extremely fast prints. It was actually possible to make the clear dome versions look good but only when printed at 0.1mm layer thickness and that made it take over 15 minutes just to print one! Our final version can be printed in under four minutes and we can print a large batch of 30 in under an hour.

We're very excited to be using this awesome technology for a (hopefully) shipping product. Even for such a small, simple component, it would have cost many thousands of dollars to produce with traditional manufacturing methods.

So, if you would like your very own PrismaChron, please visit our [Tindie Fundraiser](https://www.tindie.com/products/ManiacalLabs/prismachron-clock/) page and pre-order now to help us reach our funding goal and make this kit a reality. We even have a fully assembled option!

1 Infill is how much the printer actually fills in the "solid" parts of of object. To save material this is often set to something low, like 10%, making it still structurally sound but without wasting material. Normally this is inconsequential because most plastics used are completely opaque.

2 It's only _mostly_ clear and in reality has about an 20% level of opacity.

