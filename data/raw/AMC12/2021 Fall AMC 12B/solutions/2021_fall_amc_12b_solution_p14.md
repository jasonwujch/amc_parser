# 2021 Fall AMC 12B Problem 14

## Problem

Suppose that $P(z), Q(z)$ , and $R(z)$ are polynomials with real coefficients, having degrees $2$ , $3$ , and $6$ , respectively, and constant terms $1$ , $2$ , and $3$ , respectively. Let $N$ be the number of distinct complex numbers $z$ that satisfy the equation $P(z) \cdot Q(z)=R(z)$ . What is the minimum possible value of $N$ ?

$\textbf{(A)}\: 0\qquad\textbf{(B)} \: 1\qquad\textbf{(C)} \: 2\qquad\textbf{(D)} \: 3\qquad\textbf{(E)} \: 5$

## Solution
The answer cannot be $0,$ as every nonconstant polynomial has at least $1$ distinct complex root (Fundamental Theorem of Algebra). Since $P(z) \cdot Q(z)$ has degree $2 + 3 = 5,$ we conclude that $R(z) - P(z)\cdot Q(z)$ has degree $6$ and is thus nonconstant.
It now suffices to illustrate an example for which $N = 1$ : Take \begin{align*} P(z)&=z^2+1, \\ Q(z)&=z^3+2, \\ R(z)&=(z+1)^6 + P(z) \cdot Q(z). \end{align*} Note that $R(z)$ has degree $6$ and constant term $3,$ so it satisfies the conditions.
We need to find the solutions to \begin{align*} P(z) \cdot Q(z) &= (z+1)^6 + P(z) \cdot Q(z) \\ 0 &= (z+1)^6. \end{align*} Clearly, the only distinct complex root is $-1,$ so our answer is $N=\boxed{\textbf{(B)} \: 1}.$
~kingofpineapplz ~kgator

## Video Solution
https://youtu.be/HLhetkPGfX4
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .