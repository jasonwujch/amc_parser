# 2009 AMC 8 Problem 20

## Problem

How many non-congruent triangles have vertices at three of the eight points in the array shown below?

[asy]dot((0,0)); dot((.5,.5)); dot((.5,0)); dot((.0,.5)); dot((1,0)); dot((1,.5)); dot((1.5,0)); dot((1.5,.5));[/asy]

$\textbf{(A)}\ 5 \qquad \textbf{(B)}\ 6 \qquad \textbf{(C)}\ 7 \qquad \textbf{(D)}\ 8 \qquad \textbf{(E)}\ 9$

## Solution
Assume the base of the triangle is on the bottom four points because a congruent triangle can be made by reflecting the base on the top four points. For a triangle with a base of length $1$ , there are $3$ triangles. For a triangle with a base of length $2$ , there are $3$ triangles. For length $3$ , there are $2$ . In total, the number of non-congruent triangles is $3+3+2=\boxed{\textbf{(D)}\ 8}$ .
### See Also