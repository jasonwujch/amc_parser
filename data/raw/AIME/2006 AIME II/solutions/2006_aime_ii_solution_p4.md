# 2006 AIME II Problem 4

## Problem

Let $(a_1,a_2,a_3,\ldots,a_{12})$ be a permutation of $(1,2,3,\ldots,12)$ for which

An example of such a permutation is $(6,5,4,3,2,1,7,8,9,10,11,12).$ Find the number of such permutations.

## Solution
Clearly, $a_6=1$ . Now, consider selecting $5$ of the remaining $11$ values. Sort these values in descending order, and sort the other $6$ values in ascending order. Now, let the $5$ selected values be $a_1$ through $a_5$ , and let the remaining $6$ be $a_7$ through ${a_{12}}$ . It is now clear that there is a bijection between the number of ways to select $5$ values from $11$ and ordered 12-tuples $(a_1,\ldots,a_{12})$ . Thus, there will be ${11 \choose 5}=\boxed{462}$ such ordered 12-tuples.

## Solution 2
There are $\binom{12}{6}$ ways to choose 6 numbers from $(1,2,3,\ldots,12)$ , and then there will only be one way to order them. And since that $a_6<a_7$ , only half of the choices will work, so the answer is $\frac{\binom{12}{6}}{2}=462$ 12-tuples - mathleticguyyy

## Solution 3
Clearly, $a_6=1$ , and either $a_1$ or $a_{12}$ is 12.
Case 1: $a_1 = 12$
In this case, there are 4 empty spaces between $a_1$ and $a_6$ , and 6 empty spaces between $a_6$ and $a_{12}$ . $\binom{10}{4}$ is 210. This splits the remaining 10 numbers into two distinct sets that are automatically ordered. For this reason, there is no need to multiply by two to count doubles or treat as a permutation.
Case 2: $a_{12} = 12$
In this case, there are 5 empty spaces between $a_1$ and $a_6$ , and 5 empty spaces between $a_6$ and $a_{12}$ . $\binom{10}{5}$ is 252. Like last time, this splits the remaining 10 numbers into two distinct sets that are automatically ordered. It is important to realize that the two sets are distinct because one side has 12 and the other does not. There is no need to multiply by two.
$210 + 252 = \boxed{462}$ ordered 12-tuples.
-jackshi2006
These problems are copyrighted © by the Mathematical Association of America.