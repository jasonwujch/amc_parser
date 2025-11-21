# 2008 AMC 10B Problem 8

## Problem

A class collects 50 dollars to buy flowers for a classmate who is in the hospital. Roses cost 3 dollars each, and carnations cost 2 dollars each. No other flowers are to be used. How many different bouquets could be purchased for exactly 50 dollars?

$\mathrm{(A)}\ 1 \qquad \mathrm{(B)}\ 7 \qquad \mathrm{(C)}\ 9 \qquad \mathrm{(D)}\ 16 \qquad \mathrm{(E)}\ 17$

## Solution 1
The cost of a rose is odd, hence we need an even number of roses. Let there be $2r$ roses for some $r\geq 0$ . Then we have $50-3\cdot 2r = 50-6r$ dollars left. We can always reach the sum exactly $50$ by buying $(50-6r)/2 = 25-3r$ carnations. Of course, the number of roses must be such that the number of carnations is non-negative. We get the inequality $25-3r \geq 0$ which solves to $r\leq 8 \frac13$ . $r$ must be an integer, so there are $\boxed{9 \text{ (C)}}$ possible values of $r$ , and each gives us one solution.

## Solution 2
Let $x$ and $y$ be the number of roses and carnations bought. The equation should be $3x+2y = 50$ . Since $50$ is an even number, the product of $3x$ must be even and smaller than $50$ . You can try nonnegative even integers for $x$ and you will end up with the numbers $0$ , $2$ , $4$ , $6$ , $8$ , $10$ , $12$ , $14$ , and $16$ . There are $9$ numbers in total, so the answer is $\boxed{9 \text{ (C)}}$ .

## Solution 3
Let $r$ represent the number of roses, and let $c$ represent the number of carnations. Then, we get the linear Diophantine equation, $3r+2c=50$ . Using the Euclidean algorithm, we get the initial solutions to be $r_0=50$ and $c_0=-50$ , meaning the complete solution will be, $r=50+\frac{2}{\gcd(2,3)}$ $k=50+2k$ , $c=-50-\frac{3}{\gcd(2,3)}k=-50-3k$
The solution range for which both $r$ and $c$ are positive is $17$ $\leq k$ $\leq$ $25$ . There are $\boxed{9 \text{ (C)}}$ possible values for $k$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .