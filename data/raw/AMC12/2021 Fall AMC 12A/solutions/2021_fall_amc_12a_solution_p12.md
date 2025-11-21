# 2021 Fall AMC 12A Problem 12

## Problem

What is the number of terms with rational coefficients among the $1001$ terms in the expansion of $\left(x\sqrt[3]{2}+y\sqrt{3}\right)^{1000}?$

$\textbf{(A)}\ 0 \qquad\textbf{(B)}\ 166 \qquad\textbf{(C)}\ 167 \qquad\textbf{(D)}\ 500 \qquad\textbf{(E)}\ 501$

## Solution 1
By the Binomial Theorem, each term in the expansion is of the form \[\binom{1000}{k}\left(x\sqrt[3]{2}\right)^k\left(y\sqrt{3}\right)^{1000-k}=\binom{1000}{k}2^{\frac k3}3^{\frac{1000-k}{2}}x^k y^{1000-k},\] where $k\in\{0,1,2,\ldots,1000\}.$
This problem is equivalent to counting the values of $k$ such that both $\frac k3$ and $\frac{1000-k}{2}$ are integers. Note that $k$ must be a multiple of $3$ and a multiple of $2,$ so $k$ must be a multiple of $6.$ There are $\boxed{\textbf{(C)}\ 167}$ such values of $k:$ \[6(0), 6(1), 6(2), \ldots, 6(166).\]
~MRENTHUSIASM

## Solution 2 (Rough Conceptual Approach)
Similar to Solution 1, however, instead of applying the Binomial Theorem, we can notice that it "takes" two $\;\sqrt{3}\;$ terms multiplied by each other to get a rational coefficient for $y$ and it "takes" three $\;\sqrt[3]{2}\;$ terms multiplied by each other to get a rational coefficient for $x$ . Since the only way to get a total rational coefficient (that results when you multiply the final coefficient of $y$ by that of for $x$ ) is for both $x$ 's and $y$ 's coefficients to be rational, we can notice that the solution simply comes down to the number of multiples of $6$ between $0$ and $1000$ , which turns out to be $\boxed{\textbf{(C)}\ 167}$ .
~satyam2009

## Video Solution by TheBeautyofMath
https://youtu.be/ToiOlqWz3LY?t=169
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .