# 2007 AIME I Problem 7

## Problem

Let $N = \sum_{k = 1}^{1000} k ( \lceil \log_{\sqrt{2}} k \rceil - \lfloor \log_{\sqrt{2}} k \rfloor )$

Find the remainder when $N$ is divided by 1000. ( $\lfloor{k}\rfloor$ is the greatest integer less than or equal to $k$ , and $\lceil{k}\rceil$ is the least integer greater than or equal to $k$ .)

## Solution
The ceiling of a number minus the floor of a number is either equal to zero (if the number is an integer ); otherwise, it is equal to 1. Thus, we need to find when or not $\log_{\sqrt{2}} k$ is an integer.
The change of base formula shows that $\frac{\log k}{\log \sqrt{2}} = \frac{2 \log k}{\log 2}$ . For the $\log 2$ term to cancel out, $k$ is a power of $2$ . Thus, $N$ is equal to the sum of all the numbers from 1 to 1000, excluding all powers of 2 from $2^0 = 1$ to $2^9 = 512$ .
The formula for the sum of an arithmetic sequence and the sum of a geometric sequence yields that our answer is $\left[\frac{(1000 + 1)(1000)}{2} - (1 + 2 + 2^2 + \ldots + 2^9)\right] \mod{1000}$ .
Simplifying, we get $\left[1000\left(\frac{1000+1}{2}\right) -1023\right] \mod{1000} \equiv [500-23] \mod{1000} \equiv 477 \mod{1000}.$ The answer is $\boxed{477}$
- Logarithm
These problems are copyrighted © by the Mathematical Association of America.