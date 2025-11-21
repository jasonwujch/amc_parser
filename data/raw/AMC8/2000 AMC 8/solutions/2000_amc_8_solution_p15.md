# 2000 AMC 8 Problem 15

## Problem

Triangles $ABC$ , $ADE$ , and $EFG$ are all equilateral. Points $D$ and $G$ are midpoints of $\overline{AC}$ and $\overline{AE}$ , respectively. If $AB = 4$ , what is the perimeter of figure $ABCDEFG$ ?

[asy] pair A,B,C,D,EE,F,G; A = (4,0); B = (0,0); C = (2,2*sqrt(3)); D = (3,sqrt(3)); EE = (5,sqrt(3)); F = (5.5,sqrt(3)/2); G = (4.5,sqrt(3)/2); draw(A--B--C--cycle); draw(D--EE--A); draw(EE--F--G); label("$A$",A,S); label("$B$",B,SW); label("$C$",C,N); label("$D$",D,NE); label("$E$",EE,NE); label("$F$",F,SE); label("$G$",G,SE);[/asy]

$\text{(A)}\ 12\qquad\text{(B)}\ 13\qquad\text{(C)}\ 15\qquad\text{(D)}\ 18\qquad\text{(E)}\ 21$

## Solution 1
The large triangle $ABC$ has sides of length $4$ . The medium triangle has sides of length $2$ . The small triangle has sides of length $1$ . There are $3$ segment sizes, and all segments depicted are one of these lengths.
Starting at $A$ and going clockwise, the perimeter is:
$AB + BC + CD + DE + EF + FG + GA$
$4 + 4 + 2 + 2 + 1 + 1 + 1$
$15$ , thus the answer is $\boxed{C}$

## Solution 2
The perimeter of $ABCDEFG$ is the perimeter of the three triangles, minus segments $AD$ and $EG$ , which are on the interior of the figure. Because each of these segments is on two triangles, each segment must be subtracted two times.
As in solution 1, the sides of the triangles are $4, 2,$ and $1$ , and the perimeters of the triangles are thus $12, 6,$ and $3$ .
The perimeter of the three triangles is $12 + 6 + 3 = 21$ . Subtracting the two segments $AD$ and $EG$ two times, the perimeter of $ABCDEFG$ is $21 - 2 - 1 - 2 - 1 = 15$ , and the answer is $\boxed{C}$ .
### See Also