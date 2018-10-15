---
title: STL Is Not Open Source
date: 2018-10-14T20:15:09-04:00
draft: true
tags: []
categories: []
weight: 20
# slug:
# description:
# author:
---

In the last decade the availability of cheap and easy to use 3D printers has advanced by leaps and bounds. As such, the sharing of designs for objects to print has also exploded. There’s no lack of communities where you can find just about any design you could imagine. Many, if not most, of which are listed as being under an open source license, such as Creative Commons. There’s just one problem with this; in nearly every case the only model files provided are STL. What we hope to bring to light here is that, despite being the near ubiquitous standard for sharing CAD models, these files are absolutely not in the spirit of open source.

# Defining Open

The 3D printer community is nearly synonymous with the Open Source Hardware (OSHW) movement. There have been ups, downs, scandals, and violations, but 3D printer technology would not be where it is now without having embraced OSHW. The original RepRap designs are basically the golden standard, not just for the electronics (which is the most common thing associated with OSHW) but for the entire design specifications of the system as well.

Open source software is a known quantity these days but how to handle OSHW has lagged behind until the last few years. Fortunately we’ve had the Open Source Hardware Association to help guide the path of how to license and share hardware designs. The OSHW Association has already laid out a [best practices document](https://www.oshwa.org/sharing-best-practices/) to help those wanting to share their designs, which it seems that almost no one who shares open CAD designs has ever read. The most pertinent section to pay attention to is defining what constitutes the “original design files” (emphasis ours):

“Ideally, your open-source hardware project would be designed using a free and open-source software application, to maximize the ability of others to view and edit it. For better or worse however, hardware design files are often created in proprietary programs and stored in proprietary formats. It is still essential to share these original design files; they constitute the original “source code” for the hardware. They are the very files that someone will need in order to contribute changes to a given design.”

Even with open tools such as FreeCAD the statement above still stands true with regards to STLs. No matter what tool you use to design your object it is essential to share whatever format is native to the tool you used. Otherwise it is impossible for anyone else to truly contribute changes to your design.

# What Is Wrong with STL?

While not an entirely correct analogy, providing an STL is closer to providing compiled binary software versus providing the full, original source code. We use that analogy because it’s easier to understand and it resonates with the open source community.

The problem lies in what is provided by the STL format; an aggregate representation of the object and a whole lot of triangles. The key here is that this format is and always has been intended as a common standard manufacturing format that all of the many CAD tools could export to. It was created so that whoever was machining your item (STL goes back to CNC machining tools) didn’t have to have the very expensive software you designed your object with. But what it provides in portability and compatibility, it lacks in history.

STL files only provide the result of all the steps taken to arrive at a final object. But, for reasons that are too complicated to go into here, it represents the final object as nothing more than a series of 2D triangles in 3D space. But what if you want to change the size of a hole from 3mm to 4mm? The interior surface of that hole is now many triangles and the actual circumference is a series of lines (which themselves are parts of other triangles). So, now, to modify that simple circular hole you must modify dozens if not hundreds of triangles and somehow maintain the roughly circular shape.

A proper CAD tool, however, provides far more information and far greater base object types. That same circular hole would be simply defined by a circle and an extrusion. If using a parametric design tool (as many are), changing the diameter of that hole is as simple as redefining the diameter of the circle. CAD tools often have facilities to import STLs for modification and provide a certain amount of cleanup, but it will always be much more difficult to affect significant changes to the design.

# What *Should* Be Provided?
Again, the OSHW Association [best practices document](https://www.oshwa.org/sharing-best-practices/) covers this but the simple answer is: the native format of whatever tool you use and the STL files. Sure, not everyone has or knows how to use the tool you use but not every open source software developer is familiar with every programming language. Having the native file format is still the only way to make your design actually open source.

That’s not to say that you should not provide the STL files! You absolutely, 100% should! Again, most people that use open source software just run it and never look at the code but it’s still not open source without that source. STL files are perfect for what they were designed for; manufacturing. For those that just want to print,  CNC mill, or laser cut the design you’ve created, an STL file is a wonderful thing to have. Particularly because, as alluded to above, most software for 3D printing or machining is only able to read STL or similar, simple, formats.

You should also consider exporting other formats if your tool supports it. We’re not saying you have to export to every file format available, just that you should consider if any of those formats would be useful to those who might want to contribute or modify your design.

One specific format you should consider exporting is STEP. These files are highly supported by nearly every CAD tool available but contain far more information and detail. They were designed to be an exchange format between various CAD tools and therefore contain far more detail on a model than the STL file can. While still not as good as having the native format of the original tool to design the model, STEP files can in fact be used to create modifications on the design easily in nearly any CAD tool a user desires.
