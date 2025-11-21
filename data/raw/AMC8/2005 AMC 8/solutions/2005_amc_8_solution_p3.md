# 2005 AMC 8 Problem 3

## Problem

What is the minimum number of small squares that must be colored black so that a line of symmetry lies on the diagonal $\overline{BD}$ of square $ABCD$ ?

[asy] defaultpen(linewidth(1)); for ( int x = 0; x < 5; ++x ) { draw((0,x)--(4,x)); draw((x,0)--(x,4)); } fill((1,0)--(2,0)--(2,1)--(1,1)--cycle); fill((0,3)--(1,3)--(1,4)--(0,4)--cycle); fill((2,3)--(4,3)--(4,4)--(2,4)--cycle); fill((3,1)--(4,1)--(4,2)--(3,2)--cycle); label("$A$", (0, 4), NW); label("$B$", (4, 4), NE); label("$C$", (4, 0), SE); label("$D$", (0, 0), SW); [/asy]

$\textbf{(A)}\ 1\qquad\textbf{(B)}\ 2\qquad\textbf{(C)}\ 3\qquad\textbf{(D)}\ 4\qquad\textbf{(E)}\ 5$

## Solution
Rotating square $ABCD$ counterclockwise $45^\circ$ so that the line of symmetry $BD$ is a vertical line makes it easier to see that $\boxed{\textbf{(D)}\ 4}$ squares need to be colored to match its corresponding square.
### See Also