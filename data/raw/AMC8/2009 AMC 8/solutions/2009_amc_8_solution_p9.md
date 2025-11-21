# 2009 AMC 8 Problem 9

## Problem

Construct a square on one side of an equilateral triangle. On one non-adjacent side of the square, construct a regular pentagon, as shown. On a non-adjacent side of the pentagon, construct a hexagon. Continue to construct regular polygons in the same way, until you construct an octagon. How many sides does the resulting polygon have?

[asy] defaultpen(linewidth(0.6)); pair O=origin, A=(0,1), B=A+1*dir(60), C=(1,1), D=(1,0), E=D+1*dir(-72), F=E+1*dir(-144), G=O+1*dir(-108); draw(O--A--B--C--D--E--F--G--cycle); draw(O--D, dashed); draw(A--C, dashed);[/asy]

$\textbf{(A)}\ 21 \qquad \textbf{(B)}\ 23 \qquad \textbf{(C)}\ 25 \qquad \textbf{(D)}\ 27 \qquad \textbf{(E)}\ 29$

## Solution
Of the six shapes used to create the polygon, the triangle and octagon are adjacent to the others on one side, and the others are adjacent on two sides. In the triangle and octagon $3+8-2(1)=9$ sides are on the outside of the final polygon. In the other shapes $4+5+6+7-4(2) = 14$ sides are on the outside. The resulting polygon has $9+14 = \boxed{\textbf{(B)}\ 23}$ sides.

## Solution 2
We can quickly see a pattern if we draw out the other shapes. Every shape will have two of its sides taken out except the triangle and octagon. We can then make the expression $2+2+3+4+5+7$ which is $\boxed{\textbf{(B)}\ 23}$
~Trex226

## Video Solution
https://youtu.be/eG8w13-3S8M
~savannahsolver
### See Also