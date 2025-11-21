# 2018 AMC 10B Problem 23

## Problem

How many ordered pairs $(a, b)$ of positive integers satisfy the equation \[a\cdot b + 63 = 20\cdot \text{lcm}(a, b) + 12\cdot\text{gcd}(a,b),\] where $\text{gcd}(a,b)$ denotes the greatest common divisor of $a$ and $b$ , and $\text{lcm}(a,b)$ denotes their least common multiple?

$\textbf{(A)} \text{ 0} \qquad \textbf{(B)} \text{ 2} \qquad \textbf{(C)} \text{ 4} \qquad \textbf{(D)} \text{ 6} \qquad \textbf{(E)} \text{ 8}$

## Solution
Let $x = \text{lcm}(a, b)$ , and $y = \text{gcd}(a, b)$ . Therefore, $a\cdot b = \text{lcm}(a, b)\cdot \text{gcd}(a, b) = x\cdot y$ . Thus, the equation becomes
\[x\cdot y + 63 = 20x + 12y\] \[x\cdot y - 20x - 12y + 63 = 0\]
Using Simon's Favorite Factoring Trick , we rewrite this equation as
\[(x - 12)(y - 20) - 240 + 63 = 0\] \[(x - 12)(y - 20) = 177\]
Since $177 = 3\cdot 59$ and $x > y$ , we have $x - 12 = 59$ and $y - 20 = 3$ , or $x - 12 = 177$ and $y - 20 = 1$ . This gives us the solutions $(71, 23)$ and $(189, 21)$ . Since the $\text{GCD}$ must be a divisor of the $\text{LCM}$ , the first pair does not work. Assume $a>b$ . We must have $a = 21 \cdot 9$ and $b = 21$ , and we could then have $a<b$ , so there are $\boxed{\textbf{(B)} ~2}$ solutions. (awesomeag)
Edited by IronicNinja, Firebolt360, and mprincess0229~

## Video Solution by OmegaLearn
https://youtu.be/zfChnbMGLVQ?t=494
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=JWGHYUeOx-k
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .