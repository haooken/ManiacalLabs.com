---
author: adam
date: 2014-04-01 14:21:47+00:00
draft: false
title: 'Dial-A-Song: Part 2'
type: post
url: /2014/04/01/dial-a-song-part-2/
categories:
- Dial-A-Song
- Projects
---

For part two of the Dial-A-Song project, I'm going to go through the hookup of the phone's keypad so that it can act as an input to the Raspberry Pi.

The first thing to do was remove the short ribbon cable that came on the keypad and replace it with something a little longer so I could more easily hook it up to the Pi. Here's the old ribbon cable:

{{< figure src="/wp-content/uploads/2014/03/IMG_20140309_102644.jpg" caption="Dial Pad and Tone Generator" >}}

And now with the new, more colorful, cable:

{{< figure src="/wp-content/uploads/2014/03/IMG_20140331_135245.jpg" caption="Keypad Wiring" >}}

On the other end, I attached a 2x5 IDC female header (I didn't have a 2x4, so there's a couple wasted pins). This is what will eventually connect to the Pi interface board I'll create, but for now I mocked up a breakout board (the green perf-board) so I could connect it to a breadboard along with Adafruit's great ["Cobbler" kit](http://learn.adafruit.com/adafruit-pi-cobbler-kit/overview).

The keypad's internal wiring is setup as shown below (which the red wire being pin 1 and increasing to the left, from the image above):


    
      5 6 7
    4|1|2|3|
    3|4|5|6|
    2|7|8|9|
    1|*|0|#|



Most matrix keypads are very similar so, the keypad pins should be connected to the Raspberry Pi GPIO as follows:


    
    Pad | Pi
    ________
    1   - 25
    2   - 24
    3   - 23
    4   - 18
    5   - 22
    6   - 17
    7   - 4



Now for the software. Originally, I was going to use [a library](http://crumpspot.blogspot.com/p/keypad-matrix-python-package.html) designed for specifically this purpose. It did exactly what it said it would with the exception that it uses polling to detect the keypads. This works, but required a significant amount of the CPU resources to get any decent response time. Often around 80%. This was not acceptable.

So, I decided to try converting the library to use the interrupt capability of the [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) library that comes pre-installed on Raspbian. It took a little fiddling because the Pi GPIO pins are really susceptible to noise making button debouncing a real issue. But in the end, it works quite well:


    
    
    #!/usr/bin/python
     
    import RPi.GPIO as GPIO
    import time
    
    class keypad():
        def __init__(self, callback):
            GPIO.setmode(GPIO.BCM)
            self._count = 0
            self._inInterrupt = False
            self._callback = callback
    
            # CONSTANTS 
            self.KEYPAD = [
                [1,2,3],
                [4,5,6],
                [7,8,9],
                ["*",0,"#"]
            ]
    
            #hook the rows (1,4,7,*) to these GPIO pins
            self.ROW         = [18,23,24,25]
            #hook the columns (1,2,3) to these GPIO pins
            self.COLUMN      = [4,17,22]
    
            self.__setInterruptMode()
    
        def __colInt(self, channel):
            time.sleep(0.05) #give it a moment to settle
            if GPIO.input(channel) > 0:
                return
    
            #remove interrupts temporarily
            for c in range(len(self.COLUMN)):
                GPIO.remove_event_detect(self.COLUMN[c][/c])
    
            #get column number
            colVal = -1
            for c in range(len(self.COLUMN)):
                if channel == self.COLUMN[c][/c]:
                    colVal = c
    
            #continue if valid column (it should always be)
            if colVal >=0 and colVal < len(self.COLUMN):
    
                #set rows as intputs
                for r in range(len(self.ROW)):
                    GPIO.setup(self.ROW[r], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
                #set triggered column as low output
                GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)
    
                # Scan rows for pushed key/button
                rowVal = -1
                for r in range(len(self.ROW)):
                    tmpRead = GPIO.input(self.ROW[r])
                    if tmpRead == 0:
                        rowVal = r
                        break
    
                #continue if row is valid (possible that it might not be if the key was very quickly released)
                if rowVal >= 0 and rowVal < len(self.ROW):
                    #send key info right away
                    self._callback(self.KEYPAD[rowVal][colVal])
                    #This avoids nasty boucning errors when the key is released
                    #By waiting for the rising edge before re-enabling interrupts it 
                    #avoids interrupts fired due to bouncing on key release and 
                    #any repeated interrupts that would otherwise fire.
                    try:
                        GPIO.wait_for_edge(self.ROW[rowVal], GPIO.RISING)
                        self.__setInterruptMode()
                    except RuntimeError:
                        pass
                    
                    return
    
                else:
                    print "Invalid Row!"
            else:
                print "Invalid Col!"
    
            #re-enable interrupts
            self.__setInterruptMode()
    
        def __changeWrapper(self, channel):
            #if there is already another interrupt going on (multiple key press or something)
            #return right away to avoid collisions
            if self._inInterrupt:
                return;
    
            self._inInterrupt = True
            self.__colInt(channel) #handle the actual interrupt
            self._inInterrupt = False
    
        def __setInterruptMode(self):
            #set the first row as output low
            #only first one needed as it will ground to all columns
            for r in range(len(self.ROW)):
                GPIO.setup(self.ROW[r], GPIO.OUT, initial=GPIO.LOW)
    
            #set columns as inputs and attach interrupt handlers on rising edge
            for c in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[c][/c], GPIO.IN, pull_up_down=GPIO.PUD_UP)
                GPIO.add_event_detect(self.COLUMN[c][/c], GPIO.FALLING, bouncetime=250, callback=self.__changeWrapper)
         
    
        def cleanup(self):
            GPIO.cleanup()
            print "Cleanup done!"
    



It's super simple to use as you can see from the code below. Instantiate the class with a callback function and that function gets called when there's a keypress on the pad. Just note that the callback will be running on the context of a different thread from the main thread. While it uses interrupts, RPi.GPIO cheats a little bit and the interrupts are actually running on background threads and so will the callback. Not usually a big problem but something to be aware of.


    
    
    import time     
    if __name__ == '__main__':
        def keypadCallback(value):
            print "Keypad: " + value
    
        key = keypad(keypadCallback)
    
        try:
            while True:
                time.sleep(1)
    
        except KeyboardInterrupt:
            key.cleanup()
    



You can grab the full library and find any updates to it on [GitHub](https://github.com/ManiacalLabs/RPi-Matrix-Keypad).
That's all for now. Check back soon for more progress on Dial-A-Song!
