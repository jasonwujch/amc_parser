# 2005 AIME II Problem 3

## Problem

An infinite geometric series has sum 2005. A new series, obtained by squaring each term of the original series, has 10 times the sum of the original series. The common ratio of the original series is $\frac mn$ where $m$ and $n$ are relatively prime integers . Find $m+n.$

## Solution 1
Let's call the first term of the original geometric series $a$ and the common ratio $r$ , so $2005 = a + ar + ar^2 + \ldots$ . Using the sum formula for infinite geometric series, we have $\;\;\frac a{1 -r} = 2005$ . Then we form a new series, $a^2 + a^2 r^2 + a^2 r^4 + \ldots$ . We know this series has sum $20050 = \frac{a^2}{1 - r^2}$ . Dividing this equation by $\frac{a}{1-r}$ , we get $10 = \frac a{1 + r}$ . Then $a = 2005 - 2005r$ and $a = 10 + 10r$ so $2005 - 2005r = 10 + 10r$ , $1995 = 2015r$ and finally $r = \frac{1995}{2015} = \frac{399}{403}$ , so the answer is $399 + 403 = \boxed{802}$ .
(We know this last fraction is fully reduced by the Euclidean algorithm -- because $4 = 403 - 399$ , $\gcd(403, 399) | 4$ . But 403 is odd , so $\gcd(403, 399) = 1$ .)

## Solution 2
We can write the sum of the original series as $a + a\left(\dfrac{m}{n}\right) + a\left(\dfrac{m}{n}\right)^2 + \ldots = 2005$ , where the common ratio is equal to $\dfrac{m}{n}$ . We can also write the sum of the second series as $a^2 + a^2\left(\dfrac{m}{n}\right)^2 + a^2\left(\left(\dfrac{m}{n}\right)^2\right)^2 + \ldots = 20050$ . Using the formula for the sum of an infinite geometric series $S=\dfrac{a}{1-r}$ , where $S$ is the sum of the sequence, $a$ is the first term of the sequence, and $r$ is the ratio of the sequence, the sum of the original series can be written as $\dfrac{a}{1-\frac{m}{n}}=\dfrac{a}{\frac{n-m}{n}}=\dfrac{a \cdot n}{n-m}=2005\;\text{(1)}$ , and the second sequence can be written as $\dfrac{a^2}{1-\frac{m^2}{n^2}}=\dfrac{a^2}{\frac{n^2-m^2}{n^2}}=\dfrac{a^2\cdot n^2}{(n+m)(n-m)}=20050\;\text{(2)}$ . Dividing $\text{(2)}$ by $\text{(1)}$ , we obtain $\dfrac{a\cdot n}{m+n}=10$ , which can also be written as $a\cdot n=10(m+n)$ . Substitute this value for $a\cdot n$ back into $\text{(1)}$ , we obtain $10\cdot \dfrac{n+m}{n-m}=2005$ . Dividing both sides by 10 yields $\dfrac{n+m}{n-m}=\dfrac{401}{2}$ we can now write a system of equations with $n+m=401$ and $n-m=2$ , but this does not output integer solutions. However, we can also write $\dfrac{n+m}{n-m}=\dfrac{401}{2}$ as $\dfrac{n+m}{n-m}=\dfrac{802}{4}$ . This gives the system of equations $m+n=802$ and $n-m=4$ , which does have integer solutions. Our answer is therefore $m+n=\boxed{802}$ (Solving for $m$ and $n$ gives us $399$ and $403$ , respectively, which are co-prime).

## Video Solution
https://youtu.be/z4-bFo2D3TU?list=PLZ6lgLajy7SZ4MsF6ytXTrVOheuGNnsqn&t=4500 - AMBRIGGS

## Video Solution by OmegaLearn
https://youtu.be/3wNLfRyRrMo?t=383
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.