#!/usr/bin/gnuplot

set terminal pngcairo size 1024,768

set output 'whole.png'
maks = 350
slow = 1600
set xrange [1:slow]
set yrange [1:maks]
set datafile separator " "
set logscale xy
plot 'hapax_whole.txt' using 1:3 pt 7 ps 1 title 'whole'

set output 'ksiazki.png'
maks = 350
slow = 1600
set xrange [1:slow]
set yrange [1:maks]
set datafile separator " "
set logscale xy
plot 'hapax_ksiazki.txt' using 1:3 pt 7 ps 1 title 'ksiazki'

set output 'nieksiazki.png'
maks = 350
slow = 1600
set xrange [1:slow]
set yrange [1:maks]
set datafile separator " "
set logscale xy
plot 'hapax_nieksiazki.txt' using 1:3 pt 7 ps 1 title 'nieksiazki'