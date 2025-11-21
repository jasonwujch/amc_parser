# 2004 AMC 8 Problem 14

## Problem

What is the area enclosed by the geoboard quadrilateral below?

[asy] unitsize(3mm); defaultpen(linewidth(.8pt)); dotfactor=2; for(int a=0; a<=10; ++a) for(int b=0; b<=10; ++b) { dot((a,b)); }; draw((4,0)--(0,5)--(3,4)--(10,10)--cycle); [/asy]

$\textbf{(A)}\ 15\qquad \textbf{(B)}\ 18\frac12 \qquad \textbf{(C)}\ 22\frac12 \qquad \textbf{(D)}\ 27 \qquad \textbf{(E)}\ 41$

## Solution 1
[asy] unitsize(5mm); defaultpen(linewidth(.8pt)); dotfactor=2; for(int a=0; a<=10; ++a) for(int b=0; b<=10; ++b) { dot((a,b)); }; draw((4,0)--(0,5)--(3,4)--(10,10)--cycle); draw((0,0)--(10,0)--(10,10)--(3,4)--(0,5)--cycle); draw((10,4)--(0,4)--cycle); dot("$A$", (0,5), W); dot("$B$", (3,4), N); dot("$C$", (10,10), NE); dot("$D$", (0,4), W); dot("$E$", (10,4), E); dot("$F$", (0,0), SW); dot("$G$", (10,0), SE); dot("$H$", (4,0), S); [/asy]
Divide the shape up as above. \[Area = [DEGF] + [ABD] + [BCE] - [AFH] - [CGH] = 4 \cdot 10 + \frac12 \cdot 1 \cdot 3 + \frac12 \cdot 7 \cdot 6 - \frac12 \cdot 5 \cdot 4 - \frac12 \cdot 6 \cdot 10 = 40 + \frac32 + 21 - 10 - 30 = \boxed{\textbf{(C)}\ 22\frac12}\]
~ isabelchen

## Solution 2
Let the bottom left corner be $(0,0)$ . The points would then be $(4,0),(0,5),(3,4),$ and $(10,10)$ . Applying the Shoelace Theorem ,
\[\text{Area} = \frac12 \begin{vmatrix} 4 & 0 \\ 0 & 5 \\ 3 & 4 \\ 10 & 10 \\ 4 & 0\end{vmatrix} = \frac12 |(20+30)-(15+40+40)| = \frac12 |50-95| = \boxed{\textbf{(C)}\ 22\frac12}\]

## Solution 3
The figure contains $21$ interior points and $5$ boundary points. Using Pick's Theorem , the area is \[21+\frac{5}{2}-1=\boxed{\textbf{(C)}\ 22\frac12}\]
### Ishan Also See