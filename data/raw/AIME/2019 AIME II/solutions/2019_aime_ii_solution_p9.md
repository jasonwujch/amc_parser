# 2019 AIME II Problem 9

## Problem

Call a positive integer $n$ $k$ - pretty if $n$ has exactly $k$ positive divisors and $n$ is divisible by $k$ . For example, $18$ is $6$ -pretty. Let $S$ be the sum of positive integers less than $2019$ that are $20$ -pretty. Find $\tfrac{S}{20}$ .

## Solution 1
Every 20-pretty integer can be written in form $n = 2^a 5^b k$ , where $a \ge 2$ , $b \ge 1$ , $\gcd(k,10) = 1$ , and $d(n) = 20$ , where $d(n)$ is the number of divisors of $n$ . Thus, we have $20 = (a+1)(b+1)d(k)$ , using the fact that the divisor function is multiplicative. As $(a+1)(b+1)$ must be a divisor of 20, there are not many cases to check.
If $a+1 = 4$ , then $b+1 = 5$ . But this leads to no solutions, as $(a,b) = (3,4)$ gives $2^3 5^4 > 2019$ .
If $a+1 = 5$ , then $b+1 = 2$ or $4$ . The first case gives $n = 2^4 \cdot 5^1 \cdot p$ where $p$ is a prime other than 2 or 5. Thus we have $80p < 2019 \implies p = 3, 7, 11, 13, 17, 19, 23$ . The sum of all such $n$ is $80(3+7+11+13+17+19+23) = 7440$ . In the second case $b+1 = 4$ and $d(k) = 1$ , and there is one solution $n = 2^4 \cdot 5^3 = 2000$ .
If $a+1 = 10$ , then $b+1 = 2$ , but this gives $2^9 \cdot 5^1 > 2019$ . No other values for $a+1$ work.
Then we have $\frac{S}{20} = \frac{80(3+7+11+13+17+19+23) + 2000}{20} = 372 + 100 = \boxed{472}$ .
-scrabbler94

## Solution 2
For $n$ to have exactly $20$ positive divisors, $n$ can only take on certain prime factorization forms: namely, $p^{19}, p^9q, p^4q^3, p^4qr$ where $p,q,r$ are primes. No number that is a multiple of $20$ can be expressed in the first form because 20 has two primes in its prime factorization, while the first form has only one , and the only integer divisible by $20$ that has the second form is $2^{9}5$ , which is 2560, greater than $2019$ .
For the third form, the only $20$ -pretty numbers are $2^45^3=2000$ and $2^35^4=5000$ , and only $2000$ is small enough.
For the fourth form, any number of the form $2^45r$ where $r$ is a prime other than $2$ or $5$ will satisfy the $20$ -pretty requirement. Since $n=80r<2019$ , $r\le 25$ . Therefore, $r$ can take on $3, 7, 11, 13, 17, 19,$ or $23$ .
Thus, $\frac{S}{20}=\frac{2000+80(3+7+11+...+23)}{20}=100+4(3+7+11+...+23)=\boxed{472}$ .
Rephrased for clarity by Afly
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .