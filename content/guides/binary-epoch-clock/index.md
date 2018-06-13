---
author: maniacal labs
date: 2013-07-19 22:31:22+00:00
draft: false
title: Binary Epoch Clock
type: page
url: /guides/binary-epoch-clock/
---

[printfriendly]

[![](/wp-content/uploads/2013/08/DSC_2882-2.jpg)
](/wp-content/uploads/2013/08/DSC_2882-2.jpg)

[expand title="Tools and Parts List" tag="h1" expanded="true"]



## Tools



In order to complete assembly of the kit, you will need the following tools:




  * Soldering Iron (variable temperature recommended)
  * Leaded or lead-free rosin core solder
  * Multimeter for testing verifying power and that you didn't create any shorts
  * Flush cutters for snipping leads
  * Helping hands or PCB vise (We recommend the PanaVise)




## Parts List



[table]
Image, Name, Description, Qty
[![BEC v1.0 PCB](/wp-content/uploads/2013/07/DSC_1686-300x63.jpg)
](/wp-content/uploads/2013/07/DSC_1686.jpg),PCB,Circuit Board,1

[![3mm LED](/wp-content/uploads/2013/07/DSC_1690-300x83.jpg)
](/wp-content/uploads/2013/07/DSC_1690.jpg),D1 - D32,3mm LED,33

[![MiniUSB Socket](/wp-content/uploads/2013/07/DSC_1692-300x267.jpg)
](/wp-content/uploads/2013/07/DSC_1692.jpg),USB1,USB Mini-B Connector,1

[![0.1uF Capacitor](/wp-content/uploads/2013/07/DSC_1742-300x56.jpg)
](/wp-content/uploads/2013/07/DSC_1742.jpg),C1-C3,0.1uF Ceramic Capacitor,3

[![16MHz Resonator](/wp-content/uploads/2013/07/DSC_1697-300x165.jpg)
](/wp-content/uploads/2013/07/DSC_1697.jpg),Y1,16MHz Resonator,1

[![ATMega328P](/wp-content/uploads/2013/07/DSC_1706-300x120.jpg)
](/wp-content/uploads/2013/07/DSC_1706.jpg),IC1,Pre-progammed ATMega328P-PU with bootloader and firmware,1

[![28 Pin Socket](/wp-content/uploads/2013/07/DSC_1722-300x130.jpg)
](/wp-content/uploads/2013/07/DSC_1722.jpg),IC1',28-pin socket,1

[![DS1307 ](/wp-content/uploads/2013/07/DSC_1711-300x295.jpg)
](/wp-content/uploads/2013/07/DSC_1711.jpg),DS1307,Maxim DS1307+ RTC,1

[![8 Pin Socket](/wp-content/uploads/2013/07/DSC_1720-300x300.jpg)
](/wp-content/uploads/2013/07/DSC_1720.jpg),DS1307',8-pin socket,1

[![RTC Crystal](/wp-content/uploads/2013/07/DSC_1700-300x115.jpg)
](/wp-content/uploads/2013/07/DSC_1700.jpg),Y2,32.768KHz Crystal,1

[![CR1220 Holder](/wp-content/uploads/2013/07/DSC_1694-300x255.jpg)
](/wp-content/uploads/2013/07/DSC_1694.jpg),BAT1,12mm Coin Cell Holder,1

[![CR1220 Battery](/wp-content/uploads/2013/07/DSC_1737-300x156.jpg)
](/wp-content/uploads/2013/07/DSC_1737.jpg),BAT1',CR1220 3V Button Battery,1

[![330 Ohm Resistor](/wp-content/uploads/2013/07/DSC_1734-300x28.jpg)
](/wp-content/uploads/2013/07/DSC_1734.jpg),R1 - R4,330 Ohm Resistor (Orange | Orange | Brown),4

[![10k Ohm Resistor](/wp-content/uploads/2013/07/DSC_1730-300x31.jpg)
](/wp-content/uploads/2013/07/DSC_1730.jpg),R5,10k Ohm Resistor (Brown | Black | Orange),1

[![110 Ohm Resistor](/wp-content/uploads/2013/07/DSC_1728-300x36.jpg)
](/wp-content/uploads/2013/07/DSC_1728.jpg),R6,110 Ohm Resistor (Brown | Brown | Brown),1

[![Tactile Switch](/wp-content/uploads/2013/07/DSC_1747-300x285.jpg)
](/wp-content/uploads/2013/07/DSC_1747.jpg),S1 S2,6x6mm Tactile Switches,2

[![FTDI Header](/wp-content/uploads/2013/07/DSC_1716-300x180.jpg)
](/wp-content/uploads/2013/07/DSC_1716.jpg),FTDI,1x6 header for FTDI connection (optional),1

[![ICSP Header](/wp-content/uploads/2013/07/DSC_1713-300x250.jpg)
](/wp-content/uploads/2013/07/DSC_1713.jpg),ICSP,2x3 header for ICSP connection (optional),1

[![4-40 Standoff](/wp-content/uploads/2013/07/DSC_1727-300x146.jpg)
](/wp-content/uploads/2013/07/DSC_1727.jpg),,0.75" 4-40 Standoff for stand (optional),2

[![4-40 Screw](/wp-content/uploads/2013/07/DSC_1744-300x221.jpg)
](/wp-content/uploads/2013/07/DSC_1744.jpg),,0.25" 4-40 Screw for stand (optional),2

[![Mini-USB Cable](/wp-content/uploads/2013/07/USB_Cable-300x94.jpg)
](/wp-content/uploads/2013/07/USB_Cable.jpg),,USB Mini Cable for power,1

[/table]
[/expand]
[expand title="Assembly" tag="h1" expanded="true"]




  * Start with the Mini-USB port, which mounts to the left side of the board. This provides power only and cannot be used to communicate with or program the board.


    * The pins are very delicate. Be sure none are bent before proceeding.
    * Insert the USB port and, while holding it with your finger, carefully flip the whole board over so that it is resting on top of the USB port.
    * Start by soldering the two structural points (in the large holes) on each side of the port. This will take a decent amount of solder. Check that the port is mounted flush and straight before proceeding.
    * Now solder the other 5 USB pins. The are very small and close together, so go slowly, use as little solder as possible, and be absolutely sure there are no shorts between pins. (This could cause problems with whatever you use for power later). The pins may not extend above the surface of the board, so after you have a bit of melted solder on the pad, leave the iron in contact with the pad for an extra second to make sure the solder wicks onto the pin.
[gallery link="attachment" columns="2" ids="298,299,301,302"]

  * Now that the Mini-USB port is attached, let's test it to make sure nothing gets fried.


    * First, before connecting power, use your multimeter’s continuity tester to make sure that none of the adjacent pins are shorted with one another.
    * Next, using the included USB cable (or one of your own), hook up the board to a 5V wall power adapter or a powered USB hub. While it can be powered off of any USB port, including the one on your computer, avoid using a computer port for now. No need to risk your computer if you have a bad solder.
    * With power connected, use a multimeter to check the voltage across the power filter capacitor pads, C2, directly to the right of the USB port. If it reads ~ +/-5V you can move forward. If not, check you have a good solder connection on the Mini-USB port pins.
[gallery link="attachment" columns="2" ids="303,304,305"]

  * Now, solder on the resistors R1 - R6


    * Note: All resistors have a gold fourth band that we don't mention below. In this case, it just means that these resistors have a +/- 5% tolerance on the labeled value.
    * First, there are four 330 ohm resistors with color code Orange, Orange, Brown. Insert these in R1 - R4 and bend the leads to hold in place.
    * Next, there is one 10k ohm resistor with color code Brown, Black, Orange. Insert into R5 and bend the leads to hold in place.
    * Finally, there is one 110 ohm resistor with color code Brown, Brown, Brown. Insert into R6 and bend the leads to hold in place.
    * Flip the board and solder all the resistors then snip the leads.
[gallery columns="2" ids="306,308,309,311"]

  * C1 - C3 are all 0.1uF ceramic, non-polarized capacitors.


    * Insert each of the three, solder and snip the leads.
[gallery columns="2" ids="312,313,314,316"]

  * Now for the fun part: LEDs!


    * Since the LEDs are directional, if there ever was a time to pay extreme attention to detail, _now is that time!_ The silk screen shows a flat side to the LED, but 3mm LEDs don’t actually have a flat side. We’ll have to go by the lead length. The flat side of an LED is negative and so is the shorter lead. So be absolutely sure that **the shorter lead corresponds with the flat side on the silk screen**.
    * The Maniacal Labs Maniacal Minions have found that it’s a bit easier to place the LEDs four at a time instead of trying to solder all 32 at once. Insert 4 LEDs, bend the short lead towards the bottom of the board and the long lead towards the top to hold the LEDs in place. Be sure to insert the LED all the way and bend the leads as close to the board as possible so that all LEDs are at the same height. Then solder, snip the leads, and move on to the next group of four. Try to always solder the LEDs with the board in the same orientation so that the LEDs all face roughly the same direction.
    * Take your time. Once complete, there is a display mode that pulses all LEDs are oriented correctly. But since you would still have to de-solder to correct any mistakes, we say again: take your time!
    * "I see an extra LED! Where does it go?" you might ask. Your eyes do not deceive you. There should be one extra LED, which we have thoughtfully provided in each kit, just in case.
[gallery columns="2" ids="320,321,322,323,324,329,331,332,333,334"]

  * Now, insert the 16 MHz resonator into Y1, located just under the space for the 28 pin ATMega328P.


    * Bend a couple of the leads in opposite directions to secure the resonator, flip over the board, solder and snip the leads.
[gallery columns="2" ids="337,338,339"]

  * Just above the resonator sits IC1, the ATMega328P, which rides in a 28-pin socket that you will attach next.


    * Orient the notch on the socket with the notch shown on the silkscreen and insert the socket. Blue painter's tape (or similar) works great to hold the socket in place while it’s soldered since the pins are too short to bend.
    * Flip the board over and solder all pins. No need to clip them afterwards.
    * Don’t insert the ATMega328P just yet.
[gallery columns="2" ids="341,342,343"]

  * Y2 is the 32.768 KHz oscillator for the RTC (Real Time Clock) module.


    * **DO NOT** insert the oscillator, solder and then bend it to lie flat on the board. If you soldered it too close, when you bend it, the leads might be damaged. Instead, see the following pictures demonstrating a nifty lead-bending technique using the edge of the PCB. This ensures that the oscillator will lie flat on the PCB with no stress on its leads.
    * Now insert the leads (the body of the oscillator should lie within the solder mask outline).  Carefully bend them in opposite directions to hold the crystal in place and solder. Snip off the excess and head on to the next step.
[gallery columns="2" ids="345,346,347,348,349"]

  * Find the 8 pin socket and insert it into the spot labeled DS1307, just to the right of the crystal. Ensure that the notch in the socket lines up with the one on the solder mask.


    * Tape (or otherwise secure) the socket in place, flip the board, and solder all 8 pins. As with the other socket, no need to snip them when complete.
[gallery columns="2" ids="350"]

  * On the spot for BAT1, there is a square solder pad in the center.


    * Melt a _small_ amount of solder to the pad. While still molten, spread it around with the soldering iron tip.
    * This extra glob of solder is required to ensure that the battery makes good contact. Be careful not to add too much or the battery may not fit into the holder!

  * Place the battery holder on BAT1, matching orientation with the solder mask outline.


    * Solder both retaining pins from the top side of the board.
    * Flip the board over and solder the pins from the back as well to ensure a strong physical connection.
[gallery columns="2" ids="351,352,353,354,355,356,357"]

  * Find the two tactile switches and place them in S1 and S2.


    * They are a tight fit and will require some force to push into the holes. _Make sure you do not have a finger directly behind the the holes! If the buttons snap in quickly, the pins will draw blood!_ (Adam found this out the hard way).
    * The switches will not fit in an incorrect orientation.
    * Flip the board and solder all 4 pins on each switch. No need to snip the pins.
[gallery columns="2" ids="358,359"]

  * **Optional**: The FTDI header is only needed if you plan to upload new code to the board or want to sync the time with your PC via the FTDI COM port. If your cable is capable, it can power the clock directly. DO NOT connect the USB power while powering via FTDI.


    * The header can also be soldered onto the back of the board so that you can connect the FTDI cable without obstructing the clock.

  * **Optional**: The ICSP header is only needed if you want to reflash the bootloader or flash new code without using a bootloader.


    * This header CANNOT be soldered on the back of the board because the pin orientation would no longer match the connector.
[gallery columns="2" ids="361,364,363"]

  * Next, install the ATMega328P (28 pin) and DS1307 (8 pin) chips.


    * For both chips, press the pins on each side against a flat surface to bend them _slightly_ inward so that they will fit into the socket.
    * Carefully insert both chips into their sockets.
    * Make sure to match the notch on the chips with the notch on the sockets.
[gallery columns="2" ids="366,369,367,368"]

  * Finally, install the CR1220 backup battery. Make sure the positive side is facing up. Slide the battery into the holder and push until is fully inserted.


    * This battery will not power the clock but is required for it to function. Without it, the DS1307 RTC will not work, even with main power connected. Without a working RTC module, the clock will need to be reset time if main power is lost.
[gallery columns="2" ids="365"]

  * Optionally, you can install the metal stand-offs in the holes on either side of the PCB in order to act as a stand for the clock. Place the stand-offs on the back side of the PCB and insert the supplied screws from the front. _Do not tighten the screws too much or you could damage the PCB!_
[gallery columns="2" ids="370,371,373"]
  * Side note: As the pins on the board are exposed, it might be possible to short some of the IC pins with your fingers. With electronics in general, touching exposed pins should be avoided when at all possible. Try to pick up the board only by the edges while pressing the buttons for the various functions. If the board will be frequently handled for any reason, it is recommended that a strip of electrical or masking tape be adhered to the back of the board in order to guard against any shorts.




[/expand]
[expand title="First Usage" tag="h1" expanded="true"]




  * Now it’s time to power up your clock for the first time. All that is required is a mini-USB port and just about any standard 5V USB power source. In order of most suggested to least, this can come in the form of:


    * Any standard wall-plug USB charger. (Recommended)
    * A powered USB hub.
    * Any computer’s USB port. This last option, while generally possible, may or may not work depending on the machine. Computers don’t have to provide power to a device if it doesn’t have a data connection (which the clock doesn’t) but most will if the power draw is less than 100mA, which is true for the clock. So this option may not work, but on most computers it should. We highly suggest trying one of the previous two options first just in case there is a problem with your soldering to avoid any damage to your computer’s USB port.

  * Once you’ve chosen you power source, plug it in and within a few seconds you should see the display light up and start counting. If you don’t see any lights, recheck all of your solder points and that the IC chips are properly seated in the sockets.


    * The first time it starts, the RTC will be un-initialized and the firmware will automatically set the time to the time and date that the chip was flashed back at Maniacal Labs HQ. Yes, you’re probably thinking that it is not the right time, and you'd be right... but I dare you to tell the difference.





## Setting the Time



Should you actually want the time to be correct, there are two options for setting the time.




  * _First is the manual set mode. Either follow the directions below or just watch the video._


    * [youtube http://www.youtube.com/watch?v=zpKhnDOOV8o]
    * You can also use the [Binary Epoch Clock Simulator](/guides/binary-epoch-clock/binary-epoch-clock-simulator/) to help with the process.
    * Press and hold the A button for at least a second.
    * The left-most LEDs show the current date/time position you are in and are (from left to right), Year 1, Year 2, Month 1, Month 2, Day 1, Day 2, Hour 1, Hour 2, Minute 1, Minute 2. Whereas Year 1 is the 1 in 2013, Year 2 is the 3, Hour 1 is the 2 in Hour 21 (9pm), Hour 2 is the 1, etc.
    * The right-most LEDs show the value for the current date/time position.
    * Step through each of the date/time positions mentioned above with Button A and increment that position's value with Button B.
    * Note that the Hour 1 and Hour 2 state MUST be set in 24-hour time!
    * When complete, hold down Button A again to make the change permanent.
    * If at any time you want to cancel setting the time, hold down Button B to exit manual set mode.

  * The second, and easier option, is to use the sync_time script, which can be downloaded with the clock source code from [GitHub](https://github.com/ManiacalLabs/BinaryEpochClock);. This requires the use of the FTDI connection on the board with a 5V FTDI USB cable. Connect the cable to the headers ensuring to match up the BLK/GRN marking with either the wire colors or markings on your FTDI connector. The clock should power on as it draws power from the FTDI cable. You should NOT connect the mini-USB cable during this step.


    * Hold down A and B until the Larson scanner (Knight Rider or Cylon if you prefer)  effect starts. This should happen after about one second.
    * _While the scanner effect is still running, run the sync_time script on the connected computer.The script should auto-detect the COM port and try to send the time, showing a success or error message, whatever the case may be._


      * On Mac and Linux, run “python sync_time.py” (On Mac, get the drivers from: [http://www.ftdichip.com/Drivers/VCP.htm](http://www.ftdichip.com/Drivers/VCP.htm))
      * On Windows with Python 2.7 is installed, run the above command. Otherwise run sync_time.exe from the command line so that the output can be seen.

    * After a success, the larson effect should terminate and the clock should go back to normal mode displaying the new time.
    * Pause the clock and check!
    * There are multiple reasons that the script could fail:


      * There is no available COM port. Check the connections and that the FTDI drivers are installed correctly.
      * There is more than one COM port. The “auto-detect” is done by just grabbing the most recent port in the system’s list (since most people don’t have them anymore). If there is another port, it may be trying to connect to another device! Use the --list option on the script to show the available ports and check this. If there are multiple, confirm which is for the FTDI connection and use “-p <COMx>” (use the actual name not number) and try again.
      * The baud rate is not correct. This shouldn’t be a problem with the exception of modified firmware or sync script. In both they are hard-coded to 115200. But you can use “-b <baud>” to specify if the current firmware uses something different. Note, in Windows, the baud rate can be specified in the driver properties. This is irrelevant as long as it’s specified in code when opening the port, so the Windows setting shouldn’t matter.
      * Lastly and the worst option is that the reset disable is not working. Normally, when you put the clock in serial set mode, the firmware holds the ATMega reset pin high via pin 11 and R6 to prevent the serial connection from resetting the chip. The automatic reset is a "feature" of Arduino boards allowing you to reprogram the chip without manually resetting. But we don't want to do that in this case. Ensure that R6 on the board is properly connected.




[/expand]

