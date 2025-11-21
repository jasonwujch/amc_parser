# 2018 AIME II Problem 13

## Problem

Misha rolls a standard, fair six-sided die until she rolls $1-2-3$ in that order on three consecutive rolls. The probability that she will roll the die an odd number of times is $\dfrac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 0
Let $P_n$ be the probability of getting consecutive $1,2,3$ rolls in $n$ rolls and not rolling $1,2,3$ prior to the nth roll.
Let $x = P_3+P_5+...=1-(P_4+P_6+..)$ . Following Solution 2, one can see that \[P_{n+1}=P_{n}-\frac{P_{n-2}}{6^3}\] for all positive integers $n \ge 5$ . Summing for $n=5,7,...$ gives \[(1-x)-\frac{1}{6^3}=x-\frac{1}{6^3}-\frac{x}{6^3}\] \[\implies x = \frac{m}{n} = \frac{216}{431} \implies m+n=216+431= \boxed{647}\]

## Solution 1
Let $P_{odd}=\frac{m}{n}$ , with the subscript indicating an odd number of rolls. Then $P_{even}=1-\frac{m}{n}$ .
The ratio of $\frac{P_{odd}}{P_{even}}$ is just $\frac{P_{odd}}{1-P_{odd}}$ .
We see that $P_{odd}$ is the sum of $P_3$ , $P_5$ , $P_7$ ,... , while $P_{even}$ is the sum of $P_4$ , $P_6$ , $P_8$ ,... .
$P_3$ , the probability of getting rolls of 1-2-3 in exactly 3 rolls, is obviously $\frac{1}{216}$ .
We set this probability of $P_3$ aside, meaning we totally remove the chance of getting 1-2-3 in 3 rolls. Now the ratio of $P_4+P_6+P_8+...$ to $P_5+P_7+P_9+...$ should be equal to the ratio of $\frac{P_{odd}}{P_{even}}$ , because in this case the 1st roll no longer matters, so we can disregard the very existence of it in counting how many times of rolls, and thus, 4 rolls, 6 rolls, 8 rolls... would become an odd number of rolls (while 5 rolls, 7 rolls, 9 rolls... would become even number of rolls).
Notice $P_4+P_6+P_8+...=P_{even}$ , and also $P_5+P_7+P_9+...=P_{odd}-P_3=P_{odd}-\frac{1}{216}$
So we have $\frac{P_{even}}{P_{odd}-\frac{1}{216}}=\frac{P_{odd}}{P_{even}}$ .
Finally, we get $P_{odd}=\frac{m}{n}=\frac{216}{431}$ . Therefore, $m+n = \boxed{647}$ .

## Solution 2
Call the probability you win on a certain toss $f_n$ , where $n$ is the toss number. Obviously, since the sequence has length 3, $f_1=0$ and $f_2=0$ . Additionally, $f_3=\left(\frac{1}{6}\right)^3$ . We can call this value $x$ , to keep our further equations looking clean. We can now write our general form for $f$ as $f_n=x\left(1-\sum_{i=1}^{n-3}f_i\right)$ . This factors the probability of the last 3 rolls being 1-2-3, and the important probability that the sequence has not been rolled in the past (because then the game would already be over). Note that $\sum_{i=1}^{\infty}f_i=1$ since you'll win at some point. An intermediate step here is figuring out $f_n-f_{n+1}$ . This is equal to $x\left(1-\sum_{i=1}^{n-3}f_i\right)-x\left(1-\sum_{i=1}^{n-2}f_i\right)=x\left(\sum_{i=1}^{n-2}f_i-\sum_{i=1}^{n-3}f_i\right)=xf_{n-2}$ . Adding up all the differences, i.e. $\sum_{i=2}^{\infty}(f_{2n-1}-f_{2n})$ will give us the amount by which the odds probability exceeds the even probability. Since they sum to 1, that means the odds probability will be half of the difference above one-half. Subbing in our earlier result from the intermediate step, the odd probability is equal to $\frac{1}{2}+\frac{1}{2}x\sum_{i=2}^{\infty}f_{2n-3}$ . Another way to find the odd probability is simply summing it up, which turns out to be $\sum_{i=1}^{\infty}f_{2n-1}$ . Note the infinite sums in both expressions are equal; let's call it $P$ . Equating them gives $\frac{1}{2}+\frac{1}{2}xP=P$ , or $P=\frac{1}{2-x}$ . Finally, substituting $x=\frac{1}{216}$ , we find that $P=\frac{216}{431}$ , giving us a final answer of $216 + 431 = \boxed{647}$ .
~First

## Solution 3
Let $S(n)$ be the number of strings of length $n$ containing the digits $1$ through $6$ that do not contain the string $123$ . Then we have $S(n) = 6 \cdot S(n-1) - S(n-3)$ because we can add any digit to end of a string with length $n-1$ but we have to subtract all the strings that end in $123$ . We rewrite this as \begin{align*} S(n) &= 6 \cdot S(n-1) - S(n-3) \\ &= 6 \cdot (6 \cdot S(n-2) - S(n-4)) - (6 \cdot (S(n-4) - S(n-6)) \\ &= 36 \cdot S(n-2) - 12 \cdot S(n-4) + S(n-6) \end{align*} We wish to compute $P=\sum_{n=0}^\infty \frac{S(2n)}{6^{2n+3}}$ since the last three rolls are $123$ for the game to end. Summing over the recursion, we obtain \[\sum_{n=0}^\infty \frac{S(2n)}{6^{2n+3}} =36 \cdot \sum_{n=0}^\infty \frac{S(2n-2)}{6^{2n+3}} - 12 \cdot \sum_{n=0}^\infty \frac{S(2n-4)}{6^{2n+3}}+ \sum_{n=0}^\infty \frac{S(2n-6)}{6^{2n+3}}\] Now shift the indices so that the inside term is the same: \begin{align*} \sum_{n=3}^\infty \frac{S(2n)}{6^{2n+3}} &= \frac{36}{6^2} \cdot \sum_{n=2}^\infty \frac{S(2n)}{6^{2n+3}} - \frac{12}{6^4} \cdot \sum_{n=1}^\infty \frac{S(2n)}{6^{2n+3}} + \frac{1}{6^6} \cdot \sum_{n=0}^\infty \frac{S(2n)}{6^{2n+3}} \\ \left(P - \frac{S(0)}{6^3} - \frac{S(2)}{6^5} -\frac{S(4)}{6^7} \right) &= \frac{36}{6^2} \cdot \left( P - \frac{S(0)}{6^3} - \frac{S(2)}{6^5}\right) - \frac{12}{6^4} \cdot \left( P - \frac{S(0)}{6^3} \right) + \frac{1}{6^6} \cdot P \end{align*} Note that $S(0) = 1, S(2) = 36$ and $S(4) = 6^4 - 2 \cdot 6 = 1284$ . Therefore, \begin{align*} \left(P - \frac{1}{6^3} - \frac{36}{6^5} -\frac{1284}{6^7} \right) = \frac{36}{6^2} \cdot \left( P - \frac{1}{6^3} - \frac{36}{6^5}\right) - \frac{12}{6^4} \cdot \left( P - \frac{1}{6^3} \right) + \frac{1}{6^6} \cdot P \end{align*} Solving for $P$ , we obtain $P = \frac{216}{431} \implies m+n = \boxed{647}$ .
-Vfire

## Solution 4
Let $A=\frac{1}{6} \begin{bmatrix} 5 & 1 & 0 & 0 \\ 4 & 1 & 1 & 0 \\ 4 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ \end{bmatrix}$ . $A$ is a transition matrix for the prefix of 1-2-3 matched so far. The state corresponding to a complete match has no outgoing probability mass. The probability that we roll the dice exactly $k$ times is $(A^k)_{1,4}$ . Thus the probability that we roll the dice an odd number of times is $1-\left(\sum_{k=0}^\infty A^{2k}\right)_{1,4} = 1-\left((I - A^2)^{-1}\right)_{1,4} = \frac{216}{431}$ . Thus the answer is $216+431=\boxed{647}$ .

## Solution 5 (quick cheat)
Consider it as a contest of Odd and Even. Let $P_o$ and $P_e$ be probability that Odd and Even wins, respectively. If we consider every 3 rolls as an atomic action, then we can have a simple solution. If the rolls is 1-2-3, Odd wins; otherwise, Odd and Even switch the odds of winning. Therefore, we have \[P_o = \frac{1}{216} + \frac{215}{216}P_e\] Plug in $P_e = 1 - P_o$ and we can easily solve for $Po=\frac{216}{431}$ .
$\boxed{647}$ .
Of course this is not a rigorous solution. I think it works because the requirement is a strict sequence of pure random events.
-Mathdummy

## Solution 6 (Markov Chain)
Let $P_o$ , $P_e$ be the winning probabilities respectively. We call Odd "in position" when a new sequence of 1-2-3 starts at odd position, and likewise, call Even is "in position" when a new sequence starts at even position.
Now, consider the situation when the first roll is $1.$ The conditional probability for Odd or Even to eventually win out depends on whose is in position. So let's denote by $P_o(1), P_e(1)$ the probabilities of Odd and Even winning out, respectively, both when Odd is in position. Remember that the probabilities simply switch if Even is in position. Similarly, after 1-2 is rolled, we denote by $P_o(2), P_e(2)$ the conditional probabilities of Odd and Even winning out, when Odd is in position.
Consider the first roll. If it's not a 1, the sequence restarts, but Even is now in position; if it's a 1, then Odd's winning probability becomes $P_o(1)$ . So, \[P_o = \frac{1}{6}P_o(1) + \frac{5}{6}P_e\] In the next roll, there are 3 outcomes. If the roll is 2, then Odd's winning probability becomes $P_o(2)$ ; if the roll is 1, then we stay in the sequence, but Even is now in position, so the probability of Odd winning now becomes $P_e(1)$ ; if the rolls is any other number, then the sequence restarts, and Odd is still in position. So, \[P_o(1) = \frac{1}{6}P_o(2) + \frac{1}{6}P_e(1) + \frac{4}{6}P_o\] In the next roll after a 1-2 sequence, there are 3 outcomes. If the roll is a 3, Odd wins; if it's a 1, we go back to the state when 1 is just rolled, and Odd is in position; if it's any other number, then the sequence restarts, and Even is in position. So, \[P_o(2) = \frac{1}{6} + \frac{1}{6}P_o(1) + \frac{4}{6}P_e\]
Plug in $P_e = 1-P_o$ and $P_e(1) = 1 - P_o(1)$ , we have a 3-equation linear system which is not hard to solve. The final answer is $Po=\frac{216}{431}$ . $\boxed{647}$ . (We want P_o because if it starts odd, it will also end odd)
-Mathdummy
### Markov Chain Diagram
mathboy282
$\LaTeX$ done by CrazyVideoGamez

## Solution 7(Blocks)
Take a block of any three possible rolls. You have $6^3$ different possibilities for a block and $6^3 - 1$ different possibilities to have a block without 1-2-3. This gives two probabilities of $\frac{6^3-1}{6^3}$ and $\frac{1}{6^3}$ , respectively. To get an odd number of total rolls, we need an even number of blocks without a 1-2-3. Then, we can sum up the probabilities up to infinity to see the total probability of getting an even number of rolls. \[\frac{1}{6^3}\sum_{k=0}^{\infty}\left(\frac{6^3-1}{6^3}\right)^{2k}\] \[=\frac{\frac{1}{6^3}}{1-\left(\frac{6^3-1}{6^3}\right)^2}\] Using difference of squares on the bottom half we can reduce it to $\left(1-\frac{6^3-1}{6^3}\right)\left(1+\frac{6^3-1}{6^3}\right)=\frac{2\times 6^3 -1}{(6^3)^2}$ . Plugging this back in to the equation we get- \[\frac{\frac{1}{6^3}}{\frac{2\times 6^3 -1}{(6^3)^2}} = \frac{6^3}{2\times 6^3 - 1} = \frac{216}{431}\] Then, our answer is $\boxed{647}$ -Mathiscool109
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .