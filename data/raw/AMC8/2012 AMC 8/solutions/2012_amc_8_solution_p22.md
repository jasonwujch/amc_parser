# 2012 AMC 8 Problem 22

## Problem

Let $R$ be a set of nine distinct integers. Six of the elements are $2$ , $3$ , $4$ , $6$ , $9$ , and $14$ . What is the number of possible values of the median of $R$ ?

$\textbf{(A)}\hspace{.05in}4\qquad\textbf{(B)}\hspace{.05in}5\qquad\textbf{(C)}\hspace{.05in}6\qquad\textbf{(D)}\hspace{.05in}7\qquad\textbf{(E)}\hspace{.05in}8$

## Solution 1
First, we find that the minimum value of the median of $R$ will be $3$ .
We then experiment with sequences of numbers to determine other possible medians.
Median: $3$
Sequence: $-2, -1, 0, 2, 3, 4, 6, 9, 14$
Median: $4$
Sequence: $-1, 0, 2, 3, 4, 6, 9, 10, 14$
Median: $5$
Sequence: $0, 2, 3, 4, 5, 6, 9, 10, 14$
Median: $6$
Sequence: $0, 2, 3, 4, 6, 9, 10, 14, 15$
Median: $7$
Sequence: $2, 3, 4, 6, 7, 8, 9, 10, 14$
Median: $8$
Sequence: $2, 3, 4, 6, 8, 9, 10, 14, 15$
Median: $9$
Sequence: $2, 3, 4, 6, 9, 14, 15, 16, 17$
Any number greater than $9$ also cannot be a median of set $R$ .
Therefore, the answer is $\boxed{\textbf{(D)}\ 7}$ .

## Solution 2
Let the values of the missing integers be $x, y, z$ . We will find the bound of the possible medians.
The smallest possible median will happen when we order the set as $\{x, y, z, 2, 3, 4, 6, 9, 14\}$ . The median is $3$ .
The largest possible median will happen when we order the set as $\{2, 3, 4, 6, 9, 14, x, y, z\}$ . The median is $9$ .
Therefore, the median must be between $3$ and $9$ inclusive, yielding $\boxed{\textbf{(D)}\ 7}$ possible medians.
~superagh

## Video Solution
https://youtu.be/yBSrLxv0LbY ~savannahsolver
### See Also