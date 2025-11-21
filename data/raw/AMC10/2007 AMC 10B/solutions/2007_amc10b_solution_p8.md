# 2007 AMC 10B Problem 8

## Problem

On the trip home from the meeting where this AMC10 was constructed, the Contest Chair noted that his airport parking receipt had digits of the form $bbcac,$ where $0 \le a < b < c \le 9,$ and $b$ was the average of $a$ and $c.$ How many different five-digit numbers satisfy all these properties?

$\textbf{(A) } 12 \qquad\textbf{(B) } 16 \qquad\textbf{(C) } 18 \qquad\textbf{(D) } 20 \qquad\textbf{(E) } 25$

## Solution
Case $1$ : The numbers are separated by $1$ .
We this case with $a=0, b=1,$ and $c=2$ . Following this logic, the last set we can get is $a=7, b=8,$ and $c=9$ . We have $8$ sets of numbers in this case.
Case $2$ : The numbers are separated by $2$ .
This case starts with $a=0, b=2,$ and $c=4$ . It ends with $a=5, b=7,$ and $c=9$ . There are $6$ sets of numbers in this case.
Case $3$ : The numbers start with $a=0, b=3,$ and $c=6$ . It ends with $a=3, b=6,$ and $c=9$ . This case has $4$ sets of numbers.
It's pretty clear that there's a pattern: $8$ sets, $6$ sets, $4$ sets. The amount of sets per case decreases by $2$ , so it's obvious Case $4$ has $2$ sets. The total amount of possible five-digit numbers is $8+6+4+2=\boxed{\textbf{(D)}\ 20}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .