# file: Makefile
# vim:fileencoding=utf-8:fdm=marker:ft=make
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-14T19:44:33+0100
# Last modified: 2018-11-18T14:50:47+0100
.SUFFIXES:
.SUFFIXES: .pdf .eps .py .png
.PHONY: all clean

all: gelcoat-nomogram.pdf gelcoat-nomogram.png nomogram-constructie.pdf \
	nomogram-constructie.png

# eps2png is a script that I wrote myself. You can find it in my scripts
# repository on github.
.eps.png:
	eps2png $<

.eps.pdf:
	gs -q -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dEPSCrop \
		-sOutputFile=$@ -c .setpdfwrite -f $<

.py.eps: Makefile
	python3 $< >body.ps
	echo '%!PS-Adobe-3.0 EPSF-3.0' >header.ps
	gs -q -sDEVICE=bbox -dBATCH -dNOPAUSE body.ps >>header.ps 2>&1
	cat header.ps body.ps > $@
	rm -f body.ps header.ps

clean::
	rm -f *.eps foo.ps body.ps header.ps *.pdf *.png
