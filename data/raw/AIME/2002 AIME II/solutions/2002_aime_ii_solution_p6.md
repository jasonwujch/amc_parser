# 2002 AIME II Problem 6

## Problem

Find the integer that is closest to $1000\sum_{n=3}^{10000}\frac1{n^2-4}$ .

## Solution 1
We know that $\frac{1}{n^2 - 4} = \frac{1}{(n+2)(n-2)}$ . We can use the process of fractional decomposition to split this into two fractions: $\frac{1}{(n+2)(n-2)} = \frac{A}{(n+2)} + \frac{B}{(n-2)}$ for some A and B.
Solving for A and B gives $1 = (n-2)A + (n+2)B$ or $1 = n(A+B)+ 2(B-A)$ . Since there is no n term on the left hand side, $A+B=0$ and by inspection $1 = 2(B-A)$ . Solving yields $A=\frac{-1}{4}, B=\frac{1}{4}$
Therefore, $\frac{1}{n^2-4} = \frac{1}{(n+2)(n-2)} = \frac{ \frac{1}{4} }{(n-2)} + \frac{ \frac{-1}{4} }{(n+2)} = \frac{1}{4} \left( \frac{1}{n-2} - \frac{1}{n+2} \right)$ .
And so, $1000\sum_{n=3}^{10,000} \frac{1}{n^2-4} = 1000\sum_{n=3}^{10,000} \frac{1}{4} \left( \frac{1}{n-2} - \frac{1}{n+2} \right) = 250\sum_{n=3}^{10,000} (\frac{1}{n-2} - \frac{1}{n + 2})$ .
This telescopes into:
$250 (1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} - \frac{1}{9999} - \frac{1}{10000} - \frac{1}{10001} - \frac{1}{10002}) = 250 + 125 + 83.3 + 62.5 - 250 (\frac{1}{9999} + \frac{1}{10000} + \frac{1}{10001} + \frac{1}{10002})$
The small fractional terms are not enough to bring $520.8$ lower than $520.5,$ so the answer is $\fbox{521}$

## Solution 2
Using the fact that $\frac{1}{n(n+k)} = \frac{1}{k} ( \frac{1}{n}-\frac{1}{n+k} )$ or by partial fraction decomposition, we both obtained $\frac{1}{x^2-4} = \frac{1}{4}(\frac{1}{x-2}-\frac{1}{x+2})$ . The denominators of the positive terms are $1,2,..,9998$ , while the negative ones are $5,6,...,10002$ . Hence we are left with $1000 \cdot \frac{1}{4} (1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} - \frac{1}{9999} - \frac{1}{10000} - \frac{1}{10001} - \frac{1}{10002})$ . We can simply ignore the last $4$ terms, and we get it is approximately $1000*\frac{25}{48}$ . Computing $\frac{25}{48}$ which is about $0.5208..$ and moving the decimal point three times, we get that the answer is $521$
These problems are copyrighted © by the Mathematical Association of America.