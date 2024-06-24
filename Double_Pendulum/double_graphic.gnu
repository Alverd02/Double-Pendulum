set terminal pngcairo enhanced font 'Verdana,10'
set output 'Double Graphic.png'

set title "Double Pendulum"
set xlabel "X"
set ylabel "Y"


set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5   


plot 'double_data.dat' using 1:2 with linespoints linestyle 1 title "",'double_data.dat' using 3:4 with linespoints linestyle 1 title ""
