# 2017 AIME I Problem 11

## Problem

Consider arrangements of the $9$ numbers $1, 2, 3, \dots, 9$ in a $3 \times 3$ array. For each such arrangement, let $a_1$ , $a_2$ , and $a_3$ be the medians of the numbers in rows $1$ , $2$ , and $3$ respectively, and let $m$ be the median of $\{a_1, a_2, a_3\}$ . Let $Q$ be the number of arrangements for which $m = 5$ . Find the remainder when $Q$ is divided by $1000$ .

## Solution 1
Assume that $5 \in \{a_1, a_2, a_3\}$ , $m \neq 5$ , and WLOG, $\max{(a_1, a_2, a_3)} = 5$ . Then we know that the other two medians in $\{a_1, a_2, a_3\}$ and the smallest number of rows 1, 2, and 3 are all less than 5. But there are only 4 numbers less than 5 in $1, 2, 3, \dots, 9$ , a Contradiction. Thus, if $5 \in \{a_1, a_2, a_3\}$ , then $m = 5$ .
WLOG, assume $5$ is in the upper left corner. One of the two other values in the top row needs to be below $5$ , and the other needs to be above $5$ . This can be done in $4\cdot4\cdot2=32$ ways. The other $6$ can be arranged in $6!=720$ ways. Finally, accounting for when $5$ is in every other space, our answer is $32\cdot720\cdot9$ , which is $207360$ . But we only need the last $3$ digits, so $\boxed{360}$ is our answer.
~Solution by SuperSaiyanOver9000, mathics42, edited by zhaohm
### Alternative Proof
Claim: As long as one median is equal to $5,$ the overall median is equal to $5.$
Proof: Notice that to obtain a median of $5,$ we need one number greater and one number lesser than $5$ along with $5.$
Thus, we remain with 3 numbers greater than $5$ and 3 less than $5,$ meaning that the overall median, no matter the distribution, of the remaining two rows must be $5.$
mathboy282

## Solution 2
(Complementary Counting with probability)
Notice that m can only equal 4, 5, or 6, and 4 and 6 are symmetric.
WLOG let $m=4$
1. There is a $\frac{15}{28}$ chance that exactly one of 1, 2, 3 is in the same row with 4.
There are 3 ways to select which of the smaller numbers will get in the row, and then 5
ways to select the number larger than 4.
$\frac{\dbinom{3}{1}\cdot\dbinom{5}{1}}{\dbinom{8}{2}} = \frac{15}{28}$
2. There is a $\frac{2}{5}$ chance that the other two smaller numbers end up in the same row.
There are 2 ways to select the row that the two smaller number are in, and then $\dbinom{3}{2}$ ways
to place the smaller numbers in the row.
$\frac{\dbinom{2}{1}\cdot\dbinom{3}{2}}{\dbinom{6}{2}} = \frac{2}{5}$
$9!(1-2*\frac{15}{28}*\frac{2}{5})=362880*\frac{4}{7}=207\boxed{360}$ .

## Solution 3
We will make sure to multiply by $3!$ in the end to account for all the possible permutation of the rows.
WLOG, let $5$ be present in the Row # $1$ .
Notice that $5$ MUST be placed with a number lower than it and a number higher than it.
This happens in $4\cdot4$ ways. You can permutate Row # $1$ in $3!$ ways.
Now, take a look at Row $2$ and Row $3$ .
Because there are $6$ numbers to choose from now, you can assign #'s to Row's #2&3 in
$\frac{\binom{6}{3}\cdot\binom{3}{3}}{2}$ ways. There are $3!\cdot3!$ ways to permute the numbers in the individual Rows.
Hence, our answer is $3!(4\cdot4\cdot3!\cdot{10}\cdot{3!}\cdot{3!})=3!(16\cdot60\cdot36)=3!(34560)\implies{207\boxed{360}}$

## Solution 4
We see that if one of the medians is 5, then there are two remaining numbers greater than 5 and two less than 5, so it follows that $m=5$ . There are 3 ways to choose which row to have 5 in, $4\cdot 4=16$ ways to choose the other two numbers in that row, $3!=6$ ways to arrange the numbers in that row, and $6!=720$ ways for the remaining numbers, for our answer is $3\cdot 16\cdot 6\cdot 720=207\boxed{360}$ . -Stormersyle

## Solution 5
We take the grid, and we do a bunch of stuff with it. First, we sort each row, smallest on the left, largest on the right, then we arrange these 3 rows such that the middle #s are increasing, from top to bottom. Thus, we get that the cell in the very center of the grid must be 5. (We need to multiply by 1296 at the end)
Let S mean a number that is < 5, L mean a number > 5.
In the 2 blank corners, one can be S, and the other one has to be L.
If the top right corner is S, there are 16 ways, otherwise, there are 144 ways. (This is left as an exercise to the reader).
Thus, there are 160 * 1296 total configurations, which gets us an answer of $207\boxed{360}$
-AlexLikeMath

## Solution 6
We note that if $5$ is a median of one of the rows, then $m=5$ . First, focus on the row with $5$ in it. There are $4^2$ ways to choose the other numbers in that row and then $3!$ ways to order it. Now, clearly, there are $6!$ ways to put the other $6$ numbers into the remaining slots so $Q=6!\cdot3!\cdot4^2\cdot3=207360$ . Hence, our answer is $\boxed{360}$ .
~pleaseletmewin

## Solution 7
Let $A = \{1,2,3,4\}$ and $B = \{6,7,8,9\}$ . WLOG, if we let 5 be on the first row, then $m=5$ if and only if $a_1=5$ . Thus, the two other numbers that are on row 1 $p, q$ satisfies one of the two following conditions:
\[(1) \quad p\in A \quad \textrm{and} \quad q\in B\] or \[(2) \quad p\in B \quad \textrm{and} \quad q\in A\]
The probability of this happening can be calculated through $\frac{4^2}{{8 \choose 2}} = \frac{4}{7}$ . Therefore, \[Q = 9! \cdot \frac{4}{7} = 207360 \equiv \boxed{360} \pmod {1000} .\]
~Kscv
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .