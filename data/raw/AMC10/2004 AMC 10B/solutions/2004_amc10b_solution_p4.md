# 2004 AMC 10B Problem 4

## Problem

A standard six-sided die is rolled, and $P$ is the product of the five numbers that are visible. What is the largest number that is certain to divide $P$ ?

$\mathrm{(A) \ } 6 \qquad \mathrm{(B) \ } 12 \qquad \mathrm{(C) \ } 24 \qquad \mathrm{(D) \ } 144\qquad \mathrm{(E) \ } 720$

## Solution 1
The product of all six numbers is $6!=720$ . The products of numbers that can be visible are $720/1$ , $720/2$ , ..., $720/6$ . The answer to this problem is their greatest common divisor -- which is $720/L$ , where $L$ is the least common multiple of $\{1,2,3,4,5,6\}$ . Clearly $L=60$ and the answer is $720/60=\boxed{\mathrm{(B)}\ 12}$ .

## Solution 2
Clearly, $P$ cannot have a prime factor other than $2$ , $3$ and $5$ .
We can not guarantee that the product will be divisible by $5$ , as the number $5$ can end on the bottom.
We can guarantee that the product will be divisible by $3$ (one of $3$ and $6$ will always be visible), but not by $3^2$ .
Finally, there are three even numbers, hence two of them are always visible and thus the product is divisible by $2^2$ . This is the most we can guarantee, as when the $4$ is on the bottom side, the two visible even numbers are $2$ and $6$ , and their product is not divisible by $2^3$ .

## Solution 3
The product P can be one of the following six numbers excluding the number that is hidden under, so we have: \begin{align*} 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 = 2^4 \cdot 3^2 \cdot 5 \\ 1 \cdot 3 \cdot 4 \cdot 5 \cdot 6 = 2^3 \cdot 3^2 \cdot 5 \\ 1 \cdot 2 \cdot 4 \cdot 5 \cdot 6 = 2^4 \cdot 3 \cdot 5 \\ 1 \cdot 2 \cdot 3 \cdot 5 \cdot 6 = 2^2 \cdot 3^2 \cdot 5 \\ 1 \cdot 2 \cdot 3 \cdot 4 \cdot 6 = 2^4 \cdot 3^2 \\ 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 = 2^3 \cdot 3 \cdot 5 \end{align*}
The largest number that is certain to divide product P is basically GCD of all the above 6 products which is $2^2 \cdot 3$ .
Hence $P=3\cdot2^2=\boxed{\mathrm{(B)}\ 12}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .