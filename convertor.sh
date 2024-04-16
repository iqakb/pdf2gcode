#!/bin/bash
NAME=$1
PAGES=$(pdfinfo splitf.pdf |grep Pages | sed 's/[^0-9]*//')
echo converting $NAME with $PAGES pages

gs -o _$NAME -dNoOutputFonts -sDEVICE=pdfwrite $NAME
pdfseparate _$NAME ${NAME%".pdf"}_%d.pdf

for i in $(eval echo {1..$PAGES})
do
   inkscape --without-gui --file=${NAME%".pdf"}_$i.pdf --export-plain-svg=${NAME%".pdf"}_$i.svg
   rm ${NAME%".pdf"}_$i.pdf
   svg2gcode ${NAME%".pdf"}_$i.svg -o _${NAME%".pdf"}_$i.gcode
   rm ${NAME%".pdf"}_$i.svg
   python3.8 processor.py -f _${NAME%".pdf"}_$i.gcode -o ${NAME%".pdf"}_$i.gcode
   rm _${NAME%".pdf"}_$i.gcode
done

rm _$NAME
