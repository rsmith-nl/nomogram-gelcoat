# file: Makefile
# vim:fileencoding=utf-8:fdm=marker:ft=make
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-14T19:44:33+0100
# Last modified: 2018-11-15T10:25:10+0100
.PHONY: all clean

all: gelcoat-nomogram.pdf gelcoat-nomogram.png

# The page size is a hack. Adapt to BoundingBox, now 20 24 267 350.
# Convert postscript points to inch by dividing by 72. Then multiply by the
# resolution in the -r argument.
#
#In [6]: round(267/72*300)
#Out[6]: 1112
#
#In [7]: round(350/72*300)
#Out[7]: 1458
#
gelcoat-nomogram.png: gelcoat-nomogram.eps
	gs -q -sDEVICE=png256 -dBATCH -dNOPAUSE -g1154x1458 -dFIXEDMEDIA \
		-dPSFitPage -r300 -sOutputFile=gelcoat-nomogram.png gelcoat-nomogram.eps


gelcoat-nomogram.pdf: gelcoat-nomogram.eps
	gs -q -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dEPSCrop \
		-sOutputFile=gelcoat-nomogram.pdf -c .setpdfwrite -f gelcoat-nomogram.eps

gelcoat-nomogram.eps: gelcoat-nomogram.py
	python3 gelcoat-nomogram.py >foo.ps
	echo '%!PS-Adobe-3.0 EPSF-3.0' >header.ps
	gs -q -sDEVICE=bbox -dBATCH -dNOPAUSE foo.ps >>header.ps 2>&1
	cat header.ps foo.ps > gelcoat-nomogram.eps
	rm -f foo.ps header.ps

clean::
	rm -f gelcoat-nomogram.eps foo.ps header.ps gelcoat-nomogram.pdf
