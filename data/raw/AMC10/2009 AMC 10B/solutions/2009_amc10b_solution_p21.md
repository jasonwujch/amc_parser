# 2009 AMC 10B Problem 21

## Problem

What is the remainder when $3^0 + 3^1 + 3^2 + \cdots + 3^{2009}$ is divided by 8?

$\mathrm{(A)}\ 0\qquad \mathrm{(B)}\ 1\qquad \mathrm{(C)}\ 2\qquad \mathrm{(D)}\ 4\qquad \mathrm{(E)}\ 6$

## Solution

## Solution 1
The sum of any four consecutive powers of 3 is divisible by $3^0 + 3^1 + 3^2 +3^3 = 40$ and hence is divisible by 8. Therefore
is divisible by 8. So the required remainder is $3^0 + 3^1 = \boxed {4}$ . The answer is $\mathrm{(D)}$ .

## Solution 2
We have $3^2 = 9 \equiv 1 \pmod 8$ . Hence for any $k$ we have $3^{2k}\equiv 1^k = 1 \pmod 8$ , and then $3^{2k+1} = 3\cdot 3^{2k} \equiv 3\cdot 1 = 3 \pmod 8$ .
Therefore our sum gives the same remainder modulo $8$ as $1 + 3 + 1 + 3 + 1 + \cdots + 1 + 3$ . There are $2010$ terms in the sum, hence there are $2010/2 = 1005$ pairs of $1+3$ , and thus the sum is $1005 \cdot 4 = 4020 \equiv 20 \equiv \boxed{4} \pmod 8$ .

## Solution 3
We have the formula $\frac{a(r^n-1)}{r-1}$ for the sum of a finite geometric sequence which we want to find the residue modulo 8. \[\frac{1 \cdot (3^{2010}-1)}{2}\] \[\frac{3^{2010}-1}{2} = \frac{9^{1005}-1}{2}\] \[\frac{9^{1005}-1}{2} \equiv \frac{1^{1005}-1}{2} \equiv \frac{0}{2} \pmod 8\] Therefore, the numerator of the fraction is divisible by $8$ . However, when we divide the numerator by $2$ , we get a remainder of $4$ modulo $8$ , giving us $\mathrm{(D)}$ .
Note: you need to prove that \[\frac{9^{1005}-1}{2}\] is not congruent to 0 mod 16 because if so, then the whole thing would be congruent to 0 mod 8, even after dividing by 2 ~ ilikepi12

## Solution 4 (Patterns)
We can see that $\frac{3^0}{8}$ is has a remainder of 1. $\frac{3^1}{8}$ has a remainder of 4. $\frac{3^2}{8}$ also has a remainder of 4. $\frac{3^3}{8}$ has a remainder of 0.
If we keep on going, we can see that this pattern repeats every 4 powers of 3 - that is to say, the reminder cycles through $1$ , $4$ , $4$ , and $0$ .
Using simple math, we can see that if assume the pattern repeats every 4 numbers, $3^{2009}$ has a remainder of $\boxed {4}$ . The answer is $\mathrm{(D)}$ .

## Video Solution
https://youtu.be/V8VydUpAsS8
~savannahsolver
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .