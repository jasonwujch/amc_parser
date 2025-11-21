# 2000 AMC 8 Problem 24

## Problem

If $\angle A = 20^\circ$ and $\angle AFG =\angle AGF$ , then $\angle B+\angle D =$

[asy] pair A,B,C,D,EE,F,G; A = (0,0); B = (9,4); C = (21,0); D = (13,-12); EE = (4,-16); F = (13/2,-6); G = (8,0); draw(A--C--EE--B--D--cycle); label("$A$",A,W); label("$B$",B,N); label("$C$",C,E); label("$D$",D,SE); label("$E$",EE,SW); label("$F$",F,WSW); label("$G$",G,NW);[/asy]

$\text{(A)}\ 48^\circ\qquad\text{(B)}\ 60^\circ\qquad\text{(C)}\ 72^\circ\qquad\text{(D)}\ 80^\circ\qquad\text{(E)}\ 90^\circ$

## Solution
As a strategy, think of how $\angle B + \angle D$ would be determined, particularly without determining either of the angles individually, since it may not be possible to determine $\angle B$ or $\angle D$ alone. If you see $\triangle BFD$ , then you can see that the problem is solved quickly after determining $\angle BFD$ .
But start with $\triangle AGF$ , since that's where most of our information is. Looking at $\triangle AGF$ , since $\angle AFG = \angle AGF$ , and $\angle A = 20$ , we can write:
$\angle A + \angle AFG + \angle AGF = 180$
$20 + 2\angle AFG = 180$
$\angle AFG = 80$
By noting that $\angle AFG$ and $\angle GFD$ make a straight line, we know
$\angle AFG + \angle GFD = 180$
$80 + \angle GFD = 180$
$\angle GFD = 100$
Ignoring all other parts of the figure and looking only at $\triangle BFD$ , you see that $\angle B + \angle D + \angle BFD = 180$ . But $\angle BFD$ is the same as $\angle GFD$ . Therefore:
$\angle B + \angle D + \angle GFD = 180$
$\angle B + \angle D + 100 = 180$
$\angle B + \angle D = 80^\circ$ , and the answer is thus $\boxed{D}$

## Video Solution
https://www.youtube.com/watch?v=8ntXubG2Iho ~David
### See Also