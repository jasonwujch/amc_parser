# 2000 AIME II Problem 2

## Problem

A point whose coordinates are both integers is called a lattice point. How many lattice points lie on the hyperbola $x^2 - y^2 = 2000^2$ ?

## Solution
\[(x-y)(x+y)=2000^2=2^8 \cdot 5^6\]
Note that $(x-y)$ and $(x+y)$ have the same parities , so both must be even. We first give a factor of $2$ to both $(x-y)$ and $(x+y)$ . We have $2^6 \cdot 5^6$ left. Since there are $7 \cdot 7=49$ factors of $2^6 \cdot 5^6$ , and since both $x$ and $y$ can be negative, this gives us $49\cdot2=\boxed{098}$ lattice points.

## Solution 2
As with solution 1, note that both $x-y$ and $x+y$ must have the same parities, meaning both have to be even. Additionally, we can express both of them in terms of $2^a\cdot3^b$ and $2^c\cdot3^d$ . Now, $a+c$ must be equal to 6, and both have to be greater than or equal to 1, so there are by stars and bars 7 ways to do this. Similarly, for $b+d$ , we have that both only need to be greater than or equal to 0, so this time there are 7 ways to do so. Since both can be negative, we multiply $7\cdot7\cdot2$ which gives $098$ .

## Solution 3
If we restrict ourselves to the first quadrant, this is equivalent to finding Pythagorean triples for $2000^2 + y^2 = x^2$ . We know that every Pythagorean triple corresponds to a pair of integers $m$ and $n$ giving:
\begin{align*} y = m^2 - n^2, && b = 2mn, && x = m^2 + n^2 \end{align*}
If we let $b=2mn=2000$ then each Pythagorean triple corresponds to a factorization $mn = 1000 = 2^35^3$ , of which there are $4\times4=25$ .
But we've been only looking at the first quadrant. If we reflect this quadrant to the others, and eliminate the two duplicate reflections where $y=0$ , we end up with $25\times4-2 = 098$ solutions.
These problems are copyrighted © by the Mathematical Association of America.