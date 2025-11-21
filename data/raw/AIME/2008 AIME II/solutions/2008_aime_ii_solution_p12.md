# 2008 AIME II Problem 12

## Problem

There are two distinguishable flagpoles, and there are $19$ flags, of which $10$ are identical blue flags, and $9$ are identical green flags. Let $N$ be the number of distinguishable arrangements using all of the flags in which each flagpole has at least one flag and no two green flags on either pole are adjacent. Find the remainder when $N$ is divided by $1000$ .

## Solution

## Solution 1
The well known problem of ordering $x$ elements of a string of $y$ elements such that none of the $x$ elements are next to each other has ${y-x+1\choose x}$ solutions. (1)
We generalize for $a$ blues and $b$ greens. Consider a string of $a+b$ elements such that we want to choose the greens such that none of them are next to each other. We would also like to choose a place where we can divide this string into two strings such that the left one represents the first pole, and the right one represents the second pole, in order up the pole according to position on the string.
However, this method does not account for the fact that the first pole could end with a green, and the second pole could start with a green, since the original string assumed that no greens could be consecutive. We solve this problem by introducing an extra blue, such that we choose our divider by choosing one of these $a+1$ blues, and not including that one as a flag on either pole.
From (1), we now have ${a+2\choose b}$ ways to order the string such that no greens are next to each other, and $a+1$ ways to choose the extra blue that will divide the string into the two poles: or $(a+1){a+2\choose b}$ orderings in total.
However, we have overcounted the solutions where either pole has no flags, we have to count these separately. This is the same as choosing our extra blue as one of the two ends, and ordering the other $a$ blues and $b$ greens such that no greens are next to each other: for a total of $2{a+1\choose b}$ such orderings.
Thus, we have $(a+1){a+2\choose b}-2{a+1\choose b}$ orderings that satisfy the conditions in the problem: plugging in $a=10$ and $b=9$ , we get $2310 \equiv \boxed{310} \pmod{1000}$ .

## Solution 2
Split the problem into two cases:
Case 1 - Both poles have blue flags: There are 9 ways to place the 10 blue flags on the poles. In each of these configurations, there are 12 spots that a green flag could go. (either in between two blues or at the tops or bottoms of the poles) Then, since there are 9 green flags, all of which must be used, there are ${12\choose9}$ possiblities for each of the 9 ways to place the blue flags. Total: ${12\choose9}*9$ possibilities.
Case 2 - One pole has no blue flags: Since each pole is non empty, the pole without a blue flag must have one green flag. The other pole has 10 blue flags and, by the argument used in case 1, there are ${11\choose8}$ possibilities, and since the poles are distinguishable, there are a total of $2*{11\choose8}$ possiblities for this case.
Finally, we have $9*{12\choose9}+2*{11\choose8}=2310 \equiv \boxed{310} \pmod{1000}$ as our answer.

## Solution 3 (mad bash)
Call the two flagpoles Flagpole A and Flagpole B. Case 1: Flag distribution: 1|18 B|variable: $\dbinom{10}{9}=10$ ways G|variable: $\dbinom{11}{8}=165$ ways Case 2: Flag distribution: 2|17 BB|variable: $\dbinom{9}{9}=1$ way BG|variable (two ways to arrange the first sequence): $\dbinom{10}{8} \times 2 = 90$ ways GG|variable: can't happen Case 3: Flag distribution: 3|16 BBB|variable: can't happen BBG|variable (3 legal ways to arrange): $\dbinom{9}{8} \times 3 = 27$ ways GBG|variable (1 legal way to arrange): $\dbinom{10}{7} = 120$ ways GGG|variable: clearly can't happen Case 4: Flag distribution: 4|15 BBBB|variable: can't happen BBBG|variable (4 legal ways to arrange): $\dbinom{8}{8} \times 4 = 4$ ways GBBG|variable (3 legal ways to arrange): $\dbinom{9}{7} \times 3 = 108$ ways GGBG|variable: can't happen GGGG|variable: can't happen Case 5: Flag distribution: 5|14 BBBBB|variable: can't happen BBBBG|variable: can't happen BBGBG|variable (6 legal ways to arrange): $\dbinom{8}{7} \times 6 = 48$ ways GBGBG|variable (1 legal way to arrange): $\dbinom{9}{6} = 84$ ways GGGGB|variable: can't happen GGGGG|variable: can't happen Case 6: Flag distribution: 6|13 BBBBBB|variable: can't happen BBBBBG|variable: can't happen BBBBGG|variable (10 legal ways to arrange): $\dbinom{7}{7} \times 10 = 10$ ways BBBGGG|variable (4 legal ways to arrange): $\dbinom{8}{6} \times 4 = 112$ ways BBGGGG|variable: can't happen BGGGGG|variable: can't happen GGGGGG|variable: can't happen Case 7: Flag distribution: 7|12 BBBBBBB|variable: can't happen BBBBBBG|variable: can't happen BBBBBGG|variable: can't happen BBBBGGG|variable (10 legal ways to arrange): $\dbinom{7}{6} \times 10 = 70$ ways BBBGGGG|variable (1 legal way to arrange): $\dbinom{8}{5} = 56$ ways rest can't happen Case 8: Flag distribution: 8|11 BBBBBBBB|variable: can't happen BBBBBBBG|variable: can't happen BBBBBBGG|variable: can't happen BBBBBGGG|variable (20 legal ways to arrange): $\dbinom{6}{6} \times 20 = 20$ ways BBBBGGGG|variable: (5 legal ways to arrange): $\dbinom{7}{5} \times 5 = 105$ ways others can't happen Case 9: Flag distribution: 9|10 BBBBBGGGG|variable (15 legal ways to arrange): $\dbinom{6}{5} \times 15 = 90$ ways BBBBGGGGG|variable (1 legal way to arrange): $\dbinom{7}{4} = 35$ ways others can't happen So our total number of ways is $2$ times $10+165+1+90+27+120+4+108+48+84+10+112+70+56+20+105+90+35$ (since the two flagpoles are distinguishable) which is $2310$ ways. We have to find the last 3 digits, so our final answer is $310$ .
Solution by fidgetboss_4000
Note: Do not attempt unless you are good at bashing.

## Solution 4 (Vandermonde's)
Let the number of blue flags on the first flagpole be $b$ and define $g$ similarly. Now note the bound $g \le b+1.$ Now we cannot have any two consecutive greens. This condition is the same as "there are $b+1$ spaces between each blue flag. How many ways can we put the $g$ green flags in the $b+1$ spaces?" Therefore given $b$ blue flags on the first flagpole and $g$ green flags on the first flagpole we have a total of $\binom{b+1}{g}.$ Similarly there are $\binom{11-b}{9-g}$ ways for the second flagpole. Summing over all possible possibilities we see the sum is $\sum_{g = 0}^{b+1} \sum_{b=0}^{10}\binom{b+1}{g}\binom{11-b}{9-g}.$ Swapping the sum we have $\sum_{g = 0}^{b+1} \sum_{b=0}^{10}\binom{b+1}{g}\binom{11-b}{9-g} = \sum_{b=0}^{10} \sum_{g = 0}^{b+1}\binom{b+1}{g}\binom{11-b}{9-g}.$ Then applying Vandermonde's yields $\sum_{b=0}^{10}\binom{12}{9}$ so the sum is $11 \cdot\binom{12}{9}.$ However, this answer overcounts. We cannot have no flags on a pole, so we subtract $2 \cdot\binom{11}{9}$ since we can have empty flags for the first or second flag. Therefore the answer is $11 \cdot\binom{12}{9} - 2 \cdot\binom{11}{9} \pmod{1000} \equiv \boxed{310} \pmod{1000}.$

## Solution 5
Consider this as arranging the flags on one big flagpole, then splitting the flagpole into two.
Example: Start with big flagpole $BGBGBGGBBGBGBGBGBGB$ , and then split it into $BGBGBG$ and $GBBGBGBGBGBGB$ .
We will split this problem into two cases:
Case 1: The split is not two greens. Basically if arranging 10 blue flags and 9 green flags does not give any consecutive green flags, then we can split it into two flagpoles wherever. For example, \[BGBBGBGBGBGBGBGBGBG\] can become \[BGB|BGBGBGBGBGBGBGBG\] or \[BGBBG|BGBGBGBGBGBGBG\] .
By stars and bars, there are $\binom{11}{2}$ ways to arrange the flags, then $18$ ways to split the big flagpole, so total $\binom{11}{2}\cdot 18$ ways.
Case 2: The split is two greens. Here the big flagpole has two consecutive green flags, so we are forced to split the two green flags.
There are $\binom{11}{3}\cdot 8$ ways for this case, since we first place 8 “ $G$ ”s among 10 blue flags, then choose one to become $GG$ . (Look at the first example)
Thus the total number of ways is \[\binom{11}{2}\cdot 18 + \binom{11}{3}\cdot 8 = 2310 \equiv \boxed{310} \pmod{1000}.\]
~ RubixMaster21

## Solution 6
We split the 9 green flags over the two poles: $0$ and $9$ , $1$ and $8$ , $2$ and $7$ , and so on, respectively.
For the first case, $0$ and $9$ , 8 of the 10 blue flags must be placed between the 9 green flags on the same pole, and the 9th blue flag must be placed on the other pole so that there is at least one flag on each pole. This leaves $\textbf{11}$ choices for the last blue flag.
Moving on, notice that now for every other case there will always be 3 blue flags left to place. Since we want to distribute 3 indistinguishable flags to 11 distinguishable spots, we use stars and bars. There are $\binom{13}{10} = \textbf{286}$ ways to distribute the flags for the other cases.
Then the total number of ways is $2 * (11 + 4 * 286) = 2310 \equiv \boxed{310} \pmod{1000}$ , since the poles are distinguishable.
~ AXcatterwocky
These problems are copyrighted © by the Mathematical Association of America.