# 1999 AMC 8 Problem 14

## Problem

In trapezoid $ABCD$ , the sides $AB$ and $CD$ are equal. The perimeter of $ABCD$ is

[asy] draw((0,0)--(4,3)--(12,3)--(16,0)--cycle); draw((4,3)--(4,0),dashed); draw((3.2,0)--(3.2,.8)--(4,.8)); label("$A$",(0,0),SW); label("$B$",(4,3),NW); label("$C$",(12,3),NE); label("$D$",(16,0),SE); label("$8$",(8,3),N); label("$16$",(8,0),S); label("$3$",(4,1.5),E); [/asy]

$\text{(A)}\ 27 \qquad \text{(B)}\ 30 \qquad \text{(C)}\ 32 \qquad \text{(D)}\ 34 \qquad \text{(E)}\ 48$

## Solution
[asy] draw((0,0)--(4,3)--(12,3)--(16,0)--cycle); draw((4,3)--(4,0),dashed); draw((12,3)--(12,0),dashed); draw((3.2,0)--(3.2,.8)--(4,.8)); label("$A$",(0,0),SW); label("$B$",(4,3),NW); label("$C$",(12,3),NE); label("$D$",(16,0),SE); label("$8$",(8,3),N); label("$8$",(8,0),S); label("$3$",(4,1.5),E); label("$4$",(2,0),S); label("$4$",(14,0),S); label("$5$",(0,0)--(4,3),NW); label("$5$",(12,3)--(16,0),NE); [/asy]
There is a rectangle present, with both horizontal bases being $8$ units in length. The excess units on the bottom base must then be $16-8=8$ . The fact that $AB$ and $CD$ are equal in length indicate, by the Pythagorean Theorem, that these excess lengths are equal. There are two with a total length of $8$ units, so each is $4$ units. The triangle has a hypotenuse of $5$ , because the triangles are $3-4-5$ right triangles. So, the sides of the trapezoid are $8$ , $5$ , $16$ , and $5$ . Adding those up gives us the perimeter, $8 + 5 + 16 + 5 = 13 + 21 = \boxed{\text{(D)}\ 34}$ units.

## Video Solution
https://youtu.be/DKoTd9S4y-Q Soo, DRMS, NM
### See Also