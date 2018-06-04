---
author: adam
date: 2013-12-23 21:26:34+00:00
draft: false
title: Doing things the "hard" way
type: post
url: /2013/12/23/doing-things-the-hard-way/
categories:
- Arduino
- Tutorial
---

I'm in the middle of designing a new Maniacal Labs product (more on that in another post) and have been working with a library intended for the ATMega328 but need it working on an ATTiny4313. If you ever feel cramped for flash space while working on an Arduino project, try out the ATTiny series of chips and you will quickly feel like 32KB of flash is downright massive! The ATTiny4313 is a decently capable chip, with only 5 less I/O pins than the ATMega328 but a somewhat less proportional 4KB of flash. Right away, this library was going to be trouble since a bare minimum sketch compiled down to 4667 bytes. Practically nothing for a '328 but more than 500 bytes more than the '4313 could handle and that was without actually _doing_ anything!

Much of the problem comes from that fact that the Arduino platform enables easy programming by abstracting the complicated stuff behind single methods. It may _look_ like less code but is, in reality, more code than is needed for many tasks. For example, the blink example from the Arduino IDE:


    
    
        void setup() {                
          pinMode(13, OUTPUT);     
        }
    
        void loop() {
          digitalWrite(13, HIGH);  
          delay(1000);               
          digitalWrite(13, LOW);   
          delay(1000);               
        }
    



This compiles to 1076 bytes. Now let's do it the "hard" way:


    
    
        void setup() {
          //Digital 13 is PB5, set as output
          DDRB |= _BV(PINB5);  
        }
    
        void loop() {
          //set the pin HIGH
          PORTB |= _BV(PINB5); 
          delay(1000);   
          //set the pin LOW  
          PORTB &= ~_BV(PINB5);    
          delay(1000);               
        }
    



This compiles to 674 bytes, a 37% decrease!! On a chip like the '4313 those 402 extra bytes comprise nearly 10% of the total flash available! To further understand what all the DDRB and PORTB stuff is about, take a look at Arduino's article about direct [port manipulation](http://arduino.cc/en/Reference/PortManipulation). If you want to up your Arduino/AVR game, it's some great stuff to learn.

So, I'm sure you're asking why there's such a huge difference. It's simple really... take a look in the Arduino core file wiring_digital.c and you will find that digitalWrite() is really this:


    
    
    void digitalWrite(uint8_t pin, uint8_t val)
    {
        uint8_t timer = digitalPinToTimer(pin);
        uint8_t bit = digitalPinToBitMask(pin);
        uint8_t port = digitalPinToPort(pin);
        volatile uint8_t *out;
    
        if (port == NOT_A_PIN) return;
    
        // If the pin that support PWM output, we need to turn it off
        // before doing a digital write.
        if (timer != NOT_ON_TIMER) turnOffPWM(timer);
    
        out = portOutputRegister(port);
    
        uint8_t oldSREG = SREG;
        cli();
    
        if (val == LOW) {
            *out &= ~bit;
        } else {
            *out |= bit;
        }
    
        SREG = oldSREG;
    }
    



Wow, lots of magic going on there, right? A large part of what's happening is converting an easy to remember pin number (like D13) into the actual port register and register bit. The rest is mostly code to protect you from yourself, like disabling interrupts and PWM output. Much of the time, this should be of little concern but the bright people who wrote the Arduino core included it to ensure as little barrier as possible. That's wonderful when getting started but, as you can see, wastes a lot of program flash.

So next time you find yourself running out of program flash, think about digging in a bit, looking at some datasheets, and learning to do things the hard way.

