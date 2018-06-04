---
author: adam
date: 2013-08-26 11:32:51+00:00
draft: false
title: Automatic Cat Lasers!
type: post
url: /2013/08/26/automatic-cat-lasers/
---

[I just have one question for you! LAAAASERS?!?!](http://youtu.be/-YRyhqsUgag?t=21s)

If you have cats, like I do, lasers are probably on their brain most of the time. My cat, Skeletor, has a severe addiction to lasers and is demanding of them every day. Recently, when my wife and I were going to be on vacation for a week, she joked that she wished there was something that would automatically move a laser pointer around a room and automatically turn on every few hours.

The first part was easy and I quickly found the [FroliCat BOLT](http://www.amazon.com/FroliCat-BOLT-Interactive-Laser-Pet/dp/B0021L8W6K). But the second part was a bit harder; everything I could find turned _off_ automatically but not _on_. _**Challenge Accepted!**_

Read on for instructions on how to hack a FroliCat BOLT to automatically turn itself on.

<!-- more -->


## Disassembly


The BOLT is pretty easy to open up; just take something thin and plastic and carefully pry along the seam to pop the tabs. Be sure not to pull apart the two halves before you are sure the tabs are popped, otherwise you will just break them. If a few become broken, not to worry, it will stay together quite well with only a few of them.

Inside you will find a battery pack, controller circuit, motor, laser assembly, and mirror.

[gallery columns="4" ids="527,526"]

Unseat the controller circuit from its slot in the plastic casing. Some poking around with a multi-meter determined that there are 3 points of importance on the board. See the image below as reference.

[gallery columns="4" ids="522,528"]

- Top, left red wire: VCC (The AA batteries are arranged as two sets of serial batteries connected in parallel, providing ~3.2V and double the usual capacity)
- Top, right orange wire: Ground to batteries
- Middle, right yellow: switch (on back of casing) contact for activating laser


## The Plan: Building the circuit


While automatically activating the laser via these contacts could easily be done with a 555 timer and the right resistor/capacitor values, I wanted to have a little more functionality available. So, instead, I went with an ATTiny45.

The basic plan is as follows:

- Turn on the laser every two hours (the main controller turns it off after 15 minutes).
- Play a short tune as an audio queue that the laser is about to start.
- Run with as little power as possible to conserve battery life.

Solder extension leads, at least 3" long, to all three of the previously mentioned points (as shown in the second image above) being careful not to disconnect the wires that are already there as they are only surface mounted. With the batteries inserted, you can test the connections by touching the switch contact to VCC which will activate the laser.

The circuit is quite simple and quick to put together on some perf-board. Just follow the schematic below. I used a 28x6 hole board that fit nicely inside of the plastic enclosure. When complete, the circuit should look something like the circuit below. All that' needed are the following components:

- ATTiny45 (the 85 would work as well, but the included code is too big for the 25).
- Small 3V piezo buzzer (salvaged from computer motherboard)
- 10k ohm resistor
- 0.1uF ceramic capacitor
- Optional: ICSP (2x3) header for programming

[gallery columns="4" ids="538,524"]

Once built, use the leads soldered to the controller board earlier to connect to VCC and ground on the ATTiny and then connect the yellow switch lead to PB4, which will pulse at the specified interval to activate the laser.


## The Firmware


The ATTinyX5 series worked out quite well for this project. It is able to run between 2.7V and 5.V making it quite usable on the ~3.2V from the AA batteries. To make the code a little easier to write, I used the [arduino-tiny](https://code.google.com/p/arduino-tiny/) core so that I could take advantage of the (mostly) full Arduino framework. This made driving the piezo buzzer quite easy as I could just use the built-in tone() method - at the cost of adding about 1100 bytes to the total firmware size (hence why the ATTiny25 was ruled out).

The board needs to be set to "ATTiny45 @ 1 MHz" in the Arduino IDE so that it can save a little power by running slower than the usual 8MHz. In the code below, you can see I've used some other power saving options at the top of the setup() method. Using all of these along with the Watchdog Timer in order to sleep most of the time actually allows the ATTiny to draw as little as 10uA. If it just ran at that power level without ever activating the laser, it could continue to do so for nearly 20 years!

Originally, I planned to user Timer0 or Timer1 to keep track of the elapsed time but these were unsuitable for a couple reasons:

- They require extra power when enabled and would only allow the chip to sleep for very short periods of time (much less than one second).
- Their timeouts are a factor of the clock speed (1MHz) and the overflow comparator making it difficult to measure intervals of exactly one second.

So, instead, I cheated and used the [Watchdog Timer](http://en.wikipedia.org/wiki/Watchdog_timer). Normally, it's used to check if the program code is hung and reset the chip to get things back on track. It has it's own 128Khz clock so it uses less power than the normal timers and has built-in clock dividers allowing it to fire at 8, 4, 2, 1, 0.5, 0.25, and 0.125 seconds, making it great for counting things in one second intervals. So the code below sets up the Watchdog Timer to fire every one second, increment a global value and _not_ reset the chip. This value is then compared to the laser activation interval (120 minutes), and if equal, another global (bool _doPulse) is set to tell the code in loop() to play "Twinkle Little Star" on the piezo and then activate the laser before putting the chip back to sleep. Except for the times that it has to actually play the tune and activate the laser, the chip is asleep for the majority of every second.

Expand to read through the firmware code. [Download the full code](https://github.com/ManiacalLabs/FroliCatBoltHack) to get the included notes.h header which contains values for playing the music.

[cpp collapse="true"]
//arduino-tiny "ATTiny45 @ 1 MHz"

#include <avr/wdt.h>        // Supplied Watch Dog Timer Macros
#include <avr/sleep.h>      // Supplied AVR Sleep Macros
#include <avr/power.h>
#include <EEPROM.h>
#include "notes.h"

volatile uint32_t _intervalCount = 0;
uint32_t _interval = 0;
volatile bool _doPulse = false;

void playSong()
{
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < _songDur; thisNote++) {

    // to calculate the note duration, take one second
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000/_noteDurations[thisNote];
    tone(_speakerPin, _melody[thisNote],noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(_speakerPin);
  }
}

void setup()
{
  //power savings
  ADCSRA &= ~(1<<ADEN); //Disable ADC
  power_usi_disable();
  ACSR = (1<<ACD); //Disable the analog comparator
  DIDR0 = 0x3F; //Disable digital input buffers on all ADC0-ADC5 pins.

  cli();
  // Set up Watch Dog Timer for Inactivity
  WDTCR |= (_BV(WDCE) | _BV(WDE));   // Enable the WD Change Bit
  WDTCR =   _BV(WDIE) |              // Enable WDT Interrupt
  _BV(WDP2) | _BV(WDP1);   // Set Timeout to ~1 seconds

  if(MCUSR & _BV(WDRF)){            // If a reset was caused by the Watchdog Timer...
    MCUSR &= ~_BV(WDRF);                 // Clear the WDT reset flag
    WDTCR |= (_BV(WDCE) | _BV(WDE));   // Enable the WD Change Bit
    WDTCR = 0x00;                      // Disable the WDT
  }

  // Enable Sleep Mode for Power Down
  set_sleep_mode(SLEEP_MODE_PWR_DOWN);    // Set Sleep Mode: Power Down
  sleep_enable();                     // Enable Sleep Mode

    DDRB |= _BV(PINB4); // Set PB4 as output;
  PORTB &= ~_BV(PINB4); //Set it to low, just to be safe

  //avrdude -C C:\avrdude.conf -P usb -p t45 -c avrispmkII -U eeprom:w:0x16:m
  uint8_t val = EEPROM.read(0);
  if(val == 0){
    val =  22;
    EEPROM.write(0, val);
  }

  _interval = map(val, 0, 255, 0, 86400);

  //_interval = (uint32_t)val;//for testing, when you want the interval to be mere seconds

  sei();  // Enable Interrupts

  _doPulse = true;
}

void loop()
{
  if(_doPulse)
  {
    _doPulse = false;
    playSong();
    PORTB |= _BV(PINB4);
    delay(100);
    PORTB &= ~_BV(PINB4);
  }

  if (MCUCR & _BV(SE)){    // If Sleep is Enabled...
    sleep_cpu();           // Go to Sleep
  }

}

ISR(WDT_vect)
{
  sleep_disable();          // Disable Sleep on Wakeup

  _intervalCount++;
  if(_intervalCount >= _interval)
  {
    _intervalCount = 0;
    _doPulse = true;
  }

  sleep_enable();           // Enable Sleep Mode
}
[/cpp]


## Setup and Testing


Once you have arduino-tiny installed and build the firmware you will need an AVR ISP, USBTinyISP or similar to flash the ATTiny. If the circuit is already wired to the BOLT, simply install the batteries so that the chip has power, connect the ISP and use "Upload via Programmer" in the Arduino IDE.

In the picture above, I wired in an ICSP header and had originally intended to somehow make it accessible for outside the plastic casing so that I could re-flash without taking it apart again. But the curved surface made that complicated so I scrapped the plan.

With everything wired and the firmware flashed, let's test it before re-assembling everything. The code is setup to read a byte from the EEPROM and map the 0 - 255 value to 0 - 86400 (the number of seconds in a day). This make each increment from 0 - 255 equal to ~5.6 minutes. So in order to run every 2 hours, I've set defaulted the EEPROM value to 22, which gives you 22 x 5.6 = ~123 minutes. Close enough.

Because of this, you can simply rewrite the EEPROM using an ISP to change the time, instead of changing the whole firmware. The following would set the interval to roughly 3 hours:

`avrdude -C C:\avrdude.conf -P usb -p t45 -c avrispmkII -U eeprom:w:0x21:m`

Note that the EEPROM byte is being set to 33 which is 0x21 in hex.

For the purpose of testing that your circuit works though, uncomment line 69 in the code:

`_interval = (uint32_t)val;`

This will not map the value (in which case the minimum interval is 5 minutes) and will activate the laser ever 22 seconds. Since the laser normally stays on for 15 minutes, every _other_ pulse will turn the laser back _off_ again, just as it would if you pressed the button on the back of the casing. If this works and the laser activates every 22 seconds, comment that line again and re-upload the firmware.

Now, re-seat the controller board in it's mounts and then place the ATTiny circuit in the empty space of the casing on the opposite side from the main controller board as shown in the picture below.  Now the casing can be closed back up, again carefully to avoid breaking the tabs.

[gallery columns="4" ids="525,523"]


## Wrap Up


As with the external ICSP header, I also wanted to include a switch that would turn the ATTiny circuit on or off to allow the BOLT to be used as normal. But the curved casing just made that more trouble when it's worth so I just take the batteries out when it's not being used. As you can see in the code, it's programmed to play the tune and activate the laser as soon as power is applied and then at the specified interval afterwards.

I included the piezo on a whim thinking that Skeletor might learn that hearing it meant lasers, but didn't really believe this would be the case. I was _**wrong**_. It doesn't matter where he is in the house: when he hears "Twinkle Little Star" playing on that buzzer he comes running!

While the ATTiny would likely draw so little power compared to the laser and motor as to not make a difference in the battery life, I'm glad I chose to include the power saving features. By the time we returned from our week-long vacation, the laser and it's movement was pitiful, with the laser actually dimming every time the motor turned. This could be alleviated but increasing the  activation interval as the default of 2 hours means it will run 12 times per day for 15 minutes each. That's 3 hours of the laser and motor being on every day! So, I guess a week is not that bad. But in the future, I might just wired in a 3.3V wall power supply to keep things running at full power indefinitely.

I hope you enjoyed this little tutorial and that your cats might enjoy it too. Thanks for reading!

And now, for the requisite cat video:
{{< youtube K4VAz9f-km4 >}}

-Adam
