# 2021 AIME I Problem 1

## Problem

Zou and Chou are practicing their $100$ -meter sprints by running $6$ races against each other. Zou wins the first race, and after that, the probability that one of them wins a race is $\frac23$ if they won the previous race but only $\frac13$ if they lost the previous race. The probability that Zou will win exactly $5$ of the $6$ races is $\frac mn$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

## Solution 1 (Casework 🪅)
For the next five races, Zou wins four and loses one. Let $W$ and $L$ denote a win and a loss, respectively. There are five possible outcome sequences for Zou:
1. $LWWWW$
1. $WLWWW$
1. $WWLWW$
1. $WWWLW$
1. $WWWWL$
We proceed with casework:
Case (1): Sequences #1-4, in which Zou does not lose the last race.
The probability that Zou loses a race is $\frac13,$ and the probability that Zou wins the next race is $\frac13.$ For each of the three other races, the probability that Zou wins is $\frac23.$
There are four sequences in this case. The probability of one such sequence is $\left(\frac13\right)^2\left(\frac23\right)^3.$
Case (2): Sequence #5, in which Zou loses the last race.
The probability that Zou loses a race is $\frac13.$ For each of the four other races, the probability that Zou wins is $\frac23.$
There is one sequence in this case. The probability is $\left(\frac13\right)^1\left(\frac23\right)^4.$
Answer
The requested probability is \[4\left(\frac13\right)^2\left(\frac23\right)^3+\left(\frac13\right)^1\left(\frac23\right)^4=\frac{32}{243}+\frac{16}{243}=\frac{48}{243}=\frac{16}{81},\] from which the answer is $16+81=\boxed{097}.$
~MRENTHUSIASM

## Solution 2 (Casework but Bashier)
We have $5$ cases, depending on which race Zou lost. Let $\text{W}$ denote a won race, and $\text{L}$ denote a lost race for Zou. The possible cases are $\text{WWWWL, WWWLW, WWLWW, WLWWW, LWWWW}$ . The first case has probability $\left(\frac{2}{3} \right)^4 \cdot \frac{1}{3} = \frac{16}{3^5}$ . The second case has probability $\left( \frac{2}{3} \right)^3 \cdot \frac{1}{3} \cdot \frac{1}{3} = \frac{8}{3^5}$ . The third has probability $\left( \frac{2}{3} \right)^2 \cdot \frac{1}{3} \cdot \frac{1}{3} \cdot \frac{2}{3} = \frac{8}{3^5}$ . The fourth has probability $\frac{2}{3} \cdot \frac{1}{3} \cdot \frac{1}{3} \cdot \left( \frac{2}{3} \right)^2 = \frac{8}{3^5}$ . Lastly, the fifth has probability $\frac{1}{3} \cdot \frac{1}{3} \cdot \left( \frac{2}{3} \right)^3 = \frac{8}{3^5}$ . Adding these up, the total probability is $\frac{16 + 8 \cdot 4}{3^5} = \frac{16 \cdot 3}{3^5} = \frac{16}{81}$ , so $m+n = \boxed{097}$ .
~rocketsri
This is for if you're paranoid like me, and like to sometimes write out all of the cases if there are only a few.

## Solution 3 (Even More Casework)
Case 1: Zou loses the first race
In this case, Zou must win the rest of the races. Thus, our probability is $\frac{8}{243}$ .
Case 2: Zou loses the last race
There is only one possibility for this, so our probability is $\frac{16}{243}$ .
Case 3: Neither happens
There are three ways that this happens. Each has one loss that is not the last race. Therefore, the probability that one happens is $\frac{1}{3} \cdot \frac{1}{3} \cdot \frac{2}{3} \cdot \frac{2}{3} \cdot \frac{2}{3} = \frac{8}{243}$ . Thus, the total probability is $\frac{8}{243} \cdot 3 = \frac{24}{243}$ .
Adding these up, we get $\frac{48}{243} = \frac{16}{81}$ , so $16+81=\boxed{097}$ .
~mathboy100

## Solution 4 (Observations)
Note that Zou wins one race. The probability that he wins the last race is $\left(\frac{2}{3}\right)^4\left(\frac{1}{3}\right)=\frac{16}{243}.$ Now, if he doesn't win the last race, then there must be two races where the winner of the previous race loses. We can choose any $4$ of the middle races for Zou to win. So the probability for this case is $4\left(\frac{2}{3}\right)^3\left(\frac{1}{3}\right)^2=\frac{32}{243}.$ Thus, the answer is $\frac{16}{243}+\frac{32}{243}=\frac{16}{81}\implies\boxed{097}.$
~pinkpig

## Video Solution by Punxsutawney Phil
https://youtube.com/watch?v=H17E9n2nIyY

## Video Solution
https://youtu.be/M3DsERqhiDk?t=15

## Video Solution by Steven Chen (in Chinese)
https://youtu.be/F21t0PAzhLM

## Video Solution by Power of Logic
https://youtu.be/WS6X1MQ37jg
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .