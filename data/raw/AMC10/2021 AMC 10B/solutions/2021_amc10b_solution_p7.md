# 2021 AMC 10B Problem 7

## Problem

In a plane, four circles with radii $1,3,5,$ and $7$ are tangent to line $\ell$ at the same point $A,$ but they may be on either side of $\ell$ . Region $S$ consists of all the points that lie inside exactly one of the four circles. What is the maximum possible area of region $S$ ?

$\textbf{(A) }24\pi \qquad \textbf{(B) }32\pi \qquad \textbf{(C) }64\pi \qquad \textbf{(D) }65\pi \qquad \textbf{(E) }84\pi$

## Solution
Suppose that line $\ell$ is horizontal, and each circle lies either north or south to $\ell.$ We construct the circles one by one:
1. Without the loss of generality, we draw the circle with radius $7$ north to $\ell.$
1. To maximize the area of region $S,$ we draw the circle with radius $5$ south to $\ell.$
1. Now, we need to subtract the circle with radius $3$ at least . The optimal situation is that the circle with radius $3$ encompasses the circle with radius $1,$ in which we do not need to subtract more. That is, the two smallest circles are on the same side of $\ell,$ but can be on either side.
The diagram below shows one possible configuration of the four circles: [asy] /* diagram made by samrocksnature, edited by MRENTHUSIASM */ pair A=(10,0); pair B=(-10,0); draw(A--B); filldraw(circle((0,7),7),yellow); filldraw(circle((0,-5),5),yellow); filldraw(circle((0,-3),3),white); filldraw(circle((0,-1),1),white); dot((0,0)); label("$A$",(0,0),(0,1.5)); label("$\ell$",(10,0),(1.5,0)); [/asy] Together, the answer is $\pi\cdot7^2+\pi\cdot5^2-\pi\cdot3^2=\boxed{\textbf{(D) }65\pi}.$
~samrocksnature ~MRENTHUSIASM

## Video Solution by OmegaLearn (Area of Circles and Logic)
https://youtu.be/yPIFmrJvUxM
~ pi_is_3.14

## Video Solution by TheBeautyofMath
https://youtu.be/GYpAm8v1h-U?t=206
~IceMatrix

## Video Solution by Interstigation
https://youtu.be/DvpN56Ob6Zw?t=555
~Interstigation

## Video Solution
https://youtu.be/3jC_yOKA7xE
~Education, the Study of Everything
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .