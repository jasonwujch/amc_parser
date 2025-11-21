# 2014 AMC 10B Problem 11

## Problem

For the consumer, a single discount of $n\%$ is more advantageous than any of the following discounts:

(1) two successive $15\%$ discounts

(2) three successive $10\%$ discounts

(3) a $25\%$ discount followed by a $5\%$ discount

What is the smallest possible positive integer value of $n$ ?

$\textbf{(A)}\ \ 27\qquad\textbf{(B)}\ 28\qquad\textbf{(C)}\ 29\qquad\textbf{(D)}\ 31\qquad\textbf{(E)}\ 33$

## Solution 1
Let the original price be $x$ . Then, for option $1$ , the discounted price is $(1-.15)(1-.15)x = .7225x$ . For option $2$ , the discounted price is $(1-.1)(1-.1)(1-.1)x = .729x$ . Finally, for option $3$ , the discounted price is $(1-.25)(1-.05) = .7125x$ . Therefore, $n$ must be greater than $\max(x - .7225x, x-.729x, x-.7125x)$ . It follows $n/100$ must be greater than $.2875$ . We multiply this by $100$ to get the percent value, and then round up because $n$ is the smallest integer that provides a greater discount than $28.75$ , leaving us with the answer of $\boxed{\textbf{(C) } 29}$

## Solution 2 (a bit easier)
Assume the original price was $100$ dollars. Thus, after a discount of $n\%$ , the price will be $100-n$ dollars. Using basic calculations, find out the value of the other discounts. This leaves us with the prices: $100-n$ , $\frac{289}{4}$ , $\frac{9^3}{10}$ , and $\frac{15\cdot19}{4}$ . Simplify these to get $100-n$ , $72$ (rounded down), $72.9$ , and $71$ (rounded down). To have the greatest discount, we need the least price, which is $71$ dollars. Now we get the original fractional value of this, and the discount of this is $100-\frac{285}{4}$ , and we round this down to $28$ . Now, it's pretty easy. The integer value greater than this is $\boxed{\textbf{(C) } 29}$
~solution by sakshamsethi
~edited by sosiaops

## Solution 3 (Straightforward)
Assume WLOG that the original price was $\$100$ . Then, option 1 would cost $100 \cdot \frac{17}{20} \cdot \frac{17}{20} = \$ 72.25$ . Option 2 would cost $100 \cdot \frac{9}{10} \cdot \frac{9}{10} \cdot \frac{9}{10} = \$72.90$ . Option 3 would cost $100 \cdot \frac{3}{4} \cdot \frac{19}{20} = \$71.25$ . Therefore, the largest integer smaller than all of these three is $71$ , so $100-71= \boxed{\textbf{(C) } 29}$ .
~MrThinker

## Video Solution
https://youtu.be/TVk6fRdTFJU
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .