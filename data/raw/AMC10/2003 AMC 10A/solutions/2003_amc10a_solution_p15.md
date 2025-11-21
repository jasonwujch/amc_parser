# 2003 AMC 10A Problem 15

## Problem

What is the probability that an integer in the set $\{1,2,3,...,100\}$ is divisible by $2$ and not divisible by $3$ ?

$\mathrm{(A) \ } \frac{1}{6}\qquad \mathrm{(B) \ } \frac{33}{100}\qquad \mathrm{(C) \ } \frac{17}{50}\qquad \mathrm{(D) \ } \frac{1}{2}\qquad \mathrm{(E) \ } \frac{18}{25}$

## Solution
There are $100$ integers in the set.
Since every $2^{\text{nd}}$ integer is divisible by $2$ , there are $\left\lfloor\frac{100}{2}\right\rfloor = 50$ integers divisible by $2$ in the set.
To be divisible by both $2$ and $3$ , a number must be divisible by $\operatorname{lcm}(2,3)=6$ .
Since every $6^{\text{th}}$ integer is divisible by $6$ , there are $\left\lfloor\frac{100}{6}\right\rfloor = 16$ integers divisible by both $2$ and $3$ in the set.
So there are $50-16=34$ integers in this set that are divisible by $2$ and not divisible by $3$ .
Therefore, the desired probability is $\frac{34}{100}=\frac{17}{50}\Rightarrow\boxed{\mathrm{(C)}\ \frac{17}{50}}$ .

## Video Solution by WhyMath
https://youtu.be/UfzS5griBic
~savannahsolver

## Video Solution
https://www.youtube.com/watch?v=4IlfkRW660E ~David
### Controversy
Due to the wording of the problem statement, it might be taken as "Find the probability that an integer exists in said set that is divisible by $2$ and not $3$ ". One example would be $2$ , which is not a multiple of $3$ , and thus the probability would appear to be $1$ . But because $1$ is not an answer choice, we can assume that that was not the intended meaning.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .