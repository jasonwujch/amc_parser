# 2009 AMC 8 Problem 18

## Problem

The diagram represents a $7$ -foot-by- $7$ -foot floor that is tiled with $1$ -square-foot black tiles and white tiles. Notice that the corners have white tiles. If a $15$ -foot-by- $15$ -foot floor is to be tiled in the same manner, how many white tiles will be needed?

[asy]unitsize(10); draw((0,0)--(7,0)--(7,7)--(0,7)--cycle); draw((1,7)--(1,0)); draw((6,7)--(6,0)); draw((5,7)--(5,0)); draw((4,7)--(4,0)); draw((3,7)--(3,0)); draw((2,7)--(2,0)); draw((0,1)--(7,1)); draw((0,2)--(7,2)); draw((0,3)--(7,3)); draw((0,4)--(7,4)); draw((0,5)--(7,5)); draw((0,6)--(7,6)); fill((1,0)--(2,0)--(2,7)--(1,7)--cycle,black); fill((3,0)--(4,0)--(4,7)--(3,7)--cycle,black); fill((5,0)--(6,0)--(6,7)--(5,7)--cycle,black); fill((0,5)--(0,6)--(7,6)--(7,5)--cycle,black); fill((0,3)--(0,4)--(7,4)--(7,3)--cycle,black); fill((0,1)--(0,2)--(7,2)--(7,1)--cycle,black);[/asy]

$\textbf{(A)}\ 49 \qquad \textbf{(B)}\ 57 \qquad \textbf{(C)}\ 64 \qquad \textbf{(D)}\ 96 \qquad \textbf{(E)}\ 126$

## Solutions

## Solution 1
In a $1$ -foot-by- $1$ -foot floor, there is $1$ white tile. In a $3$ -by- $3$ , there are $4$ . Continuing on, you can deduce the $n^{th}$ positive odd integer floor has $n^2$ white tiles. $15$ is the $8^{th}$ odd integer, so there are $\boxed{\textbf{(C)}\ 64}$ white tiles.

## Solution 2
After testing a couple of cases, we find that the number of white squares is $(s/2)^2$ , where s is the side length of the square and $s/2$ is rounded up to the next whole number. Therefore, $15/2$ rounded up is 8, so $8^2=64$ , or $\framebox{(C) 64}$ .

## Video Solution
https://www.youtube.com/watch?v=VThwtOomWYQ ~David
### See Also