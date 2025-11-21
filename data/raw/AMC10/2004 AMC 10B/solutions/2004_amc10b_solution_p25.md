# 2004 AMC 10B Problem 25

## Problem

A circle of radius $1$ is internally tangent to two circles of radius $2$ at points $A$ and $B$ , where $AB$ is a diameter of the smaller circle. What is the area of the region, shaded in the picture, that is outside the smaller circle and inside each of the two larger circles?

$\mathrm{(A) \ } \frac{5}{3} \pi - 3\sqrt 2 \qquad \mathrm{(B) \ } \frac{5}{3} \pi - 2\sqrt 3 \qquad \mathrm{(C) \ } \frac{8}{3} \pi - 3\sqrt 3 \qquad \mathrm{(D) \ } \frac{8}{3} \pi - 3\sqrt 2 \qquad \mathrm{(E) \ } \frac{8}{3} \pi - 2\sqrt 3$

[asy] unitsize(1cm); defaultpen(0.8); pair O=(0,0), A=(0,1), B=(0,-1); path bigc1 = Circle(A,2), bigc2 = Circle(B,2), smallc = Circle(O,1); pair[] P = intersectionpoints(bigc1, bigc2); filldraw( arc(A,P[0],P[1])--arc(B,P[1],P[0])--cycle, lightgray, black ); draw(bigc1); draw(bigc2); unfill(smallc); draw(smallc); dot(O); dot(A); dot(B); label("$A$",A,N); label("$B$",B,S); draw( O--dir(30) ); draw( A--(A+2*dir(30)) ); draw( B--(B+2*dir(210)) ); label("$1$", O--dir(30), N ); label("$2$", A--(A+2*dir(30)), N ); label("$2$", B--(B+2*dir(210)), S ); [/asy]

## Solution 1
The area of the small circle is $\pi$ . We can add it to the shaded region, compute the area of the new region, and then subtract the area of the small circle from the result.
Let $C$ and $D$ be the intersections of the two large circles. Connect them to $A$ and $B$ to get the picture below:
[asy] unitsize(1.5cm); defaultpen(0.8); pair O=(0,0), A=(0,1), B=(0,-1); path bigc1 = Circle(A,2), bigc2 = Circle(B,2), smallc = Circle(O,1); pair[] P = intersectionpoints(bigc1, bigc2); filldraw( arc(A,P[0],P[1])--arc(B,P[1],P[0])--cycle, lightgray, black ); draw(bigc1); draw(bigc2); dot(A); dot(B); label("$A$",A,N); label("$B$",B,S); /* dot(O); unfill(smallc); draw(smallc); draw( O--dir(30) ); draw( A--(A+2*dir(30)) ); draw( B--(B+2*dir(210)) ); label("$1$", O--dir(30), N ); label("$2$", A--(A+2*dir(30)), N ); label("$2$", B--(B+2*dir(210)), S ); */ label("$C$",P[0],W); label("$D$",P[1],E); draw( P[0]--A--P[1] ); draw( P[0]--B--P[1] ); draw( A--B ); [/asy]
We can see that the triangles $\triangle ABC$ and $\triangle ABD$ are both equilateral with side $2$ .
Take a look at the lower circle. The angle $ABC$ is $60^\circ$ , thus sector $ABC$ is $1/6$ of the circle. The same is true for sector $ABD$ of the lower circle, and sectors $CAB$ and $BAD$ of the upper circle.
If we now sum the areas of these four sectors, we will almost get the area of the new shaded region - except that each of the two equilateral triangles will be counted twice. The area of an equilateral triangle given its side, $s,$ is $\frac{\sqrt3}4s^2.$
Therefore, the area of the new shaded region is $4\cdot \left( \frac 16 \cdot \pi\cdot 2^2 \right) - 2 \cdot \left( 4 \cdot \frac{\sqrt3}4 \right) = \frac 83 \pi - 2\sqrt 3$ . Lastly, we must subtract the area of the circle that we added earlier, $\pi$ , and we get
$\left( \frac 83 \pi - 2\sqrt 3 \right) - \pi = \boxed{\mathrm{(B)\ } \frac 53 \pi - 2\sqrt 3 }$ .

## Solution 2 (Cheap - Out Of Time)
Notice that answer choices (C), (D), and (E) are exactly $\pi$ more than answer choices (A), (B). This suggests that answer choices (C), (D), and (E) are meant to trick you into forgetting to subtract the circle with radius $1$ (area $\pi$ ) From this, (A) or (B) are probably the answer choices (since you do need to subtract $\pi$ at the end!) Since the angle measures of the sectors are $120^{\circ},$ and we are working with the areas of some equilateral triangles, it only makes sense for the answer to have a $\sqrt 3$ and not a $\sqrt 2$ in them (There's no $45^{\circ}$ angle either). So, our answer is $\boxed{\mathrm{(B)\ } \frac 53 \pi - 2\sqrt 3 }$ .
~lpieleanu (minor editing and extra details)
https://www.youtube.com/watch?v=ajApE9bdUJQ
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .