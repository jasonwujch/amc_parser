# 2009 AIME I Problem 8

## Problem

Let $S = \{2^0,2^1,2^2,\ldots,2^{10}\}$ . Consider all possible positive differences of pairs of elements of $S$ . Let $N$ be the sum of all of these differences. Find the remainder when $N$ is divided by $1000$ .

## Solution 1 (bash)
When computing $N$ , the number $2^x$ will be added $x$ times (for terms $2^x-2^0$ , $2^x-2^1$ , ..., $2^x - 2^{x-1}$ ), and subtracted $10-x$ times. Hence $N$ can be computed as $N=10\cdot 2^{10} + 8\cdot 2^9 + 6\cdot 2^8 + \cdots - 8\cdot 2^1 - 10\cdot 2^0$ . Evaluating $N \bmod {1000}$ yields:
\begin{align*} N & = 10(2^{10}-1) + 8(2^9 - 2^1) + 6(2^8-2^2) + 4(2^7-2^3) + 2(2^6-2^4) \\ & = 10(1023) + 8(510) + 6(252) + 4(120) + 2(48) \\ & = 10(1000+23) + 8(500+10) + 6(250+2) + 480 + 96 \\ & \equiv (0 + 230) + (0 + 80) + (500 + 12) + 480 + 96 \\ & \equiv \boxed{398} \end{align*}

## Solution 2
This solution can be generalized to apply when $10$ is replaced by other positive integers.
Extending from Solution 1, we get that the sum $N$ of all possible differences of pairs of elements in $S$ when $S = \{2^0,2^1,2^2,\ldots,2^{n}\}$ is equal to $\sum_{x=0}^{n} (2x-n) 2^x$ . Let $A = \sum_{x=0}^{n} x2^x$ , $B=\sum_{x=0}^{n} 2^x$ . Then $N=2A - nB$ .
For $n = 10$ , $B = 2^{11}-1 = 2047 \equiv 47 \pmod{1000}$ by the geometric sequence formula.
$2A = \sum_{x=1}^{n+1} (x-1)2^x$ , so $2A - A = A = n2^{n+1} - \sum_{x=1}^{n} 2^x$ . Hence, for $n = 10$ , $A = 10 \cdot 2^{11} - 2^{11} + 2 = 9 \cdot 2^{11} + 2 \equiv 48 \cdot 9 + 2 =$
$434 \pmod{1000}$ , by the geometric sequence formula and the fact that $2^{10} = 1024 \equiv 24 \pmod{1000}$ .
Thus, for $n = 10$ , $N = 2A - 10B \equiv 2\cdot 434 - 10\cdot 47 = 868 - 470 = \boxed{398}$ .

## Solution 3
Consider the unique differences $2^{a + n} - 2^a$ . Simple casework yields a sum of $\sum_{n = 1}^{10}(2^n - 1)(2^{11 - n} - 1) = \sum_{n = 1}^{10}2^{11} + 1 - 2^n - 2^{11 - n} = 10\cdot2^{11} + 10 - 2(2 + 2^2 + \cdots + 2^{10})$ $= 10\cdot2^{11} + 10 - 2^2(2^{10} - 1)\equiv480 + 10 - 4\cdot23\equiv\boxed{398}\pmod{1000}$ . This method generalizes nicely as well.

## Solution 4 (Extreme bash)
Find the positive differences in all $55$ pairs and you will get $\boxed{398}$ . (This is not recommended unless you can't find any other solutions to this problem)
List of Differences :
1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2, 6, 14, 30, 62, 126, 254, 510, 1022, 4, 12, 28, 60, 124, 252, 508, 1020, 8, 24, 56, 120, 248, 504, 1016, 16, 48, 112, 240, 496, 1008, 32, 96, 224, 480, 992, 64, 192, 448, 960, 128, 384, 896, 256, 768, 512
These problems are copyrighted © by the Mathematical Association of America.