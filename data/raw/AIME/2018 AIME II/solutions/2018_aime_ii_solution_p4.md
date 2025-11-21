# 2018 AIME II Problem 4

## Problem

In equiangular octagon $CAROLINE$ , $CA = RO = LI = NE =$ $\sqrt{2}$ and $AR = OL = IN = EC = 1$ . The self-intersecting octagon $CORNELIA$ encloses six non-overlapping triangular regions. Let $K$ be the area enclosed by $CORNELIA$ , that is, the total area of the six triangular regions. Then $K =$ $\dfrac{a}{b}$ , where $a$ and $b$ are relatively prime positive integers. Find $a + b$ .

## Solution
We can draw $CORNELIA$ and introduce some points.
The diagram is essentially a 3x3 grid where each of the 9 squares making up the grid have a side length of 1.
In order to find the area of $CORNELIA$ , we need to find 4 times the area of $\bigtriangleup$ $ACY$ and 2 times the area of $\bigtriangleup$ $YZW$ .
Using similar triangles $\bigtriangleup$ $ARW$ and $\bigtriangleup$ $YZW$ (We look at their heights), $YZ$ $=$ $\frac{1}{3}$ . Therefore, the area of $\bigtriangleup$ $YZW$ is $\frac{1}{3}\cdot\frac{1}{2}\cdot\frac{1}{2}$ $=$ $\frac{1}{12}$
Since $YZ$ $=$ $\frac{1}{3}$ and $XY = ZQ$ , $XY$ $=$ $\frac{1}{3}$ and $CY$ $=$ $\frac{4}{3}$ .
Therefore, the area of $\bigtriangleup$ $ACY$ is $\frac{4}{3}\cdot$ $1$ $\cdot$ $\frac{1}{2}$ $=$ $\frac{2}{3}$
Our final answer is $\frac{1}{12}$ $\cdot$ $2$ $+$ $\frac{2}{3}$ $\cdot$ $4$ $=$ $\frac{17}{6}$
$17 + 6 =$ $\boxed{023}$

## Solution 2
$CAROLINE$ is essentially a plus sign with side length 1 with a few diagonals, which motivates us to coordinate bash. We let $N = (1, 0)$ and $E = (0, 1)$ . To find $CORNELIA$ 's self intersections, we take
\[CO = y = 2, AI = y = -3x + 6, RN = y = 3x - 3\]
And plug them in to get $C_1 = \left(\frac{4}{3}, 2 \right)$ where $C_1$ is the intersection of $CO$ and $AI$ , and $C_2 = \left(\frac{5}{3}, 2 \right)$ is the intersection of $RN$ and $CO$ .
We also track the intersection of $AI$ and $RN$ to get $\left(\frac{3}{2}, \frac{3}{2} \right)$ .
By vertical symmetry, the other 2 points of intersection should have the same x-coordinates. We can then proceed with Solution 1 to calculate the area of the triangle (compare the $y$ -coordinates of $A,R,I,N$ and $CO$ and $EL$ ).
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .