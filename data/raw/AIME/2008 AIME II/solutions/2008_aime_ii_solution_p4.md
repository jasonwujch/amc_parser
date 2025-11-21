# 2008 AIME II Problem 4

## Problem

There exist $r$ unique nonnegative integers $n_1 > n_2 > \cdots > n_r$ and $r$ unique integers $a_k$ ( $1\le k\le r$ ) with each $a_k$ either $1$ or $- 1$ such that \[a_13^{n_1} + a_23^{n_2} + \cdots + a_r3^{n_r} = 2008.\] Find $n_1 + n_2 + \cdots + n_r$ .

## Solution
In base $3$ , we find that $\overline{2008}_{10} = \overline{2202101}_{3}$ . In other words,
In order to rewrite as a sum of perfect powers of $3$ , we can use the fact that $2 \cdot 3^k = 3^{k+1} - 3^k$ :
The answer is $7+5+4+3+2+0 = \boxed{021}$ .
Note : Solution by bounding is also possible, namely using the fact that $1+3+3^2 + \cdots + 3^{n} = \displaystyle\frac{3^{n+1}-1}{2}.$
These problems are copyrighted © by the Mathematical Association of America.