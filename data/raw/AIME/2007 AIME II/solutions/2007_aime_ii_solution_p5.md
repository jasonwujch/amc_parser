# 2007 AIME II Problem 5

## Problem

The graph of the equation $9x+223y=2007$ is drawn on graph paper with each square representing one unit in each direction. How many of the $1$ by $1$ graph paper squares have interiors lying entirely below the graph and entirely in the first quadrant ?

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4

## Solution

## Solution 1
There are $223 \cdot 9 = 2007$ squares in total formed by the rectangle with edges on the x and y axes and with vertices on the intercepts of the equation, since the intercepts of the lines are $(223,0),\ (0,9)$ .
Count the number of squares that the diagonal of the rectangle passes through. Since the two diagonals of a rectangle are congruent , we can consider instead the diagonal $y = \frac{223}{9}x$ . This passes through 8 horizontal lines ( $y = 1 \ldots 8$ ) and 222 vertical lines ( $x = 1 \ldots 222$ ). Every time we cross a line, we enter a new square. Since 9 and 223 are relatively prime , we don’t have to worry about crossing an intersection of a horizontal and vertical line at one time. We must also account for the first square. This means that it passes through $222 + 8 + 1 = 231$ squares.
The number of non-diagonal squares is $2007 - 231 = 1776$ . Divide this in 2 to get the number of squares in one of the triangles, with the answer being $\frac{1776}2 = 888$ .

## Solution 2
Count the number of each squares in each row of the triangle. The intercepts of the line are $(223,0),\ (0,9)$ .
In the top row, there clearly are no squares that can be formed. In the second row, we see that the line $y = 8$ gives a $x$ value of $\frac{2007 - 8(223)}{9} = 24 \frac 79$ , which means that $\lfloor 24 \frac 79\rfloor = 24$ unit squares can fit in that row. In general, there are
$\sum_{i=0}^{8} \lfloor \frac{223i}{9} \rfloor$
triangles. Since $\lfloor \frac{223}{9} \rfloor = 24$ , we see that there are more than $24(0 + 1 + \ldots + 8) = 24(\frac{8 \times 9}{2}) = 864$ triangles. Now, count the fractional parts. $\lfloor \frac{0}{9} \rfloor = 0, \lfloor \frac{7}{9} \rfloor = 0, \lfloor \frac{14}{9} \rfloor = 1,$ $\lfloor \frac{21}{9} \rfloor = 2, \lfloor \frac{28}{9} \rfloor = 3, \lfloor \frac{35}{9} \rfloor = 3,$ $\lfloor \frac{42}{9} \rfloor = 4, \lfloor \frac{49}{9} \rfloor = 5, \lfloor \frac{56}{9} \rfloor = 6$ . Adding them up, we get $864 + 1 + 2 + 3 + 3 + 4 + 5 + 6 = 888$ .

## Solution 3
From Pick's Theorem , $\frac{2007}{2}=\frac{233}{2}-\frac{2}{2}+\frac{2I}{2}$ . In other words, $2I=1776$ and I is $888$ .
Do you see why we simply set $I$ as the answer as well? That's because every interior point, if moved down and left one (southwest direction), can have that point and the previous point create a unit square. For example, $(1, 1)$ moves to $(0, 0)$ , so the square of points ${(0, 0), (1, 0), (1, 1), (0, 1)}$ is one example. This applies, of course, for $888$ points.

## Solution 4
We know that the number of squares intersected in an $m\times{n}$ rectangle is $m + n -\mbox{gcd}(m,n)$ . So if we apply that here, we get that the number of intersected squares is:
$9 + 223 - 1 = 231$ .
Now just subtract that from the total number of squares and divide by 2, since we want the number of squares below the line.
So,
$\frac{2007 - 231}{2} = \frac{1776}{2} = \fbox{888}$
These problems are copyrighted © by the Mathematical Association of America.