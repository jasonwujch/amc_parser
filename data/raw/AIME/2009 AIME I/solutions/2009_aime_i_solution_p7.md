# 2009 AIME I Problem 7

## Problem

The sequence $(a_n)$ satisfies $a_1 = 1$ and $5^{(a_{n + 1} - a_n)} - 1 = \frac {1}{n + \frac {2}{3}}$ for $n \geq 1$ . Let $k$ be the least integer greater than $1$ for which $a_k$ is an integer. Find $k$ .

## Solution
The best way to solve this problem is to get the iterated part out of the exponent: \[5^{(a_{n + 1} - a_n)} = \frac {1}{n + \frac {2}{3}} + 1\] \[5^{(a_{n + 1} - a_n)} = \frac {n + \frac {5}{3}}{n + \frac {2}{3}}\] \[5^{(a_{n + 1} - a_n)} = \frac {3n + 5}{3n + 2}\] \[a_{n + 1} - a_n = \log_5{\left(\frac {3n + 5}{3n + 2}\right)}\] \[a_{n + 1} - a_n = \log_5{(3n + 5)} - \log_5{(3n + 2)}\] Plug in $n = 1, 2, 3, 4$ to see the first few terms of the sequence: \[\log_5{5},\log_5{8}, \log_5{11}, \log_5{14}.\] We notice that the terms $5, 8, 11, 14$ are in arithmetic progression. Since $a_1 = 1 = \log_5{5} = \log_5{(3(1) + 2)}$ , we can easily use induction to show that $a_n = \log_5{(3n + 2)}$ . So now we only need to find the next value of $n$ that makes $\log_5{(3n + 2)}$ an integer. This means that $3n + 2$ must be a power of $5$ . We test $25$ : \[3n + 2 = 25\] \[3n = 23\] This has no integral solutions, so we try $125$ : \[3n + 2 = 125\] \[3n = 123\] \[n = \boxed{041}\]

## Solution 2 (Telescoping)
We notice that by multiplying the equation from an arbitrary $a_n$ all the way to $a_1$ , we get: \[5^{a_n-a_1}=\dfrac{n+\tfrac23}{1+\tfrac23}\] This simplifies to \[5^{a_n}=3n+2.\] We can now test powers of $5$ .
$5$ - that gives us $n=1$ , which is useless.
$25$ - that gives a non-integer $n$ .
$125$ - that gives $n=\boxed{41}$ .
-integralarefun

## Solution 3 (I did too many FE's)
The given recursion is equivalent to $\frac{5^{a_{n+1}}}{3(n+1)+2}=\frac{5^{a_n}}{3n+2}$ . By a simple inductive argument, the value $\frac{5^{a_k}}{3k+2}$ is constant for all naturals $k$ . In particular, when $k=1$ , the expression is equal to $1$ , so $\frac{5^{a_k}}{3k+2}=1$ for all naturals $k$ . Therefore, $a_k=\log_5(3k+2)$ , and testing powers of $5$ yields $k=\boxed{41}$ as the answer, which is when $a_{41}=\log_5(3\cdot41+2)=\log_5(125)=3$ .
~ eevee9406
These problems are copyrighted © by the Mathematical Association of America.