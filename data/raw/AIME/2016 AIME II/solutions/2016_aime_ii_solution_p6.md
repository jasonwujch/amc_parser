# 2016 AIME II Problem 6

## Problem

For polynomial $P(x)=1-\dfrac{1}{3}x+\dfrac{1}{6}x^{2}$ , define $Q(x)=P(x)P(x^{3})P(x^{5})P(x^{7})P(x^{9})=\sum_{i=0}^{50} a_ix^{i}$ . Then $\sum_{i=0}^{50} |a_i|=\dfrac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
Note that all the coefficients of odd-powered terms is an odd number of odd degree terms multiplied together, and all coefficients of even-powered terms have an even number of odd degree terms multiplied together. Since every odd degree term is negative, and every even degree term is positive, the sum is just equal to $Q(-1)=P(-1)^{5}=\left( \dfrac{3}{2}\right)^{5}=\dfrac{243}{32}$ , so the desired answer is $243+32=\boxed{275}$ .
[YINGLINWU] Just a quick comment: After multiplying out the product for Q(x) into the sum of monomials, the coefficient of a monomial of even degree is always positive while the coefficient of a monomial of odd degree is always negative. Therefore, as we are collecting similar terms, no coefficients of monomials cancel out. It follows that the sum of absolute values of coefficients of Q(x) is the same as that of Q(-x), which is given by Q(-1).

## Solution 2
We are looking for the sum of the absolute values of the coefficients of $Q(x)$ . By defining $P'(x) = 1 + \frac{1}{3}x+\frac{1}{6}x^2$ , and defining $Q'(x) = P'(x)P'(x^3)P'(x^5)P'(x^7)P'(x^9)$ , we have made it so that all coefficients in $Q'(x)$ are just the positive/absolute values of the coefficients of $Q(x)$ . .
To find the sum of the absolute values of the coefficients of $Q(x)$ , we can just take the sum of the coefficients of $Q'(x)$ . This sum is equal to \[Q'(1) = P'(1)P'(1)P'(1)P'(1)P'(1) = \left(1+\frac{1}{3}+\frac{1}{6}\right)^5 = \frac{243}{32},\]
so our answer is $243+32 = \boxed{275}$ .
Note: this method doesn't work for every product of polynomials. Example: The sum of the absolute values of the coefficients of $K(x) = (2x^2 - 6x - 5)(10x - 1)$ is $131$ but when you find the sum of the coefficients of $K'(x)$ which is $K'(1)$ , then you get $143$ . - whatRthose

## Solution 3 (risky)
Multiply $P(x)P(x^3)$ and notice that the odd degree terms have a negative coefficient. Observing that this is probably true for all polynomials like this (including $P(x)P(x^3)P(x^5)P(x^7)P(x^9)$ ), we plug in $-1$ to get $\frac{243}{32} \implies \boxed{275}$ .

## Solution 4 (bash for life)
We expand and add the numbers (I made two very easy mistakes and fixed them).
https://cdn.artofproblemsolving.com/attachments/1/6/c4e3bea5cf2d5bb7d7796049b5dc17fcd8a2ba.jpg
-maxamc
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .