# 2016 AIME II Problem 11

## Problem

For positive integers $N$ and $k$ , define $N$ to be $k$ -nice if there exists a positive integer $a$ such that $a^{k}$ has exactly $N$ positive divisors. Find the number of positive integers less than $1000$ that are neither $7$ -nice nor $8$ -nice.

## Solution
We claim that an integer $N$ is only $k$ -nice if and only if $N \equiv 1 \pmod k$ . By the number of divisors formula, the number of divisors of $\prod_{i=1}^n p_i^{a_i}$ is $\prod_{i=1}^n (a_i+1)$ . Since all the $a_i$ 's are divisible by $k$ in a perfect $k$ power, the only if part of the claim follows. To show that all numbers $N \equiv 1 \pmod k$ are $k$ -nice, write $N=bk+1$ . Note that $2^{kb}$ has the desired number of factors and is a perfect kth power. By PIE, the number of positive integers less than $1000$ that are either $1 \pmod 7$ or $1\pmod 8$ is $143+125-18=250$ , so the desired answer is $999-250=\boxed{749}$ .
Solution by Shaddoll and firebolt360

## Solution 2
All integers $a$ will have factorization $2^a3^b5^c7^d...$ . Therefore, the number of factors in $a^7$ is $(7a+1)(7b+1)...$ , and for $a^8$ is $(8a+1)(8b+1)...$ . The most salient step afterwards is to realize that all numbers $N$ not $1 \pmod{7}$ and also not $1 \pmod{8}$ satisfy the criterion. The cycle repeats every $56$ integers, and by PIE, $7+8-1=14$ of them are either $7$ -nice or $8$ -nice or both. Therefore, we can take $\frac{42}{56} * 1008 = 756$ numbers minus the $7$ that work between $1000-1008$ inclusive, to get $\boxed{749}$ positive integers less than $1000$ that are not nice for $k=7, 8$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .