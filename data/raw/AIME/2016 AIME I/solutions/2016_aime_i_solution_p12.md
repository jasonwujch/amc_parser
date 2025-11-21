# 2016 AIME I Problem 12

## Problem

Find the least positive integer $m$ such that $m^2 - m + 11$ is a product of at least four not necessarily distinct primes.

## Solution 1
$m(m-1)$ is the product of two consecutive integers, so it is always even. Thus $m(m-1)+11$ is odd and never divisible by $2$ . Thus any prime $p$ that divides $m^2-m+11$ must divide $4m^2-4m+44=(2m-1)^2+43$ . We see that $(2m-1)^2\equiv -43\pmod{p}$ . We can verify that $-43$ is not a perfect square mod $p$ for each of $p=3,5,7$ . Therefore, all prime factors of $m^2-m+11$ are $\ge 11$ .
Let $m^2 - m + 11 = pqrs$ for primes $11\le p \le q \le r \le s$ . From here, we could go a few different ways:

## Solution 1a
Suppose $p=11$ ; then $m^2-m+11=11qrs$ . Reducing modulo 11, we get $m\equiv 1,0 \pmod{11}$ so $k(11k\pm 1)+1 = qrs$ .
Suppose $q=11$ . Then we must have $11k^2\pm k + 1 = 11rs$ , which leads to $k\equiv \pm 1 \pmod{11}$ , i.e., $k\in \{1,10,12,21,23,\ldots\}$ .
$k=1$ leads to $rs=1$ (impossible)! Then $k=10$ leads to $rs=101$ , a prime (impossible). Finally, for $k=12$ we get $rs=143=11\cdot 13$ .
Thus our answer is $m=11k= \boxed{132}$ .

## Solution 1b
Let $m^2 - m + 11 = pqrs$ for primes $p, q, r, s\ge11$ . If $p, q, r, s = 11$ , then $m^2-m+11=11^4$ . We can multiply this by $4$ and complete the square to find $(2m-1)^2=4\cdot 11^4-43$ . But \[(2\cdot 11^2-1)^2=4\cdot 11^4-4\cdot 11^2+1 <4\cdot 11^4-43<(2\cdot 11^2)^2,\] hence we have pinned a perfect square $(2m-1)^2=4\cdot 11^4-43$ strictly between two consecutive perfect squares, a contradiction. Hence $pqrs \ge 11^3 \cdot 13$ . Thus $m^2-m+11\ge 11^3\cdot 13$ , or $(m-132)(m+131)\ge0$ . From the inequality, we see that $m \ge 132$ . $132^2 - 132 + 11 = 11^3 \cdot 13$ , so $m = \boxed{132}$ and we are done.

## Solution 2
First, we can show that $2,3,5,7$ $\not |$ $m^2 - m + 11$ . This can be done by just testing all residue classes.
For example, we can test $m \equiv 0 \mod 2$ or $m \equiv 1 \mod 2$ to show that $m^2 - m + 11$ is not divisible by 2.
Case 1: m = 2k
Case 2: m = 2k+1
Now, we can test $m^2 - m + 11 = 11^4$ , which fails, so we test $m^2 - m + 11 = 11^3 \cdot 13$ , and we get m = $132$ .
-AlexLikeMath

## Video Solution
https://youtu.be/KRleD8iDRhI
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .