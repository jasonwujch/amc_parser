# 2005 AIME I Problem 3

## Problem

How many positive integers have exactly three proper divisors (positive integral divisors excluding itself), each of which is less than 50?

## Solution (Basic Casework and Combinations)
Suppose $n$ is such an integer . Because $n$ has $3$ proper divisors, it must have $4$ divisors,, so $n$ must be in the form $n=p\cdot q$ or $n=p^3$ for distinct prime numbers $p$ and $q$ .
In the first case, the three proper divisors of $n$ are $1$ , $p$ and $q$ . Thus, we need to pick two prime numbers less than $50$ . There are fifteen of these ( $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43$ and $47$ ) so there are ${15 \choose 2} =105$ ways to choose a pair of primes from the list and thus $105$ numbers of the first type.
In the second case, the three proper divisors of $n$ are 1, $p$ and $p^2$ . Thus we need to pick a prime number whose square is less than $50$ . There are four of these ( $2, 3, 5,$ and $7$ ) and so four numbers of the second type.
Thus there are $105+4=\boxed{109}$ integers that meet the given conditions.
~lpieleanu (Minor editing) ~ rollover2020 (extremely minor editing)
- Counting divisors of positive integers
These problems are copyrighted © by the Mathematical Association of America.