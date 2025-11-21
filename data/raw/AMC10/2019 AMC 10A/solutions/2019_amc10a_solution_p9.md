# 2019 AMC 10A Problem 9

## Problem

What is the greatest three-digit positive integer $n$ for which the sum of the first $n$ positive integers is $\underline{\text{not}}$ a divisor of the product of the first $n$ positive integers?

$\textbf{(A) } 995 \qquad\textbf{(B) } 996 \qquad\textbf{(C) } 997 \qquad\textbf{(D) } 998 \qquad\textbf{(E) } 999$

## Solutions

## Solution 1
The sum of the first $n$ positive integers is $\frac{(n)(n+1)}{2}$ , and we want this to not be a divisor of $n!$ (the product of the first $n$ positive integers). Notice that if and only if $n+1$ were composite, all of its factors would be less than or equal to $n$ , which means they would be able to cancel with the factors in $n!$ . Thus, the sum of $n$ positive integers would be a divisor of $n!$ when $n+1$ is composite. (Note: This is true for all positive integers except for 1 because 2 is not a divisor/factor of 1.) Hence in this case, $n+1$ must instead be prime. The greatest three-digit integer that is prime is $997$ , so we subtract $1$ to get $n=\boxed{\textbf{(B) } 996}$ .

## Solution 1.1
The sum of the first \( n \) positive integers starting from 1 is \( \frac{n(n+1)}{2} \). The product of the first \( n \) positive integers starting from \( n \), then going to \( (n-1) \), all the way down to 1, is \( n! \). If there exists a number such that \( n! / \frac{n(n-1)}{2} = +\mathbb{Z} \), then we call that solution invalid. \( n! / \frac{n(n-1)}{2} \) is just \( \frac{2n!}{n(n+1)} \). We see that the first term of \( n! \), which is \( n \), will cancel out with the \( n \) term on the denominator. In order for \( n-1 \) to not cancel out, it needs to be a prime number. The only answer choice that satisfies this $n=\boxed{\textbf{(B) } 996}$ .
~Pinotation (not the creator of Solution 1)

## Solution 2 (easier answer choice elimination)
As in Solution 1, we deduce that $n+1$ must be prime.
It's hard to remember all of your primes up to a thousand, so we eliminate answer choices choices $A$ , $C$ , and $E$ don't work because $n+1$ is even, and all even numbers are divisible by two, which makes choices $A$ , $C$ , and $E$ composite and not prime.
Choice $D$ also does not work since $999$ is divisible by $9$ , which means it's a composite number and not prime. Thus, the correct answer must be $\boxed{\textbf{(B) } 996}$ .

## Solution 3 (Elimination)
The sum of the first $n$ positive integers is $\frac{(n)(n+1)}{2}$ and the product of the positive integers upto $n$ is $n!$ . The quotient of the two is -
$\frac{(2)(n!)}{(n)(n+1)}$
which simplifies to $\frac{(2)((n-1)!)}{n+1}$ . Thus, $n+1$ must be odd for the remainder to not be 0 (as $2$ will multiply with some number in $n!$ , cancelling out $n+1$ if it is even, which leaves us with the answer choices $n = 996$ and $n = 998$ . Notice that $n + 1$ must also be prime as otherwise there will be a factor of $n + 1$ in $2$ x $n!$ somewhere. So either $997$ or $999$ must be prime - $999$ is obviously not prime as it is divisible by 9, so our answer should be $n$ where $n + 1 = 997$ , and so our answer is $n = 996$ or $\boxed{\textbf{(B) } 996}$ .
- youtube.com/indianmathguy

## Video Solutions

## Video Solution 1
https://youtu.be/2vucE8HTiuU
~savannahsolver

## Video Solution 2 by OmegaLearn
https://youtu.be/FDgcLW4frg8?t=33
~ pi_is_3.14

## Video Solution 3
https://youtu.be/ikRv_0kNc2w
Education, the Study of Everything
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .