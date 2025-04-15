set logscale x 10 
set logscale y 10
set xlabel " log h"
set ylabel "log Error"
set title "Error depending on h value"
set grid
plot "double.txt" using 1:2 with lines title "wzor a", \
     "double.txt" using 1:3 with lines title "wzor b"
pause -1
