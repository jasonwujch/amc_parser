# 2011 AMC 8 Problem 19

## Problem

How many rectangles are in this figure?

[asy] pair A,B,C,D,E,F,G,H,I,J,K,L; A=(0,0); B=(20,0); C=(20,20); D=(0,20); draw(A--B--C--D--cycle); E=(-10,-5); F=(13,-5); G=(13,5); H=(-10,5); draw(E--F--G--H--cycle); I=(10,-20); J=(18,-20); K=(18,13); L=(10,13); draw(I--J--K--L--cycle);[/asy]

$\textbf{(A)}\ 8\qquad\textbf{(B)}\ 9\qquad\textbf{(C)}\ 10\qquad\textbf{(D)}\ 11\qquad\textbf{(E)}\ 12$

## Solution 1 (Splitting It Up)
The figure can be divided into $7$ sections. The number of rectangles with just one section is $3.$ The number of rectangles with two sections is $5.$ There are none with only three sections. The number of rectangles with four sections is $3.$
$3+5+3=\boxed{\textbf{(D)}\ 11}$

## Solution 2 (Count by Reduction)
We can remove the 3 big blocks of rectangles one by one. 7 (left) + 3 (bottom) + 1 = 11 are removed in total.
~aliciawu

## Video Solution by WhyMath
https://youtu.be/IEeJsGh3ltk
### See Also