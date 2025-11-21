# 2013 AIME I Problem 10

## Problem

There are nonzero integers $a$ , $b$ , $r$ , and $s$ such that the complex number $r+si$ is a zero of the polynomial $P(x)={x}^{3}-a{x}^{2}+bx-65$ . For each possible combination of $a$ and $b$ , let ${p}_{a,b}$ be the sum of the zeros of $P(x)$ . Find the sum of the ${p}_{a,b}$ 's for all possible combinations of $a$ and $b$ .

## Solution
Since $r+si$ is a root, by the Complex Conjugate Root Theorem, $r-si$ must be the other imaginary root. Using $q$ to represent the real root, we have
$(x-q)(x-r-si)(x-r+si) = x^3 -ax^2 + bx -65$
Applying difference of squares, and regrouping, we have
$(x-q)(x^2 - 2rx + (r^2 + s^2)) = x^3 -ax^2 + bx -65$
So matching coefficients, we obtain
$q(r^2 + s^2) = 65$
$b = r^2 + s^2 + 2rq$
$a = q + 2r$
By Vieta's each ${p}_{a,b} = a$ so we just need to find the values of $a$ in each pair. We proceed by determining possible values for $q$ , $r$ , and $s$ and using these to determine $a$ and $b$ .
If $q = 1$ , $r^2 + s^2 = 65$ so (r, s) = $(\pm1, \pm 8), (\pm8, \pm 1), (\pm4, \pm 7), (\pm7, \pm 4)$
Similarly, for $q = 5$ , $r^2 + s^2 = 13$ so the pairs $(r,s)$ are $(\pm2, \pm 3), (\pm3, \pm 2)$
For $q = 13$ , $r^2 + s^2 = 5$ so the pairs $(r,s)$ are $(\pm2, \pm 1), (\pm1, \pm 2)$
Now we can disregard the plus minus signs for s because those cases are included as complex conjugates of the counted cases. The positive and negative values of r will cancel, so the sum of the ${p}_{a,b} = a$ for $q = 1$ is $q$ times the number of distinct $r$ values (as each value of $r$ generates a pair $(a,b)$ ). Our answer is then $(1)(8) + (5)(4) + (13)(4) = \boxed{080}$ .
### Remark:
The complex conjugate theorem states that a polynomial with real coefficients must have an even amount of complex numbers. One of them is the complex number $a + bi$ , and the other is it's conjugate, or $a - bi$ . These, when multiplied cancel out and become real numbers ( $a^2 + b^2$ ). Similar logic for addition.
~Aarav22
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .