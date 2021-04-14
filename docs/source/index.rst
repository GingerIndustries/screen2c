.. screen2c documentation master file, created by
   sphinx-quickstart on Mon Apr 12 17:32:10 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


screen2c
=========
PCF8574 + LCD = fun

.. toctree::
   :maxdepth: 2
   :caption: Contents:

What is it?
============
Exactly what it sounds like. I couldn't find any good libraries to do this, so I modified one and made it better.
Much thanks to the original dev, Denis Pleic.

How do I get it?
===================
::

	pip install screen2c

How do I use it?
==================
Easy-peasy.

1. Import the module, and create a Display object. This is what you'll use to do all the stuff to the screen.
::

	import screen2c
	
	display = screen2c.Display()

2. Do stuff with the Display! To display text, call write(), with the text as the first argument and line as the second one.
::

	display.write("Hello", 1)
	display.write("World!", 2)
	# Infinite loop so that the program doesn't instantly stop
	while True:
		pass

Examples
========
Display "Hello World" on the screen
-----------------------------------
::

	import screen2c
	
	display = screen2c.Display()
	
	display.write("Hello World!!!", 1)
	
	while True:
		pass

Typewriter out text
-------------------
::

	import screen2c
	import time
	
	display = screen2c.Display()
	display.setCursor(screen2c.CursorMode.BLINK)
	
	typewriter = "Hello again!"
	for x in range(0, len(typewriter)):
		display.write(typewriter[x], 1, x)
		time.sleep(0.2)
	
	while True:
		pass

Disco party, because why not
----------------------------
::

	import screen2c
	import time
	display = screen2c.Display()
	
	while True:
		display.setBacklight(not display.backlightOn)
		time.sleep(0.2)

Troubleshooting
===============
Oh noes! Something's gone wrong, and you've encountered that most dreaded of Python classes, an **Exception!** Don't worry, it's not *usually* a severe issue. Keep reading!

PermissionDeniedError
---------------------
This one's pretty self-explanatory. There are two fixes:

1. Run your script as root.
2. Add yourself to the GPIO group using:

::

	sudo usermod -aG gpio yourusername

and reboot.

NoDeviceError
-------------
Again, self-explanatory. Check your screen is connected to the right GPIO pins and that no cables are loose! If it is, then you may have the wrong address for the screen. To check the address, type:
::

	sudo i2cdetect -y 1
	# or, if you have a really old RaspPi
	sudo i2cdetect -y 0

You'll get output that looks like this:
::

	     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
	00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
	10: -- -- -- -- -- -- -- -- -- -- 1a -- -- -- -- -- 
	20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- -- 
	30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	70: -- -- -- -- -- -- -- -- 

My Pi has 2 devices, one at address 27 and one at address 1a. 27 is my screen, and also happens to be the default for the Display. Keey note of the screen address. (If you have multiple and don't know which it is, then try each. XD)

Then, change the code for your Display object to look like this
::

	display = screen2c.Display(0xYourAddress)

For me, it would be
::

	display = screen2c.Display(0x27)

CommunicationError
------------------
This error generally occurs when one of the cables connecting the Pi to the screen has become disconnected between Display object creation and a method being called. Plug the cables back in and try again.

*Very rarely* this error can occur due to other factors. If this happens, `file an issue on GitHub. <https://github.com/GingerIndustries/screen2c/issues/new/choose>`_

I2CDisabledError
----------------
This error occurs because you have the I2C interface disabled on your RaspPi (this is how it is by default.) To fix it, follow this simple five-step process:

1. Type ``sudo raspi-config`` in Terminal.
2. Go to ``Interface Options``.
3. Choose ``I2C``
4. Select ``Yes``, and then ``OK``.
5. Select ``Finish``.

Piece of cake.

Anything else
-------------
Basically, this is an issue either with something in the depths of the Linux kernel underworld or an issue with screen2c itself. In both cases, `file an issue on GitHub and I'll see what I can do about it. <https://github.com/GingerIndustries/screen2c/issues/new/choose>`_

API
===
.. automodule:: screen2c
	:members:
	:undoc-members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
