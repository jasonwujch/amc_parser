# 2016 AMC 10B Problem 14

## Problem

How many squares whose sides are parallel to the axes and whose vertices have coordinates that are integers lie entirely within the region bounded by the line $y=\pi x$ , the line $y=-0.1$ and the line $x=5.1?$

$\textbf{(A)}\ 30 \qquad \textbf{(B)}\ 41 \qquad \textbf{(C)}\ 45 \qquad \textbf{(D)}\ 50 \qquad \textbf{(E)}\ 57$

## Solution 1
The region is a right triangle which contains the following lattice points: $(0,0); (1,0)\rightarrow(1,3); (2,0)\rightarrow(2,6); (3,0)\rightarrow(3,9); (4,0)\rightarrow(4,12); (5,0)\rightarrow(5,15)$
[asy]size(10cm); for(int i=0;i<6;++i)for(int j=0;j<=3*i;++j)dot((i,j)); draw((0,-1)--(0,16),EndArrow);draw((-1,0)--(6,0),EndArrow); draw((-.5,-pi/2)--(5.2,5.2*pi),gray);draw((-1,-.1)--(6,-.1)^^(5.1,-1)--(5.1,16),gray); [/asy]
Squares $1\times 1$ : Suppose that the top-right corner is $(x,y)$ , with $2\le x\le 5$ . Then to include all other corners, we need $1\le y\le 3(x-1)$ . This produces $3+6+9+12=30$ squares.
Squares $2\times 2$ : Here $3\le x\le 5$ . To include all other corners, we need $2\le y\le 3(x-2)$ . This produces $2+5+8=15$ squares.
Squares $3\times 3$ : Similarly, this produces $5$ squares.
No other squares will fit in the region. Therefore the answer is $\boxed{\textbf{(D) }50}$ .

## Solution 2
(While not needed for this solution, rather, for reference, the lines given in the problem are in light blue and the triangle formed by these lines under the x interval $0 \le x \le 5$ are colored in red)
We understand that $\pi > 3$ , therefore, all other vertices of the square can lie at most on the line $y = 3x$ .
We also see that $-0.1 < 0$ , so the vertices of the square can lie at least on the line $y = 0$ .
Finally, we see that $5.1 > 5$ , so the vertices of the square can lie at most on the line $x = 5$ .
Drawing these 3 lines (displayed in the image above as dark blue), we see a triangle of height 15 and base length 5. This triangle, for simplicity, denote it as AMC, has area $\frac{1}{2} \cdot 5 \cdot 15 = \frac{75}{2}$ .
From here, we can do one of two things.
A. Algebra Bash to see the maximum possible square that fits inside this triangle AMC (shown in above solutions).
B. If you drew your graphs accurately enough, just draw the squares in their optimal configuration (best case).
Doing this (squares are shown on graph), one can see that we can either have squares of length 1, 2, or 3.
To find the number of possible squares, we want to find $\left\lfloor \frac{[AMC]}{[square]} \right\rfloor$ , where $\lfloor x \rfloor$ denotes the greatest integer less than or equal to $x$ and $[x]$ denotes the area of a figure. (In simpler terms, we want the floor function $\lfloor x \rfloor$ of the area of triangle AMC divided by the area of a square, which is either side length 1, 2, or 3).
For the $1x1$ square, we have $\left\lfloor \frac{37.5}{1} \right\rfloor = 37$ .
For the $2x2$ square, we have $\left\lfloor \frac{37.5}{4} \right\rfloor = 9$ .
For the $3x3$ square, we have $\left\lfloor \frac{37.5}{9} \right\rfloor = 4$ .
There are $37 + 9 + 4 =$ $\boxed{\textbf{(D)}\ 50}$ squares that satisfy the conditions.
~Pinotation
~Diagram by Pinotation

## Solution 3
The vertical line is just to the right of $x = 5$ , the horizontal line is just under $y = 0$ , and the sloped line will always be above the $y$ value of $3x$ . This means they will always miss being on a coordinate with integer coordinates so you just have to count the number of squares to the left, above, and under these lines. After counting the number of $1\cdot1$ , $2\cdot2$ , and $3\cdot3$ squares and getting $30$ , $15$ , and $5$ respectively, and we end up with $\boxed{\textbf{(D)}\ 50}$ .
Solution by Wwang

## Solution 4
The endpoint lattice points are $(1,3), (2,6), (3,9), (4,12), (5,15).$ Now we split this problem into cases.
Case 1: Square has length .
The $x$ coordinates must be $(1,2)$ or $(2,3)$ and so on to $(4,5).$ The idea is that you start at $y=1$ and add at the endpoint, namely $y=3.$ The number ends up being $3+6+9+12 = 30$ squares for this case.
Case 2: Square has length .
The $x$ coordinates must be $(1,3)$ or $(2,4)$ or $(3,15)$ and so now it starts at $y=2.$ It ends up being $2+5+8 = 15.$
Case 3: Square has length .
The $x$ coordinates must be $(1,4)$ or $(2,5)$ so there is $1+4 = 5$ squares for this case.
Therefore, $30+15+5 = \boxed{\textbf{(D)}\ 50}$ .

## Video Solution
Video Solution by Ryan Yang ~pixelpyguy
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .