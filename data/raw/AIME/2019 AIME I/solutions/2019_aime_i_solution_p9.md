# 2019 AIME I Problem 9

## Problem

Let $\tau(n)$ denote the number of positive integer divisors of $n$ . Find the sum of the six least positive integers $n$ that are solutions to $\tau (n) + \tau (n+1) = 7$ .

## Solution
In order to obtain a sum of $7$ , we must have:
- either a number with $5$ divisors ( a fourth power of a prime ) and a number with $2$ divisors ( a prime ), or
- a number with $4$ divisors ( a semiprime or a cube of a prime ) and a number with $3$ divisors ( a square of a prime ). (No integer greater than $1$ can have fewer than $2$ divisors.)
Since both of these cases contain a number with an odd number of divisors, that number must be an even power of a prime. These can come in the form of a square-like $3^2$ with $3$ divisors, or a fourth power like $2^4$ with $5$ divisors. We then find the smallest such values by hand.
- $2^2$ has two possibilities: $3$ and $4$ or $4$ and $5$ . Neither works.
- $3^2$ has two possibilities: $8$ and $9$ or $9$ and $10$ . $\boxed{(8,9)}$ and $\boxed{(9,10)}$ both work.
- $2^4$ has two possibilities: $15$ and $16$ or $16$ and $17$ . Only $\boxed{(16,17)}$ works.
- $5^2$ has two possibilities: $24$ and $25$ or $25$ and $26$ . Only $\boxed{(25,26)}$ works.
- $7^2$ has two possibilities: $48$ and $49$ or $49$ and $50$ . Neither works.
- $3^4$ has two possibilities: $80$ and $81$ or $81$ and $82$ . Neither works.
- $11^2$ has two possibilities: $120$ and $121$ or $121$ and $122$ . Only $\boxed{(121,122)}$ works.
- $13^2$ has two possibilities: $168$ and $169$ or $169$ and $170$ . Neither works.
- $17^2$ has two possibilities: $288$ and $289$ or $289$ and $290$ . Neither works.
- $19^2$ has two possibilities: $360$ and $361$ or $361$ and $362$ . Only $\boxed{(361,362)}$ works.
Having computed the working possibilities, we take the sum of the corresponding values of $n$ : $8+9+16+25+121+361 = \boxed{\textbf{540}}$ . ~Kepy.
Possible improvement: since all primes $>2$ are odd, their fourth powers are odd as well, which cannot be adjacent to any primes because both of the adjacent numbers will be even. Thus, we only need to check $16$ for the fourth power case. - mathleticguyyy

## Solution 2
Let the ordered pair $(a,b)$ represent the number of divisors of $n$ and $n+1$ respectively. We see that to obtain a sum of $7$ , we can have $(2,5), (3,4), (4,3),$ and $(5,2)$ .
Case 1: When we have $(2,5)$ For $n$ to have 2 divisors, it must be a prime number. For $n+1$ to have 5 divisors, it must be in the form $a^4$ . If $n+1$ is in the form $a^4$ , then $n = a^4-1 = (a^2+1)(a-1)(a+1)$ . This means that $n$ , or $a^4-1$ has factors other than 1 and itself; $n$ is not prime. No cases work in this case
Case 2: When we have $(4,3)$ For $n$ to have 4 divisors, it must be in the form $a^3$ or $ab$ , where $a$ and $b$ are distinct prime numbers . For $n+1$ to have 3 divisors, it must be a square number. Let $n+1 = A^2$ ( $A$ is a prime number). When $n = a^3, a^3+1 = A^2, (A-1)(A+1)=a^3$ . We see that the only case when it works is when $a=2, A=3$ , so $n=8$ works.
Case 3: When we have $(5,2)$ For $n$ to have 5 divisors, it must be in the form $a^4$ , where $a$ is a prime number. For $n+1$ to have 2 divisors, it must be a prime number. Notice that $a$ and $a^4$ have the same parity (even/odd). Since every prime greater than 2 are odd, $n = a^4$ must be even. Since $a^4$ is even, $a$ must be even as well, and the only prime number that is even is 2. When $a=2, n=16$ .
Case 4: When we have $(3,4)$ For $n$ to have 3 divisors, it must be a square number. For $n+1$ to have 4 divisors, it must be in the form $a^3$ or $ab$ , where $a$ and $b$ are distinct prime numbers. Similar to Case 2, let $n = A^2$ ( $A$ is a prime number).
- When $n+1 = a^3, A^2+1 = a^3$ .
There are no cases that satisfy this equation.
- When $n+1=ab, A^2+1 = ab$ .
We test squares of primes to find values of n that work.
- $A=2$ , $4+1=5$ . Doesn't work.
- $A=3$ , $9+1=10=2*5$ . It works. $n=9$
- $A=5$ , $25+1=26=2*13$ . It works. $n=25$
- $A=7$ , $49+1=50=2*5^2$ . Doesn't work.
- $A=11$ , $121+1=122=2*61$ . It works. $n=121$
- $A=13$ , $169+1=170=2*5*17$ . Doesn't work
- $A=17$ , $289+1=290=2*5*29$ . Doesn't work
- $A=19$ , $361+1=362=2*181$ . It works. $n=361$
Now we add up the values of $n$ to get the answer: $8+16+9+25+121+361 = \boxed{540}$ . ~toastybaker

## Solution 3 (Official MAA)
Let $p,\,q,$ and $r$ represent primes. Because $\tau(n)=1$ only for $n=1,$ there is no $n$ for which $\{\tau(n),\tau(n+1)\}=\{1,6\}$ . If $\{\tau(n),\tau(n+1)\}=\{2,5\},$ then $\{n,n+1\}=\{p,q^4\},$ so $|p-q^4|=1.$ Checking $q=2$ and $p=17$ yields the solution $n=16.$ If $q>2,$ then $q$ is odd, and $p=q^4\pm 1$ is even, so $p$ cannot be prime.
If $\{\tau(n),\tau(n+1)\}=\{3,4\},$ then $\{n,n+1\}=\{p^2,q^3\}$ or $\{p^2,qr\}.$ Consider $|p^2-q^3|=1.$ If $p^2-1=(p-1)(p+1)=q^3,$ Then $q=2.$ This yields the solution $p=3$ and $q=2,$ so $n=8.$ If $q^3-1=(q-1)(q^2+q+1)=p^2,$ then $q-1=1,$ which does not give a solution. Consider $|p^2-qr|=1.$ If $p^2-1=(p-1)(p+1)=qr,$ then if $p>2,$ the left side is divisible by 8, so there are no solutions. Finding the smallest four primes such that $p^2+1=qr$ gives $3^2+1=10,\,5^2+1=26,\,11^2+1=122,$ and $19^2+1=362.$ The six least values of $n$ are $8,9,16,25,121,$ and $361,$ whose sum is $540.$

## Video Solution
https://www.youtube.com/watch?v=2ouOexOnG1A
~ North America Math COntest Go Go Go
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .