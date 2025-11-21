# 2003 AIME I Problem 3

## Problem

Let the set $\mathcal{S} = \{8, 5, 1, 13, 34, 3, 21, 2\}.$ Susan makes a list as follows: for each two-element subset of $\mathcal{S},$ she writes on her list the greater of the set's two elements. Find the sum of the numbers on the list.

## Solution
Order the numbers in the set from greatest to least to reduce error: $\{34, 21, 13, 8, 5, 3, 2, 1\}.$ Each element of the set will appear in $7$ two-element subsets , once with each other number.
- $34$ will be the greater number in $7$ subsets.
- $21$ will be the greater number in $6$ subsets.
- $13$ will be the greater number in $5$ subsets.
- $8$ will be the greater number in $4$ subsets.
- $5$ will be the greater number in $3$ subsets.
- $3$ will be the greater number in $2$ subsets.
- $2$ will be the greater number in $1$ subsets.
- $1$ will be the greater number in $0$ subsets.
Therefore the desired sum is $34\cdot7+21\cdot6+13\cdot5+8\cdot4+5\cdot3+3 \cdot2+2\cdot1+1\cdot0=\boxed{484}$ .
Note: Note that $7+6+5+4+3+2+1=\binom{8}{2}$ , so we have counted all the possible cases.
~Yiyj1

## Solution
Thinking of this problem algorithmically, one can "sort" the array to give: \[{1, 2, 3, 5, 8, 13, 21, 34}\]
Now, notice that when we consider different pairs, we are only going to fixate one element and look at the all of the next elements in the array, basically the whole $j = i + 1$ shebang. Then, we see that if we set the sum of the whole array to $x,$ we get out answer to be
\[(x-1) + (x-3) + (x-6) + (x-11) + (x-19) + (x-32) + (x-53) = 7x - 125\]
Finding $7x$ isn't hard, and we see that it is equal to $609$ :
\[609 - 125 = \boxed{484}\]
These problems are copyrighted © by the Mathematical Association of America.