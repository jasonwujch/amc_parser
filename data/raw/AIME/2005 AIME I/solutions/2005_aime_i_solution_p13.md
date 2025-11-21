# 2005 AIME I Problem 13

## Problem

A particle moves in the Cartesian plane according to the following rules:

1. From any lattice point $(a,b),$ the particle may only move to $(a+1,b), (a,b+1),$ or $(a+1,b+1).$

1. There are no right angle turns in the particle's path.

How many different paths can the particle take from $(0,0)$ to $(5,5)$ ?

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

## Solution

## Solution 1
The length of the path (the number of times the particle moves) can range from $l = 5$ to $9$ ; notice that $d = 10-l$ gives the number of diagonals. Let $R$ represent a move to the right, $U$ represent a move upwards, and $D$ to be a move that is diagonal. Casework upon the number of diagonal moves:
- Case $d = 1$ : It is easy to see only $2$ cases.
- Case $d = 2$ : There are two diagonals. We need to generate a string with $3$ $R$ 's, $3$ $U$ 's, and $2$ $D$ 's such that no two $R$ 's or $U$ 's are adjacent. The $D$ 's split the string into three sections ( $-D-D-$ ): by the Pigeonhole principle all of at least one of the two letters must be all together (i.e., stay in a row).
- Case $d = 3$ : Now $2$ $R$ 's, $2$ $U$ 's, and $3$ $D$ 's, so the string is divided into $4$ partitions ( $-D-D-D-$ ).
- Case $d = 4$ : Now $1$ $R$ , $1$ $U$ , $4$ $D$ 's ( $-D-D-D-D-$ ). There are $5$ places to put $R$ , $4$ places to put $U$ , giving $20$ ways.
- Case $d = 5$ : It is easy to see only $1$ case.
Together, these add up to $2 + 18 + 42 + 20 + 1 = \boxed{083}$ .

## Solution 2
Another possibility is to use block-walking and recursion : for each vertex, the number of ways to reach it is $a + b + c$ , where $a$ is the number of ways to reach the vertex from the left (without having come to that vertex (the one on the left) from below), $b$ is the number of ways to reach the vertex from the vertex diagonally down and left, and $c$ is the number of ways to reach the vertex from below (without having come to that vertex (the one below) from the left).
Assign to each point $(i,j)$ the triplet $(a_{i,j}, b_{i,j}, c_{i,j})$ . Let $s(i,j) = a_{i,j}+ b_{i,j}+ c_{i,j}$ . Let all lattice points that contain exactly one negative coordinate be assigned to $(0,0,0)$ . This leaves the lattice points of the first quadrant, the positive parts of the $x$ and $y$ axes, and the origin unassigned. As a seed, assign to $(0,1,0)$ . (We will see how this correlates with the problem.) Then define for each lattice point $(i,j)$ its triplet thus: \begin{align*} a_{i,j} &= s(i-1,j) - c_{i-1,j}\\ b_{i,j} &= s(i-1,j-1) \\ c_{i,j} &= s(i,j-1) - a_{i,j-1}. \end{align*} It is evident that $s(i,j)$ is the number of ways to reach $(i,j)$ from $(0,0)$ . Therefore we compute vertex by vertex the triplets $(a_{i,j}, b_{i,j}, c_{i,j})$ with $0 \leq i, j \leq 5$ . [asy] defaultpen(fontsize(8)+0.8+heavyblue); size(250); for(int i = 0; i<6; ++i) { draw((0,i)--(5,i)^^(i,0)--(i,5), gray+0.25); } label("$(0,0,0)$", (0,0), N); for(int i = 1; i<6; ++i) { label("$(0,0,1)$", (0,i), N); label("$(1,0,0)$", (i,0), N); label("$({"+string(i-1)+"},1,0)$", (i,1), N); label("$(0,1,{"+string(i-1)+"})$", (1,i), N);} real[] val={1,2,4,7}; for(int i = 2; i<6; ++i) { label("$(1,{"+string(i-1)+"}, {"+string(val[i-2])+"})$", (2,i), N); label("$({"+string(val[i-2])+"},{"+string(i-1)+"}, 1)$", (i,2), N);} label("$(3,3,3)$", (3,3), N); label("$(9,9,9)$", (4,4), N); label("$(28,27,28)$", (5,5), N); label("$(4,5,6)$", (3,4), N); label("$(6,5,4)$", (4,3), N); label("$(5,8,11)$", (3,5), N); label("$(11,8,5)$", (5,3), N); label("$(13,15,18)$", (4,5), N); label("$(18,15,13)$", (5,4), N); [/asy] Finally, after simple but tedious calculations, we find that $(a_{5,5}, b_{5,5}, c_{5,5}) = (28,27,28)$ , so $s(i,j)=28+27+28 = \boxed{083}$ .
These problems are copyrighted © by the Mathematical Association of America.