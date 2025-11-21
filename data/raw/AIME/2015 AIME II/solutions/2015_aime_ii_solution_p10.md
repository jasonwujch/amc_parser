# 2015 AIME II Problem 10

## Problem

Call a permutation $a_1, a_2, \ldots, a_n$ of the integers $1, 2, \ldots, n$ quasi-increasing if $a_k \leq a_{k+1} + 2$ for each $1 \leq k \leq n-1$ . For example, 53421 and 14253 are quasi-increasing permutations of the integers $1, 2, 3, 4, 5$ , but 45123 is not. Find the number of quasi-increasing permutations of the integers $1, 2, \ldots, 7$ .

## Solution
The simple recurrence can be found.
When inserting an integer $n$ into a string with $n - 1$ integers, we notice that the integer $n$ has 3 spots where it can go: before $n - 1$ , before $n - 2$ , and at the very end.
Ex. Inserting 4 into the string 123: 4 can go before the 2 (1423), before the 3 (1243), and at the very end (1234).
Only the addition of the next number, $n$ , will change anything.
Thus the number of permutations with $n$ elements is three times the number of permutations with $n-1$ elements.
Start with $n=3$ since all $6$ permutations work. And go up: $18, 54, 162, 486$ .
Thus for $n=7$ there are $2*3^5=\boxed{486}$ permutations.
When you are faced with a brain-fazing equation and combinatorics is part of the problem, use recursion! This same idea appeared on another AIME with an 8-box problem.
- 2006 AIME I Problem 11
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .