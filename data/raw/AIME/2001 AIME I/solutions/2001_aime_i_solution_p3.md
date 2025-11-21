# 2001 AIME I Problem 3

## Problem

Find the sum of the roots , real and non-real, of the equation $x^{2001}+\left(\frac 12-x\right)^{2001}=0$ , given that there are no multiple roots.

## Solution 1
By Vieta's formulae , for a polynomial equation of the form $a_nx^n + a_{n-1}x^{n-1} + \dotsb + a_0 = 0$ , the sum of the roots, counted with multiplicity , is $-\frac{a_{n-1}}{a_n}$ .
Now, by the Binomial Theorem , the highest-degree term of the expansion of $\left(\frac 12-x\right)^{2001}$ is $-x^{2001}$ , but $x^{2001}+\left(-x^{2001}\right) = 0$ , so the highest-degree term is in fact the $x^{2000}$ term. Since there are no multiple roots, counting them with multiplicity includes each root exactly once, so the required sum will be given by precisely the formula above.
We accordingly need to compute the coefficients of the $x^{2000}$ and $x^{1999}$ terms, which is straightforward using the Binomial Theorem again:
\begin{align*}&\binom{2001}{1} \cdot (-x)^{2000} \cdot \left(\frac{1}{2}\right)^1 =\frac{2001}{2}x^{2000}, \quad\text{and} \\ &\binom{2001}{2} \cdot (-x)^{1999} \cdot \left(\frac{1}{2}\right)^2 =-\frac{2001 \cdot 2000}{8}x^{1999} = -2001 \cdot 250x^{1999}. \end{align*}
Hence the sum of all the distinct roots is $-\frac{-2001 \cdot 250}{\left(\frac{2001}{2}\right)} = 250 \cdot 2 = \boxed{500}$ .

## Solution 2
As in Solution 1, we find that the $x^{2001}$ terms cancel, so the left-hand side of the given equation is a $2000^{\text{th}}$ -degree polynomial. This means there are $2000$ roots, counted with multiplicity , but as there are no multiple roots, all of these $2000$ roots are actually distinct. Moreover, noting the symmetry of the equation in the form given, we observe that if $x$ is a root, then $\left(\frac{1}{2}-x\right)$ is also a root. In each case, we must have $x \neq \frac{1}{2}-x$ , since otherwise the solution of $x = \frac{1}{2}-x$ , i.e. $x = \frac{1}{4}$ , would be a multiple root. Thus we can pair up the $2000$ distinct roots to obtain $\frac{2000}{2} = 1000$ distinct pairs, each of which contains $2$ distinct roots that sum to $\frac{1}{2}$ . Summing these pairs will therefore count each root exactly once, as desired, so the answer is $1000 \cdot \frac{1}{2} = \boxed{500}$ .

## Solution 3
As in Solution 2, observe that if $r$ is a root, then $\left(\frac{1}{2}-r\right)$ is also a root, yielding a pair of roots that sum to $\frac{1}{2}$ . This motivates us to substitute $y = x-\frac{\left(\frac{1}{2}\right)}{2}$ , i.e. $y = x-\frac{1}{4}$ , so that the left-hand side of the equation becomes even more symmetric: \[\left(\frac{1}{4}+y\right)^{2001}+\left(\frac{1}{4}-y\right)^{2001} = 0.\] Using the Binomial Theorem , this expands as \[2\cdot\frac{1}{4}\cdot\binom{2001}{1}y^{2000}-0y^{1999}+\dotsb = 0,\] so by Vieta's formulae , the sum of the roots for $y$ is 0. Since the original equation in $x$ has degree $2000$ , there are also $2000$ roots for $x$ , all of which are distinct since there are no multiple roots. Therefore, letting these roots be $x_n = y_n+\frac{1}{4}$ for $1 \leq n \leq 2000$ , their sum is \[\sum_{n=1}^{2000}\left(y_n+\frac{1}{4}\right) = \sum_{n=1}^{2000}y_n + 2000 \cdot \frac{1}{4} = 0 + 500 =\boxed{500}.\]
These problems are copyrighted © by the Mathematical Association of America.