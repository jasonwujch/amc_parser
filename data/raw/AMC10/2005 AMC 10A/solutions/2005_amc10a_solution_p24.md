# 2005 AMC 10A Problem 24

## Problem

For each positive integer $m > 1$ , let $P(m)$ denote the greatest prime factor of $m$ . For how many positive integers $n$ is it true that both $P(n) = \sqrt{n}$ and $P(n+48) = \sqrt{n+48}$ ?

$\textbf{(A) } 0\qquad \textbf{(B) } 1\qquad \textbf{(C) } 3\qquad \textbf{(D) } 4\qquad \textbf{(E) } 5$

## Solution 1
If $P(n) = \sqrt{n}$ , then $n = p_{1}^{2}$ , where $p_{1}$ is a prime number .
If $P(n+48) = \sqrt{n+48}$ , then $n + 48$ is a square, but we know that n is $p_{1}^{2}$ .
This means we just have to check for squares of primes, add $48$ and look whether the root is a prime number. We can easily see that the difference between two consecutive square after $576$ is greater than or equal to $49$ , Hence we have to consider only the prime numbers till $23$ .
Squaring prime numbers below $23$ including $23$ we get the following list.
$4 , 9 , 25 , 49 , 121, 169 , 289 , 361 , 529$
But adding $48$ to a number ending with $9$ will result in a number ending with $7$ , but we know that a perfect square does not end in $7$ , so we can eliminate those cases to get the new list.
$4 , 25 , 121 , 361$
Adding $48$ , we get $121$ as the only possible solution. Hence the answer is $\boxed{\textbf{(B) }1}$ .
edited by mobius247

## Note: Solution 1
Since all primes greater than $2$ are odd, we know that the difference between the squares of any two consecutive primes greater than $2$ is at least $(p+2)^2-p^2=4p+4$ , where p is the smaller of the consecutive primes. For $p>11$ , $4p+4>48$ . This means that the difference between the squares of any two consecutive primes both greater than $11$ is greater than $48$ , so $n$ and $n+48$ can't both be the squares of primes if $n=p^2$ and $p>11$ . So, we only need to check $n=2^2, 3^2, 5^2, 7^2,$ and $11^2$ .
~apsid

## Video Solution
https://youtu.be/IsqrsMkR-mA
~ rudolf1279

## Solution 2(completely useless unless you have 75 minutes for this problem only)
This solution is extremely tedious and hard to understand. Therefore, I recommend solution 4 down below.
View at your own cost!!
If $P(n) = \sqrt{n}$ , then $n = p_{1}^{2}$ , where $p_{1}$ is a prime number .
If $P(n+48) = \sqrt{n+48}$ , then $n+48 = p_{2}^{2}$ , where $p_{2}$ is a different prime number.
So:
$p_{2}^{2} = n+48$
$p_{1}^{2} = n$
$p_{2}^{2} - p_{1}^{2} = 48$
$(p_{2}+p_{1})(p_{2}-p_{1})=48$
Since $p_{1} > 0$ : $(p_{2}+p_{1}) > (p_{2}-p_{1})$ .
Looking at pairs of divisors of $48$ , we have several possibilities to solve for $p_{1}$ and $p_{2}$ :
(Note: you can skip several cases below by observing that $p_1+p_2$ and $p_1-p_{2}$ must be even, and $p_1+p_2 \neq p_1-p_2 \pmod 4$ .)
$(p_{2}+p_{1}) = 48$
$(p_{2}-p_{1}) = 1$ (impossible)
$p_{1} = \frac{47}{2}$
$p_{2} = \frac{49}{2}$
$(p_{2}+p_{1}) = 24$
$(p_{2}-p_{1}) = 2$
$p_{1} = 11$
$p_{2} = 13$ (Valid!)
$(p_{2}+p_{1}) = 16$
$(p_{2}-p_{1}) = 3$ (impossible)
$p_{1} = \frac{13}{2}$
$p_{2} = \frac{19}{2}$
$(p_{2}+p_{1}) = 12$
$(p_{2}-p_{1}) = 4$ (impossible)
$p_{1} = 4$
$p_{2} = 8$
$(p_{2}+p_{1}) = 8$
$(p_{2}-p_{1}) = 6$
$p_{1} = 1$ (not prime)
$p_{2} = 7$
The only solution $(p_{1} , p_{2})$ where both numbers are primes is $(11,13)$ .
Therefore the number of positive integers $n$ that satisfy both statements is $\boxed{\textbf{(B) }1}.$

## Solution 3(Compact and hard to understand)
For the statement to be true, we must have both $n$ and $n + 48$ be squares of primes. Support we have the number $x^2$ , where $x$ is a positive integer. Then the next perfect square, $(x+1)^2$ , is $(x+1)^2 - x^2 = 2x+1$ greater than $x^2$ . The next perfect square after that will be $(x+2)^2 = 4x + 4$ greater than $x^2$ . In general, the prime $(x+n)^2$ will be $nx + n^2$ greater than $x^2$ . However, we must have that $nx + n^2 = 48$ . $n$ can take on any value between $1$ and $6$ (if $n$ is equal to $7$ , we have $14x + 49$ , where $x$ would have to be negative for the difference to be $48$ ). However, we can eliminate all the cases where $n$ is odd, because we would then have a number of the form $even + odd$ , which is odd because $x$ can take only integral values. As such, we consider $n = 2$ , $n = 4$ , and $n = 6$ . If $n = 2$ , then $4x + 4 = 48 \implies x = 11$ . Then our squares are $11^2$ and $13^2$ , both of which are squares of primes. If $n = 4$ , then $8x + 16 = 48 \implies x = 4$ . However, $4$ isn't prime, so we discard this case. Finally, if $n = 6$ , then $12x + 36 = 48 \implies x = 1$ . Again, $1$ isn't prime, so we discard this case as well. Thus, we only have $\boxed{\textbf{(B)}~1}$ valid case.
~ cxsmi

## Solution 4(Looks long but easiest solution)
We are given that both $n$ and $n + 48$ are squares of prime numbers. That is:
\[n = p^2 \quad \text{and} \quad n + 48 = q^2,\]
where $p$ and $q$ are prime numbers.
Then,
\[q^2 - p^2 = 48.\]
Factoring the left-hand side:
\[(q - p)(q + p) = 48.\]
Since both $q$ and $p$ are **primes**, their difference $q - p$ must be an even number (because except for 2, all primes are odd). So $q + p$ and $q - p$ are both even, and hence their product is divisible by 4 — consistent with 48.
Now, let’s list factor pairs of 48 where both factors are even (since sum and difference of two odd primes are even):
\[(2, 24),\ (4, 12),\ (6, 8)\]
These correspond to:
1. 1. ,
1. 1. ,
1. 1. ,
1. 1. $q - p = 2$ , $q + p = 24$
Solving: Add: $2q = 26 \Rightarrow q = 13 \Rightarrow p = 11$ Then:
\[n = p^2 = 121,\quad n + 48 = q^2 = 169\]
Both 121 and 169 are perfect squares of primes.
1. 2. ,
1. 2. ,
1. 2. ,
1. 2. $q - p = 4$ , $q + p = 12$
Add: $2q = 16 \Rightarrow q = 8$ , but 8 is not prime
1. 3. ,
1. 3. ,
1. 3. ,
1. 3. $q - p = 6$ , $q + p = 8$
Add: $2q = 14 \Rightarrow q = 7,\ p = 1$ , but 1 is not prime
Only one valid pair works.
---
1. Final Answer:
1. Final Answer:
1. Final Answer:
\[\boxed{\textbf{(B)}~1}\]
There is only 1 valid pair $(p, q) = (11, 13)$ such that both $p^2$ and $q^2$ differ by 48 and are squares of prime numbers*
~Ak
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .