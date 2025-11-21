# 2004 AMC 10B Problem 16

## Problem

Three circles of radius $1$ are externally tangent to each other and internally tangent to a larger circle. What is the radius of the large circle?

$\mathrm{(A) \ } \frac{2 + \sqrt{6}}{3} \qquad \mathrm{(B) \ } 2 \qquad \mathrm{(C) \ } \frac{2 + 3\sqrt{2}}{2} \qquad \mathrm{(D) \ } \frac{3 + 2\sqrt{3}}{3} \qquad \mathrm{(E) \ } \frac{3 + \sqrt{3}}{2}$

## Solution 1
The situation is shown in the picture below. The radius we seek is $SD = AD + AS$ . Clearly $AD=1$ . The point $S$ is the center of the equilateral triangle $ABC$ , thus $AS$ is $2/3$ of the altitude of this triangle. We get that $AS = \frac23 \cdot \sqrt 3$ . Therefore the radius we seek is $1 + \frac23 \cdot \sqrt 3 = \boxed{\mathrm{(D)\ }\frac{3+2\sqrt{3}}3}$ .
[asy] unitsize(2cm); pair A=(0,0), B=dir(0)*2, C=dir(60)*2; draw(circle(A,1)); draw(circle(B,1)); draw(circle(C,1)); dot(A); dot(B); dot(C); draw(A--B--C--cycle); pair D=A+dir(210), E=B+dir(-30), F=C+dir(90); draw(circumcircle(D,E,F)); dot(D); dot(E); dot(F); pair S=(A+B+C)/3; dot(S); draw(S--D); draw(S--E); draw(S--F); label("$S$",S,S); label("$A$",A,SE); label("$D$",D,SW); label("$B$",B,NE); label("$C$",C,ENE); [/asy]

## Solution 2
Using Descartes' Circle Formula , we can assign curvatures to all the circles: $1$ , $1$ , $1$ , and $-\frac{1}{r}$ (b/c the bigger circle is externally tangent to all the other circles, the radius of the bigger circle is negative). Then, we can solve:
$2(1^2+1^2+1^2+(-\frac{1}{r})^2) = (1+1+1-\frac{1}{r})^2$
$r = \boxed{\mathrm{(D)\ }\frac{3+2\sqrt{3}}3}$
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .