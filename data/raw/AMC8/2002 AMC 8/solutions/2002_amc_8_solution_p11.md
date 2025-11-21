# 2002 AMC 8 Problem 11

## Problem

A sequence of squares is made of identical square tiles. The edge of each square is one tile length longer than the edge of the previous square. The first three squares are shown. How many more tiles does the seventh square require than the sixth?

[asy] path p=origin--(1,0)--(1,1)--(0,1)--cycle; draw(p); draw(shift(3,0)*p); draw(shift(3,1)*p); draw(shift(4,0)*p); draw(shift(4,1)*p); draw(shift(7,0)*p); draw(shift(7,1)*p); draw(shift(7,2)*p); draw(shift(8,0)*p); draw(shift(8,1)*p); draw(shift(8,2)*p); draw(shift(9,0)*p); draw(shift(9,1)*p); draw(shift(9,2)*p);[/asy]

$\text{(A)}\ 11 \qquad \text{(B)}\ 12 \qquad \text{(C)}\ 13 \qquad \text{(D)}\ 14 \qquad \text{(E)}\ 15$

## Solutions

## Solution 1
The first square has a sidelength of $1$ , the second square $2$ , and so on. The seventh square has $7$ and is made of $7^2=49$ unit tiles. The sixth square has $6$ and is made of $6^2=36$ unit tiles. The seventh square has $49-36=\boxed{\text{(C)}\ 13}$ more tiles than the sixth square.

## Solution 2
The edge of each square is one tile length longer than the edge of the previous square, which means that each square has $2*$ edge length $- 1$ more tiles than the previous square, because each square is just one edge added on the top and on the right to the previous square, with one overlapping tile. Then the seventh square has $2*7-1=13$ more tiles than the sixth square, which is $\boxed{\text{(C)}\ 13}$ .

## Solution 3
We see a pattern of 1, 4, and 9, all of which are the squares of 1, 2,and 3 respectively. So, the 6th and 7th squares will also follow the same pattern. Via the difference of squares, we see that $7^2 - 6^2$ . Now we can see that the seventh square has $(7-6)(7+6) =$ $\boxed{\text{(C)}\ 13}$ more tiles than the sixth square.
~ AkCANdo

## Video Solution by Whymath
https://youtu.be/QGxNCcUB5zw
### See Also