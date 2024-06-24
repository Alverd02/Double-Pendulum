set terminal pngcairo enhanced font 'Verdana,10'
set output 'Simple Graphic Time.png'

set title "Simple Pendulum"
set xlabel "t"
set ylabel "Y"


set key bmargin center horizontal box

plot 'simple_time.dat' using 3:1 with linespoints linestyle 1 title "Theta",'simple_time.dat' using 3:2 with linespoints linestyle 2 title "V_Theta"