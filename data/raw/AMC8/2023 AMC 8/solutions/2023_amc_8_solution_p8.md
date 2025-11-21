# 2023 AMC 8 Problem 8

## Problem

Lola, Lolo, Tiya, and Tiyo participated in a ping pong tournament. Each player competed against each of the other three players exactly twice. Shown below are the win-loss records for the players. The numbers $1$ and $0$ represent a win or loss, respectively. For example, Lola won five matches and lost the fourth match. What was Tiyo’s win-loss record?

\[\begin{tabular}{c | c} Player & Result \\ \hline Lola & \texttt{111011}\\ Lolo & \texttt{101010}\\ Tiya & \texttt{010100}\\ Tiyo & \texttt{??????} \end{tabular}\] $\textbf{(A)}\ \texttt{000101} \qquad \textbf{(B)}\ \texttt{001001} \qquad \textbf{(C)}\ \texttt{010000} \qquad \textbf{(D)}\ \texttt{010101} \qquad \textbf{(E)}\ \texttt{011000}$

## Solution 1
We can calculate the total number of wins ( $1$ 's) by seeing how many matches were players, which is $12$ matches played. Then, we can calculate the # of wins already on the table, which is $5 + 3 + 2 = 10$ , so there are $12 - 10 = 2$ wins left in the mystery player. Now, we will make the key observation that there is only $2$ wins ( $1$ 's) per column as there are $2$ winners and $2$ losers in each round. Strategically looking through the columns counting the $1$ 's and putting our own $2$ $1$ 's when the column isn't already full yields $\boxed{\textbf{(A)}\ \texttt{000101}}$ .
~SohumUttamchandani -edits apex304, lpieleanu

## Solution 2 (Similar to #1 but More Detailed)
In total, there will be $\binom{4}{2} \cdot 2 = 6 \cdot 2 = 12$ games because there are $\binom{4}{2}$ ways to choose a pair of people from the four players. And, each player will play each other player exactly twice. Each of these $12$ games will have $1$ winner and $1$ loser, so there will be a total of $12$ $1$ 's and $12$ $0$ 's in the win-loss table. Therefore, Tiyo will have $12-10=2$ $1$ 's and $12-8=4$ $0$ 's in his record.
Now, all we have to do is figure out the order of these $1$ 's and $0$ 's. In every round, there are two games; the players are split into two pairs and the people in those pairs play each other. Thus, every round should have $2$ winners and $2$ losers which means that every column of the win-loss table should have $2$ $1$ 's and $2$ $0$ 's. Looking at the filled-in table so far, we see that columns $4$ and $6$ need one more $1$ , so Tiyo must have $1$ 's in those columns and $0$ 's gone in the others. Therefore, our answer is $\boxed{\textbf{(A)}\ \texttt{000101}}.$
~lpieleanu
Remark: Note that we can skip straight to the reasoning used in the second paragraph (which is Solution 3 below).

## Solution 3 (Faster)
We can look one by one. We see that Lola and Lolo won the first game and Tiya lost. This shows that Tiyo must have lost as well because the results must be $2$ wins and $2$ loses. We use the same logic for games $2$ and $3$ , giving us $0$ 's again. We look at the choices, and we see A is the only that starts with $3$ $0$ 's
This shows our answer is $\boxed{\textbf{(A)}\ \texttt{000101}}.$
~stevens0209, soapk

## Solution 4 (Patterns)
We look at the scores. Notice how every column of numbers represents one round. We see that each column either has 2 wins and 1 loss, or 2 losses and 1 win. So, we come to the conclusion that Tiyo’s score must make it 2:2. So, now we solve. The first column has two wins already, and only one loss, so we decide that Tiyo lost (0). The second column also has to wins, so we give Tiyo 0. The third column follows this as well. In the fourth column, we see that Lola and Lolo both lost, and Tiya is the only one who won (1), so Tiyo also won (1). The fifth column follows the same as the first three, and the last column shows that Tiyo also won. So, Tiyo got: 000101. The only option that fits this is A.
~revaprayag

## Solution 5 (Easiest Solution)
There should be two wins and two losses in each column of the graph of the win-loss records. Thus, for the first column, there are already two wins and a loss, which means that, for the column to have the same amount of wins and losses, Tiyo would have to lose. Use the same logic for the other columns, and find that the answer is A, or 000101. ~SuperVince1

## Solution 6 (Fastest Solution)
Each player has six games and there are four players so there will be 6 x 4 = 24 games. Total wins and losses of all players should be equal so there should be 12 total wins and losses among all players. By counting, it is known that there are already 10 total wins and 8 total losses. Tiyo's games must make each of these 12 so he will have 2 wins and 4 losses.
However, this leaves three different answers. To tell which is correct, we look at the 4th game of all players. There is 1 win and 2 losses, forcing Tiyo's 4th game to be a win.
Therefore, the answer is $\boxed{\textbf{(A)}\ \texttt{000101}}.$
~ArjunBhumula

## Video Solution by CoolMathProblmes
https://youtu.be/Pf93RGtKo1I?feature=shared&t=534

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=427 ~hsnacademy

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/p8NciAa6_d8
~Education the Study of everything

## Video Solution by Math-X (Smart and Simple)
https://youtu.be/Ku_c1YHnLt0?si=FgQZTccMh685we_H&t=1177 ~Math-X

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=5016

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=EcrktBc8zrM

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=661

## Video Solution by WhyMath
https://youtu.be/ut66DD0QNZE
~savannahsolver

## Video Solution by harungurcan
https://www.youtube.com/watch?v=35BW7bsm_Cg&t=973s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/WJnMLXRBBD0
### See Also