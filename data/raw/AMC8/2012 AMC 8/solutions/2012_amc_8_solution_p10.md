# 2012 AMC 8 Problem 10

## Problem

How many 4-digit numbers greater than 1000 are there that use the four digits of 2012?

$\textbf{(A)}\hspace{.05in}6\qquad\textbf{(B)}\hspace{.05in}7\qquad\textbf{(C)}\hspace{.05in}8\qquad\textbf{(D)}\hspace{.05in}9\qquad\textbf{(E)}\hspace{.05in}12$

## Solution 1
For this problem, all we need to do is find the amount of valid 4-digit numbers that can be made from the digits of $2012$ , since all of the valid 4-digit number will always be greater than $1000$ . The best way to solve this problem is by using casework.
There can be only two leading digits, namely $1$ or $2$ .
When the leading digit is $1$ , you can make $\frac{3!}{2!1!} \implies 3$ such numbers.
When the leading digit is $2$ , you can make $3! \implies 6$ such numbers.
Summing the amounts of numbers, we find that there are $\boxed{\textbf{(D)}\ 9}$ such numbers.

## Solution 2
Notice that the first digit cannot be $0$ , as the number is greater than $1000$ . Therefore, there are three digits that can be in the thousands.
The rest three digits of the number have no restrictions, and therefore there are $3! \implies 6$ for each leading digit.
Since the two $2$ 's are indistinguishable, there are $\frac {3\cdot6}{2}$ such numbers $\implies \boxed{\textbf{(D)}\ 9}$ .
Note by algebramaster2: 1 and 2 are the only digits that can be in the thousands place as 0 in the thousands place will not make the number 4 digit anymore.

## Solution 3 (a simpler version of Solution 2)
We can list out the four digits in the number. The first digit of the number can’t be 0 since the number is greater than $1000$ . This leaves us with three integers for the digit in the thousands place. We have no restrictions in the hundreds place except for the fact that it can’t be the integer we chose for the thousands place. Continuing this pattern, there are $3$ choices for the thousands place, $3$ for the hundreds, $2$ for the tens, and $1$ for the ones. Adding this up we get $9$ which is choice $\boxed{\textbf{(D)} }$ .
—-jason.ca

## Solution 4 (Complementary Counting)
There are $\frac{4!}{2!}$ ways to arrange the numbers in $2012$ . The number of ways to arrange 2012 with 0 as the first digit is 3 because there are three places to put the 1 and the 2s are the same. $12-3= 9$ which is choice $\boxed{\textbf{(D)} }$ .
~ Edited by GeometryMystery

## Video Solution
https://youtu.be/OBKIeTgw4Zg ~savannahsolver
### See Also