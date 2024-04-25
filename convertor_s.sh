#!/bin/bash
NAME=$1
PAGES=$(pdfinfo splitf.pdf |grep Pages | sed 's/[^0-9]*//')
echo converting $NAME with $PAGES pages

gs -o _$NAME -dNoOutputFonts -sDEVICE=pdfwrite $NAME
inkscape --without-gui --file=_$NAME --export-plain-svg=${NAME%".pdf"}.svg
rm _$NAME
svg2gcode ${NAME%".pdf"}.svg -o _${NAME%".pdf"}.gcode
rm ${NAME%".pdf"}.svg
python3.8 processor.py -f _${NAME%".pdf"}.gcode -o ${NAME%".pdf"}.gcode
rm _${NAME%".pdf"}.gcode

rm _$NAME
