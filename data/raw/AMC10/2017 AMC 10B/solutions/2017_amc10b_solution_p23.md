# 2017 AMC 10B Problem 23

## Problem

Let $N=123456789101112\dots4344$ be the $79$ -digit number that is formed by writing the integers from $1$ to $44$ in order, one after the other. What is the remainder when $N$ is divided by $45$ ?

$\textbf{(A)}\ 1\qquad\textbf{(B)}\ 4\qquad\textbf{(C)}\ 9\qquad\textbf{(D)}\ 18\qquad\textbf{(E)}\ 44$

## Solution 1
We only need to find the remainders of N when divided by 5 and 9 to determine the answer. By inspection, $N \equiv 4 \text{ (mod 5)}$ . The remainder when $N$ is divided by $9$ is $1+2+3+4+ \cdots +1+0+1+1 +1+2 +\cdots + 4+3+4+4$ , but since $10 \equiv 1 \text{ (mod 9)}$ , we can also write this as $1+2+3 +\cdots +10+11+12+ \cdots 43 + 44 = \frac{44 \cdot 45}2 = 22 \cdot 45$ , which has a remainder of 0 mod 9. Solving these modular congruence using the Chinese Remainder Theorem we get the remainder to be $9 \pmod{45}$ . Therefore, the answer is $\boxed{\textbf{(C) } 9}$ .

## Alternative Ending to Solution 1
Once we find our 2 modular congruences, we can narrow our options down to ${C}$ and ${D}$ because the remainder when $N$ is divided by $45$ should be a multiple of 9 by our modular congruence that states $N$ has a remainder of $0$ when divided by $9$ . Also, our other modular congruence states that the remainder when divided by $45$ should have a remainder of $4$ when divided by $5$ . Out of options $C$ and $D$ , only $\boxed{\textbf{(C) } 9}$ satisfies that the remainder when $N$ is divided by $45 \equiv 4 \text{ (mod 5)}$ .

## Solution 2
Realize that $10 \equiv 10 \cdot 10 \equiv 10^{k} \pmod{45}$ for all positive integers $k$ .
Apply this on the expanded form of $N$ : \[N = 1(10)^{78} + 2(10)^{77} + \cdots + 9(10)^{70} + 10(10)^{68} + 11(10)^{66} + \cdots + 43(10)^{2} + 44 \equiv\] \[10(1 + 2 + \cdots + 43) + 44 \equiv 10 \left (\frac{43 \cdot 44}2 \right ) + 44 \equiv\] \[10 \left (\frac{-2 \cdot -1}2 \right ) - 1 \equiv \boxed{\textbf{(C) } 9} \pmod{45}\]

## Solution 3 (Clever way using divisibility rules)
We know that $45 = 5 \cdot 9$ , so we can apply our restrictions to that. We know that the units digit must be $5$ or $0$ , and the digits must add up to a multiple of $9$ . $1+2+3+4+\cdots + 44 = \frac{44 \cdot 45}{2}$ . We can quickly see this is a multiple of $9$ because $\frac{44}{2} \cdot 45 = 22 \cdot 45$ . We know $123 \ldots 4344$ is not a multiple of $5$ because the units digit isn't $5$ or $0$ . We can just subtract by 9 until we get a number whose units digit is 5 or 0.
We have $123 \ldots 4344$ is divisible by $9$ , so we can subtract by $9$ to get $123 \ldots 4335$ and we know that this is divisible by 5. So our answer is $\boxed{\textbf{(C) } 9}$
~Arcticturn

## Solution 4
Since $N$ ends with the number $4$ , $N\equiv 4\pmod 5$ . Also, the sum of the digits of $N$ are divisible by $9$ , so $N$ must be divisible by $9$ . Therefore, we have the system of equations:
According to the second equation, $N\equiv \{0, 9, 18, 27, 36\} \pmod {45}$ . The only one of these solutions that is $4\pmod 5$ is $\boxed{\textbf{(C) } 9}$ ~ sid2012
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .