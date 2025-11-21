# 2002 AMC 12P Problem 7

## Problem

How many three-digit numbers have at least one $2$ and at least one $3$ ?

$\text{(A) }52 \qquad \text{(B) }54 \qquad \text{(C) }56 \qquad \text{(D) }58 \qquad \text{(E) }60$

## Solution 1
We can do this problem with some simple case work.
Case 1: The hundreds place is not $2$ or $3.$ This means that the tens place and ones place must be $2$ and $3$ respectively or $3$ and $2$ respectively. This case covers $1, 4, 5, 6, 7, 8,$ and $9,$ so it gives us $2 \cdot 7 = 14$ cases.
Case 2: The hundreds place is $2.$ This means that $3$ must be in the tens place or ones place. Starting with cases in which the tens place is not $3$ , we get $203, 213, 223, 243, 253, 263, 273, 283,$ and $293.$ With cases in which the tens place is $3$ , we have $230-239$ , or $10$ more cases. This gives us $9 + 10=19$ cases.
Case 3: The hundreds place is $3.$ This case is almost identical to the second case, just swap the $2$ s with $3$ s and $3$ s with $2$ s in the reasoning and its the same, giving us an additional $19$ cases.
Adding up all of these cases gives $14+19+19=52$ cases, or $\boxed{\textbf{(A) }52}.$

## Solution 2 (PIE)
We can solve this problem with the principle of inclusion-exclusion. Let $\#(A)$ be the number of three-digit numbers without the digit $2$ , let $\#(B)$ be the number of three-digit numbers without the digit $3$ , and let $\#(A \cap B)$ be the number of three-digit numbers without digits $2$ or $3$ .
Notice that $\#(A)=\#(B)$ by symmetry. We use constructive counting to find that \[\#(A) = 8 \cdot 9 \cdot 9 = 648\] so $\#(A) = \#(B) = 648$ . Similarly, \[\#(A \cap B) = 7 \cdot 8 \cdot 8 = 448.\]
Hence, by PIE, \[\#(A \cup B) = \#(A) + \#(B) - \#(A \cap B) = 648 + 648 - 448 = 848\] so the count of three-digit numbers that do not have a digit $2$ or a digit $3$ is $\#(A \cup B) = 848$ .
There are $9 \cdot 10 \cdot 10 = 900$ ways to construct a three-digit number in total, so we have $900 - 848 = \boxed{\textbf{(A) }52}$ numbers that have at least one of digit $2$ and $3$ .
~ Math-lover1
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .