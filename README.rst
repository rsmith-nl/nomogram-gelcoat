Making a nomogram with Python and Postscript
############################################

:date: 2018-11-18
:tags: python, postscript, nomogram
:author: Roland Smith

.. Last modified: 2018-11-18T11:46:02+0100

Introduction
------------

At work I needed a suitable way to check the callibration of gelcoat spray
equipment. Gelcoat requires an initiator (often called “catalyst”) in the form
of a peroxide to cure. The peroxide/gelcoat ratio is important, so it is
checked regularly by spraying the separate components into a suitable
container and weighing them.

For those familiar with gelcoat spraying, this is *not* a system with coupled
gelcoat and peroxide pumps. But rather an *external mixing* spray gun where
the peroxide is simply fed from a pressurized container to the spray gun.

Since we're handling resins, solvents and peroxide, protective equipment
including gloves is a must.  That makes it cumbersome to whip out a smartphone
to use it as a calculator to check the ratio.  Since you don't want to get
gelcoat or peroxide on your expensive phone, you have to take off your gloves
to handle it. This might have to be repeated several times.

So I decided to make a diagram where one could relatively easy read off the
peroxide percentage given the quantities of both compontents. This can be
printed and laminated between plastic to make it resistant against stains.

.. PELICAN_END_SUMMARY


Description
-----------

Such a diagram (basically a graphical analog computation device) is called a nomogram_.
The linked wikipedia article gives and excellent overview.

.. _nomogram: https://en.wikipedia.org/wiki/Nomogram


Python and PostScript
---------------------

Although PostScript is good at creating graphics, I find it cumbersome for
calculations.  So in this case, I'm using Python to do most of the
calculations and have it generate PostScript commands for drawing.


Building
--------

The supplied ``Makefile`` specifies how the Python code is used to create the
graphs.

It uses my eps2png_ script to create PNG images. The link takes you to my
github repository for scripts.

.. _eps2png: https://github.com/rsmith-nl/scripts/blob/master/eps2png.sh


Requirements
------------

* python_ 3.6+
* ghostscript_
* eps2png_
* make (I'm using FreeBSD's ``make``, but GNU ``make`` works as well)

.. _python: https://www.python.org/
.. _ghostscript: https://www.ghostscript.com/


License
-------

MIT. See LICENSE.txt.
