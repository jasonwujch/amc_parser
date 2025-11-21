# 2007 AMC 8 Problem 23

## Problem

What is the area of the shaded pinwheel shown in the $5 \times 5$ grid?

[asy] filldraw((2.5,2.5)--(0,1)--(1,1)--(1,0)--(2.5,2.5)--(4,0)--(4,1)--(5,1)--(2.5,2.5)--(5,4)--(4,4)--(4,5)--(2.5,2.5)--(1,5)--(1,4)--(0,4)--cycle, gray, black); int i; for(i=0; i<6; i=i+1) { draw((i,0)--(i,5)); draw((0,i)--(5,i)); } [/asy]

$\textbf{(A)}\: 4\qquad\textbf{(B)}\: 6\qquad\textbf{(C)}\: 8\qquad\textbf{(D)}\: 10\qquad\textbf{(E)}\: 12$

## Solution 1
The area of the square around the pinwheel is 25. The area of the pinwheel is equal to $\text{the square } - \text{ the white space.}$ Each of the four triangles have a base of 3 units and a height of 2.5 units, and so their combined area is 15 units squared. Then the unshaded space consists of the four triangles with total area of 15, and there are four white corner squares. Therefore the area of the pinwheel is $25-(15+4)$ which is $\boxed{\textbf{(B) 6}}$

## Solution 2
The pinwheel is composed of $8$ congruent obtuse triangles whose base measures length $1$ and height measures length $1.5$ . Using the area formula for triangles, the pinwheel has an area of \[8(\frac12\cdot1\cdot1.5)=8(0.75)=\boxed{\textbf{(B) 6}}.\]

## Video Solution
https://www.youtube.com/watch?v=dQw4w9WgXcQ -Happytwin

## Video Solution by OmegaLearn
https://youtu.be/abSgjn4Qs34?t=748
~ pi_is_3.14

## Video Solution by WhyMath
https://youtu.be/CGpR3VKeVV0
### See Also