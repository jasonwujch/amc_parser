# 2019 AMC 8 Problem 13

## Problem

A palindrome is a number that has the same value when read from left to right or from right to left. (For example, 12321 is a palindrome.) Let $N$ be the least three-digit integer which is not a palindrome but which is the sum of three distinct two-digit palindromes. What is the sum of the digits of $N$ ?

$\textbf{(A) }2\qquad\textbf{(B) }3\qquad\textbf{(C) }4\qquad\textbf{(D) }5\qquad\textbf{(E) }6$

## Solution 1
Note that the only positive 2-digit palindromes are multiples of 11, namely $11, 22, \ldots, 99$ . Since $N$ is the sum of 2-digit palindromes, $N$ is necessarily a multiple of 11. The smallest 3-digit multiple of 11 which is not a palindrome is 110, so $N=110$ is a candidate solution. We must check that 110 can be written as the sum of three distinct 2-digit palindromes; this suffices as $110=77+22+11$ . Then, $N = 110$ , and the sum of the digits of $N$ is $1+1+0 = \boxed{\textbf{(A) }2}$ .

## Solution 2 (variant of Solution 1)
We already know that two-digit palindromes can only be two-digit multiples of 11; which are: $11, 22, 33, 44, 55, 66, 77, 88,$ and $99$ . Since this is clear, we will need to find out the least multiple of 11 that is not a palindrome. Then, we start counting. $110 \ldots$ Aha! This multiple of 11, 110, not only isn’t a palindrome, but it also is the sum of three distinct two-digit palindromes, for example: 11 + 22 + 77, 22 + 33 + 55, and 44 + 11 + 55! The sum of $N$ ’s digits is $1+1+0 = \boxed{\textbf{(A) }2}$ .
Thank you to the writer of Solution 1 for inspiring me to create this!
EarthSaver 15:13, 11 June 2021 (EDT)

## Solution 3 (basically a version of the above solutions)
As stated above, two-digit palindromes can only be two-digit multiples of 11. We can see that if we add anything that are multiples of 11 together, we will again get a multiple of 11. For instance, $11+22=33$ . Since we know this fact and we are finding the smallest value possible, we can start with the first three-digit multiple of 11 which is $110$ . Since this is not a palindrome and can be the sum of 3 two-digit palindromes (see above solutions for more details), $110$ fits the bill. We can see that the sum of $110$ 's digits is $1+1+0 = \boxed{\textbf{(A) }2}$ .
~yeye

## Video Solution by Pi Academy (Really Easy 👍)
https://youtu.be/7xlBdxcsP3I?si=sFJGKXnBUUN7Su-C

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/IgpayYB48C4?si=AbOfamWIMyCRNHTA&t=3984 ~Math-X

## Video Solution 1
https://youtu.be/gOZOCFNXMhE ~ The Learning Royal

## Video Solution 2
https://www.youtube.com/watch?v=bOnNFeZs7S8

## Video Solution 3
Solution detailing how to solve the problem: https://www.youtube.com/watch?v=PJpDJ23sOJM&list=PLbhMrFqoXXwmwbk2CWeYOYPRbGtmdPUhL&index=14

## Video Solution 4
https://youtu.be/WeQuJEQKVdo
~savannahsolver

## Video Solution (CREATIVE ANALYSIS!!!)
https://youtu.be/FISgn9laDaI
~Education, the Study of Everything

## Video Solution by The Power of Logic(1 to 25 Full Solution)
https://youtu.be/Xm4ZGND9WoY
~Hayabusa1