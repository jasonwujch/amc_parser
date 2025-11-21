# 2012 AIME I Problem 15

## Problem

There are $n$ mathematicians seated around a circular table with $n$ seats numbered $1,$ $2,$ $3,$ $...,$ $n$ in clockwise order. After a break they again sit around the table. The mathematicians note that there is a positive integer $a$ such that

Find the number of possible values of $n$ with $1 < n < 1000.$

## Solution
It is a well-known fact that the set $0, a, 2a, ... (n-1)a$ forms a complete set of residues if and only if $a$ is relatively prime to $n$ .
Thus, we have $a$ is relatively prime to $n$ . In addition, for any seats $p$ and $q$ , we must have $ap - aq$ not be equivalent to either $p - q$ or $q - p$ modulo $n$ to satisfy our conditions. These simplify to $(a-1)p \not\equiv (a-1)q$ and $(a+1)p \not\equiv (a+1)q$ modulo $n$ , so multiplication by both $a-1$ and $a+1$ must form a complete set of residues mod $n$ as well.
Thus, we have $a-1$ , $a$ , and $a+1$ are relatively prime to $n$ . We must find all $n$ for which such an $a$ exists. $n$ obviously cannot be a multiple of $2$ or $3$ , but for any other $n$ , we can set $a = n-2$ , and then $a-1 = n-3$ and $a+1 = n-1$ . All three of these will be relatively prime to $n$ , since two numbers $x$ and $y$ are relatively prime if and only if $x-y$ is relatively prime to $x$ . In this case, $1$ , $2$ , and $3$ are all relatively prime to $n$ , so $a = n-2$ works.
Now we simply count all $n$ that are not multiples of $2$ or $3$ , which is easy using inclusion-exclusion. We get a final answer of $998 - (499 + 333 - 166) = \boxed{332}$ .
Note: another way to find that $(a-1)$ and $(a+1)$ have to be relative prime to $n$ is the following: start with $ap-aq \not \equiv \pm(p-q) \pmod n$ . Then, we can divide by $p-q$ to get $a \not \equiv \pm 1$ modulo $\frac{n}{\gcd(n, p-q)}$ . Since $\gcd(n, p-q)$ ranges through all the divisors of $n$ , we get that $a \not \equiv \pm 1$ modulo the divisors of $n$ or $\gcd(a-1, n) = \gcd(a+1, n) = 1$ .

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/355
~ dolphin7
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .