# 2018 AMC 10B Problem 13

## Problem

How many of the first $2018$ numbers in the sequence $101, 1001, 10001, 100001, \dots$ are divisible by $101$ ?

$\textbf{(A) }253 \qquad \textbf{(B) }504 \qquad \textbf{(C) }505 \qquad \textbf{(D) }506 \qquad \textbf{(E) }1009 \qquad$

## Solution 1
The number $10^n+1$ is divisible by 101 if and only if $10^n\equiv -1\pmod{101}$ . We note that $(10,10^2,10^3,10^4)\equiv (10,-1,-10,1)\pmod{101}$ , so the powers of 10 are 4-periodic mod 101.
It follows that $10^n\equiv -1\pmod{101}$ if and only if $n\equiv 2\pmod 4$ .
In the given list, $10^2+1,10^3+1,10^4+1,\dots,10^{2019}+1$ , the desired exponents are $2,6,10,\dots,2018$ , and there are $\dfrac{2020}{4}=\boxed{\textbf{(C) } 505}$ numbers in that list.

## Solution 2 (Similar to solution 1)
Note that $10^{2k}+1$ for some odd $k$ will satisfy $10^{2k}+1 \equiv -1\pmod {101}$ . Each $2k \in \{2,6,10,\dots,2018\}$ , so the answer is $\boxed{\textbf{(C) } 505}$

## Solution 3
If we divide each number by $101$ , we see a pattern occuring in every 4 numbers. $101, 1000001, 10000000001, \dots$ . We divide $2018$ by $4$ to get $504$ with $2$ left over. Looking at our pattern of four numbers from above, the first number is divisible by $101$ . This means that the first of the $2$ left over will be divisible by $101$ , so our answer is $\boxed{\textbf{(C) } 505}$ .

## Solution 4
Note that $909$ is divisible by $101$ , and thus $9999$ is too. We know that $101$ is divisible and $1001$ isn't so let us start from $10001$ . We subtract $9999$ to get 2. Likewise from $100001$ we subtract, but we instead subtract $9999$ times $10$ or $99990$ to get $11$ . We do it again and multiply the 9's by $10$ to get $101$ . Following the same knowledge, we can use mod $101$ to finish the problem. The sequence will just be subtracting 1, multiplying by 10, then adding 1. Thus the sequence is ${0,-9,-99 ( 2),11, 0, ...}$ . Thus it repeats every four. Consider the sequence after the 1st term and we have 2017 numbers. Divide $2017$ by four to get $504$ remainder $1$ . Thus the answer is $504$ plus the 1st term or $\boxed{\textbf{(C) } 505}$ .

## Solution 5
Note that $101=x^2+1$ and $100...0001=x^n+1$ , where $x=10$ . We have that $\frac{x^n+1}{x^2+1}$ must have a remainder of $0$ . By the remainder theorem, the roots of $x^2+1$ must also be roots of $x^n+1$ . Plugging in $i,-i$ to $x^n+1$ yields that $n\equiv2\mod{4}$ . Because the sequence starts with $10^2+1$ , the answer is $\lceil 2018/4 \rceil=\boxed{\textbf{(C) } 505}$

## Solution 6 (Complex Numbers)
The $n$ th term of the sequence is $10^n+1$ for $n\ge 2$ (since $10^2+1=101$ , $10^3+1=1001$ , etc.). We seek those $n$ for which \[101 \mid (10^n+1).\] Let $x = 10$ . Note that $101=10^2+1$ , so this is equivalent to the polynomial divisibility
\[x^2+1 \mid x^n+1\]
Over $\mathbb{C}$ , $x^2+1$ has roots $i,-i$ . Thus $x^2+1 \mid x^n+1$ if both $i,-i$ are roots of $x^n+1$ , since, $i^n=-1 \quad \text{and} \quad (-i)^n=-1.$ Because $i^4=1$ , we have $i^n=-1$ exactly when $n\equiv 2 \pmod{4}$ . For such $n$ , $(-i)^n=(-1)^n i^n=i^n=-1$ as well, so the condition holds precisely when $n \equiv 2 \pmod{4}.$
Among the first $2018$ terms of the sequence (which correspond to $n=2,3,\dots,2019$ ), the values of $n$ congruent to $2 \pmod{4}$ are $2,6,10,\dots,2018$ . This is an arithmetic progression with common difference $4$ ; the count is
$\frac{2018-2}{4}+1=\frac{2016}{4}+1=504+1=505$ . Therefore, exactly $\boxed{505}$ of the first $2018$ numbers are divisible by $101$ , which corresponds to choice $\boxed{\textbf{(C)}}$ .
~ Aeioujyot
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .