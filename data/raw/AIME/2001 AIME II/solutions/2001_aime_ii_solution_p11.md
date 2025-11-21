# 2001 AIME II Problem 11

## Problem

Club Truncator is in a soccer league with six other teams, each of which it plays once. In any of its 6 matches, the probabilities that Club Truncator will win, lose, or tie are each $\frac {1}{3}$ . The probability that Club Truncator will finish the season with more wins than losses is $\frac {m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
Note that the probability that Club Truncator will have more wins than losses is equal to the probability that it will have more losses than wins; the only other possibility is that they have the same number of wins and losses. Thus, by the complement principle , the desired probability is half the probability that Club Truncator does not have the same number of wins and losses.
The possible ways to achieve the same number of wins and losses are $0$ ties, $3$ wins and $3$ losses; $2$ ties, $2$ wins, and $2$ losses; $4$ ties, $1$ win, and $1$ loss; or $6$ ties. Since there are $6$ games, there are $\frac{6!}{3!3!}$ ways for the first, and $\frac{6!}{2!2!2!}$ , $\frac{6!}{4!}$ , and $1$ ways for the rest, respectively, out of a total of $3^6$ . This gives a probability of $141/729$ . Then the desired answer is $\frac{1 - \frac{141}{729}}{2} = \frac{98}{243}$ , so the answer is $m+n = \boxed{341}$ .

## Solution 2
At first, it wins $6$ games, only one way
Secondly, it wins $5$ games, the other game can be either win or loss, there are $\binom{6}{5}\cdot 2=12$ ways
Thirdly, it wins $4$ games, still the other two games can be either win or loss, there are $\binom{6}{4}\cdot 2^2=60$ ways
Fourthly, it wins $3$ games, this time, it can't lose $3$ games but other arrangements of the three non-winning games are fine, there are $\binom{6}{3}\cdot (2^3-1)=140$ ways
Fifth case, it wins $2$ games, only $0/1$ lose and $4/3$ draw is ok, so there are $\binom{6}{2}(1+\binom{4}{1})=75$ cases
Last case, it only wins $1$ game so the rest games must be all draw, $1$ game
The answer is $\frac{1+12+60+140+75+6}{3^6}=\frac{98}{243}$ leads to $\boxed{341}$
~bluesoul

## Solution 3
This problem is symmetrical, and we should probably take advantage of that. We have that:
\begin{align*} 1 &= P(\#\text{ of wins} > \text{losses}) + P(\#\text{ of wins} < \text{losses}) + P(\#\text{ of wins} = \text{losses}) \\ &= 2P(\#\text{ of wins} > \text{losses}) + P(\#\text{ of wins} = \text{losses}) \end{align*}
Now, all we need to do is find the probability that the number of wins is equal to the number of losses, and then it's simple linear equations from there! We have 4 cases. We can let $W/L/T$ be the format for these cases. For example, $3/2/1$ would mean 3 wins, 2 losses, and 1 tie. Now, we begin our casework.
\[C_1: 3/3/0 \Longrightarrow \binom{6}{3} \cdot \left(\frac{1}{3}\right)^6 = \frac{20}{729}\]
\[C_2: 2/2/2 \Longrightarrow \binom{6}{2}\binom{4}{2} \cdot \left(\frac{1}{3}\right)^6 = \frac{90}{729}\]
\[C_3: 1/1/4 \Longrightarrow \binom{6}{4} \cdot 2 \cdot \left(\frac{1}{3}\right)^6 = \frac{30}{729}\]
\[C_4: 0/0/6 \Longrightarrow \left(\frac{1}{3}\right)^6 = \frac{1}{729}\]
Summing these up we get $\dfrac{141}{729} = \dfrac{47}{243}$ . Now, we have $2x + \dfrac{47}{243} = 1$ , where $x = P(\#\text{ of wins} > \text{losses})$ . Solving, we get $x = \dfrac{98}{243} \Longrightarrow \boxed{341}$
-jb2015007
These problems are copyrighted © by the Mathematical Association of America.