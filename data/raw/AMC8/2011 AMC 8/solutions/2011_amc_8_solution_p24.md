# 2011 AMC 8 Problem 24

## Problem

In how many ways can $10001$ be written as the sum of two primes?

$\textbf{(A) }0\qquad\textbf{(B) }1\qquad\textbf{(C) }2\qquad\textbf{(D) }3\qquad\textbf{(E) }4$

## Solution
For the sum of two numbers to be odd, one must be odd and the other must be even, because all odd numbers are of the form $2n+1$ where n is an integer, and all even numbers are of the form $2m$ where m is an integer. \[2n + 1 + 2m = 2m + 2n + 1 = 2(m+n) + 1\] and $m+n$ is an integer because $m$ and $n$ are both integers. The only even prime number is $2,$ so our only combination could be $2$ and $9999.$ But, $9999$ is clearly divisible by $3$ , so the number of ways $10001$ can be written as the sum of two primes is $\boxed{\textbf{(A)}\ 0}$ .

## Solution 2(Simple)
First, we noticed that 10001 is equal to 5000+5001, if you subtract n to 5000 and add n to 5001, you always get an even number, even number is never a prime number except 2. We also see that whenever an addend is an odd number, the other addend will be even, so having an odd number as an addend is not possible, other than 9999 and 2, because 2 is a prime. We try 2 and 9999 but we can see 9999 is divisible by 3 and 9 clearly. So the answer is $\boxed{\textbf{(A)} 0}$

## Solution 3 (assumed previous knowledge)
It is helpful to know and understand the Goldbach Conjecture - that every even number can be written as the sum of $2$ primes - and also, that the ${\textbf{odd numbers}\ }$ that are the sum of two primes are exactly two more than a prime. This is because to make the sum of two numbers odd, you must have one even and one odd. There is only one even prime, which is two, so the sum will be of the form $2+p$ . Hence, the odd numbers that are the sum of two primes are exactly $2$ more than a prime. Relating to the problem, $10001$ is not $2$ more than a prime, because $10001-2=9999$ and we can easily see that $9999$ is divisible by $3$ . Therefore, $10001$ cannot be written as the sum of two primes, and the answer is $\boxed{\textbf{(A)}\ 0}$ ~mk

## Solution 4 (similar to solution 1)
Our equation can be rewritten to $Odd = Even + Odd$ . Since both addends have to be prime, one has to be even and one prime, which means it's $2$ . Plugging this in, the other number has to be $9999$ which is not prime (divisible by $9$ ) meaning there are $\boxed{\textbf{(A)}\ 0}$ answers.
~RandomMathGuy500 Comment from WrenMath: This is literally the same thing.

## Video Solution
https://youtu.be/qJuoLucUn9o by David

## Video Solution 2
https://youtu.be/GqTHx0tOB4o
~savannahsolver
### See Also