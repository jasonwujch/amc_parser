# 2000 AMC 8 Problem 8

## Problem

Three dice with faces numbered $1$ through $6$ are stacked as shown. Seven of the eighteen faces are visible, leaving eleven faces hidden (back, bottom, between). The total number of dots NOT visible in this view is

[asy] draw((0,0)--(2,0)--(3,1)--(3,7)--(1,7)--(0,6)--cycle); draw((3,7)--(2,6)--(0,6)); draw((3,5)--(2,4)--(0,4)); draw((3,3)--(2,2)--(0,2)); draw((2,0)--(2,6)); dot((1,1)); dot((.5,.5)); dot((1.5,.5)); dot((1.5,1.5)); dot((.5,1.5)); dot((2.5,1.5)); dot((.5,2.5)); dot((1.5,2.5)); dot((1.5,3.5)); dot((.5,3.5)); dot((2.25,2.75)); dot((2.5,3)); dot((2.75,3.25)); dot((2.25,3.75)); dot((2.5,4)); dot((2.75,4.25)); dot((.5,5.5)); dot((1.5,4.5)); dot((2.25,4.75)); dot((2.5,5.5)); dot((2.75,6.25)); dot((1.5,6.5)); [/asy]

$\text{(A)}\ 21 \qquad \text{(B)}\ 22 \qquad \text{(C)}\ 31 \qquad \text{(D)}\ 41 \qquad \text{(E)}\ 53$

## Solution
The numbers on one die total $1+2+3+4+5+6 = 21$ , so the numbers on the three dice total $63$ . Numbers $1, 1, 2, 3, 4, 5, 6$ are visible, and these total $22$ . This leaves $63 - 22 = \boxed{\text{(D) 41}}$ not seen.
### See Also