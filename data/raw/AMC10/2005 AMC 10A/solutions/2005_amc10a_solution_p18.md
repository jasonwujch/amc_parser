# 2005 AMC 10A Problem 18

## Problem

Team $A$ and team $B$ play a series. The first team to win three games wins the series. Each team is equally likely to win each game, there are no ties, and the outcomes of the individual games are independent. If team $B$ wins the second game and team $A$ wins the series, what is the probability that team $B$ wins the first game?

$\textbf{(A) } \frac{1}{5}\qquad \textbf{(B) } \frac{1}{4}\qquad \textbf{(C) } \frac{1}{3}\qquad \textbf{(D) } \frac{1}{2}\qquad \textbf{(E) } \frac{2}{3}$

## Solution
There are at most $5$ games played.
If team $B$ won the first two games, team $A$ would need to win the next three games. So the only possible order of wins is $BBAAA$ .
If team $A$ won the first game, and team $B$ won the second game, the possible orders of wins are $ABBAA$ , $ABABA$ , and $ABAAX$ , where $X$ denotes that the $5$ th game wasn't played.
There is $1$ possibility where team $B$ wins the first game, and $4$ total possibilities when team $A$ wins the series and team $B$ wins the second game. Note that the fourth possibility, $ABAAX$ , occurs twice as often as the others because it is dependent on the outcome of only $4$ games rather than $5$ , so we put $1$ over $1 \cdot 2 + (4-1) = 5$ total possibilities. The desired probability is then $\boxed{\textbf{(A) } \frac{1}{5}}$ .
### Note
The original final problem was poorly worded, since the problem directly stated that the answer is $\boxed{1/2}$ (the probability of team $B$ simply winning the first game, as opposed to the desired conditional probability of this event given that both team $B$ wins the second game and team $A$ wins the series).
The problem should therefore say something like "What fraction of possible sets of game outcomes have $B$ winning the first game?" or "Given the observed results, what is the conditional probability that $B$ won the first game?"
(Many problems in probability are poorly worded.)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .