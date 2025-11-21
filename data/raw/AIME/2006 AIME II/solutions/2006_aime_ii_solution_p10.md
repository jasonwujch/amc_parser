# 2006 AIME II Problem 10

## Problem

Seven teams play a soccer tournament in which each team plays every other team exactly once. No ties occur, each team has a $50\%$ chance of winning each game it plays, and the outcomes of the games are independent. In each game, the winner is awarded a point and the loser gets 0 points. The total points are accumulated to decide the ranks of the teams. In the first game of the tournament, team $A$ beats team $B.$ The probability that team $A$ finishes with more points than team $B$ is $m/n,$ where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4

## Solution

## Solution 1
The results of the five remaining games are independent of the first game, so by symmetry, the probability that $A$ scores higher than $B$ in these five games is equal to the probability that $B$ scores higher than $A$ . We let this probability be $p$ ; then the probability that $A$ and $B$ end with the same score in these five games is $1-2p$ .
Of these three cases ( $|A| > |B|, |A| < |B|, |A|=|B|$ ), the last is the easiest to calculate (see solution 2 for a way to directly calculate the other cases).
There are ${5\choose k}$ ways to $A$ to have $k$ victories, and ${5\choose k}$ ways for $B$ to have $k$ victories. Summing for all values of $k$ ,
Thus $p = \frac 12 \left(1-\frac{126}{512}\right) = \frac{193}{512}$ . The desired probability is the sum of the cases when $|A| \ge |B|$ , so the answer is $\frac{126}{512} + \frac{193}{512} = \frac{319}{512}$ , and $m+n = \boxed{831}$ .

## Solution 2
You can break this into cases based on how many rounds $A$ wins out of the remaining $5$ games.
- If $A$ wins 0 games, then $B$ must win 0 games and the probability of this is $\frac{{5 \choose 0}}{2^5} \frac{{5 \choose 0}}{2^5} = \frac{1}{1024}$ .
- If $A$ wins 1 games, then $B$ must win 1 or less games and the probability of this is $\frac{{5 \choose 1}}{2^5} \frac{{5 \choose 0}+{5 \choose 1}}{2^5} = \frac{30}{1024}$ .
- If $A$ wins 2 games, then $B$ must win 2 or less games and the probability of this is $\frac{{5 \choose 2}}{2^5} \frac{{5 \choose 0}+{5 \choose 1}+{5 \choose 2}}{2^5} = \frac{160}{1024}$ .
- If $A$ wins 3 games, then $B$ must win 3 or less games and the probability of this is $\frac{{5 \choose 3}}{2^5} \frac{{5 \choose 0}+{5 \choose 1}+{5 \choose 2}+{5 \choose 3}}{2^5} = \frac{260}{1024}$ .
- If $A$ wins 4 games, then $B$ must win 4 or less games and the probability of this is $\frac{{5 \choose 4}}{2^5} \frac{{5 \choose 0}+{5 \choose 1}+{5 \choose 2}+{5 \choose 3}+{5 \choose 4}}{2^5} = \frac{155}{1024}$ .
- If $A$ wins 5 games, then $B$ must win 5 or less games and the probability of this is $\frac{{5 \choose 5}}{2^5} \frac{{5 \choose 0}+{5 \choose 1}+{5 \choose 2}+{5 \choose 3}+{5 \choose 4}+{5 \choose 5}}{2^5} = \frac{32}{1024}$ .
Summing these 6 cases, we get $\frac{638}{1024}$ , which simplifies to $\frac{319}{512}$ , so our answer is $319 + 512 = \boxed{831}$ .

## Solution 3
We can apply the concept of generating functions here.
The generating function for $B$ is $(1 + 0x^{1})$ for the first game where $x^{n}$ is winning n games. Since $B$ lost the first game, the coefficient for $x^{1}$ is 0. The generating function for the next 5 games is $(1 + x)^{5}$ . Thus, the total generating function for number of games he wins is
The generating function for $A$ is the same except that it is multiplied by $x$ instead of $(1+0x)$ . Thus, the generating function for $A$ is
$1x + 5x^{2} + 10x^{3} + 10x^{4} + 5x^{5} + x^{6}$ .
The probability that $B$ wins 0 games is $\frac{1}{32}$ . Since the coefficients for all $x^{n}$ where
$n \geq 1$ sums to 32, the probability that $A$ wins more games is $\frac{32}{32}$ .
Thus, the probability that $A$ has more wins than $B$ is $\frac{1}{32} \times \frac{32}{32} + \frac{5}{32} \times \frac{31}{32} + \frac{10}{32} \times \frac{26}{32} + \frac{10}{32} \times \frac{16}{32} + \frac{5}{32} \times \frac{6}{32} +\frac{1}{32} \times \frac{1}{32} = \frac{638}{1024} = \frac{319}{512}$ .
Thus, $319 + 512 = \boxed{831}$ .

## Solution 4
After the first game, there are $10$ games we care about-- those involving $A$ or $B$ . There are $3$ cases of these $10$ games: $A$ wins more than $B$ , $B$ wins more than $A$ , or $A$ and $B$ win the same number of games. Also, there are $2^{10} = 1024$ total outcomes. By symmetry, the first and second cases are equally likely, and the third case occurs $\binom{5}{0}^2+\binom{5}{1}^2+\binom{5}{2}^2+\binom{5}{3}^2+\binom{5}{4}^2+\binom{5}{5}^2 = \binom{10}{5} = 252$ times, by a special case of Vandermonde's Identity . There are therefore $\frac{1024-252}{2} = 386$ possibilities for each of the other two cases.
If $B$ has more wins than $A$ in its $5$ remaining games, then $A$ cannot beat $B$ overall. However, if $A$ has more wins or if $A$ and $B$ are tied, $A$ will beat $B$ overall. Therefore, out of the $1024$ possibilites, $386+252 = 638$ ways where $A$ wins, so the desired probability is $\frac{638}{1024} = \frac{319}{512}$ , and $m+n=\boxed{831}$ .
These problems are copyrighted © by the Mathematical Association of America.