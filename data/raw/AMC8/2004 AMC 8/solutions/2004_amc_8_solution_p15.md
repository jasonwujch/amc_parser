# 2004 AMC 8 Problem 15

## Problem

Thirteen black and six white hexagonal tiles were used to create the figure below. If a new figure is created by attaching a border of white tiles with the same size and shape as the others, what will be the difference between the total number of white tiles and the total number of black tiles in the new figure?

[asy] defaultpen(linewidth(1)); real x=sqrt(3)/2; path p=rotate(30)*polygon(6); filldraw(p^^shift(0,3)*p^^shift(4x,0)*p^^shift(3x,1.5)*p^^shift(2x,3)*p^^shift(-4x,0)*p^^shift(-3x,1.5)*p^^shift(-2x,3)*p^^shift(3x,-1.5)*p^^shift(-3x,-1.5)*p^^shift(2x,-3)*p^^shift(-2x,-3)*p^^shift(0,-3)*p, black, black); draw(shift(2x,0)*p^^shift(-2x,0)*p^^shift(x,1.5)*p^^shift(-x,1.5)*p^^shift(x,-1.5)*p^^shift(-x,-1.5)*p); [/asy]

$\textbf{(A)}\ 5\qquad \textbf{(B)}\ 7\qquad \textbf{(C)}\ 11\qquad \textbf{(D)}\ 12 \qquad \textbf{(E)}\ 18$

## Solution
The first ring around the middle tile has $6$ tiles, and the second has $12$ . From this pattern, the third ring has $18$ tiles. Of these, $6+18=24$ are white and $1+12=13$ are black, with a difference of $24-13 = \boxed{\textbf{(C)}\ 11}$ .
### See Also