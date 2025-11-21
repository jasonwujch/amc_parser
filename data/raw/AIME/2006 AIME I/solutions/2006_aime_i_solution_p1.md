# 2006 AIME I Problem 1

## Problem

In quadrilateral $ABCD$

## Solution 1
We construct the following diagram: [asy] pathpen = black; pair C=(0,0),D=(0,-14),A=(-sqrt(765),0),B=IP(circle(C,21),circle(A,18)); D(MP("A",A,W)--MP("B",B,N)--MP("C",C,E)--MP("D",D,E)--A--C); D(rightanglemark(A,C,D,40)); D(rightanglemark(A,B,C,40)); [/asy] Using the Pythagorean Theorem , we get the following two equations: \[AD^2 = AC^2 + CD^2\] \[AC^2 = AB^2 + BC^2\] Substituting $AB^2 + BC^2$ for $AC^2$ gives us $AD^2 = AB^2 + BC^2 + CD^2$ . Plugging in the given information, we get $AD^2 = 18^2 + 21^2 + 14^2 = 961 \implies AD = 31$ , so the perimeter is $AB+BC+CD+AD = 18+21+14+31 = \boxed{84}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.