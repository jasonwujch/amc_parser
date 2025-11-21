# 2012 AIME I Problem 6

## Problem

The complex numbers $z$ and $w$ satisfy $z^{13} = w,$ $w^{11} = z,$ and the imaginary part of $z$ is $\sin{\frac{m\pi}{n}}$ , for relatively prime positive integers $m$ and $n$ with $m<n.$ Find $n.$

## Solution
Substituting the first equation into the second, we find that $(z^{13})^{11} = z$ and thus $z^{143} = z.$ We know that $z \neq 0,$ since we are given the imaginary part of $z$ , so we can divide by $z$ to get $z^{142} = 1.$ So, $z$ must be a $142$ nd root of unity, and thus, by De Moivre's theorem, the imaginary part of $z$ will be of the form $\sin{\frac{2k\pi}{142}} = \sin{\frac{k\pi}{71}},$ where $k \in \{1, 2, \ldots, 70\}.$ Note that $71$ is prime and $k<71$ by the conditions of the problem, so the denominator in the argument of this value will always be $71.$ Thus, $n = \boxed{071}.$

## Video Solutions
https://www.youtube.com/watch?v=cQmmkfZvPgU&t=30s
https://www.youtube.com/watch?v=DMka35X-3WI&list=PLyhPcpM8aMvIo_foUDwmXnQClMHngjGto&index=6 (Solution by Richard Rusczyk) - AMBRIGGS
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .