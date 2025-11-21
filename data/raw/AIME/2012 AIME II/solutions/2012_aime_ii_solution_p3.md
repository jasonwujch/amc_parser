# 2012 AIME II Problem 3

## Problem

At a certain university, the division of mathematical sciences consists of the departments of mathematics, statistics, and computer science. There are two male and two female professors in each department. A committee of six professors is to contain three men and three women and must also contain two professors from each of the three departments. Find the number of possible committees that can be formed subject to these requirements.

## Solution
There are two cases:
Case 1: One man and one woman is chosen from each department.
Case 2: Two men are chosen from one department, two women are chosen from another department, and one man and one woman are chosen from the third department.
For the first case, in each department there are ${{2}\choose{1}} \times {{2}\choose{1}} = 4$ ways to choose one man and one woman. Thus there are $4^3 = 64$ total possibilities conforming to case 1.
For the second case, there is only ${{2}\choose{2}} = 1$ way to choose two professors of the same gender from a department, and again there are $4$ ways to choose one man and one woman. Thus there are $1 \cdot 1 \cdot 4 = 4$ ways to choose two men from one department, two women from another department, and one man and one woman from the third department. However, there are $3! = 6$ different department orders, so the total number of possibilities conforming to case 2 is $4 \cdot 6 = 24$ .
Summing these two values yields the final answer: $64 + 24 = \boxed{088}$ .

## Solution 2
Use generating functions . For each department, there is 1 way to pick 2 males, 4 ways to pick one of each, and 1 way to pick 2 females. Since there are three departments in total, and we wish for three males and three females, the answer will be equal to the coefficient of $x^3y^3$ in the expansion of $(x^2+4xy+y^2)^3$ . The requested coefficient is $\boxed{088}$
~sigma
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .