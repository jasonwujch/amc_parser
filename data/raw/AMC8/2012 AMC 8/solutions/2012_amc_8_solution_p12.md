# 2012 AMC 8 Problem 12

## Problem

What is the units digit of $13^{2012}$ ?

$\textbf{(A)}\hspace{.05in}1\qquad\textbf{(B)}\hspace{.05in}3\qquad\textbf{(C)}\hspace{.05in}5\qquad\textbf{(D)}\hspace{.05in}7\qquad\textbf{(E)}\hspace{.05in}9$

## Video Solution by Pi Academy
https://youtu.be/7xlBdxcsP3I?si=sFJGKXnBUUN7Su-C

## Video Solution 2
https://youtu.be/6RGNZj0tt2w ~David
https://youtu.be/7an5wU9Q5hk?t=1186 ~ pi_is_3.14
https://youtu.be/6c_s967T7cA ~savannahsolver

## Solution 1
The problem wants us to find the units digit of $13^{2012}$ , therefore, we can eliminate the tens digit of $13$ , because the tens digit will not affect the final result. So our new expression is $3^{2012}$ . Now we need to look for a pattern in the units digit.
$3^1 \implies 3$
$3^2 \implies 9$
$3^3 \implies 7$
$3^4 \implies 1$
$3^5 \implies 3$
We observe that there is a pattern for the units digit which recurs every four powers of three. Using this pattern, we can subtract 1 from 2012 and divide by 4. The remainder is the power of three that we are looking for, plus one. $2011$ divided by $4$ leaves a remainder of $3$ , so the answer is the units digit of $3^{3+1}$ , or $3^4$ . Thus, we find that the units digit of $13^{2012}$ is $\boxed{{\textbf{(A)}\ 1}}$ .

## Solution 2
Ignore the tens digit of $13$ , we find a pattern in the units digit that $3^4 \implies 1$ . We also find $2012$ can be divided by $4$ evenly, which is $2012/4=503$ . So $3^{2012}$ = $(3^4)^{503}$ . Because the units digit of $3^4 \implies 1$ ，so the units digit $1^{503} \implies 1$ . Thus, the units digit of $13^{2012}$ is $\boxed{{\textbf{(A)}\ 1}}$ . ---LarryFlora
### See Also