# 2000 AMC 8 Problem 6

## Problem

Figure $ABCD$ is a square. Inside this square three smaller squares are drawn with the side lengths as labeled. The area of the shaded $L$ -shaped region is

[asy] pair A,B,C,D; A = (5,5); B = (5,0); C = (0,0); D = (0,5); fill((0,0)--(0,4)--(1,4)--(1,1)--(4,1)--(4,0)--cycle,gray); draw(A--B--C--D--cycle); draw((4,0)--(4,4)--(0,4)); draw((1,5)--(1,1)--(5,1)); label("$A$",A,NE); label("$B$",B,SE); label("$C$",C,SW); label("$D$",D,NW); label("$1$",(1,4.5),E); label("$1$",(0.5,5),N); label("$3$",(1,2.5),E); label("$3$",(2.5,1),N); label("$1$",(4,0.5),E); label("$1$",(4.5,1),N); [/asy]

$\text{(A)}\ 7 \qquad \text{(B)}\ 10 \qquad \text{(C)}\ 12.5 \qquad \text{(D)}\ 14 \qquad \text{(E)}\ 15$

## Solution 1
The side of the large square is $1 + 3 + 1 = 5$ , so the area of the large square is $5^2 = 25$ .
The area of the middle square is $3^2$ , and the sum of the areas of the two smaller squares is $2 * 1^2 = 2$ .
Thus, the big square minus the three smaller squares is $25 - 9 - 2 = 14$ . This is the area of the two congruent L-shaped regions.
So the area of one L-shaped region is $\frac{14}{2} = 7$ , and the answer is $\boxed{A}$

## Solution 2
The shaded area can be divided into two regions: one rectangle that is 1 by 3, and one rectangle that is 4 by 1. (Or the reverse, depending on which rectangle the 1 by 1 square is "joined" to.) Either way, the total area of these two regions is $3 + 4 = 7$ , and the answer is $\boxed{A}$ .

## Solution 3
Chop the entire 5 by 5 region into $25$ squares like a piece of graph paper. When you draw all the lines, you can count that only $7$ of the small 1 by 1 squares will be shaded, giving $\boxed{A}$ as the answer.

## Solution 4
In the bottom left corner of the 5 by 5 square there is a 4 by 4 square which has an area of $4\cdot4=16$ . In the top right of that 4 by 4 square is a 3 by 3 square with an area of $3\cdot3=9$ . When we remove the 3 by 3 square from the 4 by 4 square we get the L-shaped figure so our answer is $16-9=\boxed{\text{(A)}\ 7}$
### See Also