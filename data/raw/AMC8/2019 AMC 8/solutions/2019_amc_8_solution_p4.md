# 2019 AMC 8 Problem 4

## Problem

Quadrilateral $ABCD$ is a rhombus with perimeter $52$ meters. The length of diagonal $\overline{AC}$ is $24$ meters. What is the area in square meters of rhombus $ABCD$ ?

[asy] draw((-13,0)--(0,5)); draw((0,5)--(13,0)); draw((13,0)--(0,-5)); draw((0,-5)--(-13,0)); dot((-13,0)); dot((0,5)); dot((13,0)); dot((0,-5)); label("A",(-13,0),W); label("B",(0,5),N); label("C",(13,0),E); label("D",(0,-5),S); [/asy]

$\textbf{(A) }60\qquad\textbf{(B) }90\qquad\textbf{(C) }105\qquad\textbf{(D) }120\qquad\textbf{(E) }144$

## Solution 1
[asy] draw((-12,0)--(0,5)); draw((0,5)--(12,0)); draw((12,0)--(0,-5)); draw((0,-5)--(-12,0)); draw((0,0)--(12,0)); draw((0,0)--(0,5)); draw((0,0)--(-12,0)); draw((0,0)--(0,-5)); dot((-12,0)); dot((0,5)); dot((12,0)); dot((0,-5)); label("A",(-12,0),W); label("B",(0,5),N); label("C",(12,0),E); label("D",(0,-5),S); label("E",(0,0),SW); [/asy]
A rhombus has sides of equal length. Because the perimeter of the rhombus is $52$ , each side is $\frac{52}{4}=13$ . In a rhombus, diagonals are perpendicular and bisect each other, which means $\overline{AE}$ = $12$ = $\overline{EC}$ .
Consider one of the
[asy] draw((-12,0)--(0,5)); draw((0,0)--(-12,0)); draw((0,0)--(0,5)); dot((-12,0)); dot((0,5)); label("A",(-12,0),W); label("B",(0,5),N); label("E",(0,0),SE); [/asy]
$\overline{AB}$ = $13$ , and $\overline{AE}$ = $12$ . Using the Pythagorean theorem, we find that $\overline{BE}$ = $5$ . You know the Pythagorean triple, (5, 12, 13).
Thus the values of the two diagonals are $\overline{AC}$ = $24$ and $\overline{BD}$ = $10$ . The area of a rhombus is = $\frac{d_1\cdot{d_2}}{2}$ = $\frac{24\cdot{10}}{2}$ = $120$
$\boxed{\textbf{(D)}\ 120}$

## Solution 2
Right off the bat, we can see that the perimeter of the figure is 52. Dividing this by four, we can get that each side is equal to 13. By drawing a line perpendicular to the one given, we can split the figure into four right triangles. 12 (24/2) is equal to the height of one small right triangle, and 13 is the slanted side. Using the Pythagorean theorem we can find that 169 (13 squared) - 144 (12 squared) = 25 (five squared). With this, we can determine that each small right triangle equals 30. Multiplying that by four we can get $\boxed{\textbf{(D)}\ 120}$ ~math4all

## Video Solutions

## Video Solution 1 (Detailed Explanation)
https://youtu.be/nbcPvG024_o
~ChillGuyDoesMath

## Video Solution 2 by Math-X (First fully understand the problem)
https://youtu.be/IgpayYB48C4?si=CGr1gRwXKdjrhl24&t=678
~Math-X

## Video Solution 3
The Learning Royal: https://youtu.be/IiFFDDITE6Q

## Video Solution 4
https://www.youtube.com/watch?v=-yHfOUapg7I&list=PLbhMrFqoXXwmwbk2CWeYOYPRbGtmdPUhL&index=5

## Video Solution 5
https://youtu.be/mL6gIb5y3B0
~savannahsolver

## Video Solution 6 (CREATIVE THINKING)
https://youtu.be/UCaEXbe7mN0
~Education, the Study of Everything

## Video Solution 7 by The Power of Logic(1 to 25 Full Solution)
https://youtu.be/Xm4ZGND9WoY
~Hayabusa1