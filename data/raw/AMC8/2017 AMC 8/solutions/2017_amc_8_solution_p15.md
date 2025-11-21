# 2017 AMC 8 Problem 15

## Problem

In the arrangement of letters and numerals below, by how many different paths can one spell AMC8? Beginning at the A in the middle, a path only allows moves from one letter to an adjacent (above, below, left, or right, but not diagonal) letter. One example of such a path is traced in the picture.

[asy] fill((0.5, 4.5)--(1.5,4.5)--(1.5,2.5)--(0.5,2.5)--cycle,lightgray); fill((1.5,3.5)--(2.5,3.5)--(2.5,1.5)--(1.5,1.5)--cycle,lightgray); label("$8$", (1, 0)); label("$C$", (2, 0)); label("$8$", (3, 0)); label("$8$", (0, 1)); label("$C$", (1, 1)); label("$M$", (2, 1)); label("$C$", (3, 1)); label("$8$", (4, 1)); label("$C$", (0, 2)); label("$M$", (1, 2)); label("$A$", (2, 2)); label("$M$", (3, 2)); label("$C$", (4, 2)); label("$8$", (0, 3)); label("$C$", (1, 3)); label("$M$", (2, 3)); label("$C$", (3, 3)); label("$8$", (4, 3)); label("$8$", (1, 4)); label("$C$", (2, 4)); label("$8$", (3, 4));[/asy]

$\textbf{(A) }8\qquad\textbf{(B) }9\qquad\textbf{(C) }12\qquad\textbf{(D) }24\qquad\textbf{(E) }36$

## Solution 1 (Not Very Efficient)
Notice that the upper-most section contains a 3 by 3 square that looks like:
[asy]label("$8$", (1, 2)); label("$C$", (2, 2)); label("$8$", (3, 2)); label("$C$", (1, 1)); label("$M$", (2, 1)); label("$C$", (3, 1)); label("$M$", (1, 0)); label("$A$", (2, 0)); label("$M$", (3, 0));[/asy]
It has 6 paths in which you can spell out AMC8. You will find four identical copies of this square in the figure, so multiply ${6 \cdot 4}$ to get $\boxed{\textbf{(D)}\ 24}$ total paths.

## Solution 2
There are three different kinds of paths that are on this diagram. The first kind is when you directly count $A$ , $M$ , $C$ in a straight line. The second is when you count $A$ , turn left or right to get $M$ , then go up or down to count $8$ and $C$ . The third is the one where you start with $A$ , move up or down to count $M$ , turn left or right to count $C$ , then move straight again to get $8$ .
There are 8 paths for each kind of path, making for $8 \cdot 3=\boxed{\textbf{(D)}\ 24}$ paths.

## Solution 3 (easy and recommended)
Notice that the $A$ is adjacent to $4$ $M$ s, each $M$ is adjacent to $3$ $C$ s, and each $C$ is adjacent to $2$ $8$ 's. So for each $A$ , there are $4$ $M$ s, and for each $M$ , there are $3$ $C$ s, and for each $C$ , there are $2$ $8$ s. Thus, the answer is $1\cdot 4\cdot 3\cdot 2 = \boxed{\textbf{(D)}\ 24}.$

## Solution 4
We can do this problem by computing how many ways there are to get to each letter (in order). There is $1$ way to get to the $A$ in the center. We can only get to each of the other $M$ s by going there from the $A$ , so there is $1$ way to get to each of the four $M$ s. For the $C$ s, we notice that four $C$ s are surrounded by one $M$ , and four $C$ s are surrounded by two $M$ s. Finally, each of the $8$ s is surrounded by one $C$ with one way to get there and one $C$ with two ways to get there. Therefore, there are three paths to any of the $8$ s. Since there are eight $8$ s, the answer is $3 \cdot 8 = \boxed{\textbf{(D)}\ 24}.$

## Video Solution (CREATIVE THINKING + ANALYSIS!!!)
https://youtu.be/oWMU6ph6LBM
~Education, the Study of Everything

## Video Solution
https://youtu.be/GIo37KUPQ5o
https://youtu.be/CTnICuhvbAk
~savannahsolver
### See Also