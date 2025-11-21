# 2004 AIME II Problem 8

## Problem

How many positive integer divisors of $2004^{2004}$ are divisible by exactly 2004 positive integers?

## Solution 1
The prime factorization of 2004 is $2^2\cdot 3\cdot 167$ . Thus the prime factorization of $2004^{2004}$ is $2^{4008}\cdot 3^{2004}\cdot 167^{2004}$ .
We can count the number of divisors of a number by multiplying together one more than each of the exponents of the prime factors in its prime factorization. For example, the number of divisors of $2004=2^2\cdot 3^1\cdot 167^1$ is $(2+1)(1+1)(1+1)=12$ .
A positive integer divisor of $2004^{2004}$ will be of the form $2^a\cdot 3^b\cdot 167^c$ . Thus we need to find how many $(a,b,c)$ satisfy
We can think of this as partitioning the exponents to $a+1,$ $b+1,$ and $c+1$ . So let's partition the 2's first. There are two 2's so this is equivalent to partitioning two items in three containers. We can do this in ${4 \choose 2} = 6$ ways. We can partition the 3 in three ways and likewise we can partition the 167 in three ways. So we have $6\cdot 3\cdot 3 = \boxed{54}$ as our answer.

## Solution 2 (bash)
Clearly we need to find a group of numbers that multiply to 2004. We can list them all out since we know that 2004 is only $167 \cdot 2^2 \cdot 3$ .
167, 2, 2, 3
4, 3, 167
12, 167
4, 501
2, 1002
2, 3, 334
2, 2, 501*
6, 2, 167
3, 668
6, 334
2004*
To begin, the first multiple doesn't work because there are only 3 prime divisors of 2004. We can apply all multiples because the prime factorization of $2004^{2004}$ is $2^{4008} \cdot 3^{2004} \cdot 167^{2004}.$ Every multiple has six ways of distributing numbers to become powers of 167, 3, and 2, except for the ones with a star. For a single power of 2004, we have three choices (2, 3, and 167) to give a power of 2003 to. For 2, 2, 501, there are three choices to give a power of 500 to and the rest get a power of 1.
Therefore we have $8 \cdot 6$ normal multiples and $3 \cdot 2$ "half" multiples. Sum to get $\boxed{54}$ as our answer.

## Solution 3
we want $167^a \cdot 3^b \cdot 2^c$ such that this number has exactly $2004$ positive factors. Note that $2004$ has $(1 + 1) \cdot (1 + 1) \cdot (2 + 1) = 12$ factors.
Case 1: $(a + 1)(b + 1)(c + 1) = 2004$ , and no variable equals $0.$
The three variables can either be the three elements of $\{166, 1, 5\}, \{500, 1, 1\}, \{333, 2, 1\},$ or $\{166, 3, 2\}.$ They can be permuted in $6 + 3 + 6 + 6 = 21$ ways.
Case 2: $(x + 1)(y + 1) = 2004$ , where $x$ and $y$ are two variables chosen out of $\{a, b, c\}$ and none of them equal $0$
There are $12 - 2 = 10$ ways to choose the values of $x$ and $y$ . There are $\binom{3}{2} = 3$ ways to choose the variables $x$ and $y$ out of $\{a, b, c\}$ , giving $30$ ways.
Case 3: $(x + 1) = 2004$
$x$ must be $2003$ . We can let $x = a,b,$ or $c$ , so this case gives us $3$ ways.
The answer is $21 + 30 + 3 = \boxed{54}.$
~ grogg007
These problems are copyrighted © by the Mathematical Association of America.