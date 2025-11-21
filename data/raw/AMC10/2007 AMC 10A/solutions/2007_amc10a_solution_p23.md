# 2007 AMC 10A Problem 23

## Problem

How many ordered pairs $(m,n)$ of positive integers , with $m \ge n$ , have the property that their squares differ by $96$ ?

$\text{(A)}\ 3 \qquad \text{(B)}\ 4 \qquad \text{(C)}\ 6 \qquad \text{(D)}\ 9 \qquad \text{(E)}\ 12$

## Solution 1
\[m^2 - n^2 = (m+n)(m-n) = 96 = 2^{5} \cdot 3\]
For every two factors $xy = 96$ , we have $m+n=x, m-n=y \Longrightarrow m = \frac{x+y}{2}, n = \frac{x-y}{2}$ . It follows that the number of ordered pairs $(m,n)$ is given by the number of ordered pairs $(x,y): xy=96, x > y > 0$ . There are $(5+1)(1+1) = 12$ factors of $96$ , which give us six pairs $(x,y)$ . However, since $m,n$ are positive integers, we also need that $\frac{x+y}{2}, \frac{x-y}{2}$ are positive integers, so $x$ and $y$ must have the same parity . Thus we exclude the factors $(x,y) = (1,96)(3,32)$ , and we are left with $4$ pairs $\mathrm{(B)}$ .

## Solution 2
We first start as in Solution 1. However, as an alternative, we could also "give" each of the factors a factor of $2.$ This would force each one to be even. Now we have $\dfrac{96} {4} = 24,$ and since $24= 2^3 \cdot 3,$ the number of factors is $4 \cdot 2 = 8.$ We then divide by $2$ because $m-n \le m+n.$ This gives $4,$ as desired.
~clever14710owl

## Solution 3
Similarly to the solution above, write $96$ as $2^5\cdot3^1$ . To find the number of distinct factors, add $1$ to both exponents and multiply, which gives us $6\cdot2=12$ factors. Divide by $2$ since $m$ must be greater than or equal to $n$ . We don't need to worry about $m$ and $n$ being equal because $96$ is not a perfect square. Finally, subtract the two cases above for the same reason to get $\mathrm{(B)}$ .

## Solution 4
Find all of the factor pairs of $96$ : $(1,96),(2,48),(3,32),(4,24),(6,16),(8,12).$ You can eliminate $(1,96)$ and ( $3,32)$ because you cannot have two numbers add to be an even number and have an odd difference at the same time without them being a decimal. You only have $4$ pairs left, so the answer is $\boxed{\textbf{(B)}\; 4}$ .
~HelloWorld21

## Video Solution
https://www.youtube.com/watch?v=mNmXez4yvW0 ~David
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .