# 2002 AMC 8 Problem 15

## Problem

Which of the following polygons has the largest area?

[asy] size(330); int i,j,k; for(i=0;i<5; i=i+1) { for(j=0;j<5;j=j+1) { for(k=0;k<5;k=k+1) { dot((6i+j, k)); }}} draw((0,0)--(4,0)--(3,1)--(3,3)--(2,3)--(2,1)--(1,1)--cycle); draw(shift(6,0)*((0,0)--(4,0)--(4,1)--(3,1)--(3,2)--(2,1)--(1,1)--(0,2)--cycle)); draw(shift(12,0)*((0,1)--(1,0)--(3,2)--(3,3)--(1,1)--(1,3)--(0,4)--cycle)); draw(shift(18,0)*((0,1)--(2,1)--(3,0)--(3,3)--(2,2)--(1,3)--(1,2)--(0,2)--cycle)); draw(shift(24,0)*((1,0)--(2,1)--(2,3)--(3,2)--(3,4)--(0,4)--(1,3)--cycle)); label("$A$", (0*6+2, 0), S); label("$B$", (1*6+2, 0), S); label("$C$", (2*6+2, 0), S); label("$D$", (3*6+2, 0), S); label("$E$", (4*6+2, 0), S);[/asy]

$\textbf{(A)}\text{A}\qquad\textbf{(B)}\ \text{B}\qquad\textbf{(C)}\ \text{C}\qquad\textbf{(D)}\ \text{D}\qquad\textbf{(E)}\ \text{E}$

## Solution 1
Each polygon can be partitioned into unit squares and right triangles with sidelength $1$ . Count the number of boxes enclosed by each polygon, with the unit square being $1$ , and the triangle being $.5$ . A has 5, B has 5, C has 5, D has 4.5, and E has 5.5. Therefore, the polygon with the largest area is $\boxed{\textbf{(E)}\ \text{E}}$ .

## Solution 2 (Under 15 seconds)
Pick's Theorem:
$A = I + \frac{1}{2}B - 1$
where $I$ is the number of lattice points in the interior and $B$ being the number of lattice points on the boundary.
Ok, so we want to find the polygon with the largest area, first notice that not a single polygon has a lattice point in the interior. Now look at the formula:
$A = \frac{1}{2}B - 1$
So now just look at the polygon with the most lattice points on the boundary, and that is figure $\text{E}$ , with 13 lattice points on the boundary. So the polygon with the largest area is $\boxed{\textbf{(E)}\ \text{E}}$ .
~blankbox
### See Also