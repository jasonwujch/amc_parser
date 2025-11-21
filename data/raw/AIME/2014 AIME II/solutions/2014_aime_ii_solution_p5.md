# 2014 AIME II Problem 5

## Problem

Real numbers $r$ and $s$ are roots of $p(x)=x^3+ax+b$ , and $r+4$ and $s-3$ are roots of $q(x)=x^3+ax+b+240$ . Find the sum of all possible values of $|b|$ .

## Solution 1
Because the coefficient of $x^2$ in both $p(x)$ and $q(x)$ is 0, the remaining root of $p(x)$ is $-(r+s)$ , and the remaining root of $q(x)$ is $-(r+s+1)$ . The coefficients of $x$ in $p(x)$ and $q(x)$ are both equal to $a$ , and equating the two coefficients gives \[rs-(r+s)^2 = (r+4)(s-3)-(r+s+1)^2\] from which $s = \tfrac 12 (5r+13)$ . Substitution should give $r = -5$ and $r = 1$ , corresponding to $s = -6$ and $s = 9$ , and $|b| = 330, 90$ , for an answer of $\boxed{420}$ .

## Solution 2
Let $r$ , $s$ , and $-r-s$ be the roots of $p(x)$ (per Vieta's). Then $r^3 + ar + b = 0$ and similarly for $s$ . Also, \[q(r+4) = (r+4)^3 + a(r+4) + b + 240 = 12r^2 + 48r + 304 + 4a = 0\]
Set up a similar equation for $s$ :
\[q(s-3) = (s-3)^3 + a(s-3) + b + 240 = -9s^2 + 27s + 213 - 3a = 0.\]
Simplifying and adding the equations gives \begin{align}\tag{*} r^2 - s^2 + 4r + 3s + 49 &= 0 \end{align} Now, let's deal with the $ax$ terms. Plugging the roots $r$ , $s$ , and $-r-s$ into $p(x)$ yields a long polynomial, and plugging the roots $r+4$ , $s-3$ , and $-1-r-s$ into $q(x)$ yields another long polynomial. Equating the coefficients of $x$ in both polynomials, we get: \[rs + (-r-s)(r+s) = (r+4)(s-3) + (-r-s-1)(r+s+1),\] which eventually simplifies to \[s = \frac{13 + 5r}{2}.\] Substitution into (*) should give $r = -5$ and $r = 1$ , corresponding to $s = -6$ and $s = 9$ , and $|b| = 330, 90$ , for an answer of $\boxed{420}$ .

## Solution 3
The roots of $p(x)$ are $r$ , $s$ , and $-r-s$ since they sum to $0$ by Vieta's Formula (coefficient of $x^2$ term is $0$ ).
Similarly, the roots of $q(x)$ are $r + 4$ , $s - 3$ , and $-r-s-1$ , as they too sum to $0$ .
Then:
$a = rs+r(-r-s)+s(-r-s) = rs-(r+s)^2$ and $-b = rs(-r-s)$ from $p(x)$ and
$a=(r+4)(s-3)+(r+4)(-r-s-1)+(s-3)(-r-s-1) = (r+4)(s-3)-(r+s+1)^2$ and $-(b+240)=(r+4)(s-3)(-r-s-1)$ from $q(x)$ .
From these equations, we can write that \[rs-(r+s)^2 = (r+4)(s-3)-(r+s+1)^2 = a\] and simplifying gives \[2s-5r-13=0 \Rightarrow s = \frac{5r+13}{2}.\]
We now move to the other two equations regarding the product of the roots. We see that we can cancel a negative from both sides to get \[rs(r+s) = b\] \[(r+4)(s-3)(r+s+1)=b + 240.\] Subtracting the first equation from the second equation gives us $(r+4)(s-3)(r+s+1) - rs(r+s) = 240$ .
Expanding, simplifying, substituting $s = \frac{5r+13}{2}$ , and simplifying some more yields the simple quadratic $r^2 + 4r - 5 = 0$ , so $r = -5, 1$ . Then $s = -6, 9$ .
Finally, we substitute back into $b=rs(r+s)$ to get $b = (-5)(-6)(-5-6) = -330$ , or $b = (1)(9)(1 + 9) = 90$ .
The answer is $|-330|+|90| = \boxed{420}$ .

## Solution 4
By Vieta's, we know that the sum of roots of $p(x)$ is $0$ . Therefore, the roots of $p$ are $r, s, -r-s$ . By similar reasoning, the roots of $q(x)$ are $r + 4, s - 3, -r - s - 1$ . Thus, $p(x) = (x - r)(x - s)(x + r + s)$ and $q(x) = (x - r - 4)(x - s + 3)(x + r + s + 1)$ .
Since $p(x)$ and $q(x)$ have the same coefficient for $x$ , we can go ahead and match those up to get \begin{align*} rs - r(r + s) - s(r + s) &= (r + 4)(s - 3) - (r + 4)(r + s + 1) - (s - 3)(r + s + 1) \\ 0 &= -13 - 5r + 2s \\ s &= \frac{5r + 13}{2} \end{align*}
At this point, we can go ahead and compare the constant term in $p(x)$ and $q(x)$ . Doing so is certainly valid, but we can actually do this another way. Notice that $p(s) = 0$ . Therefore, $q(s) = 240$ . If we plug that into our expression, we get that \begin{align*} q(s) &= 3(s - r - 4)(r + 2s + 1) \\ 240 &= 3(s - r - 4)(r + 2s + 1) \\ 240 &= 3\left( \frac{3r + 5}{2} \right)(6r + 14) \\ 80 &= (3r + 5)(3r + 7) \\ 0 &= r^2 + 4r - 5 \end{align*} This tells us that $(r, s) = (1, 9)$ or $(-5, -6)$ . Since $-b$ is the product of the roots, we have that the two possibilities are $1 \cdot 9 \cdot (-10) = -90$ and $(-5)(-6)11 = 330$ . Adding the absolute values of these gives us $\boxed{420}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .