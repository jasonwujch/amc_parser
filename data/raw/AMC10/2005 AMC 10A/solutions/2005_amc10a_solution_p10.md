# 2005 AMC 10A Problem 10

## Problem

There are two values of $a$ for which the equation $4x^2 + ax + 8x + 9 = 0$ has only one solution for $x$ . What is the sum of those values of $a$ ?

$\textbf{(A) } -16 \qquad\textbf{(B) } -8 \qquad\textbf{(C) } 0 \qquad\textbf{(D) } 8 \qquad\textbf{(E) } 20$

## Solution 1
A quadratic equation has exactly $1$ distinct root if and only if the left-hand side is a perfect square. So we require
\[4x^2 + ax + 8x + 9 = (mx + n)^2 = m^2 x^2 + 2mnx + n^2.\]
Two polynomials are equal only if their coefficients are equal, so we must have $m^2 = 4$ and $n^2 = 9$ , which reduce to $m = \pm 2$ and $n = \pm 3$ respectively. By equating $x$ -coefficients, it follows that $a + 8 = 2mn = \pm 2 \cdot 2\cdot 3 = \pm 12$ , so either $a = 12-8 = 4$ or $a = -12-8 = -20$ .
Accordingly, the desired sum is $4+(-20) = \boxed{\textbf{(A) } -16}$ .
(Alternatively, we can observe that whatever the $2$ values of $a$ are, they must lead to equations of the form $px^2 + qx + r = 0$ and $px^2 - qx + r = 0$ , corresponding to the perfect squares $\left(mx \pm n\right)^2 = 0$ . So the $2$ choices of $a$ , say $a_1$ and $a_2$ , must satisfy $a_1 + 8 = q$ and $a_2 + 8 = -q$ , and adding these equations yields $a_1 + a_2 + 16 = 0 \iff a_1 + a_2 = \boxed{\textbf{(A) } -16}$ .)

## Solution 2
Since this quadratic must have a double root, its discriminant must be $0$ . Therefore we require \[(a+8)^2 - 4 \cdot 4 \cdot 9 = 0 \iff a^2 + 16a - 80 = 0.\] At this point, Vieta's formulae directly give the sum of the $2$ possible values of $a$ as $-\frac{16}{1} = \boxed{\textbf{(A) } -16}.$
(Alternatively, we could use the quadratic formula to directly solve this equation for $a$ ; the precise value of the expression under the square root does not actually matter, as it will cancel out due to the $\pm$ signs when added. This again gives the required sum as \[\frac{-16 + \sqrt{\text{something}}}{2} + \frac{-16 - \sqrt{\text{something}}}{2} = \frac{-32}{2} = \boxed{\textbf{(A) } -16}.)\]
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .