# 2008 AMC 10B Problem 7

## Problem

An equilateral triangle of side length $10$ is completely filled in by non-overlapping equilateral triangles of side length $1$ . How many small triangles are required?

$\mathrm{(A)}\ 10\qquad\mathrm{(B)}\ 25\qquad\mathrm{(C)}\ 100\qquad\mathrm{(D)}\ 250\qquad\mathrm{(E)}\ 1000$

## Solution 1
The area of the large triangle is $\frac{10^2\sqrt3}{4}$ , while the area of each small triangle is $\frac{1^2\sqrt3}{4}$ . Dividing these two quantities results in $100$ , therefore $\boxed{100} \mathrm{(C)}$ small triangles can fill the large one without overlap.

## Solution 2-4
[asy] unitsize(0.5cm); defaultpen(0.8); for (int i=0; i<10; ++i) { draw( (i*dir(60)) -- ( (10,0) + (i*dir(120)) ) ); } for (int i=0; i<10; ++i) { draw( (i*dir(0)) -- ( 10*dir(60) + (i*dir(-60)) ) ); } for (int i=0; i<10; ++i) { draw( ((10-i)*dir(60)) -- ((10-i)*dir(0)) ); } [/asy]
The number of triangles is $1+3+\dots+19 = \boxed{100}$ .
Also, another way to do it is to notice that as you go row by row (from the bottom), the number of triangles decrease by 2 from 19, so we have: $19+17+15...+3+1 = \frac{19+1}{2}\cdot 10 = \boxed{100}$
A fourth solution is to notice that the small triangles are similar to the large triangle as they are both equilateral. Therefore, the ratio of their areas is the square of the ratio of their side lengths. Hence the ratio of their areas is $(1/10)^2=1/100$ , so the answer is $\boxed{100}$ .

## Solution 5
The side length of the large equilateral triangle is $10$ . The number of equilateral triangles with side length $1$ that can fill it is $10^2$ . This is equal to the sum of the first $10$ odd integers. The sum of the first $n$ odd integers is $n^2$ . In general, an equilateral triangle with side length $n$ can be filled by $n^2$ triangles. The answer is $100\ \mathrm{(C)}$ .
~mobius247
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .