set terminal pngcairo enhanced font 'Verdana,10'
set output 'grafico.png'

set title "Gráfico de Dispersión con Líneas"
set xlabel "Eje X"
set ylabel "Eje Y"

# Configurar estilo de los puntos y líneas
set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5   # Línea azul, puntos con símbolo

# Graficar datos con líneas y puntos
plot 'data.dat' using 1:2 with linespoints linestyle 1 title 'Datos1'
