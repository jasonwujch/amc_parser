# 2016 AIME II Problem 8

## Problem

Find the number of sets $\{a,b,c\}$ of three distinct positive integers with the property that the product of $a,b,$ and $c$ is equal to the product of $11,21,31,41,51,61$ .

## Solution
Note that the prime factorization of the product is $3^{2}\cdot 7 \cdot 11 \cdot 17 \cdot 31 \cdot 41 \cdot 61$ . Ignoring overcounting, by stars and bars there are [2 (# of 3's) plus 3 (a, b, c) - 1] choose [3 - 1] = $6$ ways to choose how to distribute the factors of $3$ , and $3$ ways to distribute the factors of the other primes, so we have $3^{6} \cdot 6$ ways. However, some sets have $2$ numbers that are the same, namely the ones in the form $1,1,x$ and $3,3,x$ , which are each counted $3$ times, and each other set is counted $6$ times, so the desired answer is $\dfrac{729 \cdot 6-6}{6} = \boxed{728}$ .

## Solution 2
Again, notice that the prime factors of the product are $3, 3, 7, 11, 17, 31, 41, 61$ . In this problem, we are asked to partition this set of distinct(ish) factors into three smaller indistinct sets. To do this, we can use Stirling numbers of the second kind, but Stirling numbers of the second kind would assume no empty parts, which isn't what we want. However, this is easy to fix. Denote Stirling numbers of the second kind with $S(n,k)$ . We may start at the situation when all three sets are nonempty. Then, the number of partitions is simply $S(8,3)$ . However, we are overcounting, since every time the two threes are in different sets, (unless they are both individually in their own sets), each one is double counted. To fix this, we can see that they were in different sets $S(8, 3) - S(7,3)$ times by complementary counting, but one of these times they were in their own individual sets, so the total overcount is $\dfrac{S(8,3) - S(7,3) - 1}{2}$ . Similarly, we can do the cases for if two of the sets are nonempty and one of the sets are nonempty, (but in those last two cases the threes cannot be individually in their own sets). We then find that the "answer" is given by: \[S(8,3) - \dfrac{S(8,3) - S(7,3) - 1}{2} + S(8,2) - \dfrac{S(8,2) - S(7,2)}{2}+ S(8,1) - \dfrac{S(8,1) - S(7,1)}{2}\] \[= \dfrac{S(8,3)+S(8,2) + S(8,1) + S(7,3) + S(7,2) + S(7,1) + 1}{2}\] Drawing out the Stirling number triangle and evaluating yields $730$ for the last expression. However, throughout the entire solution, we ignored the fact that the three numbers $a$ , $b$ , and $c$ needed to be distinct. However, this is easy to fix, since there are only two sets in which they are not, namely $(1,1,x)$ and $(3,3,x)$ . Thus, the actual answer is $730 - 2 = \boxed{728}$ .
- Aathreyakadambi
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .