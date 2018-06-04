---
author: youshallnotpass
date: 2013-10-22 03:32:29+00:00
draft: false
title: 'Introducing: EpochPOV'
type: post
url: /2013/10/21/introducing-epochpov/
categories:
- Announcements
- Clocks
- Cool Stuff
- Products
---

We would like to introduce a new product. Okay, not really a new product, but a _completely_ different use for the [Binary Epoch Clock Kit](/product/becv1/) that we already sell.

We've been hinting at it for a while now but we are proud to finally announce **EpochPOV**, a custom firmware that turns your Binary Epoch Clock into a fully functional [Persistence of Vision](http://en.wikipedia.org/wiki/Persistence_of_vision) - or POV for short - display with a 32 pixel resolution!

Without further ado, some pictures to show off what this great firmware can do - with a some shout-outs to our friends at [Adafruit](http://adafruit.com) and [Hack A Day](http://hackaday.com):

{{< gallery dir="/wp-content/galleries/2013-10-22-introducing-epochpov/0/" />}}

All pictures were a 1.6 second exposure at ISO 800 by simply waving the Epoch Clock in front of the camera during the exposure.

EpochPOV supports images 32 pixel high and up to 128 pixels wide (possibly longer in the future) and has a variable refresh rate that can be configured as described below.

To grab the latest version of EpochPOV just head on over to the [GitHub repository](https://github.com/ManiacalLabs/EpochPOV), compile the firmware and upload it to your Epoch Clock board with an FTDI cable or AVR ISP.

You can change the displayed image by generating a new Image.h file with the included EpochPOVGen script located in the "Scripts" folder of the code repository. The script is written in python and supports all operating systems (though requires the installation of Pillow as described in the script header) but there is an exe file for use on Windows systems as well since compiling Pillow can be a pain on non-*nix systems.

Usage is as follows:


    
    
    usage: EpochPOVGen.py [-h] [--delay DELAY] [--flip_v] [--flip_h] [--invert] input_img output_header
    
    positional arguments:
      input_img      BMP image to process. Must be 32 pixels high.
      output_header  File to output C image data to.
    
    optional arguments:
      -h, --help     show this help message and exit
      --delay DELAY  Time (ms) between each column refresh.
      --flip_v       Flip image vertically.
      --flip_h       Flip image horizontally.
      --invert       Invert image black/white values (negative)
    



Typical usage would look like this:


    
    
    python EpochPOVGen.py mylogo.bmp Image.h
    EpochPOVGen.exe mylogo.bmp Image.h
    



The optional arguments can be used to flip or invert the image colors as well as change the refresh delay, which defaults to 4ms between column updates. This default seems to work well for greater than one second exposures and waving the EpochPOV by hand. Slower will make the image wider and faster will make it narrower. By default, the bottom of the image will be the pixel closest to the USB power port but this orientation can be flipped with --flip_v and the default left to right movement can be switched by setting --flip_h.

The script requires that the image be a bitmap (.bmp), 32 pixels high, no more than 128 pixels wide and will convert the image to 1-bit color (black and white) if it's not already, so there is not currently the ability to display gray-scale images on the EpochPOV.

Once the header file is created, copy it to Image.h in the EpochPOV firmware directory, re-compile and upload the firmware to your Binary Epoch Clock.

Don't have a Binary Epoch Clock? [Buy one](/product/becv1/) and download the [EpochPOV firmware](https://github.com/ManiacalLabs/EpochPOV) now!


{{< load-photoswipe >}}