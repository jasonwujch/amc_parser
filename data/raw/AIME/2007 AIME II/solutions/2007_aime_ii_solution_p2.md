# 2007 AIME II Problem 2

## Problem

Find the number of ordered triples $(a,b,c)$ where $a$ , $b$ , and $c$ are positive integers , $a$ is a factor of $b$ , $a$ is a factor of $c$ , and $a+b+c=100$ .

## Solution
Denote $x = \frac{b}{a}$ and $y = \frac{c}{a}$ . The last condition reduces to $a(1 + x + y) = 100$ . Therefore, $1 + x + y$ is equal to one of the 9 factors of $100 = 2^25^2$ .
Subtracting the one, we see that $x + y = \{0,1,3,4,9,19,24,49,99\}$ . There are exactly $n - 1$ ways to find pairs of $(x,y)$ if $x + y = n$ . Thus, there are $0 + 0 + 2 + 3 + 8 + 18 + 23 + 48 + 98 = \boxed{200}$ solutions of $(a,b,c)$ .
Alternatively, note that the sum of the divisors of $100$ is $(1 + 2 + 2^2)(1 + 5 + 5^2)$ (notice that after distributing, every divisor is accounted for). This evaluates to $7 \cdot 31 = 217$ . Subtract $9 \cdot 2$ for reasons noted above to get $199$ . Finally, this changes $1 \Rightarrow -1$ , so we have to add one to account for that. We get $\boxed{200}$ .

## Video Solution by OmegaLearn
https://youtu.be/LqrXinQbk1Q?t=73
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.