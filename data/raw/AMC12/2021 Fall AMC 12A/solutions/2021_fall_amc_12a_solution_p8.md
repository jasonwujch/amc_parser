# 2021 Fall AMC 12A Problem 8

## Problem

Let $M$ be the least common multiple of all the integers $10$ through $30,$ inclusive. Let $N$ be the least common multiple of $M,32,33,34,35,36,37,38,39,$ and $40.$ What is the value of $\frac{N}{M}?$

$\textbf{(A)}\ 1 \qquad\textbf{(B)}\ 2 \qquad\textbf{(C)}\ 37 \qquad\textbf{(D)}\ 74 \qquad\textbf{(E)}\ 2886$

## Solution
By the definition of least common mutiple, we take the greatest powers of the prime numbers of the prime factorization of all the numbers, that we are taking the $\text{lcm}$ of. In this case, \[M = 2^4 \cdot 3^3 \cdot 5^2 \cdot 7 \cdot 11 \cdot 13 \cdot 17 \cdot 19 \cdot 23 \cdot 29.\] Now, using the same logic, we find that \[N = M \cdot 2 \cdot 37,\] because we have an extra power of $2$ and an extra power of $37.$ Thus, $\frac{N}{M} = 2\cdot 37 = \boxed{\textbf{(D)}\ 74}.$
~NH14

## Solution 2
We know that between 32 and 40, there is one prime number, namely $37$ . This was not included in the previous $M$ , so we know that the value of $\frac{N}{M}$ will include a new 37. Then, let’s consider each individual number. \[32 = 2^5\] has a new power of 2 now included in $M$ , so we add that to our list. \[33=3 \cdot 11\] , which was included in the previous $M$ . Similarly, we can go through the numbers 32 to 40 and find that the only new powers of numbers added are \[2 \cdot 37 = 74\] , which gives $\frac{N}{M} = 2\cdot 37 = \boxed{\textbf{(D)}\ 74}.$
~MathCosine

## Video Solution by TheBeautyofMath
https://youtu.be/wlDlByKI7A8?t=410
~IceMatrix
### See Also