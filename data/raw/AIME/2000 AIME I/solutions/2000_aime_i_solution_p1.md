# 2000 AIME I Problem 1

## Problem

Find the least positive integer $n$ such that no matter how $10^{n}$ is expressed as the product of any two positive integers, at least one of these two integers contains the digit $0$ .

## Solution
If a factor of $10^{n}$ has a $2$ and a $5$ in its prime factorization , then that factor will end in a $0$ . Therefore, we have left to consider the case when the two factors have the $2$ s and the $5$ s separated, so we need to find the first power of 2 or 5 that contains a 0.
For $n = 1:$ \[2^1 = 2 , 5^1 = 5\] $n = 2:$ \[2^2 = 4 , 5 ^ 2 =25\] $n = 3:$ \[2^3 = 8 , 5 ^3 = 125\]
and so on, until,
$n = 8:$ $2^8 = 256$ | $5^8 = 390625$
We see that $5^8$ contains the first zero, so $n = \boxed{008}$ .

## Video Solution
https://www.youtube.com/watch?v=6cwg9DZ7bX4
These problems are copyrighted © by the Mathematical Association of America.