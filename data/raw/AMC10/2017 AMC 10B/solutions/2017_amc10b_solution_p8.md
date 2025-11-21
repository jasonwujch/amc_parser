# 2017 AMC 10B Problem 8

## Problem

Points $A(11, 9)$ and $B(2, -3)$ are vertices of $\triangle ABC$ with $AB=AC$ . The altitude from $A$ meets the opposite side at $D(-1, 3)$ . What are the coordinates of point $C$ ?

$\textbf{(A)}\ (-8, 9)\qquad\textbf{(B)}\ (-4, 8)\qquad\textbf{(C)}\ (-4, 9)\qquad\textbf{(D)}\ (-2, 3)\qquad\textbf{(E)}\ (-1, 0)$

## Solution 1
Since $AB = AC$ , then $\triangle ABC$ is isosceles, so $BD = CD$ . Therefore, the coordinates of $C$ are $(-1 - 3, 3 + 6) = \boxed{\textbf{(C) } (-4,9)}$ .
[asy] pair A,B,C,D; A=(11,9); B=(2,-3); C=(-4,9); D=(-1,3); draw(A--B--C--cycle); draw(A--D); draw(rightanglemark(A,D,B,30)); label("$A$",A,E); label("$B$",B,S); label("$D$",D,W); label("$C$",C,N); [/asy]

## Solution 2
Calculating the equation of the line running between points $B$ and $D$ , $y = -2x + 1$ . The only coordinate of $C$ that is also on this line is $\boxed{\textbf{(C) } (-4,9)}$ .

## Solution 3
Similar to the first solution, because the triangle is isosceles, then the line drawn in the middle separates the triangle into two smaller congruent triangles. To get from $B$ to $D$ , we go to the left $3$ and up $6$ . Then to get to point $C$ from point $D$ , we go to the right $3$ and up $6$ , getting us the coordinates $\boxed{\textbf{(C) } (-4,9)}$ . ~ $\text{KLBBC}$

## Solution 4
As stated in solution 1, the triangle is isosceles.
[asy] pair A,B,C,D; A=(11,9); B=(2,-3); C=(-4,9); D=(-1,3); draw(A--B--C--cycle); draw(A--D); draw(rightanglemark(A,D,B)); label("$A$",A,E); label("$B$",B,S); label("$D$",D,W); label("$C$",C,N); [/asy]
This means that $D(-1, 3)$ is the midpoint of $B(2, -3)$ and $C(x,y)$ . So $\frac{x+2}{2}$ $= -1$ and so $x = -4$ . Similarly for $y$ , we have $\frac{y-3}{2}$ $=3$ and so $y=9$ . So our final answer is $\boxed{\textbf{(C) } (-4,9)}$ .
- youtube.com/indianmathguy

## Video Solution
https://youtu.be/4rRckA3gcPU
~savannahsolver

## Video Solution by TheBeautyofMath
https://youtu.be/XRfOULUmWbY?t=367
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .