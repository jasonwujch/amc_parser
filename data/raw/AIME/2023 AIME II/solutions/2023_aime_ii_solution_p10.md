# 2023 AIME II Problem 10

## Problem

Let $N$ be the number of ways to place the integers $1$ through $12$ in the $12$ cells of a $2 \times 6$ grid so that for any two cells sharing a side, the difference between the numbers in those cells is not divisible by $3.$ One way to do this is shown below. Find the number of positive integer divisors of $N.$ \[\begin{array}{|c|c|c|c|c|c|} \hline \,1\, & \,3\, & \,5\, & \,7\, & \,9\, & 11 \\ \hline \,2\, & \,4\, & \,6\, & \,8\, & 10 & 12 \\ \hline \end{array}\]

## Solution 1
We replace the numbers which are $0 \pmod 3$ to $0$ , $1 \pmod 3$ to $1$ , and $2 \pmod 3$ to $2$ .
Then, the problem is equivalent to arranging four $0$ 's, four $1$ 's, and four $2$ 's into the grid (and then multiplying by $4!^3$ to account for replacing the remainder numbers with actual numbers) such that no 2 of the same numbers are adjacent.
Then, the numbers which are vertically connected must be different. Two 1s must be connected with two 2s, and two 1s must be connected with two 0s (vertically), as if there are less 1s connected with either, then there will be 2s or 0s which must be connected within the same number. For instance if we did did:
Then we would be left with one (0,2), and two remaining 0s which aren't supposed to be connected, so it is impossible. Similar logic works for why all 1s can't be connected with all 2s. Thus, we are left with the problem of re-arranging two (1,2) pairs, two (1,0) pairs, two (2,0) pairs. Notice that the pairs can be re-arranged horizontally in any configuration, but when two pairs are placed adjacent there is only one configuration for the rightmost pair to be set after the leftmost one has been placed. We have $\frac{6!}{2!2!2!}=90$ ways to horizontally re-arrange the pairs, with 2 ways to set the initial leftmost column. Thus, there are 180 ways to arrange the pairs. Accounting for the initial simplification of the problem with 1-12 $\rightarrow$ 0-3, we obtain the answer is: \[2488320=2^{11}\cdot3^5\cdot5^1\] The number of divisors is: $12\cdot6\cdot2=\boxed{144}.$ ~SAHANWIJETUNGA

## Solution 2 (Archaeological)
Let's carry out an archaeological study, that is, we will find the bones (the base) and "build up the meat."
1. Let "bones" of number $X$ be $X \pmod 3.$ Then the “skeleton” of the original table is
\[1 0 2 1 0 2\] \[2 1 0 2 1 0\] By condition, the table cannot have a column of two identical numbers (the difference of such numbers is a multiple of $3).$
There are $4$ zeros, $4$ ones and $4$ twos in the table (the order of the numbers in the columns is not important).
Therefore, there cannot be more than two identical columns (otherwise there will be four identical numbers in the remaining three, that is, the numbers in one column are the same).
Any such table has exactly $2$ columns $(0,1), 2$ columns $(0,2)$ and $2$ columns $(1,2).$
The number of possible tables of six elements of three types is \[m = \frac {6!}{2! \cdot 2! \cdot 2!} = 2 \cdot 3^2 \cdot 5.\] The number of possible tables of six elements, if the order of the digits is important, is \[M = 2^6 \cdot m = 2^7 \cdot 3^2 \cdot 5.\] 2. We are looking for the total number of options. The column $(0,1)$ can contain the following $4^2 = 16$ pairs of numbers (the order is not important, it is already taken into account) \[(1,3), (1,6), (1,9), (1, 12), (4.3), (4.6), (4.9) (4.12), (7.3), (7.6), (7.9), (7.12), (11,3), (11,6), (11,9), (11,12).\] The second column $(0,1)$ can contain $3^2 = 9$ pairs of numbers (excluding the two that are in the first column).
Similarly with the other two columns, i.e. the total number of choices \[M \cdot 16 \cdot 9 \cdot 3 = 2^{11} \cdot 3^5 \cdot 5.\] Number of divisors \[(11+1) \cdot (5+1) \cdot (1 + 1) = \boxed{144}.\] vladimir.shelomovskii@gmail.com, vvsss
### Simpler Way to Finish
Note that there are $6!/(2!2!2!)$ ways for the possible column arrangements. Then, each of those columns have two numbers, which can be permuted either way, so we multiply by $2!$ . Finally, we have $4$ numbers of each residue of $0, 1, 2 \pmod 3$ . Thus, let us put those $4$ who are $0 \pmod 3$ , and we get $4!$ ways to do this. Similarly, we can do the same for the 4 numbers each that are $1, 2 \pmod 3$ , so we multiply by $(4!)^3$ . Thus, the final answer is $\frac{6!}{2!2!2!}*2!*(4!)^3$ which leads us to the same solution as above.
mathboy282
LaTeX Edit: ~Bigbrain_2009
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .