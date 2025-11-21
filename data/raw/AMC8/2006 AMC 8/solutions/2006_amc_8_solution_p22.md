# 2006 AMC 8 Problem 22

## Problem

Three different one-digit positive integers are placed in the bottom row of cells. Numbers in adjacent cells are added and the sum is placed in the cell above them. In the second row, continue the same process to obtain a number in the top cell. What is the difference between the largest and smallest numbers possible in the top cell?

[asy] path cell=((0,0)--(1,0)--(1,1)--(0,1)--cycle); path sw=((0,0)--(1,sqrt(3))); path se=((5,0)--(4,sqrt(3))); draw(cell, linewidth(1)); draw(shift(2,0)*cell, linewidth(1)); draw(shift(4,0)*cell, linewidth(1)); draw(shift(1,3)*cell, linewidth(1)); draw(shift(3,3)*cell, linewidth(1)); draw(shift(2,6)*cell, linewidth(1)); draw(shift(0.45,1.125)*sw, EndArrow); draw(shift(2.45,1.125)*sw, EndArrow); draw(shift(1.45,4.125)*sw, EndArrow); draw(shift(-0.45,1.125)*se, EndArrow); draw(shift(-2.45,1.125)*se, EndArrow); draw(shift(-1.45,4.125)*se, EndArrow); label("$+$", (1.5,1.5)); label("$+$", (3.5,1.5)); label("$+$", (2.5,4.5));[/asy]

$\textbf{(A)}\ 16\qquad\textbf{(B)}\ 24\qquad\textbf{(C)}\ 25\qquad\textbf{(D)}\ 26\qquad\textbf{(E)}\ 35$

## Solution
If the lower cells contain $A, B$ and $C$ , then the second row will contain $A + B$ and $B + C$ , and the top cell will contain $A + 2B + C$ . To obtain the smallest sum, place $1$ in the center cell and $2$ and $3$ in the outer ones. The top number will be $7$ . For the largest sum, place $9$ in the center cell and $7$ and $8$ in the outer ones. This top number will be $33$ . The difference is $33 - 7 = \boxed{\textbf{(D)}\ 26 }$ .

## Video Solution
https://www.youtube.com/watch?v=_FAL-t93VIk ~David

## Video Solution by WhyMath
https://youtu.be/fSl8DBAk-64
### See Also