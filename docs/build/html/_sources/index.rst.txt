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
