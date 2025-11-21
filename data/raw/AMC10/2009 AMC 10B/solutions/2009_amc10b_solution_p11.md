# 2009 AMC 10B Problem 11

## Problem

How many $7$ -digit palindromes (numbers that read the same backward as forward) can be formed using the digits $2$ , $2$ , $3$ , $3$ , $5$ , $5$ , $5$ ?

$\text{(A) } 6 \qquad \text{(B) } 12 \qquad \text{(C) } 24 \qquad \text{(D) } 36 \qquad \text{(E) } 48$

## Solution
A seven-digit palindrome is a number of the form $\overline{abcdcba}$ . Clearly, $d$ must be $5$ , as we have an odd number of fives. We are then left with $\{a,b,c\} = \{2,3,5\}$ . There are $3!$ permutations of these three numbers, since each is reflected over the midpoint we only have to count the first there. Each of the $\boxed{(A)6}$ permutations of the set $\{2,3,5\}$ will give us one palindrome.

## Solution 2
Say we have a 2 first. Then, we have a 2 pinned as the last digit, so we have to fill in the remaining digits with only 3's and 5's. We have 2 options for the second digit then, and the rest is fixed. This means that we have $2$ ways for this case.
Say we have a 3 first. By symmetry, this is the same as the 2 cases, so we have $2$ ways.
Say we have a 5 first. We then have a 5 in the middle. We can either have a 2 second or a 3 second. So we have $2$ ways.
This means that our answer is $2+2+2=\boxed{\textbf{(A)}6}$
~yofro
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .