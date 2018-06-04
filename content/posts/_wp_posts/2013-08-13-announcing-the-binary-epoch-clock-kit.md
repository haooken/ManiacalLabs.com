---
author: youshallnotpass
date: 2013-08-13 05:30:43+00:00
draft: false
title: Announcing the Binary Epoch Clock Kit
type: post
url: /2013/08/13/announcing-the-binary-epoch-clock-kit/
categories:
- Announcements
- Clocks
- New Product
- Products
---

For nearly as long as the [three of us](/about/) have known each other, we have talked about the things we would make when "we had our own company". The seriousness of that statement grew and waned over time and many of the ideas, while still on our very long list, were probably more crazy than not. But then, early this year, a friend who was just getting into working with the Arduino platform built an 8-bit binary counter and an idea was born; why not make a bigger counter? Why not make it a clock?

We have been fans of unique and often barely readable timepieces for a long time and this immediately seemed like a perfect fit for a first project. So we built the [Binary Epoch Clock Kit](/product/becv1/), which we are announcing for sale, [in our store](/shop/), today!

{{< youtube F_qu8n8lXMc >}}

From the view point of a computer geek, this clock is the simplest possible way of showing time. It displays the time as a 32-bit binary representation of [Unix Epoch](http://en.wikipedia.org/wiki/Unix_epoch) time. One might ask if this is even human readable? Well, the answer to that depends on how quick you are at reading binary, converting it to decimal and then converting that number of seconds since 1/1/1970 to a normal date and time. So, obviously, around Maniacal Labs HQ we use it for our go-to clock.

This kit only requires beginner to moderate soldering skills and can be assembled in about an hour. Once complete, it can be powered from any USB port or USB power adapter using the included Mini-USB cable.

The clock can bet set manually or via any 5V FTDI cable (not included) and our handy 'sync_time' script which is included in the code repository. See the [assembly and usage guide](/guides/binary-epoch-clock/) for instructions and a handy video detailing the manual setting procedure for the clock.

We are also happy to announce that our first product and all of our future products will be fully open source. Not just the firmware, but all of the hardware designs as well. We couldn't be doing this without the amazing work coming from all of the other open source projects out there and we want to give back to that great community. We'll be making everything available for download on our [GitHub repository](https://github.com/ManiacalLabs).

It has been a long road to get where we are today and we have learned a great deal along the way. We've got a long list of products we're working on so stay tuned for what's coming next!

