# 2009 AIME II Problem 12

## Problem

From the set of integers $\{1,2,3,\dots,2009\}$ , choose $k$ pairs $\{a_i,b_i\}$ with $a_i<b_i$ so that no two pairs have a common element. Suppose that all the sums $a_i+b_i$ are distinct and less than or equal to $2009$ . Find the maximum possible value of $k$ .

## Solution
Suppose that we have a valid solution with $k$ pairs. As all $a_i$ and $b_i$ are distinct, their sum is at least $1+2+3+\cdots+2k=k(2k+1)$ . On the other hand, as the sum of each pair is distinct and at most equal to $2009$ , the sum of all $a_i$ and $b_i$ is at most $2009 + (2009-1) + \cdots + (2009-(k-1)) = \frac{k(4019-k)}{2}$ .
Hence we get a necessary condition on $k$ : For a solution to exist, we must have $\frac{k(4019-k)}{2} \geq k(2k+1)$ . As $k$ is positive, this simplifies to $\frac{4019-k}{2} \geq 2k+1$ , whence $5k\leq 4017$ , and as $k$ is an integer, we have $k\leq \lfloor 4017/5\rfloor = 803$ .
If we now find a solution with $k=803$ , we can be sure that it is optimal.
From the proof it is clear that we don't have much "maneuvering space", if we want to construct a solution with $k=803$ . We can try to use the $2k$ smallest numbers: $1$ to $2\cdot 803 = 1606$ . When using these numbers, the average sum will be $1607$ . Hence we can try looking for a nice systematic solution that achieves all sums between $1607-401=1206$ and $1607+401=2008$ , inclusive.
Such a solution indeed does exist, here is one:
Partition the numbers $1$ to $1606$ into four sequences:
- $A=1,3,5,7,\dots,801,803$
- $B=1205,1204,1203,1202,\dots,805,804$
- $C=2,4,6,8,\dots,800,802$
- $D=1606,1605,1604,1603,\dots,1207,1206$
Sequences $A$ and $B$ have $402$ elements each, and the sums of their corresponding elements are $1206,1207,1208,1209,\dots,1606,1607$ . Sequences $C$ and $D$ have $401$ elements each, and the sums of their corresponding elements are $1608,1609,1610,1611,\dots,2007,2008$ .
Thus we have shown that there is a solution for $k=\boxed{803}$ and that for larger $k$ no solution exists.

## Video Solution
https://youtu.be/yVP2MhOMSy4?si=ZC4Zo4xKe867uM8X
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.