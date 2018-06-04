---
author: adam
date: 2016-08-09 13:00:17+00:00
draft: false
title: 'New Library: ESP Serial WiFi Manager'
type: post
url: /2016/08/09/new-library-esp-serial-wifi-manager/
categories:
- Announcements
- Arduino
- Code
- ESP8266
- New Product
- Projects
---

The [ESP8266 Arduino](https://github.com/esp8266/Arduino) package provides a great and familiar to use ecosystem for developing code on the chip. However, most examples for WiFi network connection and management involve building and uploading new code every time you want to change the network settings. That's just more than should be required if you want to simply connect an existing and complete project to a new network.

A forthcoming project in which we plan to use a large number of the [Adafruit ESP8266 Feather](https://www.adafruit.com/products/2821) boards for was going to be far to cumbersome to manage if we had to upload new code not only to change the WiFi network but to set static IPs. That would just not be acceptable and we had to find a better option.

<!-- more -->

There are some [examples](https://github.com/tzapu/WiFiManager) of ESP8266 WiFi managers already but all seem to go with the more complicated process of entering AP mode, connecting to the ESP8266 with another computer, loading a webpage and configuring via that page. Again, too cumbersome so we though maybe it would be better to just use an interactive serial console. That's were our new library, [ESPSerialWiFiManager](https://github.com/ManiacalLabs/ESPSerialWiFiManager), comes in.

ESPSerialWiFiManager provides an easy to use interactive serial console for all your WiFi network management needs. It supports open, WEP, WPA, and even WPS connections as well as can commit the configuration to EEPROM to be automatically connected on reboot. And best of all, it's super simple to integrate into your own code. Check out the console example below to get an idea of what you can do:

[code]
ESP Serial WiFi Manager
=======================

================
MAIN MENU
================
1: Scan
2: Enter SSID
3: WPS Connect
4: Disconnect
5: Commit Config
6: Display Network Details
7: Quit

Timeout in 10s...
> 1

Starting network scan...

3 networks found:
==================
1: NSA_VAN_7 (-86)*
2: FREE_WIFI (-77)*
3: Linksys8021 (-80)*
==================

s: Scan Again
q: Quit Network Scan
> 3

Connect to Linksys8021:
Password> **********

Advanced Config? y/n> n

Connecting to Linksys8021
...........
Connection Sucessful
Choose Commit Config for changes to persist reboot.

=============================
Current Network Details:
=============================
SSID: Linksys8021
IP Address: 10.0.1.111
MAC address: 72:73:0:7F:CF:5C
Subnet Mask: 255.255.255.0
Gateway: 10.0.1.1
DNS 1: 10.0.1.1
DNS 2: 0.0.0.0
=============================
[/code]

You can find more details including installation, usage, and examples on the [ESPSerialWiFiManager](https://github.com/ManiacalLabs/ESPSerialWiFiManager) GitHub repo.
