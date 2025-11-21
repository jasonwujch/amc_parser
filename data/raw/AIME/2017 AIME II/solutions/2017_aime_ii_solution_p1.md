# 2017 AIME II Problem 1

## Problem

Find the number of subsets of $\{1, 2, 3, 4, 5, 6, 7, 8\}$ that are subsets of neither $\{1, 2, 3, 4, 5\}$ nor $\{4, 5, 6, 7, 8\}$ .

## Solution 1
The number of subsets of a set with $n$ elements is $2^n$ . The total number of subsets of $\{1, 2, 3, 4, 5, 6, 7, 8\}$ is equal to $2^8$ . The number of sets that are subsets of at least one of $\{1, 2, 3, 4, 5\}$ or $\{4, 5, 6, 7, 8\}$ can be found using complementary counting. There are $2^5$ subsets of $\{1, 2, 3, 4, 5\}$ and $2^5$ subsets of $\{4, 5, 6, 7, 8\}$ . It is easy to make the mistake of assuming there are $2^5+2^5$ sets that are subsets of at least one of $\{1, 2, 3, 4, 5\}$ or $\{4, 5, 6, 7, 8\}$ , but the $2^2$ subsets of $\{4, 5\}$ are overcounted. There are $2^5+2^5-2^2$ sets that are subsets of at least one of $\{1, 2, 3, 4, 5\}$ or $\{4, 5, 6, 7, 8\}$ , so there are $2^8-(2^5+2^5-2^2)$ subsets of $\{1, 2, 3, 4, 5, 6, 7, 8\}$ that are subsets of neither $\{1, 2, 3, 4, 5\}$ nor $\{4, 5, 6, 7, 8\}$ . $2^8-(2^5+2^5-2^2)=\boxed{196}$ .

## Solution 2
Upon inspection, a viable set must contain at least one element from both of the sets $\{1, 2, 3, 4, 5\}$ and $\{4, 5, 6, 7, 8\}$ . Since 4 and 5 are included in both of these sets, then they basically don't matter, i.e. if set A is a subset of both of those two then adding a 4 or a 5 won't change that fact. Thus, we can count the number of ways to choose at least one number from 1 to 3 and at least one number from 6 to 8, and then multiply that by the number of ways to add in 4 and 5. The number of subsets of a 3 element set is $2^3=8$ , but we want to exclude the empty set, giving us 7 ways to choose from $\{1, 2, 3\}$ or $\{6, 7, 8\}$ . We can take each of these $7 \times 7=49$ sets and add in a 4 and/or a 5, which can be done in 4 different ways (by adding both, none, one, or the other one). Thus, the answer is $49 \times 4=\boxed{196}$ .

## Solution 3
This solution is very similar to Solution $2$ . The set of all subsets of $\{1,2,3,4,5,6,7,8\}$ that are disjoint with respect to $\{4,5\}$ and are not disjoint with respect to the complements of sets (and therefore not a subset of) $\{1,2,3,4,5\}$ and $\{4,5,6,7,8\}$ will be named $S$ , which has $7\cdot7=49$ members. The union of each member in $S$ and the $2^2=4$ subsets of $\{4,5\}$ will be the members of set $Z$ , which has $49\cdot4=\boxed{196}$ members. $\blacksquare$
Solution by a1b2

## Solution 4
Consider that we are trying to figure out how many subsets are possible of $\{1,2,3,4,5,6,7,8\}$ that are not in violation of the two subsets $\{1,2,3,4,5\}$ and $\{4,5,6,7,8\}$ . Assume that the number of numbers we pick from the subset $\{1,2,3,4,5,6,7,8\}$ is $n$ . Thus, we can compute this problem with simple combinatorics:
If $n=1$ , $\binom{8}{1}$ $-$ ( $\binom{5}{1}$ + $\binom{5}{1}$ $- 2$ ) [subtract $2$ to eliminate the overcounting of the subset $\{4\}$ or $\{5\}$ ] = $8 - 8$ = $0$
If $n=2$ , $\binom{8}{2}$ $-$ ( $\binom{5}{2}$ + $\binom{5}{2}$ $- 1$ ) [subtract $1$ to eliminate the overcounting of the subset $\{4,5\}$ ] = $28 - 19$ = $9$
If $n=3$ , $\binom{8}{3}$ $-$ ( $\binom{5}{3}$ + $\binom{5}{3}$ ) = $56 - 20$ = $36$
If $n=4$ , $\binom{8}{4}$ $-$ ( $\binom{5}{4}$ + $\binom{5}{4}$ ) = $70 - 10$ = $60$
If $n=5$ , $\binom{8}{5}$ $-$ ( $\binom{5}{5}$ + $\binom{5}{5}$ ) = $56 - 2$ = $54$
If $n>5$ , then the set $\{1,2,3,4,5,6,7,8\}$ is never in violation of the two subsets $\{1,2,3,4,5\}$ and $\{4,5,6,7,8\}$ . Thus,
If $n=6$ , $\binom{8}{6}$ = $28$
If $n=7$ , $\binom{8}{7}$ = $8$
If $n=8$ , $\binom{8}{8}$ = $1$
Adding these together, our solution becomes $0$ + $9$ + $36$ + $60$ + $54$ + $28$ + $8$ + $1$ $=\boxed{196}$
Solution by IronicNinja~
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .