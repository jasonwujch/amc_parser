# 2009 AIME II Problem 6

## Problem

Let $m$ be the number of five-element subsets that can be chosen from the set of the first $14$ natural numbers so that at least two of the five numbers are consecutive. Find the remainder when $m$ is divided by $1000$ .

## Solution
We can use complementary counting. We can choose a five-element subset in ${14\choose 5}$ ways. We will now count those where no two numbers are consecutive. We will show a bijection between this set, and the set of 10-element strings that contain 5 $A$ s and 5 $B$ s, thereby showing that there are ${10\choose 5}$ such sets.
Given a five-element subset $S$ of $\{1,2,\dots,14\}$ in which no two numbers are consecutive, we can start by writing down a string of length 14, in which the $i$ -th character is $A$ if $i\in S$ and $B$ otherwise. Now we got a string with 5 $A$ s and 9 $B$ s. As no two numbers were consecutive, we know that in our string no two $A$ s are consecutive. We can now remove exactly one $B$ from between each pair of $A$ s to get a string with 5 $A$ s and 5 $B$ s. And clearly this is a bijection, as from each string with 5 $A$ s and 5 $B$ s we can reconstruct one original set by reversing the construction.
Hence we have $m = {14\choose 5} - {10\choose 5} = 2002 - 252 = 1750$ , and the answer is $1750 \bmod 1000 = \boxed{750}$ .

## Solution 2
Let $A$ be the number of ways in which $5$ distinct numbers can be selected from the set of the first $14$ natural numbers, and let $B$ be the number of ways in which $5$ distinct numbers, no two of which are consecutive, can be selected from the same set. Then $m = A -B$ . Because $A = \dbinom{14}{5}$ , the problem is reduced to finding $B$ . Consider the natural numbers $1 \leq a_1 < a_2 < a_3 < a_4 < a_5 \leq 14$ . If no two of them are consecutive, the numbers $b_1 = a_1, b_2 = a_2 - 1$ , $b_3 = a_3 - 2$ , $b_4 = a_4 - 3$ , and $b_5 = a_5 - 4$ are distinct numbers from the interval $[1, 10]$ . Conversely, if $b_1 < b_2 < b_3 < b_4 < b_5$ are distinct natural numbers from the interval $[1, 10]$ , then $a_1 = b_1$ , $a_2 = b_2 + 1$ , $a_3 = b_3 + 2$ , $a_4 = b_4 + 3$ , and $a_5 = b_5 + 4$ are from the interval $[1, 14]$ , and no two of them are consecutive. Therefore counting $B$ is the same as counting the number of ways of choosing $5$ distinct numbers from the set of the first $10$ natural numbers. Thus $B = \dbinom{10}{5}$ . Hence $m = A - B = \dbinom{14}{5} - \dbinom{10}{5} = 2002 - 252 = 1750$ and the answer is $750$ .

## Solution 3
We will approach this problem using complementary counting. First it is obvious, there are $\binom{14}{5}$ total sets. To find the number of sets with NO consecutive elements, we do a little experimentation. Consider the following:
Start of with any of the $14$ numbers, say WLOG, $1$ . Then we cannot have $2$ . So again WLOG, we may pick $3$ . Then we cannot have $4$ , so again WLOG, we may pick $5$ . Then not $6$ , but $7$ , then not $8$ , but $9$ . Now we have the set ${1,3,5,7,9}$ , and we had to remove $4$ digits from the $14$ total amount, so there wasn't any consecutive numbers. So we have that the number of non-consecutive cardinality $5$ sets, is $\binom{14-4}{5}=\binom{10}{5}$ . Now you already read the solutions above, and if you are here, you are either confused, or looking for more. So now the answer is simply $1750$ , which is $\boxed{750}$ (mod $1000$ ).
~th1nq3r
(To get a feel for my solution, draw the set {_, _, _, _, _}, list all the $14$ numbers on the side, and fill up the set starting with $1$ and doing the steps I used for my solution).

## Solution 4 (Stars and Bars)
We will proceed by complementary counting. We can easily see that there are $\binom{14}{5}$ ways to select $5$ element subsets from the original set. Now, we must find the number of subsets part of that group that do NOT have any consecutive integers.
We can think of this situation as stars and bars. We have $9$ stars and $5$ bars, where the stars represent the integers NOT in the subset while the bars ARE the integers in the chosen subset. We want the amount of combinations where there is at least one star between each bar (meaning that none of the integers in the subset are consecutive). To do this, we remove $4$ stars from the total $9$ stars ( $4$ because that is the amount that is between each bar). Now, we have $5$ stars and $5$ bars with no restrictions, so we calculate this as $\binom{10}{5}$ , which is $252$ . Hence, $\binom{14}{5} - \binom{10}{5} = 2002 - 252 = 1750$ , which becomes $\boxed{750}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.