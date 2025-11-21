# 2024 AMC 10B Problem 17

## Problem

In a race among $5$ snails, there is at most one tie, but that tie can involve any number of snails. For example, the result might be that Dazzler is first; Abby, Cyrus, and Elroy are tied for second; and Bruna is fifth. How many different results of the race are possible?

$\textbf{(A) } 180 \qquad\textbf{(B) } 361 \qquad\textbf{(C) } 420 \qquad\textbf{(D) } 431 \qquad\textbf{(E) } 720$

## Solution 1
Intuitive solution: We perform casework based on how many snails tie. Let's say we're dealing with the following snails: $A,B,C,D,E$ .
$5$ snails tied: All $5$ snails tied for $1$ st place, so only $1$ way.
$4$ snails tied: $A,B,C,D$ all tied, and $E$ either got $1$ st or last. ${5}\choose{1}$ ways to choose who isn't involved in the tie and $2$ ways to choose if that snail gets first or last, so $10$ ways.
$3$ snails tied: We have $ABC, D, E$ . There are $3! = 6$ ways to determine the ranking of the $3$ groups. There are $5\choose2$ ways to determine the two snails not involved in the tie. So $6 \cdot 10 = 60$ ways.
$2$ snails tied: We have $AB, C, D, E$ . There are $4! = 24$ ways to determine the ranking of the $4$ groups. There are $5\choose{3}$ ways to determine the three snails not involved in the tie. So $24 \cdot 10 = 240$ ways.
$1$ snail tied: This is basically just every snail for a place, so $5! = 120$ ways.
The answer is $1+10+60+240+120 = \boxed{\text{(D) }431}$ .
~lprado

## Solution 2
Split the problem into cases. A tie of $n$ snails has $\dbinom{5}{n}$ ways to choose the snails that are tied, $6-n$ ways to choose which place they tie for, and $(5-n)!$ to place the remaining snails.
1. No tie $\implies5!=120$
2. Tie of 2 snails $\implies\dbinom{5}{2}\cdot4\cdot3!=240$
3. Tie of 3 snails $\implies\dbinom{5}{3}\cdot3\cdot2!=60$
4. Tie of 4 snails $\implies\dbinom{5}{4}\cdot2=10$
5. Tie of all 5 snails $\implies1$
The answer is $120+240+60+10+1=\boxed{\text{(D) }431}$ ~Tacos_are_yummy_1

## Solution 3 (Get Lucky)
For the case of a 5-way tie, we have $\dbinom{5}{5}=1$ cases. We can assume this leads to an answer that ends in 1, leaving only $B$ and $D$ . By just accounting for the cases for a 1-way tie ( $5!=120$ ) and 2-way tie ( $\dbinom{5}{2}\cdot4\cdot3!=240$ ), it immediately shows that $B$ does not work. Therefore, the answer is $\boxed{\text{(D) }431}$ ~shreyan.chethan, cleaned up by cweu001, vintage_god
Notice that with 2 remaining choices, through guessing, the expected value of your points is $\frac{6}{2}=3$ , and not answering gives 1.5 points. Therefore, you gain an expected value of $1.5$ points by answering. It would be best to always guess whenever you can get rid of $2$ or more answers. If you can only eliminate $1$ answer, not guessing will give you $1.5$ points, but guessing also gives you an expected value of $1.5$ points. I usually leave it blank if I can only get rid of $1$ answer choice. ~shreyan.chethan, edited by BenjaminDong01, added by PerseverePlayer , and added by Aarav22
Sidenote : Usually, you should aim to look at the closer option choices than the extreme ones.

## Video Solution 1 by Pi Academy (Fast and Easy ⚡🚀)
https://youtu.be/c6nhclB5V1w?feature=shared
~ Pi Academy

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=Q7fwWZ89MC8
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .