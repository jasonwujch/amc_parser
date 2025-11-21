# 2006 AIME II Problem 13

## Problem

How many integers $N$ less than $1000$ can be written as the sum of $j$ consecutive positive odd integers from exactly 5 values of $j\ge 1$ ?

## Solution 1
Let the first odd integer be $2n+1$ , $n\geq 0$ . Then the final odd integer is $2n+1 + 2(j-1) = 2(n+j) - 1$ . The odd integers form an arithmetic sequence with sum $N = j\left(\frac{(2n+1) + (2(n+j)-1)}{2}\right) = j(2n+j)$ . Thus, $j$ is a factor of $N$ .
Since $n\geq 0$ , it follows that $2n+j \geq j$ and $j\leq \sqrt{N}$ .
Since there are exactly $5$ values of $j$ that satisfy the equation, there must be either $9$ or $10$ factors of $N$ . This means $N=p_1^2p_2^2$ or $N=p_1p_2^4$ . Unfortunately, we cannot simply observe prime factorizations of $N$ because the factor $(2n+j)$ does not cover all integers for any given value of $j$ .
Instead we do some casework:
- If $N$ is odd, then $j$ must also be odd. For every odd value of $j$ , $2n+j$ is also odd, making this case valid for all odd $j$ . Looking at the forms above and the bound of $1000$ , $N$ must be
\[(3^2\cdot5^2),\ (3^2\cdot7^2),\ (3^4\cdot5),\ (3^4\cdot7),\ (3^4\cdot 11)\]
- If $N$ is even, then $j$ must also be even. Substituting $j=2k$ , we get
\[N = 4k(n+k) \Longrightarrow \frac{N}{4} = k(n+k)\]
\[\frac{N}{4} = (2^2\cdot3^2),(2^2\cdot5^2),(2^2\cdot7^2), (3^2\cdot5^2), (2^4\cdot3), (2^4\cdot5), (2^4\cdot7), (2^4\cdot11), (2^4\cdot13), (3^4\cdot2)\]
The total number of integers $N$ is $5 + 10 = \boxed{15}$ .

## Solution 2
Let the largest odd number below the sequence be the $q$ th positive odd number, and the largest odd number in the sequence be the $p$ th positive odd number. Therefore, the sum is $p^2-q^2=(p+q)(p-q)$ by sum of consecutive odd numbers. Note that $p+q$ and $p-q$ have the same parity, and $q$ can equal $0$ . We then perform casework based on the parity of $p-q$ .
If $p-q$ is odd, then $p^2-q^2$ must always be odd. Therefore, to have 5 pairs of odd factors, we must have either $9$ (in which case the number is a perfect square) or $10$ factors. Considering the upper bound, the only way this can happen is $p_1^4\cdot{p_2}$ or $p_1^2\cdot{p_2^2}$ . N must then be one of \[(3^2\cdot5^2),\ (3^2\cdot7^2),\ (3^4\cdot5),\ (3^4\cdot7),\ (3^4\cdot 11)\] So, there are $5$ solutions when $(p+q)(p-q)$ is odd.
If $p-q$ is even, then $(p+q)(p-q)$ must have at least two factors of $2$ , so we can rewrite the expression as $4(k)(k-q)$ where $k=\frac{p+q}{2}$ . We can disregard the $4$ by dividing by $4$ and restricting our upper bound to $250$ . Since $k$ and $q$ don't have to be the same parity, we can include all cases less than 250 that have 9 or 10 factors. We then have \[(2^2\cdot3^2),(2^2\cdot5^2),(2^2\cdot7^2), (3^2\cdot5^2), (2^4\cdot3), (2^4\cdot5), (2^4\cdot7), (2^4\cdot11), (2^4\cdot13), (3^4\cdot2)\] as the possibilities.
Therefore, there are $10+5=\boxed{015}$ possibilities for $p^2-q^2=N$ ~sigma
These problems are copyrighted © by the Mathematical Association of America.