# 2025 AMC 10B Problem 10

## Problem

Let $f(n)=n^3-5n^2+2n+8$ and $g(n)=n^3-6n^2+5n+12.$ What is the sum of all integers $n$ such that $\tfrac{f(n)}{g(n)}$ is an integer?

$\textbf{(A)}~2\qquad\textbf{(B)}~3\qquad\textbf{(C)}~4\qquad\textbf{(D)}~5\qquad\textbf{(E)}~6$

## Solution 1
Observe that both $f(n)$ and $g(n)$ can be factored using RZT. By trying out a few values, we get that $n = -1$ is a root of $f(n)$ . Then, we can use synthetic division (regular polynomial division works, too) to get the other roots of $f(n)$ , which are $n = 4$ and $n = 2$ . Now we factor $g(n)$ . By inspection, $n = -1$ also works on $g(n)$ , and so synthetic division and factoring the remaining quadratic gets us the roots $n = 3$ and $n = 4.$ We can now express $\frac{f(n)}{g(n)}$ as: \[\frac{(n + 1)(n - 4)(n - 2)}{(n + 1)(n - 4)(n - 3)}.\] We can cancel the top and bottom to get: \[\frac{(n - 2)}{(n - 3)}\]
Notice that the only values for which this expression is an integer are $n = 4$ and $n = 2$ , because they both cause the denominator to have a magnitude of $1$ . However, $n = 4$ is an extraneous solution as plugging it back into the original expression would make it evaluate to $\frac{0}{0}$ . Our answer is then $\boxed{\textbf{(A)}\hspace{3pt} 2}$ .
~Milkdrinker.
~Note by SixthGradeBookWorm927: 'RZT' is the Rational Zero Theorem, otherwise known as the Rational Root Theorem.

## Solution 2
We have $\frac{f(n)}{g(n)} = \frac{n^3-5n^2+2n+8}{n^3-6n^2+5n+12} = 1 + \frac{n^2-3n-4}{n^3-6n^2+5n+12}.$ We factor the numerator as $(n-4)(n+1)$ . Using synthetic division on the numerator's roots, we find that the denominator can be factored as $(n+1)(n-3)(n-4)$ .
Simplifying, we get $\frac{f(n)}{g(n)} = 1 + \frac{1}{n-3}$ . This tells us that we must not include the solutions $n=-1, 3,$ or $4$ , or the fraction will be undefined.
To have $\frac{1}{n-3}$ be an integer, $n-3 = 1$ or $-1$ . This would make $n = 2$ or $4$ . Remember, $4$ is not allowed, so we have only one possible value of $n=\boxed{\textbf{(A)} 2}$ . ~OlympiadMaster

## Video Solution 1 by SpreadTheMthLove
https://www.youtube.com/watch?v=dLSWVrrKsgs

## Video Solution (Fast and Easy)
https://www.youtube.com/watch?v=hFWxfehU_Qo&t=3s
~ Pi Academy
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .