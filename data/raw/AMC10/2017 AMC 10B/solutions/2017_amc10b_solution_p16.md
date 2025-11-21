# 2017 AMC 10B Problem 16

## Problem

How many of the base-ten numerals for the positive integers less than or equal to $2017$ contain the digit $0$ ?

$\textbf{(A)}\ 469\qquad\textbf{(B)}\ 471\qquad\textbf{(C)}\ 475\qquad\textbf{(D)}\ 478\qquad\textbf{(E)}\ 481$

## Solution 1
We can use complementary counting. There are $2017$ positive integers in total to consider, and there are $9$ one-digit integers, $9 \cdot 9 = 81$ two digit integers without a zero, $9 \cdot 9 \cdot 9 = 729$ three digit integers without a zero, and $9 \cdot 9 \cdot 9 = 729$ four-digit integers starting with a 1 without a zero. Therefore, the answer is $2017 - 9 - 81 - 729 - 729 = \boxed{\textbf{(A) }469}$ .

## Solution 2
First, we notice there are no one-digit numbers that contain a zero. There are $9$ two-digit integers and $9 \cdot 9 + 9 \cdot 9 + 9 = 171$ three-digit integers containing at least one zero. Next, we consider the four-digit integers beginning with one. There are $3 \cdot 9 \cdot 9 = 243$ of these four-digit integers with one zero, ${3 \choose 2} \cdot 9 = 27$ with two zeros, and $1$ with three zeros $(1000)$ . Finally, we consider the numbers $2000$ to $2017$ which all contain at least one zero. Adding all of these together we get $9 + 171 + 243 + 27 + 1 + 18 = \boxed{\textbf{(A) }469}$ .
~vsinghminhas
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .