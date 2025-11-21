# 2021 Fall AMC 10B Problem 20

## Problem

In a particular game, each of $4$ players rolls a standard $6{ }$ -sided die. The winner is the player who rolls the highest number. If there is a tie for the highest roll, those involved in the tie will roll again and this process will continue until one player wins. Hugo is one of the players in this game. What is the probability that Hugo's first roll was a $5,$ given that he won the game?

$(\textbf{A})\: \frac{61}{216}\qquad(\textbf{B}) \: \frac{367}{1296}\qquad(\textbf{C}) \: \frac{41}{144}\qquad(\textbf{D}) \: \frac{185}{648}\qquad(\textbf{E}) \: \frac{11}{36}$

## Method 1 (see remark, this is NOT a correct solution)
Since we know that Hugo wins, we know that he rolled the highest number in the first round. The probability that his first roll is a $5$ is just the probability that the highest roll in the first round is $5$ .
Let $P(x)$ indicate the probability that event $x$ occurs. We find that $P(\text{No one rolls a 6})-P(\text{No one rolls a 5 or 6})=P(\text{The highest roll is a 5})$ ,
so \[P(\text{No one rolls a 6})=\left(\frac56\right)^4,\] \[P(\text{No one rolls a 5 or 6})=\left(\frac23\right)^4,\] \[P(\text{The highest roll is a 5})=\left(\frac56\right)^4-\left(\frac46\right)^4=\frac{5^4-4^4}{6^4}=\frac{369}{1296}=\boxed{(\textbf{C}) \: \frac{41}{144}}.\]
~kingofpineapplz
### Remark (Bayes' Theorem)
Although Solution $1$ gives the right answer, it is incorrect, since it only considered the first round, and it didn't consider that there might be one or more tiebreak rounds.
Solutions $2$ and $3$ use Bayes' theorem , and they are correct.
$P \left( A | B \right) = \frac{P \left( B | A \right) P \left( A \right) }{P \left( B \right)}$
In this problem
$P \left( \text{Hugo first rolled 5 } | \text{ Hugo won} \right) = \frac{P \left( \text{Hugo won } | \text{ Hugo first rolled 5} \right) \cdot P \left( \text{Hugo first rolled 5} \right) }{P \left( \text{Hugo won} \right)}$
~ isabelchen

## Solution 2 (Conditional Probability)
The conditional probability formula states that $P(A|B) = \frac{P(A\cap B)}{P(B)}$ , where $A|B$ means A given B and $A\cap B$ means A and B. Therefore the probability that Hugo rolls a five given he won is $\tfrac{P(A \cap B)}{P(B)}$ , where A is the probability that he rolls a five and B is the probability that he wins. In written form, \[\text{P(Hugo rolled a 5 given he won)}=\frac{\text{P(Hugo rolls a 5 and wins)}}{\text{P(Hugo wins)}}.\]
The probability that Hugo wins is $\frac{1}{4}$ by symmetry since there are four people playing and there is no bias for any one player. The probability that he gets a 5 and wins is more difficult; we will have to consider cases on how many players tie with Hugo. We consider the cases in which Hugo wins first, find the probabilities of those, and then account for the probability that Hugo rolled a 5, at the end.
$\textbf{Case 1:}$ No Players Tie With Hugo
In this case, all other players must have numbers from 1 through four, and Hugo had a probability of 1 to win after the first round.
There is a $\left(\frac{4}{6}\right)^{3} \cdot 1 = \frac{8}{27}$ chance of this happening.
$\textbf{Case 2:}$ One Player Ties With Hugo
In this case, there are $3 \choose 1$ $= 3$ ways to choose which other player ties with Hugo, and the probability that this happens is $\tfrac{1}{6} \cdot \left(\tfrac{4}{6}\right)^2$ . The probability that Hugo wins the game is then $\tfrac{1}{2}$ because there are now two players rolling die.
Therefore the total probability in this case is $3 \cdot \frac{1}{2} \cdot \frac{1}{6} \cdot \left(\frac{4}{6}\right)^2= \frac{1}{9}$ .
$\textbf{Case 3:}$ Two Players Tie With Hugo
In this case, there are $3 \choose 2$ $= 3$ ways to choose which other players tie with Hugo, and the probability that this happens is $\left(\tfrac{1}{6}\right)^2 \cdot \tfrac{4}{6}$ . The probability that Hugo wins the game is then $\tfrac{1}{3}$ because there are now three players rolling the die.
Therefore the total probability in this case is $3 \cdot \frac{1}{3} \cdot \left(\frac{1}{6}\right)^2 \cdot \frac{4}{6} = \frac{1}{54}$ .
$\textbf{Case 4:}$ All Three Players Tie With Hugo
In this case, the probability that all three players tie with Hugo is $\left(\tfrac{1}{6}\right)^3$ . The probability that Hugo wins the game is $\tfrac{1}{4}$ , so the total probability is $\frac{1}{4} \cdot \left(\frac{1}{6}\right)^3 = \frac{1}{864}$ .
Hugo has a $\frac{1}{6}$ probability of rolling a five himself, so the total probability that Hugo rolls a 5 and wins is
\[\frac{1}{6}\left(\frac{8}{27} + \frac{1}{9} + \frac{1}{54} + \frac{1}{864}\right) = \frac{1}{6}\left(\frac{369}{864}\right) = \frac{1}{6}\left(\frac{41}{96}\right).\]
Finally, the total probability is this probability divided by $\frac{1}{4}$ which is this probability times four; the final answer is
\[4 \cdot \frac{1}{6}\left(\frac{41}{96}\right) = \frac{2}{3} \cdot \frac{41}{96} = \frac{41}{48 \cdot 3} = \frac{41}{144} = \boxed{C}.\]
~KingRavi
~Edits by BakedPotato66, mathboy282

## Solution 3
We use $H$ to refer to Hugo. We use $H_1$ to denote the outcome of Hugo's $t$ th toss. We denote by $A$ , $B$ , $C$ the other three players. We denote by $N$ the number of players among $A$ , $B$ , $C$ whose first tosses are 5. We use $W$ to denote the winner.
We have \begin{align*} P \left( H_1 = 5 | W = H \right) & = \frac{P \left( H_1 = 5 , W = H \right)}{P \left( W = H \right)} \\ & = \frac{P \left( H_1 = 5 \right) P \left( W = H | H_1 = 5 \right) }{P \left( W = H \right)} \\ & = \frac{\frac{1}{6} P \left( W = H | H_1 = 5 \right)}{\frac{1}{4}} \\ & = \frac{2}{3} P \left( W = H | H_1 = 5 \right) . \end{align*}
Now, we compute $P \left( W = H | H_1 = 5 \right)$ .
We have \begin{align*} & P \left( W = H | H_1 = 5 \right) \\ & = P \left( W = H | H_1 = 5 , \max \left\{ A_1, B_1, C_1 \right\} \leq 4 \right) P \left( \max \left\{ A_1, B_1, C_1 \right\} \leq 4 | H_1 = 5 \right) \\ & \quad + P \left( W = H | H_1 = 5 , \max \left\{ A_1, B_1, C_1 \right\} = 6 \right) P \left( \max \left\{ A_1, B_1, C_1 \right\} = 6 | H_1 = 5 \right) \\ & \quad + \sum_{N = 1}^3 P \left( W = H | H_1 = 5 , \max \left\{ A_1, B_1, C_1 \right\} = 5 , N \right) P \left( \max \left\{ A_1, B_1, C_1 \right\} = 5 , N | H_1 = 5 \right) \\ & = P \left( W = H | H_1 = 5 , \max \left\{ A_1, B_1, C_1 \right\} \leq 4 \right) P \left( \max \left\{ A_1, B_1, C_1 \right\} \leq 4 \right) \\ & \quad + P \left( W = H | H_1 = 5 , \max \left\{ A_1, B_1, C_1 \right\} = 6 \right) P \left( \max \left\{ A_1, B_1, C_1 \right\} = 6 \right) \\ & \quad + \sum_{N = 1}^3 P \left( W = H | H_1 = 5 , \max \left\{ A_1, B_1, C_1 \right\} = 5 , N \right) P \left( \max \left\{ A_1, B_1, C_1 \right\} = 5 , N \right) \\ & = 1 \cdot P \left( \max \left\{ A_1, B_1, C_1 \right\} \leq 4 \right) + 0 \cdot P \left( \max \left\{ A_1, B_1, C_1 \right\} = 6 \right) \\ & \quad + \sum_{N = 1}^3 P \left( W = H | H_1 = 5 , \max \left\{ A_1, B_1, C_1 \right\} = 5 , N \right) P \left( \max \left\{ A_1, B_1, C_1 \right\} = 5 , N \right) \\ & = P \left( \max \left\{ A_1, B_1, C_1 \right\} \leq 4 \right) \\ & \quad + \sum_{N = 1}^3 P \left( W = H | H_1 = 5 , \max \left\{ A_1, B_1, C_1 \right\} = 5 , N \right) P \left( \max \left\{ A_1, B_1, C_1 \right\} = 5 , N \right) \\ & = \left( \frac{4}{6} \right)^3 + \sum_{N = 1}^3 \frac{1}{N + 1} \cdot \binom{3}{N} \left( \frac{1}{6} \right)^N \left( \frac{4}{6} \right)^{3 - N} \\ & = \frac{41}{96} . \end{align*} The first equality follows from the law of total probability. The second equality follows from the property that Hugo's outcome is independent from other players' outcomes.
Therefore, \begin{align*} P \left( H_1 = 5 | W = H \right) & = \frac{2}{3} P \left( W = H | H_1 = 5 \right) \\ & = \frac{2}{3} \frac{41}{96} \\ & = \frac{41}{144} , \end{align*}
so the answer is $\boxed{\textbf{(C) }\frac{41}{144}}$ .
~Steven Chen (www.professorchenedu.com)

## Video Solution 1
https://youtu.be/kfn0Bq1-Y5I

## Video Solution 2 (by Interstigation)
https://youtu.be/rFYTtzlN1Bw
~Interstigation

## Video Solution 3 by WhyMath
https://youtu.be/V7yTQ8CU-JI
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .