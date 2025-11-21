# 2022 AIME II Problem 5

## Problem

Twenty distinct points are marked on a circle and labeled $1$ through $20$ in clockwise order. A line segment is drawn between every pair of points whose labels differ by a prime number. Find the number of triangles formed whose vertices are among the original $20$ points.

## Solution 1
Let $a$ , $b$ , and $c$ be the vertex of a triangle that satisfies this problem, where $a > b > c$ . \[a - b = p_1\] \[b - c = p_2\] \[a - c = p_3\]
$p_3 = a - c = a - b + b - c = p_1 + p_2$ . Because $p_3$ is the sum of two primes, $p_1$ and $p_2$ , $p_1$ or $p_2$ must be $2$ . Let $p_1 = 2$ , then $p_3 = p_2 + 2$ . There are only $8$ primes less than $20$ : $2, 3, 5, 7, 11, 13, 17, 19$ . Only $3, 5, 11, 17$ plus $2$ equals another prime. $p_2 \in \{ 3, 5, 11, 17 \}$ .
Once $a$ is determined, $a = b+2$ and $b = c + p_2$ . There are $18$ values of $a$ where $b+2 \le 20$ , and $4$ values of $p_2$ . Therefore the answer is $18 \cdot 4 = \boxed{\textbf{072}}$
~ isabelchen

## Note: This solution seems incorrect.
Although the answer is correct, solution 2 below is a more accurate way to approach this problem. I agree, I don't get how $a + 2 \leq 20$ .

## Solution 2
As above, we must deduce that the sum of two primes must be equal to the third prime. Then, we can finish the solution using casework. If the primes are $2,3,5$ , then the smallest number can range between $1$ and $15$ . If the primes are $2,5,7$ , then the smallest number can range between $1$ and $13$ . If the primes are $2,11,13$ , then the smallest number can range between $1$ and $7$ . If the primes are $2,17,19$ , then the smallest number can only be $1$ .
Adding all cases gets $15+13+7+1=36$ . However, due to the commutative property, we must multiply this by 2. For example, in the $2,17,19$ case the numbers can be $1,3,20$ or $1,18,20$ . Therefore the answer is $36\cdot2=\boxed{072}$ .
Note about solution 1: I don't think that works, because if for example there are 21 points on the circle, your solution would yield $19\cdot4=76$ , but there would be $8$ more solutions than if there are $20$ points. This is because the upper bound for each case increases by $1$ , but commutative property doubles it to be $4$ .

## Video Solution by Power of Logic
https://youtu.be/iI2ZpdpGNyc
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .