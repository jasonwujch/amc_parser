# 2002 AMC 8 Problem 20

## Problem

The area of triangle $XYZ$ is 8 square inches. Points $A$ and $B$ are midpoints of congruent segments $\overline{XY}$ and $\overline{XZ}$ . Altitude $\overline{XC}$ bisects $\overline{YZ}$ . The area (in square inches) of the shaded region is

[asy] /* AMC8 2002 #20 Problem */ draw((0,0)--(10,0)--(5,4)--cycle); draw((2.5,2)--(7.5,2)); draw((5,4)--(5,0)); fill((0,0)--(2.5,2)--(5,2)--(5,0)--cycle, mediumgrey); label(scale(0.8)*"$X$", (5,4), N); label(scale(0.8)*"$Y$", (0,0), W); label(scale(0.8)*"$Z$", (10,0), E); label(scale(0.8)*"$A$", (2.5,2.2), W); label(scale(0.8)*"$B$", (7.5,2.2), E); label(scale(0.8)*"$C$", (5,0), S); fill((0,-.8)--(1,-.8)--(1,-.95)--cycle, white);[/asy]

$\textbf{(A)}\ 1\frac{1}2\qquad\textbf{(B)}\ 2\qquad\textbf{(C)}\ 2\frac{1}2\qquad\textbf{(D)}\ 3\qquad\textbf{(E)}\ 3\frac{1}2$

## Solution 1
We know the area of triangle $XYZ$ is $8$ square inches. The area of a triangle can also be represented as $\frac{bh}{2}$ or in this problem $\frac{XC\cdot YZ}{2}$ . By solving, we have \[\frac{XC\cdot YZ}{2} = 8,\] \[XC\cdot YZ = 16.\]
With SAS congruence, triangles $XCY$ and $XCZ$ are congruent. Hence, triangle $XCY = \frac{8}{2} = 4$ . (Let's say point $D$ is the intersection between line segments $XC$ and $AB$ .) We can find the area of the trapezoid $ADCY$ by subtracting the area of triangle $XAD$ from $4$ .
We find the area of triangle $XAD$ by the $\frac{bh}{2}$ formula- $\frac{XD\cdot AD}{2} = \frac{\frac{XC}{2}\cdot AD}{2}$ . $AD$ is $\frac{1}{4}$ of $YZ$ from solution 1. The area of $XAD$ is \[\frac{\frac{XC}{2}\cdot \frac{YZ}{4}}{2} = \frac{16}{16} = 1\] .
Therefore, the area of the shaded area- trapezoid $ADCY$ has area $4-1 = \boxed{\text{(D)}\ 3}$ .
- sarah07

## Video Solution
https://www.youtube.com/watch?v=zwy5U5IQi88 ~David

## Video Solution by WhyMath
https://youtu.be/wIVHVxhA7xg
### See Also