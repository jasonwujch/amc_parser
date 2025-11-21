# 2000 AIME II Problem 4

## Problem

What is the smallest positive integer with six positive odd integer divisors and twelve positive even integer divisors?

## Solution 1
We use the fact that the number of divisors of a number $n = p_1^{e_1}p_2^{e_2} \cdots p_k^{e_k}$ is $(e_1 + 1)(e_2 + 1) \cdots (e_k + 1)$ . If a number has $18 = 2 \cdot 3 \cdot 3$ factors, then it can have at most $3$ distinct primes in its factorization.
Dividing the greatest power of $2$ from $n$ , we have an odd integer with six positive divisors, which indicates that it either is ( $6 = 2 \cdot 3$ ) a prime raised to the $5$ th power, or two primes, one of which is squared. The smallest example of the former is $3^5 = 243$ , while the smallest example of the latter is $3^2 \cdot 5 = 45$ .
Suppose we now divide all of the odd factors from $n$ ; then we require a power of $2$ with $\frac{18}{6} = 3$ factors, namely $2^{3-1} = 4$ . Thus, our answer is $2^2 \cdot 3^2 \cdot 5 = \boxed{180}$ .

## Solution 2
Somewhat similar to the first solution, we see that the number $n$ has two even factors for every odd factor. Thus, if $x$ is an odd factor of $n$ , then $2x$ and $4x$ must be the two corresponding even factors. So, the prime factorization of $n$ is $2^2 3^a 5^b 7^c...$ for some set of integers $a, b, c, ...$
Since there are $18$ factors of $n$ , we can write:
$(2+1)(a+1)(b+1)(c+1)... = 18$
$(a+1)(b+1)(c+1)... = 6$
Since $6$ only has factors from the set $1, 2, 3, 6$ , either $a=5$ and all other variables are $0$ , or $a=3$ and $b=2$ , with again all other variables equal to $0$ . This gives the two numbers $2^2 \cdot 3^5$ and $2^2 \cdot 3^2 \cdot 5$ . The latter number is smaller, and is equal to $\boxed {180}$ .

## Solution 3
We see that the least number with 6 odd factors is $3^2*5$ . Multiplied by $2^2$ (as each factor of 2 doubles the odd factors, as it can be 2n or $2^2n$ . Finally, you get $180$
-dragoon
These problems are copyrighted © by the Mathematical Association of America.