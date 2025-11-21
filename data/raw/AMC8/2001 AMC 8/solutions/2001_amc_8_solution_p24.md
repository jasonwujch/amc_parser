# 2001 AMC 8 Problem 24

## Problem

Each half of this figure is composed of 3 red triangles, 5 blue triangles and 8 white triangles. When the upper half is folded down over the centerline, 2 pairs of red triangles coincide, as do 3 pairs of blue triangles. There are 2 red-white pairs. How many white pairs coincide?

[asy] draw((0,0)--(4,4*sqrt(3))); draw((1,-sqrt(3))--(5,3*sqrt(3))); draw((2,-2*sqrt(3))--(6,2*sqrt(3))); draw((3,-3*sqrt(3))--(7,sqrt(3))); draw((4,-4*sqrt(3))--(8,0)); draw((8,0)--(4,4*sqrt(3))); draw((7,-sqrt(3))--(3,3*sqrt(3))); draw((6,-2*sqrt(3))--(2,2*sqrt(3))); draw((5,-3*sqrt(3))--(1,sqrt(3))); draw((4,-4*sqrt(3))--(0,0)); draw((3,3*sqrt(3))--(5,3*sqrt(3))); draw((2,2*sqrt(3))--(6,2*sqrt(3))); draw((1,sqrt(3))--(7,sqrt(3))); draw((-1,0)--(9,0)); draw((1,-sqrt(3))--(7,-sqrt(3))); draw((2,-2*sqrt(3))--(6,-2*sqrt(3))); draw((3,-3*sqrt(3))--(5,-3*sqrt(3))); [/asy]

$\textbf{(A)}\ 4 \qquad \textbf{(B)}\ 5 \qquad \textbf{(C)}\ 6 \qquad \textbf{(D)}\ 7 \qquad \textbf{(E)}\ 9$

## Solution
Each half has $3$ red triangles, $5$ blue triangles, and $8$ white triangles. There are also $2$ pairs of red triangles, so $2$ red triangles on each side are used, leaving $1$ red triangle, $5$ blue triangles, and $8$ white triangles remaining on each half. Also, there are $3$ pairs of blue triangles, using $3$ blue triangles on each side, so there is $1$ red triangle, $2$ blue triangles, and $8$ white triangles remaining on each half. Also, we have $2$ red-white pairs. This obviously can't use $2$ red triangles on one side, since there is only $1$ on each side, so we must use $1$ red triangle and $1$ white triangle per side, leaving $2$ blue triangles and $7$ white triangles apiece. The remaining blue triangles cannot be matched with other blue triangles since that would mean there were more than $3$ blue pairs, so the remaining blue triangles must be paired with white triangles, yielding $4$ blue-white pairs, one for each of the remaining blue triangles. This uses $2$ blue triangles and $2$ white triangles on each side, leaving $5$ white triangles apiece, which must be paired with each other, so there are $5$ white-white pairs, $\boxed{\text{B}}$ .

## Video Solutions
https://www.youtube.com/watch?v=D5iOE6w2LMk -jchoi1267
### See Also