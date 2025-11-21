# 2011 AMC 10B Problem 10

## Problem

Consider the set of numbers $\{1, 10, 10^2, 10^3, \ldots, 10^{10}\}$ . The ratio of the largest element of the set to the sum of the other ten elements of the set is closest to which integer?

$\textbf{(A)}\ 1 \qquad\textbf{(B)}\ 9 \qquad\textbf{(C)}\ 10 \qquad\textbf{(D)}\ 11 \qquad\textbf{(E)} 101$

## Solution 1
The requested ratio is \[\dfrac{10^{10}}{10^9 + 10^8 + \ldots + 10 + 1}.\] Using the formula for a geometric series, we have \[10^9 + 10^8 + \ldots + 10 + 1 = \dfrac{10^{10} - 1}{10 - 1} = \dfrac{10^{10} - 1}{9},\] which is very close to $\dfrac{10^{10}}{9},$ so the ratio is very close to $\boxed{\mathrm{(B) \ } 9}.$

## Solution 2
The problem asks for the value of \[\dfrac{10^{10}}{10^9 + 10^8 + \ldots + 10 + 1}.\] Written in base 10, we can find the value of $10^9 + 10^8 + \ldots + 10 + 1$ to be $1111111111.$ Long division gives us the answer to be $\boxed{\mathrm{(B) \ } 9}.$
Alternate finish: multiply the denominator by 9 and notice that it is 1 less than $10^{10}$ . So the answer is very very close to $\boxed{\mathrm{(B) } 9}$ .
~JH. L

## Solution 3
Let $f(n)=\dfrac{10^n}{1+10+10^2+10^3+\cdots+10^{n-1}}$ . We are approximating $f(10)$ . Trying several small values of $n$ gives answers very close to $9$ , so our answer is $\boxed{\textbf{(B)}~9}$ . Note that $f(1)=10$ , but $f(2)=\dfrac{100}{11}\approx9.09.$ ~Technodoggo
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .