# 2021 AIME II Problem 3

## Problem

Find the number of permutations $x_1, x_2, x_3, x_4, x_5$ of numbers $1, 2, 3, 4, 5$ such that the sum of five products \[x_1x_2x_3 + x_2x_3x_4 + x_3x_4x_5 + x_4x_5x_1 + x_5x_1x_2\] is divisible by $3$ .

## Solution 1
Since $3$ is one of the numbers, a product with a $3$ in it is automatically divisible by $3,$ so WLOG $x_3=3,$ we will multiply by $5$ afterward since any of $x_1, x_2, \ldots, x_5$ would be $3,$ after some cancelation we see that now all we need to find is the number of ways that $x_5x_1(x_4+x_2)$ is divisible by $3,$ since $x_5x_1$ is never divisible by $3,$ now we just need to find the number of ways $x_4+x_2$ is divisible by $3.$ Note that $x_2$ and $x_4$ can be $(1, 2), (2, 1), (1, 5), (5, 1), (2, 4), (4, 2), (4, 5),$ or $(5, 4).$ We have $2$ ways to designate $x_1$ and $x_5$ for a total of $8 \cdot 2 = 16.$ So the desired answer is $16 \cdot 5=\boxed{080}.$
~math31415926535
~MathFun1000 (Rephrasing for clarity)

## Solution 2 (Symmetry and Casework)
The expression $x_1x_2x_3 + x_2x_3x_4 + x_3x_4x_5 + x_4x_5x_1 + x_5x_1x_2$ has symmetry. Without the loss of generality, let $x_1=3.$ It follows that $\{x_2,x_3,x_4,x_5\}=\{1,2,4,5\}.$ We have:
1. $x_1x_2x_3 + x_2x_3x_4 + x_3x_4x_5 + x_4x_5x_1 + x_5x_1x_2\equiv x_2x_3x_4 + x_3x_4x_5\pmod{3}.$
1. $x_2,x_3,x_4,x_5$ are congruent to $1,2,1,2\pmod{3}$ in some order.
We construct the following table for the case $x_1=3,$ with all values in modulo $3:$ \[\begin{array}{c||c|c|c|c|c||c} & & & & & & \\ [-2.5ex] \textbf{Row} & \boldsymbol{x_2} & \boldsymbol{x_3} & \boldsymbol{x_4} & \boldsymbol{x_5} & \boldsymbol{x_2x_3x_4 + x_3x_4x_5} & \textbf{Valid?} \\ [0.5ex] \hline & & & & & & \\ [-2ex] 1 & 1 & 1 & 2 & 2 & 0 & \checkmark \\ 2 & 1 & 2 & 1 & 2 & 0 & \checkmark \\ 3 & 1 & 2 & 2 & 1 & 2 & \\ 4 & 2 & 1 & 1 & 2 & 1 & \\ 5 & 2 & 1 & 2 & 1 & 0 & \checkmark \\ 6 & 2 & 2 & 1 & 1 & 0 & \checkmark \end{array}\] For Row 1, $(x_2,x_3)$ can be either $(1,4)$ or $(4,1),$ and $(x_4,x_5)$ can be either $(2,5)$ or $(5,2).$ By the Multiplication Principle, Row 1 produces $2\cdot2=4$ permutations. Similarly, Rows 2, 5, and 6 each produce $4$ permutations.
Together, we get $4\cdot4=16$ permutations for the case $x_1=3.$ By symmetry, the cases $x_2=3, x_3=3, x_4=3,$ and $x_5=3$ all have the same count. Therefore, the total number of permutations $x_1, x_2, x_3, x_4, x_5$ is $16\cdot5=\boxed{080}.$
~MRENTHUSIASM

## Solution 3
WLOG, let $x_{3} = 3$ So, the terms $x_{1}x_{2}x_{3}, x_{2}x_{3}x_{4},x_{3}x_{4}x_{5}$ are divisible by $3$ .
We are left with $x_{4}x_{5}x_{1}$ and $x_{5}x_{1}x_{2}$ . We need $x_{4}x_{5}x_{1} + x_{5}x_{1}x_{2} \equiv 0 \pmod{3}$ . The only way is when They are $(+1,-1)$ or $(-1, +1) \pmod{3}$ .
The numbers left with us are $1,2,4,5$ which are $+1,-1,+1,-1\pmod{3}$ respectively.
$+1$ (of $x_{4}x_{5}x_{1}$ or $x_{5}x_{1}x_{2}$ ) $= +1 \cdot +1 \cdot +1$ $\;\;\; OR \;\;\;+1$ (of $x_{4}x_{5}x_{1}$ or $x_{5}x_{1}x_{2}$ ) = $-1 \cdot -1 \cdot +1$ .
$-1$ (of $x_{4}x_{5}x_{1}$ or $x_{5}x_{1}x_{2}$ ) $= -1 \cdot -1 \cdot -1$ $\;\;\; OR \;\;\;-1$ (of $x_{4}x_{5}x_{1}$ or $x_{5}x_{1}x_{2}$ ) = $-1 \cdot +1 \cdot +1$
But, as we have just two $+1's$ and two $-1's$ . Hence, We will have to take $+1 = +1 \cdot -1 \cdot -1$ and $-1 = -1 \cdot +1 \cdot +1$ . Among these two, we have a $+1$ and $-1$ in common, i.e. $(x_{5}, x_{1}) = (+1, -1) or (-1, +1)$ (because $x_{1}$ and $x_{5}$ . are common in $x_{4}x_{5}x_{1}$ and $x_{5}x_{1}x_{2}$ ).
So, $(x_{5}, x_{1}) \in {(1,2), (1,5), (4,2), (4,5), (2,1), (5,1), (2,4), (5,4)}$ i.e. $8$ values.
For each value of $(x_{5}, x_{1})$ we get $2$ values for $(x_{2}, x_{4})$ . Hence, in total, we have $8 \times 2 = 16$ ways.
But any of the $x_{i} 's$ can be $3$ . So, $16 \times 5 = \boxed{080}$ .
-Arnav Nigam

## Solution 4 (Proportion)
WLOG, let $x_{3} = 3$ . Then: \[x_{1}x_{2}x_{3} + x_{2}x_{3}x_{4} + x_{3}x_{4}x_{5} + x_{4}x_{5}x_{1} + x_{5}x_{1}x_{2} = 3 (x_1 x_2 + x_2 x_4 + x_4 x_5) + x_5 x_1 (x_2 + x_4).\] The sum is divisible by $3$ if and only if $x_2 + x_4$ is divisible by $3$ . The possible sums of $x_2 + x_4$ are $1 + 2, 1 + 4, 1 + 5, 2 + 4, 2 + 5, 4 + 5.$ Two of them are not multiples of $3$ , but four of them are multiples.
A total number of permutations is $5! = 120.$
$\frac {2}{3}$ of this number, that is, $80,$ give sums that are multiples of $3.$
vladimir.shelomovskii@gmail.com, vvsss

## Solution 5 (Factoring)
This is my first time doing a solution (feel free to edit it)
We have \[x_1x_2x_3 + x_2x_3x_4 + x_3x_4x_5 + x_4x_5x_1 + x_5x_1x_2.\]
We have $5$ numbers. Considering any $x$ as $3,$ we see that we are left with two terms that are not always divisible by $3,$ which means that already gives us 5 options. Let's now consider $x_1 =3:$ We are left with \[3x_2x_3 + x_2x_3x_4 + x_3x_4x_5 + 3x_4x_5 + 3x_5x_2.\] The two terms left over are \[x_2x_3x_4 + x_3x_4x_5 \equiv 0 \pmod{3}\] since we already have used $3$ the remaining numbers are $1,2,4,5.$
We now factor \begin{align*} (x_2 + x_5)(x_3x_4) &\equiv 0 \pmod{3} \\ (x_2 + x_5) &\equiv 0 \pmod{3} \end{align*} since $1,2,4,5$ are all not factors of $3.$
Now using the number $1,2,4,5,$ we take two to get a number divisible by $3$ for $(x_2 + x_5):$ \begin{align*} 1+5 &\equiv 0 \pmod{3}, \\ 4+2 &\equiv 0 \pmod{3}, \\ 4+5 &\equiv 0 \pmod{3}, \\ 1+2 &\equiv 0 \pmod{3}. \end{align*} We have $4$ possibilities from above. Since we can also have $5+1$ or $2+4,$ there are $4\cdot2=8$ possibilities in all.
Now using \[(x_2 + x_5)(x_3x_4) \equiv 0 \pmod{3},\] we have $(x_3x_4),$ which results in $8$ more possibilities of $2$ times more. So, we get $2\cdot2\cdot4=16.$
Remember that $3$ can be any of $5$ different variables. So, we multiply by $5$ to get the answer $\boxed{080}.$

## Video Solution
https://www.youtube.com/watch?v=HikWWhQlkVw
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .