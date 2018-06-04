---
author: adam
date: 2014-07-15 13:00:40+00:00
draft: false
title: Finally, A Windows Package Manager - With Chocolate!
type: post
url: /2014/07/15/finally-a-windows-package-manager-with-chocolate/
categories:
- Arduino
- Cool Stuff
- Tools
- Tutorial
---

To the chagrin of the open source community, I'm a Windows guy. I do really like Linux based systems, but much of my professional career has remained at least partly in the Windows world. 15 years of using Visual Studio (the only Microsoft product I truly like) have brought me to prefer it greatly over any IDE out there. I even use it for all my [Arduino/AVR work](http://www.visualmicro.com/), but that's another post.

But if there is anything from the Linux world that I miss when using Windows, it is a proper package manger, a command line one like apt-get on Debian and Ubuntu. As someone who has installed Windows enough to have once had a Windows 98 serial key memorized I can say that a graphical installer is just too much of a pain. Being able to type "apt-get install vlc" (which would install the popular [VideoLan Client](http://www.videolan.org/)) and do nothing else is great. Most of the time you can even just guess at a package being available and it usually is.

The first to try to fix this on Windows was [Ninite](http://ninite.com) which is great for most people and has a very concise, curated list of available applications. But it's web-based and, well, has a curated list of applications... it has the common 90%, but I'm the type that uses that other 10%. Enter [Chocolatey](https://chocolatey.org/).

<!-- more -->

If you can forgive the odd name, Chocolatey is fantastic. Not quite up to the level of apt-get but it's pretty darn close. Essentially it works in an almost identical fashion to apt-get. It is fully command line (though there is a GUI availabe if you want to be lame) and has community added [application packages](https://chocolatey.org/packages) that span an wide range of interests (1971 in total as of this writing). First off, let's get Chocolately installed.

Installation is super simple, just paste the code below onto your command line and hit enter (you'll need Windows 7 or greater):


    
    @powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
    



Give it a minute to download and install and you are all set to get going. The official documentation makes things a little confusing by having way too many aliases for all the different commands. There are at least three ways to install a package: "cinst ", "chocolatey install ", and "choco install ". For the sake of simplicity and to keep things as similar to apt-get, I'm going to use the "choco" base command from here on. Typing "chocolatey" is just too much to type and I don't want to remember all of the aliases for the sub-commands like install, update, etc.

First up, finding a package with the "list" command, which is good for if you aren't quit sure what the exact name of the package is you want to install since you must specify the name _exactly_.


    
    choco list  #find available packages matching 
    choco list  -all #show all versions for the specified pacakge
    choco list  -localonly #find already installed packages matching 
    
    c:\>choco list arduino
    arduinoide 1.0.5.20140625
    arduinoidegalileo 0.7.5
    
    



Note that it displays the package name followed by the latest version number, which can be useful if you need to install an older version. Use the "-all" flag shown above to see what other versions are available. In this case, we also see two packages; the first is the standard Arduino IDE and the second being a special version for the new Intel Galileo boards.

So, now install Arduino using:


    
    choco install arduinoide



Note how  you can specify the package version as well as multiple packages that will all be installed at once. By default, Chocolatey will automatically install any needed dependencies.


    
    choco install arduinoide -version 1.0.5.20140625 #install specific version of arduinoide
    choco install arduinoide python2 kdiff #install Arduino, Python 2.7, and KDiff at the same time.



You can also use Chocolatey to update packages using the update command, even updating all packages on your system at once.


    
    choco update arduinoide #update just Arduino
    choco update all #update every package currently installed with Chocolatey
    



Last of all is the ability to uninstall packages which is quite simple:


    
    choco uninstall arduinoide
    



If you are unsure of the name of the packages you already have installed, simply use the list all local command:


    
    choco list all -localonly
    



That's the basics of using Chocolatey, though there are many more advanced features like package sources, missing dependency installation, python and ruby integration, and many others that can be seen on the [Chocolatey Command Reference](https://github.com/chocolatey/chocolatey/wiki/CommandsReference) page.

But last, to show why Chocolatey is so awesome, here's a one-liner that installs nearly everything I use for all of my development work:


    
    choco install arduinoide python2 notepadplusplus kdiff make mingw Sudo GnuWin SublimeText3 ConEmu githubforwindows tortoisesvn
    



That's it! I save this and can just paste it into my console on any new machine. In the above order, the tools are:




  * Arduino IDE
  * Python 2.7
  * Notepad++ - Awesome Windows text editor
  * KDiff - file diff/merge tool
  * make - Windows port of the "make" build tool
  * MinGW - Minimalist GNU for Windows (mainly used for GCC)
  * Sudo - just like Sudo on Linux but for Windows
  * GnuWin - Windows native ports of GNU tools like ls, sed, awk, grep, wget...
  * SublimeText3 - Another great text editor with more project management
  * ConEmu - Best Windows console terminal I've ever used
  * GitHub for Windows - GitHub's official Windows GUI client.
  * Tortoise SVN - Windows GUI for Subversion


Think of how long that would take to download and install off of these programs manually! Hopefully this will save you a great deal of time the next time you need a new application.
