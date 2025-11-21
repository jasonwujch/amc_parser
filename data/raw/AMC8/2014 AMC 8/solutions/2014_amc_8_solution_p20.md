# 2014 AMC 8 Problem 20

## Problem

Rectangle $ABCD$ has sides $CD=3$ and $DA=5$ . A circle of radius $1$ is centered at $A$ , a circle of radius $2$ is centered at $B$ , and a circle of radius $3$ is centered at $C$ . Which of the following is closest to the area of the region inside the rectangle but outside all three circles?

[asy] draw((0,0)--(5,0)--(5,3)--(0,3)--(0,0)); draw(Circle((0,0),1)); draw(Circle((0,3),2)); draw(Circle((5,3),3)); label("A",(0.2,0),W); label("B",(0.2,2.8),NW); label("C",(4.8,2.8),NE); label("D",(5,0),SE); label("5",(2.5,0),N); label("3",(5,1.5),E); [/asy]

$\text{(A) }3.5\qquad\text{(B) }4.0\qquad\text{(C) }4.5\qquad\text{(D) }5.0\qquad\text{(E) }5.5$

## Solution
The area in the rectangle but outside the circles is the area of the rectangle minus the area of all three of the quarter circles in the rectangle.
The area of the rectangle is $3\cdot5 =15$ . The area of all 3 quarter circles is $\frac{\pi}{4}+\frac{\pi(2)^2}{4}+\frac{\pi(3)^2}{4} = \frac{14\pi}{4} = \frac{7\pi}{2}$ . Therefore the area in the rectangle but outside the circles is $15-\frac{7\pi}{2}$ . $\pi$ is approximately $\dfrac{22}{7},$ and substituting that in will give $15-11=\boxed{\text{(B) }4.0}$

## Video Solution
https://youtu.be/e4gDE2uLQ6A ~DSA_Catachu
https://youtu.be/EPILwH5iA9Q ~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=2327
~ pi_is_3.14
### See Also