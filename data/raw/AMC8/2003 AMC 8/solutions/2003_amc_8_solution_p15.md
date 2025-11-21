# 2003 AMC 8 Problem 15

## Problem

A figure is constructed from unit cubes. Each cube shares at least one face with another cube. What is the minimum number of cubes needed to build a figure with the front and side views shown?

[asy] defaultpen(linewidth(0.8)); path p=unitsquare; draw(p^^shift(0,1)*p^^shift(1,0)*p); draw(shift(4,0)*p^^shift(5,0)*p^^shift(5,1)*p); label("FRONT", (1,0), S); label("SIDE", (5,0), S); [/asy]

$\textbf{(A)}\ 3\qquad\textbf{(B)}\ 4\qquad\textbf{(C)}\ 5\qquad\textbf{(D)}\ 6\qquad\textbf{(E)}\ 7$

## Solution
In order to minimize the amount of cubes needed, we must match up as many squares of our given figures with each other to make different sides of the same cube. One example of the solution with $\boxed{\textbf{(B)}\ 4}$ cubes. Notice the corner cube cannot be removed for a figure of 3 cubes because at least one face of a cube must be touching another face.
[asy] import three; defaultpen(linewidth(0.8)); real r=0.5; currentprojection=orthographic(3/4,8/15,7/15); draw(unitcube, white, thick(), nolight); draw(shift(1,-1,0)*unitcube, white, thick(), nolight); draw(shift(1,0,0)*unitcube, white, thick(), nolight); draw(shift(1,0,1)*unitcube, white, thick(), nolight);[/asy]

## Video Solution
https://www.youtube.com/watch?v=eDpxHt1LL7g
~David
### See Also