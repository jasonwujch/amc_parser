# 2008 AIME I Problem 7

## Problem

Let $S_i$ be the set of all integers $n$ such that $100i\leq n < 100(i + 1)$ . For example, $S_4$ is the set ${400,401,402,\ldots,499}$ . How many of the sets $S_0, S_1, S_2, \ldots, S_{999}$ do not contain a perfect square?

## Solution
The difference between consecutive squares is $(x + 1)^2 - x^2 = 2x + 1$ , which means that all squares above $50^2 = 2500$ are more than $100$ apart.
Then the first $26$ sets ( $S_0,\cdots S_{25}$ ) each have at least one perfect square because the differences between consecutive squares in them are all less than $100$ . Also, since $316$ is the largest $x$ such that $x^2 < 100000$ ( $100000$ is the upper bound which all numbers in $S_{999}$ must be less than), there are $316 - 50 = 266$ other sets after $S_{25}$ that have a perfect square.
There are $1000 - 266 - 26 = \boxed{708}$ sets without a perfect square.

## Video Solution
https://youtu.be/6eBLXnzK0n4
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.