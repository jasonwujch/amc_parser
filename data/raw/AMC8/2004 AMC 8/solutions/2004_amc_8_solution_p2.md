# 2004 AMC 8 Problem 2

## Problem

How many different four-digit numbers can be formed by rearranging the four digits in $2004$ ?

$\textbf{(A)}\ 4\qquad\textbf{(B)}\ 6\qquad\textbf{(C)}\ 16\qquad\textbf{(D)}\ 24\qquad\textbf{(E)}\ 81$

## Solution 1
We can solve this problem easily, just by calculating how many choices there are for each of the four digits. First off, we know there are only $2$ choices for the first digit, because $0$ isn't a valid choice, or the number would a 3-digit number, which is not what we want. We have $3$ choices for the second digit, since we already used up one of the digits, and $2$ choices for the third, and finally just $1$ choices for the fourth and final one. $2*3*2*1$ is 12, but there are 2 zeros that have been counted as different numbers, so divide by 2 to get $\boxed{\textbf{(B)}\ 6}$ .

## Solution 2
Note that the four-digit number must start with either a $2$ or a $4$ . The four-digit numbers that start with $2$ are $2400, 2040$ , and $2004$ . The four-digit numbers that start with $4$ are $4200, 4020$ , and $4002$ which gives us a total of $\boxed{\textbf{(B)}\ 6}$ .

## Solution 3
In order for the resulting numbers to have four digits, they cannot start with $0$ . Therefore, both zeroes must be in the last three places. There are $\binom32=3$ ways to choose which two of the last three places are zeroes. Then there are $2\cdot1=2$ ways to arrange the $2$ and the $4$ in the remaining two places, giving us a total of $3\cdot2=\boxed{\textbf{(B)}\ 6}$ .
### See Also