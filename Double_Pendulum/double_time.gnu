set terminal pngcairo enhanced font 'Verdana,10'
set output 'Simple Graphic Time.png'

set title "Simple Pendulum"
set xlabel "t"
set ylabel "Y"

set key bmargin center horizontal box


plot 'double_time.dat' using 5:1 with linespoints linestyle 1 title "Theta1",'double_time.dat' using 5:2 with linespoints linestyle 2 title "V_Theta1",'double_time.dat' using 5:3 with linespoints linestyle 3 title "Theta2",'double_time.dat' using 5:4 with linespoints linestyle 4 title "V_Theta2"