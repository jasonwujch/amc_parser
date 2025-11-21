# 2017 AMC 8 Problem 7

## Problem

Let $Z$ be a 6-digit positive integer, such as 247247, whose first three digits are the same as its last three digits taken in the same order. Which of the following numbers must also be a factor of $Z$ ?

$\textbf{(A) }11\qquad\textbf{(B) }19\qquad\textbf{(C) }101\qquad\textbf{(D) }111\qquad\textbf{(E) }1111$

## Solution 1 (detailed explanation)
To check, if a number is divisible by 19, take its unit digit and multiply it by 2, then add the result to the rest of the number, and repeat this step until the number is reduced to two digits. If the result is divisible by 19, then the original number is also divisible by 19.
After we got 19 eliminated, we can see that the other options have a lot of 1's in them. The divisibility rule for 11 is add alternating digits up, then take the difference of them. The example number works like that. If we add variables, ABCDEF to make number ABCABC, we can see that (A+C+B) - (B+A+C) = 0. Which is divisible by 11, so our answer choice is $\boxed{\textbf{(A)}\ 11}$ .
by: CHECKMATE2021 (edited by CHECKMATE2021)

## Solution 2
We are given one of the numbers that can represent $Z$ , so we can just try out the options to see which one is a factor of $247247$ . By the previous solution, 19 does not work even though it is a factor of the example number. We get $\boxed{\textbf{(A)}\ 11}$ .
~CHECKMATE2021

## Solution 3( similar to solution 1)
Similar to solution 1, let $Z=ABCABC$ . To prove it is divisible by 11, we can compute its alternating sum, which is $A-B+C-A+B-C=0$ , which is divisible by 11. Therefore, the answer is $\boxed{\textbf{(A)}\ 11}$ .
~PEKKA

## Solution 4
We can find that all numbers like $Z$ are divisible by 1001. 1001 is divisible by 11 because when we divide it, we get a whole number. So, the answer is $\boxed{\textbf{(A)}\ 11}$ .
~AfterglowBlaziken

## Video Solution (CREATIVE THINKING!!!)
https://youtu.be/WVHPSVOXE4I
~Education, the Study of Everything

## Video Solution by OmegaLearn
https://youtu.be/At4w8uylvv8?t=99 https://youtu.be/7an5wU9Q5hk?t=647

## Video Solution
https://youtu.be/-saKu3lLU0U
~savannahsolver
### See Also