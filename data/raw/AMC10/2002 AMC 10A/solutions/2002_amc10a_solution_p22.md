# 2002 AMC 10A Problem 22

## Problem

A set of tiles numbered 1 through 100 is modified repeatedly by the following operation: remove all tiles numbered with a perfect square , and renumber the remaining tiles consecutively starting with 1. How many times must the operation be performed to reduce the number of tiles in the set to one?

$\text{(A)}\ 10 \qquad \text{(B)}\ 11 \qquad \text{(C)}\ 18 \qquad \text{(D)}\ 19 \qquad \text{(E)}\ 20$

## Solution 1
The pattern is quite simple to see after listing a couple of terms.
\[\begin{tabular}{|r|r|r|} \hline \#&\text{Removed}&\text{Left}\\ \hline 1&10&90\\ 2&9&81\\ 3&9&72\\ 4&8&64\\ 5&8&56\\ 6&7&49\\ 7&7&42\\ 8&6&36\\ 9&6&30\\ 10&5&25\\ 11&5&20\\ 12&4&16\\ 13&4&12\\ 14&3&9\\ 15&3&6\\ 16&2&4\\ 17&2&2\\ 18&1&1\\ \hline \end{tabular}\]
Thus, the answer is $\boxed{\text{(C) } 18}$ .

## Solution 2
Given $n^2$ tiles, a step removes $n$ tiles, leaving $n^2 - n$ tiles behind. Now, $(n-1)^2 = n^2 - n + (1-n) < n^2 - n < n^2$ , so in the next step $n-1$ tiles are removed. This gives $(n^2 - n) - (n-1) = n^2 - 2n + 1 = (n-1)^2$ , another perfect square.
Thus each two steps we cycle down a perfect square, and in $(10-1)\times 2 = 18$ steps, we are left with $1$ tile, hence our answer is $\boxed{\text{(C) } 18}$ .

## Solution 3
We start of with $100 = 10 \cdot 10$ numbers. When we use the certain operation, call if $P(x)$ , have $100 - 10 = 90 = 10 \cdot 9$ . Then we do $P(x)$ again, to subtract $9$ numbers and get $9 \cdot 9$ . In the end, we will want $1 = 1 \cdot 1$ . We can say we have to use $P(x)$ once to make $n \cdot n$ into $n \cdot (n-1)$ . Thus we must use it twice to get from $n \cdot n$ to $(n-1)(n-1)$ . For example, it takes us $2$ of $P(x)$ to get from $10 \cdot 10$ to $9 \cdot 9$ . Then $2$ of $P(x)$ to get from $9 \cdot 9$ to $8 \cdot 8$ . You should try this with $7$ and $6$ , and see it works. This means we can have $n$ be the number we start with, and $1$ be the number we want. Then we would use $P(x)$ , $2(n - 1)$ times to get $1 \cdot 1$ . Substituting $n$ for $10$ we get $2(10-1) = 2 \cdot 9 = \boxed{18}$ . - Wiselion

## Video Solution
https://www.youtube.com/watch?v=CuKko0JpIdQ ~David
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .