# 2000 AMC 8 Problem 12

## Problem

A block wall 100 feet long and 7 feet high will be constructed using blocks that are 1 foot high and either 2 feet long or 1 foot long (no blocks may be cut). The vertical joins in the blocks must be staggered as shown, and the wall must be even on the ends. What is the smallest number of blocks needed to build this wall?

[asy] draw((0,0)--(6,0)--(6,1)--(5,1)--(5,2)--(0,2)--cycle); draw((0,1)--(5,1)); draw((1,1)--(1,2)); draw((3,1)--(3,2)); draw((2,0)--(2,1)); draw((4,0)--(4,1)); [/asy]

$\text{(A)}\ 344\qquad\text{(B)}\ 347\qquad\text{(C)}\ 350\qquad\text{(D)}\ 353\qquad\text{(E)}\ 356$

## Solution
Since the bricks are $1$ foot high, there will be $7$ rows. To minimize the number of blocks used, rows $1, 3, 5,$ and $7$ will look like the bottom row of the picture, which takes $\frac{100}{2} = 50$ bricks to construct. Rows $2, 4,$ and $6$ will look like the upper row pictured, which has $49$ 2-foot bricks in the middle, and $2$ 1-foot bricks on each end for a total of $51$ bricks.
Four rows of $50$ bricks and three rows of $51$ bricks totals $4\cdot 50 + 3\cdot 51 = 200 + 153 = 353$ bricks, giving the answer $\boxed{D}.$

## Video Solution by Soo
https://youtu.be/EeHv96Ry_Ww - Soo, DRMS, NM
### See Also