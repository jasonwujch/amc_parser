# 2007 AMC 10A Problem 15

## Problem

Four circles of radius $1$ are each tangent to two sides of a square and externally tangent to a circle of radius $2$ , as shown. What is the area of the square?

[asy] unitsize(5mm); defaultpen(linewidth(.8pt)+fontsize(8pt)); real h=3*sqrt(2)/2; pair O0=(0,0), O1=(h,h), O2=(-h,h), O3=(-h,-h), O4=(h,-h); pair X=O0+2*dir(30), Y=O2+dir(45); draw((-h-1,-h-1)--(-h-1,h+1)--(h+1,h+1)--(h+1,-h-1)--cycle); draw(Circle(O0,2)); draw(Circle(O1,1)); draw(Circle(O2,1)); draw(Circle(O3,1)); draw(Circle(O4,1)); draw(O0--X); draw(O2--Y); label("$2$",midpoint(O0--X),NW); label("$1$",midpoint(O2--Y),SE); [/asy]

$\text{(A)}\ 32 \qquad \text{(B)}\ 22 + 12\sqrt {2}\qquad \text{(C)}\ 16 + 16\sqrt {3}\qquad \text{(D)}\ 48 \qquad \text{(E)}\ 36 + 16\sqrt {2}$

## Solution 1
Draw a square connecting the centers of the four small circles of radius $1$ . This square has a diagonal of length $6$ , as it includes the diameter of the big circle of radius $2$ and two radii of the small circles of radius $1$ . Therefore, the side length of this square is \[\frac{6}{\sqrt{2}} = 3\sqrt{2}.\] The side length of the larger square is $2$ units greater than the one found by connecting the midpoints, so its side length is \[2 + 3\sqrt{2}.\] The area of the larger square is $(2+3\sqrt{2})^2 = 22 + 12\sqrt{2}$ $(B).$

## Solution 2
We draw the diagonal of the square. This diagonal yields $2\sqrt{2}+1+1+2+2=2\sqrt{2}+6$ . We know that the side length $s$ in terms of the diagonal $d$ is $s=\frac{d}{\sqrt{2}}$ , so our side length is $\frac{2\sqrt{2}+6}{\sqrt{2}}$ . However, we are trying to look for the area, so squaring $\frac{2\sqrt{2}+6}{\sqrt{2}}$ yields $\frac{44+24\sqrt{2}}{2}=\boxed{\text{(B)}22+12\sqrt{2}}$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .