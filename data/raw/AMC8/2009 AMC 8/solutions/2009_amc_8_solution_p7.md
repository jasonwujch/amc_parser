# 2009 AMC 8 Problem 7

## Problem

The triangular plot of ACD lies between Aspen Road, Brown Road and a railroad. Main Street runs east and west, and the railroad runs north and south. The numbers in the diagram indicate distances in miles. The width of the railroad track can be ignored. How many square miles are in the plot of land ACD?

[asy] size(250); defaultpen(linewidth(0.55)); pair A=(-6,0), B=origin, C=(0,6), D=(0,12); pair ac=C+2.828*dir(45), ca=A+2.828*dir(225), ad=D+2.828*dir(A--D), da=A+2.828*dir(D--A), ab=(2.828,0), ba=(-6-2.828, 0); fill(A--C--D--cycle, gray); draw(ba--ab); draw(ac--ca); draw(ad--da); draw((0,-1)--(0,15)); draw((1/3, -1)--(1/3, 15)); int i; for(i=1; i<15; i=i+1) { draw((-1/10, i)--(13/30, i)); } label("$A$", A, SE); label("$B$", B, SE); label("$C$", C, SE); label("$D$", D, SE); label("$3$", (1/3,3), E); label("$3$", (1/3,9), E); label("$3$", (-3,0), S); label("Main", (-3,0), N); label(rotate(45)*"Aspen", A--C, SE); label(rotate(63.43494882)*"Brown", A--D, NW); [/asy]

$\textbf{(A)}\ 2\qquad \textbf{(B)}\ 3 \qquad \textbf{(C)}\ 4.5 \qquad \textbf{(D)}\ 6 \qquad \textbf{(E)}\ 9$

## Solution
The area of a triangle is $\frac12 bh$ . If we let $CD$ be the base of the triangle, then the height is $AB$ , and the area is $\frac12 \cdot 3 \cdot 3 = \boxed{\textbf{(C)}\ 4.5}$ .

## Solution 2
We can see that there is a big triangle encasing $ACD$ . The area of that triangle is $\frac12 \cdot 3 \cdot 6 = 9$ . We can easily see that triangle $ABC$ is $\frac12 \cdot 3 \cdot 3$ , which is $4.5$ . $9-4.5$ is $4.5$ , so the answer is $\boxed{\textbf{(C)}\ 4.5}$ .

## Video Solution
https://www.youtube.com/watch?v=Opz71P5o4uI ~David

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=158
~ pi_is_3.14

## Video Solution by WhyMath
https://youtu.be/QfQIqS60m5s
~savannahsolver
### See Also