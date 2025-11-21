# 2004 AMC 10B Problem 11

## Problem

Two eight-sided dice each have faces numbered $1$ through $8$ . When the dice are rolled, each face has an equal probability of appearing on the top. What is the probability that the product of the two top numbers is greater than their sum?

$\mathrm{(A)\ }\frac{1}{2}\qquad\mathrm{(B)\ }\frac{47}{64}\qquad\mathrm{(C)\ }\frac{3}{4}\qquad\mathrm{(D)\ }\frac{55}{64}\qquad\mathrm{(E)\ }\frac{7}{8}$

## Solution 1
We have $1\times n = n < 1 + n$ , hence if at least one of the numbers is $1$ , the sum is larger. There $15$ such possibilities.
We have $2\times 2 = 2+2$ .
For $n>2$ we already have $2\times n = n + n > 2 + n$ , hence all other cases are good.
Out of the $8\times 8$ possible cases, we find that in $15+1=16$ the sum is greater than or equal to the product, hence in $64-16=48$ cases the sum is smaller, satisfying the condition. Therefore the answer is $\frac{48}{64}=\boxed{\mathrm{(C)\ }\frac{3}{4}}$ .

## Solution 2
Let the two rolls be $m$ , and $n$ .
From the restriction: $mn > m + n$
$mn - m - n > 0$
$mn - m - n + 1 > 1$
$(m-1)(n-1) > 1$
Since $m-1$ and $n-1$ are non-negative integers between $1$ and $8$ , either $(m-1)(n-1) = 0$ , $(m-1)(n-1) = 1$ , or $(m-1)(n-1) > 1$
$(m-1)(n-1) = 0$ if and only if $m=1$ or $n=1$ .
There are $8$ ordered pairs $(m,n)$ with $m=1$ , $8$ ordered pairs with $n=1$ , and $1$ ordered pair with $m=1$ and $n=1$ . So, there are $8+8-1 = 15$ ordered pairs $(m,n)$ such that $(m-1)(n-1) = 0$ .
$(m-1)(n-1) = 1$ if and only if $m-1=1$ and $n-1=1$ or equivalently $m=2$ and $n=2$ . This gives $1$ ordered pair $(m,n) = (2,2)$ .
So, there are a total of $15+1=16$ ordered pairs $(m,n)$ with $(m-1)(n-1) < 1$ .
Since there are a total of $8\cdot8 = 64$ ordered pairs $(m,n)$ , there are $64-16 = 48$ ordered pairs $(m,n)$ with $(m-1)(n-1) > 1$ .
Thus, the desired probability is $\frac{48}{64}=\boxed{\mathrm{(C)\ }\frac{3}{4}}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .